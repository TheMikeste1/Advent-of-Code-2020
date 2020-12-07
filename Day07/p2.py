def get_rule(bag, rules):
    for rule in rules:
        if rule["parent"] == bag:
            return rule
    raise Exception(f"Rules for \"{bag}\" not found")


def get_total_inside_bags(bag, rules):
    rule = get_rule(bag, rules)
    total = 0
    for child in rule["children"]:
        subtotal = get_total_inside_bags(child["bag"], rules)
        # Add this bag plus the subbags
        total += child["num"] + child["num"] * subtotal
    return total


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

total = get_total_inside_bags("shiny gold bag", rules)

print(total)

exit(0)
