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


def exploit_weakness(cipher, weakness):
    values = []
    total = 0
    i = 0
    while total != weakness:
        if total > weakness:
            total -= values.pop(0)
        else:
            value = cipher[i]
            i += 1
            total += value
            values.append(value)

    return values


with open("XMAS cipher.txt", 'r') as file:
    cipher = file.read().split('\n')

cipher = [int(c) for c in cipher]

weakness = find_weakness(cipher)
values = exploit_weakness(cipher, weakness)

print(values)
print(f"Min: {min(values)}, Max: {max(values)}")
print(min(values) + max(values))

exit(0)
