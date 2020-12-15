def play_game(turn, last_spoken, record, until):
    while turn < until:
        # Check is the last spoken number has already been spoken
        if last_spoken not in record:
            # If it has, write down the turn...
            record[last_spoken] = turn
            # And say 0.
            last_spoken = 0
        else:
            # Otherwise, get the turn it was last spoken...
            turn_last_spoken = record[last_spoken]
            # Replace it with this turn...
            record[last_spoken] = turn
            # And determine the next number.
            last_spoken = turn - turn_last_spoken
        turn += 1  # This turn is over, so increment the turn counter.
    return last_spoken


number_input = [0, 20, 7, 16, 1, 18, 15]
# number_input = [0, 3, 6]  # == 175594
# number_input = [1, 3, 2]  # == 2578

turn = 1
spoken = {}
for num in number_input:
    spoken[num] = turn
    turn += 1

val = play_game(turn, 0, spoken, 30000000)
print(val)

exit(0)
