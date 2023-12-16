array = open('Day15-LensLibrary.txt').read()

new_arr = array.split(',')
def hash(item):
    curr = 0
    for char in item:
        curr += ord(char)
        curr *= 17
        curr %= 256
    return curr

boxes = [[] for _ in range(256)]
focal_lengths = {}

for instruction in new_arr:
    if "-" in instruction:
        label = instruction[:-1]
        index = hash(label)
        if label in boxes[index]:
            boxes[index].remove(label)
    else:
        label, length = instruction.split("=")
        length = int(length)

        index = hash(label)
        if label not in boxes[index]:
            boxes[index].append(label)

        focal_lengths[label] = length

total = 0

for box_number, box in enumerate(boxes, 1):
    for lens_slot, label in enumerate(box, 1):
        total += box_number * lens_slot * focal_lengths[label]

print(f"Total = {total}")