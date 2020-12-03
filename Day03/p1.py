START = (0, 0)

X_MOVE = 3
Y_MOVE = 1

sled_map = []
with open('map.txt', 'r') as file:
    for line in file:
        sled_map.append([char for char in line.strip()])

max_y = len(sled_map)
max_x = len(sled_map[0])

pos_x = START[0]
pos_y = START[1]

trees = 0
while pos_y < max_y:

    pos_y = pos_y + Y_MOVE
    pos_x = (pos_x + X_MOVE) % max_x

    if pos_y < max_y:
        if sled_map[pos_y][pos_x] == '#':
            trees += 1
            sled_map[pos_y][pos_x] = 'X'
        else:
            sled_map[pos_y][pos_x] = 'O'


print(trees)
for i, line in enumerate(sled_map):
    sled_map[i] = ''.join(line)

out = '\n'.join(sled_map)

with open('out_' + 'map.txt', 'w') as file:
    file.write(out)

exit(0)
