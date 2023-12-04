lines = open('Day4-Scratchcards.txt').read().split('\n')


def get_card_points():
    total_card_points = 0
    for line in lines:
        winning_numbers, actual_numbers = line.split('|')
        _, winning_numbers = winning_numbers.split(":")
        winning_numbers = winning_numbers.strip().split(" ")
        actual_numbers = actual_numbers.strip().split(" ")
        win_temp = []
        act_temp = []
        for number in winning_numbers:
            if number == "":
                continue
            win_temp.append(int(number))
        for number in actual_numbers:
            if number == "":
                continue
            act_temp.append(int(number))
        card_points = 0
        first_num = True
        for number in act_temp:
            if number in win_temp:
                if first_num:
                    card_points += 1
                    first_num = False
                else:
                    card_points *= 2
        total_card_points += card_points
    print(f"Total card points - {total_card_points}")



get_card_points()