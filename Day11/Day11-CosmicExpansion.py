lines = open("Day11-CosmicExpansion.txt").read().splitlines()

def find_number(grid, number):
    for row in grid:
        for col in range(len(row)):
            if row[col] == number:
                return [grid.index(row), col]

space = []
for line in lines:
    new_space = []
    for char in line:
        new_space.append(char)
    space.append(new_space)

new_space = []
for line in space:
    new_space.append(line)
    if "#" not in line:
        new_line = []
        for char in line:
            new_line.append(char)
        new_space.append(new_line)

empty_cols = []
for n in range(len(space)):
    empty_cols.append(n)

for line in new_space:
    for char in range(len(line)):
        if line[char] == "#":
            if char in empty_cols:
                empty_cols.remove(char)

for line in new_space:
    count = 0
    for char in range(len(line)):
        if char in empty_cols:
            line.insert(char + 1 + count, ".")
            count += 1

print(len(new_space))
sizes = []
for line in new_space:
    sizes.append(len(line))
print(sizes)
print(empty_cols)

count = 0
for line in new_space:
    for char in range(len(line)):
        if line[char] == "#":
            count += 1
            line[char] = count

# for line in new_space:
#     print(line)

pairs = []
empty_nums = []
index = 0
for n in range(len(space)):
    empty_nums.append(n + 1)
for number in range(count - 1):
    for number_2 in range(index, len(empty_nums) - 1):
        if number + 1 != number_2 + 1:
            pairs.append([number + 1, number_2 + 1])
    index += 1

# print(len(pairs))

total_distance = 0
for pair in pairs:
    number1, number2 = pair
    coords = find_number(new_space, number1)
    coords2 = find_number(new_space, number2)
    num1 = coords2[0] - coords[0]
    num2 = coords2[1] - coords[1]
    sum = abs(num1) + abs(num2)
    total_distance += sum

print(f"Total distance between galaxies - {total_distance}")
