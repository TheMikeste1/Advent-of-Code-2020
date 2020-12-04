def valid_passport(passport: dict):
    keys = passport.keys()
    if "byr" not in keys:
        return False
    if "iyr" not in keys:
        return False
    if "eyr" not in keys:
        return False
    if "hgt" not in keys:
        return False
    if "hcl" not in keys:
        return False
    if "ecl" not in keys:
        return False
    if "pid" not in keys:
        return False

    return True


def parse_passport_string(passport_string):
    # Split into individual items
    items = passport_string.split(' ')

    # Split each item into key:value pairs
    passport_information = {}
    for item in items:
        key, value = item.split(':')
        passport_information[key] = value
    return passport_information


passports = []
with open("passports.txt", "r") as file:
    # Read in file, separating passports with \f, and changing extraneous new
    # lines to space.
    text = file.read().replace("\n\n", '\f').replace("\n", ' ')

# Split the text along \f
text = text.split('\f')
for passport in text:
    passport = parse_passport_string(passport)
    passports.append(passport)

num_valid_passports = 0
for passport in passports:
    if valid_passport(passport):
        num_valid_passports += 1

print("Valid passports:", num_valid_passports)

exit(0)
