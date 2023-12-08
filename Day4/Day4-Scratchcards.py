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


def get_matching_cards():
    total_cards = []
    for line in lines:
        winning_numbers, actual_numbers = line.split('|')
        card, winning_numbers = winning_numbers.split(":")
        _, card_nr = card.split("d")
        card_nr = int(card_nr.strip())
        total_cards.append(card_nr)

    for number in total_cards:
        line = lines[number-1]
        winning_numbers, actual_numbers = line.split('|')
        card, winning_numbers = winning_numbers.split(":")
        _, card_nr = card.split("d")
        card_nr = int(card_nr.strip())
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
        for number in act_temp:
            if number in win_temp:
                card_points += 1
        new_card_nr = card_nr
        for i in range(card_points):
            new_card_nr += 1
            total_cards.append(new_card_nr)
    print(f"Len - {len(total_cards)}")


get_card_points()
get_matching_cards()