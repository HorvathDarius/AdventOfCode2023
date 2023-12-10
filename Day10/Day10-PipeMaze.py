lines = open("Day10-PipeMaze.txt").read().split("\n")

grid = []
pipes = ["|", "-", "L", "J", "7", "F"]

for line in lines:
    row = [*line]
    grid.append(row)

for row in grid:
    print(row)

coordX = 0
coordY = 0
for row in range(len(grid)):
    for col in range(len(grid)):
        if grid[row][col] == 'S':
            print(row, col)
            coordX = row
            coordY = col


imprint_number = 0
row = coordX
col = coordY
visited = [[coordX, coordY]]

grid[row][col] = imprint_number
imprint_number += 1

if grid[row - 1][col] in ["|", "F", "7"]:
    row -= 1
elif grid[row + 1][col] in ["|", "L", "J"]:
    row += 1
elif grid[row][col - 1] in ["-", "L", "F"]:
    col -= 1
elif grid[row][col + 1] in ["-", "J", "7"]:
    col += 1

while grid[row][col] != 0:
    pipe = grid[row][col]
    grid[row][col] = imprint_number
    imprint_number += 1

    if pipe == "|":
        if not grid[row - 1][col] == imprint_number - 1 and grid[row - 1][col] in pipes:
            if grid[row - 1][col] == 0:
                row -= 1
                break
            if grid[row - 1][col] in ["|", "F", "7"]:
                row -= 1
                continue
        elif not isinstance(grid[row + 1][col], int) and grid[row + 1][col] in pipes:
            if grid[row + 1][col] == 0:
                row += 1
                break
            if grid[row + 1][col] in ["|", "L", "J"]:
                row += 1
                continue
        else:
            break
    if pipe == "-":
        if not grid[row][col - 1] == imprint_number - 1 and grid[row][col - 1] in pipes:
            if grid[row][col - 1] == 0:
                col -= 1
                break
            if grid[row][col - 1] in ["-", "F", "L"]:
                col -= 1
                continue
        elif not grid[row][col + 1] == imprint_number - 1 and grid[row][col + 1] in pipes:
            if grid[row][col + 1] == 0:
                col += 1
                break
            if grid[row][col + 1] in ["-", "7", "J"]:
                col += 1
                continue
        else:
            break
    if pipe == "F":
        if not grid[row][col + 1] == imprint_number - 1 and grid[row][col + 1] in pipes:
            if grid[row][col + 1] == 0:
                col += 1
                break
            if grid[row][col + 1] in ["-", "7", "J"]:
                col += 1
                continue
        elif not isinstance(grid[row + 1][col], int) and grid[row + 1][col] in pipes:
            if grid[row + 1][col] == 0:
                row += 1
                break
            if grid[row + 1][col] in ["|", "L", "J"]:
                row += 1
                continue
        else:
            break
    if pipe == "L":
        if not grid[row][col + 1] == imprint_number - 1 and grid[row][col + 1] in pipes:
            if grid[row][col + 1] == 0:
                col += 1
                break
            if grid[row][col + 1] in ["-", "7", "J"]:
                col += 1
                continue
        elif not grid[row - 1][col] == imprint_number - 1 and grid[row - 1][col] in pipes:
            if grid[row - 1][col] == 0:
                row -= 1
                break
            if grid[row - 1][col] in ["|", "F", "7"]:
                row -= 1
                continue
        else:
            break
    if pipe == "7":
        if not grid[row][col - 1] == imprint_number - 1 and grid[row][col - 1] in pipes:
            if grid[row][col - 1] == 0:
                col -= 1
                break
            if grid[row][col - 1] in ["-", "F", "L"]:
                col -= 1
                continue
        elif not grid[row + 1][col] == imprint_number - 1 and grid[row + 1][col] in pipes:
            if grid[row + 1][col] == 0:
                row += 1
                break
            if grid[row + 1][col] in ["|", "L", "J"]:
                row += 1
                continue
        else:
            break
    if pipe == "J":
        if not isinstance(grid[row][col - 1], int) and grid[row][col - 1] in pipes:
            if grid[row][col - 1] == 0:
                col -= 1
                break
            if grid[row][col - 1] in ["-", "F", "L"]:
                col -= 1
                continue
        elif not grid[row - 1][col] == imprint_number - 1 and grid[row - 1][col] in pipes:
            if grid[row - 1][col] == 0:
                row -= 1
                break
            if grid[row - 1][col] in ["|", "F", "7"]:
                row -= 1
                continue
        else:
            break

print(f"Final number - {int(imprint_number / 2)}")

