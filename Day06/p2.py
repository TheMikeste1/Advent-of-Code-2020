with open("customs_answers.txt", "r") as file:
    answers = [answer.split('\n') for answer in file.read().split("\n\n")]

for i, answer in enumerate(answers):
    union = set(answer[0]).intersection(*answer[1:])
    answers[i] = union

total = 0
for answer in answers:
    total += len(answer)

print(total)
