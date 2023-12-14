lines = open("Day14-ParabolicReflectorDish.txt").read().splitlines()

# print(lines)
grid = []
for line in lines:
    grid.append([*line])

for line in range(1, len(grid)):
    for rock in range(len(grid[line])):
        pos = line
        if grid[line][rock] == "O":
            while pos != 0 and grid[pos - 1][rock] == ".":
                grid[pos][rock] = "."
                grid[pos - 1][rock] = "O"
                pos -= 1


result = 0
for line in grid:
    count = 0
    for char in line:
        if char == "O":
            count += 1
    at_index = grid.index(line)
    distance = len(grid) - at_index
    result += count * distance

print(f"Result - {result}")