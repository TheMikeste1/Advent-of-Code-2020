def valid_password(info):
    letter = info[0]
    min_loc = info[1] - 1
    max_loc = info[2] - 1
    pwd = info[3]

    min_letter = pwd[min_loc]
    max_letter = pwd[max_loc]
    return max_letter != min_letter \
        and (min_letter == letter or max_letter == letter)


with open("passwords.txt", 'r') as file:
    info = file.readlines()

# Information is stored in the form (password, letter, min amount, max amount)
information = []
for line in info:
    req, pwd = line.split(':')
    length, letter = req.split(' ')
    min_, max_ = length.split('-')
    information.append((letter, int(min_), int(max_), pwd.strip()))

num_valid = 0
for info in information:
    if valid_password(info):
        num_valid += 1

print(num_valid)
