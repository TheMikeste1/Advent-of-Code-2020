def valid_byr(byr):
    byr = int(byr)
    return 1920 <= byr <= 2002


def valid_iyr(iyr):
    iyr = int(iyr)
    return 2010 <= iyr <= 2020


def valid_eyr(eyr):
    eyr = int(eyr)
    return 2020 <= eyr <= 2030


def valid_hgt(hgt):
    unit = hgt[-2:]
    amount = int(hgt[:-2])

    if unit == "cm":
        return 150 <= amount <= 193
    if unit == "in":
        return 59 <= amount <= 76
    return False


def valid_hcl(hcl):
    if hcl[0] != "#":
        return False
    hcl = hcl[1:]
    if len(hcl) != 6 or not hcl.isalnum():
        return False
    return True


VALID_ECLS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
def valid_ecl(ecl):
    global VALID_ECLS
    return ecl in VALID_ECLS


def valid_pid(pid):
    if len(pid) != 9 or not pid.isnumeric():
        return False
    return True


def valid_passport(passport: dict):
    keys = passport.keys()
    if "byr" not in keys or not valid_byr(passport["byr"]):
        return False
    if "iyr" not in keys or not valid_iyr(passport["iyr"]):
        return False
    if "eyr" not in keys or not valid_eyr(passport["eyr"]):
        return False
    if "hgt" not in keys or not valid_hgt(passport["hgt"]):
        return False
    if "hcl" not in keys or not valid_hcl(passport["hcl"]):
        return False
    if "ecl" not in keys or not valid_ecl(passport["ecl"]):
        return False
    if "pid" not in keys or not valid_pid(passport["pid"]):
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
