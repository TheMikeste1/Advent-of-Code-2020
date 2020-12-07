def find_parents(bags, rules):
    original_len = len(bags)

    bags = set(bags)



    new_bags = set(map(
        lambda rule: rule["parent"],
        filter(
            lambda rule: list(filter(
                lambda child: child["bag"] in bags,
                rule["children"]
            )),
            rules
    )))
    # I decided to go a more "functional" route for this one. If needed,
    # the below is the loop version:
    #
    # new_bags = set()
    # for rule in rules:
    #     valid = False
    #     for child in rule["children"]:
    #         if child["bag"] in bags:
    #             valid = True
    #             break
    #     if valid:
    #         new_bags.add(rule["parent"])

    bags.update(new_bags)

    if len(bags) != original_len:
        bags = find_parents(bags, rules)

    return bags


def parse_rules(rules):
    parsed = []
    for rule in rules:
        parent, children = rule.split(" contain ")
        children = children.split(", ")
        if len(children) == 1 and children[0] == '':
            children = []
        for i, child in enumerate(children):
            num = child.split(" ")[0]
            bag = " ".join(child.split(" ")[1:])
            children[i] = {"num": int(num), "bag": bag}
        parsed.append({"parent"  : parent,
                       "children": children})
    return parsed


with open("bag_rules.txt", "r") as file:
    raw_rules = file.read().replace("bags", "bag")\
        .replace("no other bag", "").split(".\n")

rules = parse_rules(raw_rules)

valid_bags = find_parents(["shiny gold bag"], rules)
print(len(valid_bags) - 1)  # Subtract 1 since we include the initial bag.


exit(0)
