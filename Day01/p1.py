numbers = []
with open("numbers.txt", "r") as file:
    numbers = [int(line) for line in file]

numbers.sort()

for number in numbers:
    desired = 2020 - number
    if desired in numbers:
        print(number, desired)
        print(number * desired)
        break
