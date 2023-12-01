f = open('Day1-Trebuchet.txt', "r")
lines = f.readlines()

sum = 0

for line in range(len(lines)):
    num1 = 0
    num2 = 0
    x = 0
    numbers = []
    for i in lines[line]:
        if i.isnumeric():
            numbers.append(i)
    num1 = numbers[0]
    num2 = numbers[-1]
    num1 = int(num1) * 10
    x = num1 + int(num2)
    sum += x
print(sum)