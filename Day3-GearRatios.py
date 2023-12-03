f = open('Day3-GearRatios.txt')


def part_numbers():
    lines = f.readlines()
    numbers_coord = set()
    matrix = []
    for line in lines:
        new_line = []
        for char in line:
            if char != "\n":
                new_line.append(char)
        matrix.append(new_line)

    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if col.isdigit() or col == ".":
                continue
            for cr in [r - 1, r, r + 1]:
                for cc in [c - 1, c, c + 1]:
                    if cr < 0 or cr >= len(matrix) or cc < 0 or cc >= len(matrix[cr]) or not matrix[cr][cc].isdigit():
                        continue
                    while cc > 0 and matrix[cr][cc - 1].isdigit():
                        cc -= 1
                    numbers_coord.add((cr, cc))

    total_sum = 0
    for r, c in numbers_coord:
        number = ""
        while c < len(matrix[r]) and matrix[r][c].isdigit():
            number += matrix[r][c]
            c += 1
        total_sum += int(number)
    print(f"Total sum is - {total_sum}")


part_numbers()
f = open('Day3-GearRatios.txt')


def gear_schematic():
    lines = f.readlines()
    numbers_coord = set()
    matrix = []
    for line in lines:
        new_line = []
        for char in line:
            if char != "\n":
                new_line.append(char)
        matrix.append(new_line)

    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if col.isdigit() or col == ".":
                continue
            if col == "*":
                temp_array = set()
                for cr in [r - 1, r, r + 1]:
                    for cc in [c - 1, c, c + 1]:
                        if cr < 0 or cr >= len(matrix) or cc < 0 or cc >= len(matrix[cr]) or not matrix[cr][cc].isdigit():
                            continue
                        while cc > 0 and matrix[cr][cc - 1].isdigit():
                            cc -= 1
                        temp_array.add((cr, cc))
                if len(temp_array) == 2:
                    numbers_coord.add(item for item in temp_array)

    total_sum = 0
    for pair in numbers_coord:
        gear_multiply = 1
        for r, c in pair:
            number = ""
            while c < len(matrix[r]) and matrix[r][c].isdigit():
                number += matrix[r][c]
                c += 1
            gear_multiply *= int(number)
        total_sum += gear_multiply
    print(f"Total Gear Ratio is - {total_sum}")


gear_schematic()