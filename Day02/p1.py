def valid_password(info):
    letter = info[0]
    min_num = info[1]
    max_num = info[2]
    pwd = info[3]

    count = pwd.count(letter)
    return min_num <= count <= max_num


with open("passwords.txt", 'r') as file:
    info = file.readlines()

# Information is stored in the form (letter, min amount, max amount)
information = []
for line in info:
    req, pwd = line.split(':')
    length, letter = req.split(' ')
    min_, max_ = length.split('-')
    information.append((letter, int(min_), int(max_), pwd[:-1]))

num_valid = 0
for info in information:
    if valid_password(info):
        num_valid += 1

print(num_valid)
