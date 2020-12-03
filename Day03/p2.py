START = (0, 0)
SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]


def traverse(sled_map, x_move, y_move):
    global START

    max_y = len(sled_map)
    max_x = len(sled_map[0])

    pos_x = START[0]
    pos_y = START[1]

    trees = 0
    while pos_y < max_y:
        pos_y = pos_y + y_move
        pos_x = (pos_x + x_move) % max_x

        if pos_y < max_y:
            if sled_map[pos_y][pos_x] == '#':
                trees += 1

    return trees


sled_map = []
with open('map.txt', 'r') as file:
    for line in file:
        sled_map.append([char for char in line.strip()])

slope_trees = []
for slope in SLOPES:
    trees = traverse(sled_map, slope[0], slope[1])
    print(f"{slope}:", trees)
    slope_trees.append(trees)

answer = 1
for trees in slope_trees:
    answer *= trees
print("Answer:", answer)
