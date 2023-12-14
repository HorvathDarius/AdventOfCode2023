from copy import *

lines = open("Day14-ParabolicReflectorDish.txt").read().splitlines()

matrix = []
for line in lines:
    matrix.append([*line])


def rotate_dish(grid):
    # NORTH
    for line in range(1, len(grid)):
        for rock in range(len(grid[line])):
            pos = line
            if grid[line][rock] == "O":
                while pos != 0 and grid[pos - 1][rock] == ".":
                    grid[pos][rock] = "."
                    grid[pos - 1][rock] = "O"
                    pos -= 1

    # WEST
    for line in range(len(grid)):
        for rock in range(1, len(grid[line])):
            pos = rock
            if grid[line][rock] == "O":
                while pos != 0 and grid[line][pos - 1] == ".":
                    grid[line][pos] = "."
                    grid[line][pos - 1] = "O"
                    pos -= 1

    # SOUTH
    for line in range(len(grid) - 1, -1, -1):
        for rock in range(len(grid[line])):
            pos = line
            if grid[line][rock] == "O":
                while pos != len(grid) - 1 and grid[pos + 1][rock] == ".":
                    grid[pos][rock] = "."
                    grid[pos + 1][rock] = "O"
                    pos += 1

    # EAST
    for line in range(len(grid)):
        for rock in range(len(grid[line]) - 1, -1, -1):
            pos = rock
            if grid[line][rock] == "O":
                while pos != len(grid[line]) - 1 and grid[line][pos + 1] == ".":
                    grid[line][pos] = "."
                    grid[line][pos + 1] = "O"
                    pos += 1

    return grid


def calculate_load(grid):
    result = 0
    for line in grid:
        count = 0
        for char in line:
            if char == "O":
                count += 1
        at_index = grid.index(line)
        distance = len(grid) - at_index
        result += count * distance
    return result

collection_grid = []
loops = 0
num = 0
i = 0
item = deepcopy(matrix)
while True:
    new_grid = deepcopy(item)
    item = rotate_dish(new_grid)
    if new_grid in collection_grid:
        loops = i
        first = collection_grid.index(new_grid)
        num = (1000000000 - first) % (loops - first) + first
        break
    else:
        collection_grid.append(item)
    i += 1

for i in range(num):
    matrix = rotate_dish(matrix)

result = calculate_load(matrix)
print(f"Result - {result}")
