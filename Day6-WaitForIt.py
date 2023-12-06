lines = open('Day6-WaitForIt.txt').read().split('\n')


def get_ways_to_beat():
    time, distance = lines
    _, times = time.split(':')
    _, distances = distance.split(':')
    times = times.strip()

    times = list(map(int, times.split()))
    distances = list(map(int, distances.split()))

    total_ways_to_beat = 1

    for i in range(len(times)):
        race_time = times[i]
        distance_to_beat = distances[i]
        origo_race_time = race_time
        ways_to_beat = 0
        for button_press in range(race_time):
            charge = origo_race_time - button_press
            if charge == origo_race_time:
                continue
            traveled = (race_time - charge) * charge
            if traveled > distance_to_beat:
                ways_to_beat += 1

        total_ways_to_beat *= ways_to_beat

    print(f"Total ways to beat - {total_ways_to_beat}")


def second_get_ways_to_beat():
    time, distance = lines
    _, times = time.split(':')
    _, distances = distance.split(':')
    times = times.strip()

    times = list(map(int, times.split()))
    distances = list(map(int, distances.split()))

    new_time = ''
    new_distance = ''

    for i in range(len(times)):
        new_time += str(times[i])
        new_distance += str(distances[i])

    times = int(new_time)
    distances = int(new_distance)

    total_ways_to_beat = 1

    race_time = times
    distance_to_beat = distances
    origo_race_time = race_time
    ways_to_beat = 0
    for button_press in range(race_time):
        charge = origo_race_time - button_press
        if charge == origo_race_time:
            continue
        traveled = (race_time - charge) * charge
        if traveled > distance_to_beat:
            ways_to_beat += 1

    total_ways_to_beat *= ways_to_beat

    print(f"Total ways to beat version 2 - {total_ways_to_beat}")


get_ways_to_beat()
second_get_ways_to_beat()
