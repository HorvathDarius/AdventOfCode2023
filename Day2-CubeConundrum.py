cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def power_of_cubes_set():
    lines = f.readlines()
    total_set_power = 0
    for line in lines:
        min_colors = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        curr_game = line.split(";")
        game_id, curr_game[0] = curr_game[0].split(":")
        for batch in curr_game:
            if batch[-1] == '\n':
                batch = batch[:-1]
            colors = batch.split(",")
            for item in colors:
                item = item.lstrip()
                number, color = item.split(" ")
                if int(number) > min_colors[color]:
                    min_colors[color] = int(number)
        set_power = min_colors['red'] * min_colors["blue"] * min_colors["green"]
        # print(f"{game_id} - {set_power}")
        total_set_power += set_power
    print(f"Total set power - {total_set_power}")


def minimum_cubes_in_bag():
    game_ids = 0
    lines = f.readlines()
    for line in lines:
        curr_game = line.split(";")
        game_id, curr_game[0] = curr_game[0].split(":")
        _, game_id = game_id.split(" ")
        add_game = True
        for batch in curr_game:
            if batch[-1] == '\n':
                batch = batch[:-1]
            if not add_game:
                break
            colors = batch.split(",")
            # print(colors)
            for item in colors:
                item = item.lstrip()
                number, color = item.split(" ")
                if int(number) > cubes[color]:
                    add_game = False
        if add_game:
            game_ids += int(game_id)

    print(f"Sum of possible game IDs: {game_ids}")


f = open('Day2-CubeConundrum.txt')
minimum_cubes_in_bag()
f = open('Day2-CubeConundrum.txt')
power_of_cubes_set()
