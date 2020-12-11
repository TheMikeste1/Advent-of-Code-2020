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
        # North-West
        x_test = x
        y_test = y
        while x_test > 0 and y_test > 0:
            x_test -= 1
            y_test -= 1
            loc = layout[y_test][x_test]
            if loc == '.':
                continue
            else:
                if loc == '#':
                    count += 1
                break
        # North
        x_test = x
        y_test = y
        while y_test > 0:
            y_test -= 1
            loc = layout[y_test][x_test]
            if loc == '.':
                continue
            else:
                if loc == '#':
                    count += 1
                break
        # North-East
        y_test = y
        while x_test < max_x and y_test > 0:
            y_test -= 1
            x_test += 1
            loc = layout[y_test][x_test]
            if loc == '.':
                continue
            else:
                if loc == '#':
                    count += 1
                break

    # West
    x_test = x
    y_test = y
    while x_test > 0:
        x_test -= 1
        loc = layout[y_test][x_test]
        if loc == '.':
            continue
        else:
            if loc == '#':
                count += 1
            break
    # East
    x_test = x
    while x_test < max_x:
        x_test += 1
        loc = layout[y_test][x_test]
        if loc == '.':
            continue
        else:
            if loc == '#':
                count += 1
            break

    # Southern
    if y < max_y:
        # South-West
        x_test = x
        y_test = y
        while x_test > 0 and y_test < max_y:
            x_test -= 1
            y_test += 1
            loc = layout[y_test][x_test]
            if loc == '.':
                continue
            else:
                if loc == '#':
                    count += 1
                break
        # South
        x_test = x
        y_test = y
        while y_test < max_y:
            y_test += 1
            loc = layout[y_test][x_test]
            if loc == '.':
                continue
            else:
                if loc == '#':
                    count += 1
                break
        # South-East
        y_test = y
        while x_test < max_x and y_test < max_y:
            y_test += 1
            x_test += 1
            loc = layout[y_test][x_test]
            if loc != '.':
                if loc == '#':
                    count += 1
                break

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
            elif num_occupied_adjs >= 5:
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
