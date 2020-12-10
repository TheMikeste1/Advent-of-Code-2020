def count_valid_adapter_arrangements(current_jolt, jolts,
                                     known_combinations=None):
    # We could iterate through each combination multiple times, but it's
    # cheaper to just keep track.
    if known_combinations is None:
        known_combinations = {}
    elif current_jolt in known_combinations:
        return known_combinations[current_jolt]

    valid_jolts = filter(
        lambda x: 0 < x - current_jolt <= 3,
        jolts
    )
    total = 0
    for jolt in valid_jolts:
        total += count_valid_adapter_arrangements(jolt, jolts,
                                                  known_combinations)
    if total == 0:
        total = 1  # If there were no others, we're at the end of the chain, so
        # we'll add 1. This is the way.
    known_combinations[current_jolt] = total
    return total


with open("jolts.txt", 'r') as file:
    jolts = [int(jolt) for jolt in file.readlines()]

valid_arrangements = count_valid_adapter_arrangements(0, jolts)
print(valid_arrangements)

exit(0)
