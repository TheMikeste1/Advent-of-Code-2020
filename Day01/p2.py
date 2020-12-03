numbers = []
with open("numbers.txt", "r") as file:
    numbers = [int(line) for line in file]

numbers.sort()

for i, number1 in enumerate(numbers):
    desired = 2020 - number1
    for j, number2 in enumerate(numbers):
        if i == j:
            continue
        subdesired = desired - number2
        if subdesired in numbers:
            print(number1, number2, subdesired)
            print(number1 * number2 * subdesired)
            exit(0)
