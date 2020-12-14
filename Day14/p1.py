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
        if mask_char != 'X':
            out += mask_char
        else:
            out += num_char
    return out


def execute_commands(commands):
    out = {}
    for section in commands:
        mask = section['mask']
        steps = section['steps']
        for loc, val in steps:
            val = apply_mask(mask, val)
            out[loc] = val  # We write, so we don't need to worry about adding.
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
