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


get_ways_to_beat()
