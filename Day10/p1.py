with open("jolts.txt", 'r') as file:
    jolts = [int(jolt) for jolt in file.readlines()]


jolts.sort()
current_jolt = 0
total_jumps = [0] * 3
for jolt in jolts:
    total_jumps[jolt - current_jolt - 1] += 1
    current_jolt = jolt

total_jumps[2] += 1  # Add one to 3 for jump to phone
print(total_jumps)
print(total_jumps[0] * total_jumps[2])

exit(0)
