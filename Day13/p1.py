from math import ceil


def calculate_remainder(target, num):
    return ceil(target / num) * num - target


def calculate_closest_multiple(target, nums):
    lowest = nums[0]
    remainder = calculate_remainder(target, lowest)

    for num in nums[1:]:
        r = calculate_remainder(target, num)
        if r < remainder:
            remainder = r
            lowest = num

    return lowest, remainder


with open("departure_notes.txt", 'r') as file:
    earliest, ids = file.read().replace("x,", '').split('\n')
earliest = int(earliest)
ids = [int(id_) for id_ in ids.split(',')]

best_id, remainder = calculate_closest_multiple(earliest, ids)

print(f"Best ID: {best_id}\nRemainder:{remainder}")
print(f"Answer: {best_id * remainder}")

exit(0)
