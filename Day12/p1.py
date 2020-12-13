def rotate_ship(current_facing, direction, amount):
    if amount == 180:  # Flip the ship
        if current_facing == 'N':
            return 'S'
        if current_facing == 'S':
            return 'N'
        if current_facing == 'E':
            return 'W'
        if current_facing == 'W':
            return 'E'

    if amount == 270:
        direction = 'L' if direction == 'R' else 'R'

    if direction == 'L':
        if current_facing == 'N':
            return 'W'
        if current_facing == 'S':
            return 'E'
        if current_facing == 'E':
            return 'N'
        if current_facing == 'W':
            return 'S'

    if direction == 'R':
        if current_facing == 'N':
            return 'E'
        if current_facing == 'S':
            return 'W'
        if current_facing == 'E':
            return 'S'
        if current_facing == 'W':
            return 'N'


def move_ship(x, y, direction, amount):
    if direction == 'N':
        y += amount
    elif direction == 'S':
        y -= amount
    elif direction == 'E':
        x += amount
    elif direction == 'W':
        x -= amount

    return x, y


def follow_instructions(movements):
    facing = 'E'
    x = 0
    y = 0

    for move, amount in movements:
        if move == 'L' or move == 'R':
            facing = rotate_ship(facing, move, amount)
        elif move == 'F':
            x, y = move_ship(x, y, facing, amount)
        else:
            x, y = move_ship(x, y, move, amount)

    return x, y


with open("movements.txt", 'r') as file:
    movements = [(move[0], int(move[1:])) for move in file.read().split()]

position = follow_instructions(movements)

print(abs(position[0]) + abs(position[1]))

exit(0)
