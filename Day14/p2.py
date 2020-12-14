def parse_section(section):
    parts = section.splitlines()

    section = {'mask': f"{parts.pop(0):X>36}", 'steps': []}

    for part in parts:
        loc, val = part.split("] = ")
        loc = loc.split('[')[1]
        val = f"{int(val):0>36b}"

        section['steps'].append((loc, val))

    return section


def parse_commands(commands):
    sections = commands.split("mask = ")

    if not sections[0]:
        # The first line start with 'mask = ', so we'll pop it.
        # I'm using an if statement in case I want to change how I split later.
        sections.pop(0)

    for i, section in enumerate(sections):
        sections[i] = parse_section(section)

    return sections


def apply_mask(mask, num):
    out = ''
    for mask_char, num_char in zip(mask, num):
        if mask_char == '0':
            out += num_char
        else:
            out += mask_char
    return out


def generate_locs(floating_loc) -> []:
    # Find the fist 'X', then recursively fill the rest.
    i = floating_loc.find('X')
    if i < 0:
        # If i == -1, there are no more floating bits. Return the floating_loc.
        return [floating_loc]

    locs = []
    temp = floating_loc[:i] + '0' + floating_loc[i + 1:]
    locs.extend(generate_locs(temp))
    temp = floating_loc[:i] + '1' + floating_loc[i + 1:]
    locs.extend(generate_locs(temp))

    return locs


def execute_commands(commands):
    out = {}
    for section in commands:
        mask = section['mask']
        steps = section['steps']
        for loc, val in steps:
            floating_loc = apply_mask(mask, f"{int(loc):0>36b}")
            locs = generate_locs(floating_loc)
            for loc in locs:
                out[loc] = val
    return out


def sum_vals(vals):
    total = 0
    for val in vals.values():
        total += int(val, 2)
    return total


with open("input.txt", 'r') as file:
    commands = file.read()

commands = parse_commands(commands)
vals = execute_commands(commands)

total = sum_vals(vals)

print(total)

exit(0)
