def count_occupied(layout):
    total = 0
    for row in layout:
        for col in row:
            if col == '#':
                total += 1
    return total


def clone_layout(layout):
    return [[seat for seat in seats] for seats in layout]


def count_occupied_adjacencies(x, y, layout):
    max_x = len(layout[0]) - 1
    max_y = len(layout) - 1
    count = 0
    # Northern
    if y > 0:
        row = layout[y - 1]
        # North-West
        if x > 0 and row[x - 1] == '#':
            count += 1
        # North
        if row[x] == '#':
            count += 1
        # North-East
        if x < max_x and row[x + 1] == '#':
            count += 1

    # West
    if x > 0 and layout[y][x - 1] == '#':
        count += 1
    # East
    if x < max_x and layout[y][x + 1] == '#':
        count += 1

    # Southern
    if y < max_y:
        row = layout[y + 1]
        # South-West
        if x > 0 and row[x - 1] == '#':
            count += 1
        # South
        if row[x] == '#':
            count += 1
        # South-East
        if x < max_x and row[x + 1] == '#':
            count += 1
    return count


def simulate(layout) -> [[]]:
    new_layout = clone_layout(layout)
    for y, row in enumerate(new_layout):
        for x, seat in enumerate(row):
            if seat == '.':
                continue
            num_occupied_adjs = count_occupied_adjacencies(x, y, layout)
            if num_occupied_adjs == 0:
                row[x] = '#'
            elif num_occupied_adjs >= 4:
                row[x] = 'L'
    return new_layout


def print_layout(layout):
    for row in layout:
        for col in row:
            print(col, end='')
        print()


def stabilize_simulation(layout):
    while True:
        new_layout = simulate(layout)
        if layout == new_layout:
            break
        else:
            layout = new_layout
    occupied = count_occupied(layout)
    return occupied


with open("seat_layout.txt", 'r') as file:
    layout = [
        [seat for seat in seats]
        for seats in file.read().split('\n')
        if seats
    ]

value = stabilize_simulation(layout)
print(value)

exit(0)
