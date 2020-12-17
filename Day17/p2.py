ACTIVE = '#'
INACTIVE = '.'
STEPS = 6


def print_grid(grid):
    for z in range(len(grid)):
        print("z =", z)
        for y in range(len(grid[z])):
            for x in range(len(grid[z][y])):
                print(grid[z][y][x], end='')
            print()
        print()


def count_active_on_layer(layer):
    total = 0

    for line in layer:
        for point in line:
            if point == ACTIVE:
                total += 1

    return total


def clone_grid(grid):
    return [
        [
            [
                [point for point in line] for line in plane
            ] for plane in dim
        ] for dim in grid
    ]


def create_empty_layer(x, y):
    return [[INACTIVE] * x] * y


def count_layer_neighbors(x, y, layer):
    total = 0

    max_y = len(layer)
    if max_y == 0:
        return total
    max_x = len(layer[0])

    # Northern
    if y + 1 < max_y:
        total += 1 if layer[y + 1][x] == ACTIVE else 0
        # East
        if x + 1 < max_x:
            total += 1 if layer[y + 1][x + 1] == ACTIVE else 0
        # West
        if x - 1 >= 0:
            total += 1 if layer[y + 1][x - 1] == ACTIVE else 0

    # Southern
    if y - 1 >= 0:
        total += 1 if layer[y - 1][x] == ACTIVE else 0
        # East
        if x + 1 < max_x:
            total += 1 if layer[y - 1][x + 1] == ACTIVE else 0
        # West
        if x - 1 >= 0:
            total += 1 if layer[y - 1][x - 1] == ACTIVE else 0

    # East
    if x + 1 < max_x:
        total += 1 if layer[y][x + 1] == ACTIVE else 0
    # West
    if x - 1 >= 0:
        total += 1 if layer[y][x - 1] == ACTIVE else 0

    return total


def get_dim_neighbors(x, y, z, dim):
    # Count cardinals
    total = count_layer_neighbors(x, y, dim[z])

    max_z = len(dim)
    if max_z <= 0:
        return total
    # Count one up
    if z + 1 < max_z:
        total += count_layer_neighbors(x, y, dim[z + 1])
        total += 1 if dim[z + 1][y][x] == ACTIVE else 0

    # Count one down
    if z - 1 >= 0:
        total += count_layer_neighbors(x, y, dim[z - 1])
        total += 1 if dim[z - 1][y][x] == ACTIVE else 0

    return total


def get_active_neighbors(x, y, z, w, grid):
    total = get_dim_neighbors(x, y, z, grid[w])

    max_w = len(grid)
    if max_w <= 0:
        return total

    if w - 1 >= 0:
        total += get_dim_neighbors(x, y, z, grid[w - 1])
        total += 1 if grid[w - 1][z][y][x] == ACTIVE else 0
    if w + 1 < max_w:
        total += get_dim_neighbors(x, y, z, grid[w + 1])
        total += 1 if grid[w + 1][z][y][x] == ACTIVE else 0

    return total


def simulate(grid):
    for step in range(STEPS):
        new_grid = clone_grid(grid)
        # Check each spot
        for w, dim in enumerate(grid):
            for z, layer in enumerate(dim):
                for y, line in enumerate(layer):
                    for x, point in enumerate(line):
                        active_neighbors = \
                            get_active_neighbors(x, y, z, w, grid)
                        if active_neighbors == 3:
                            new_grid[w][z][y][x] = ACTIVE
                        elif active_neighbors != 2 and point == ACTIVE:
                            new_grid[w][z][y][x] = INACTIVE
        grid = new_grid

    return grid


def buffer_layer(layer: [[]], times=1):
    for _ in range(times):
        layer.insert(
            0,
            [INACTIVE] * len(layer[0])
        )
        layer.append(
            [INACTIVE] * len(layer[0])
        )

        for row in layer:
            row.insert(0, INACTIVE)
            row.append(INACTIVE)


# Test answer = 848
with open("test.txt", 'r') as file:
    grid = [[[[char for char in line] for line in file.read().splitlines()]]]
# There are only 6 steps, so only the 6 cubes out of the initial grid matter.
# Let's buffer those now.
buffer_layer(grid[0][0], 6)
for _ in range(STEPS):
    dim = [[[INACTIVE]]]
    buffer_layer(dim[0], len(grid[0][0]) // 2)
    grid.append(dim)
    dim = [[[INACTIVE]]]
    buffer_layer(dim[0], len(grid[0][0]) // 2)
    grid.insert(0, dim)

grid = simulate(grid)

total = 0
for dim in grid:
    for layer in dim:
        total += count_active_on_layer(layer)
print(total)

exit(0)
