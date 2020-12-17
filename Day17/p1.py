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
    return [[[point for point in line] for line in plane] for plane in grid]


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


def get_active_neighbors(x, y, z, grid):
    # Count cardinals
    total = count_layer_neighbors(x, y, grid[z])

    max_z = len(grid)
    if max_z <= 0:
        return total
    # Count one up
    if z + 1 < max_z:
        total += count_layer_neighbors(x, y, grid[z + 1])
        total += 1 if grid[z + 1][y][x] == ACTIVE else 0

    # Count one down
    if z - 1 >= 0:
        total += count_layer_neighbors(x, y, grid[z - 1])
        total += 1 if grid[z - 1][y][x] == ACTIVE else 0

    return total


def simulate(grid):
    print("Step 0:")
    print_grid(grid)
    for step in range(STEPS):
        print(f"Step {step + 1}:")
        # Check if we need to add any layers. This is done by checking if
        # there is an active cube on the cube's surface.
        # Check bottom
        layer = grid[0]
        if count_active_on_layer(layer) > 0:
            x = len(layer[0])
            y = len(layer)
            grid = [create_empty_layer(x, y)] + grid

        # Check top
        layer = grid[-1]
        if count_active_on_layer(layer) > 0:
            x = len(layer[0])
            y = len(layer)
            grid = grid + [create_empty_layer(x, y)]

        new_grid = clone_grid(grid)

        # Check each spot
        for z, layer in enumerate(grid):
            for y, line in enumerate(layer):
                for x, point in enumerate(line):
                    active_neighbors = get_active_neighbors(x, y, z, grid)
                    if active_neighbors == 3:
                        new_grid[z][y][x] = ACTIVE
                    elif active_neighbors == 2 and point == ACTIVE:
                        new_grid[z][y][x] = ACTIVE
                    else:
                        new_grid[z][y][x] = INACTIVE

        print_grid(new_grid)
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


with open("initial_grid.txt", 'r') as file:
    grid = [[[char for char in line] for line in file.read().splitlines()]]
# There are only 6 steps, so only the 6 cubes out of the initial grid matter.
# Let's buffer those now.
buffer_layer(grid[0], 6)
grid = simulate(grid)

total = 0
for layer in grid:
    total += count_active_on_layer(layer)
print(total)

exit(0)
