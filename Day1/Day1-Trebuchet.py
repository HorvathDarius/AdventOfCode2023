f = open('Day1-Trebuchet.txt', "r")
lines = f.readlines()

sum = 0

string_number = ["one", 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def convert_numbers(lines, line):
    num1 = 0
    num2 = 0
    x = 0
    numbers = []
    num_string = ''
    for i in lines[line]:
        if i.isnumeric():
            numbers.append(i)
        else:
            num_string += i
        
        if len(num_string) >= 3:
            for number in string_number:
                if number in num_string:
                    numbers.append(string_number.index(number) + 1)
                    num_string = num_string[-1]

    print(numbers)


    num1 = numbers[0]
    num2 = numbers[-1]
    num1 = int(num1) * 10
    x = num1 + int(num2)
    return x
    

for line in range(len(lines)):
    sum += convert_numbers(lines, line)
print(sum)