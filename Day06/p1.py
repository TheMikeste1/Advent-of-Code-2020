answers = []
with open("customs_answers.txt", "r") as file:
    answer = set()
    for line in file:
        if line == '\n':
            answers.append(answer)
            answer = set()
        else:
            answer.update(line[:-1])

    answers.append(answer)

total = 0
for answer in answers:
    total += len(answer)

print(total)
