array = open('Day15-LensLibrary.txt').read()

new_arr = array.split(',')
sum = 0
for item in new_arr:
    curr = 0
    for char in item:
        curr += ord(char)
        curr *= 17
        curr %= 256
    sum += curr

print(f"Total - {sum}")