def find_weakness(cipher) -> int:
    if len(cipher) < 26:  # There are not enough elements left
        raise Exception("Reached end of cipher!")

    preamble = cipher[:25]
    target = cipher[25]
    for i in range(len(preamble) - 1):
        a = preamble[i]
        for j in range(i + 1, len(preamble)):
            b = preamble[j]
            if a == b:
                continue
            if a + b == target:
                return find_weakness(cipher[1:])
    return target


with open("XMAS cipher.txt", 'r') as file:
    cipher = file.read().split('\n')

cipher = [int(c) for c in cipher]

value = find_weakness(cipher)
print(value)

exit(0)
