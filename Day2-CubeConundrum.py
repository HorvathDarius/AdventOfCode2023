f = open('Day2-CubeConundrum.txt')

cubes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

game_ids = 0

lines = f.readlines()
for line in lines:
    # print(line)
    curr_game = line.split(";")
    game_id, curr_game[0] = curr_game[0].split(":")
    _, game_id = game_id.split(" ")
    # print(game_id)
    add_game = True
    for batch in curr_game:
        if batch[-1] == '\n':
            batch = batch[:-1]
        if not add_game:
            break
        # print(batch)
        colors = batch.split(",")
        # print(colors)
        for item in colors:
            item = item.lstrip()
            number, color = item.split(" ")
            # print(number, color)
            if int(number) > cubes[color]:
                add_game = False
    if add_game:
        print(f"Adding game_ID - {game_id}")
        game_ids += int(game_id)

print(game_ids)


