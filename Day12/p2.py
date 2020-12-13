def rotate_waypoint(x, y, direction, amount):
    if amount == 180:  # Flip the waypoint
        return -x, -y

    if amount == 270:
        direction = 'L' if direction == 'R' else 'R'

    if direction == 'L':
        return -y, x

    if direction == 'R':
        return y, -x


def move_waypoint(x, y, direction, amount):
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
    ship_x = 0
    ship_y = 0
    way_x = 10
    way_y = 1

    for move, amount in movements:
        if move == 'L' or move == 'R':
            way_x, way_y = rotate_waypoint(way_x, way_y, move, amount)
        elif move == 'F':
            ship_x += amount * way_x
            ship_y += amount * way_y
        else:
            way_x, way_y = move_waypoint(way_x, way_y, move, amount)

    return ship_x, ship_y


with open("movements.txt", 'r') as file:
    movements = [(move[0], int(move[1:])) for move in file.read().split()]

position = follow_instructions(movements)

print(abs(position[0]) + abs(position[1]))

exit(0)
