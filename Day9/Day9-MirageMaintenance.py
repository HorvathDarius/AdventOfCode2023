lines = open('Day9-MirageMaintenance.txt').read().split("\n")

histories = []
histories_value = 0
for line in lines:
    nrs = line.split()
    new_line = []
    for x in nrs:
        new_line.append(int(x))
    histories.append(new_line)

for history in histories:
    all_zeros = False
    diffs_array = []
    analyze_history = history

    # Find all histories, until you get history: 0 0 0 0 ...
    while not all_zeros:
        diff_history = []
        number_1 = 0
        number_2 = 0
        for i in range(len(analyze_history) - 1):
            number_1 = analyze_history[i]
            number_2 = analyze_history[i+1]
            diff = number_2 - number_1
            diff_history.append(diff)
        analyze_history = diff_history
        diffs_array.append(diff_history)
        all_zeros = True
        for n in analyze_history:
            if n != 0:
                all_zeros = False

    # Generate next history number
    diffs_array.reverse()

    adding_number = 0
    for diff in diffs_array:
        adding_number += diff[-1]

    adding_number += history[-1]
    histories_value += adding_number

print(f"Final value - {histories_value}")
