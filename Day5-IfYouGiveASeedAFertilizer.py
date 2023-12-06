def read_file(file_name):
    with open(file_name, "r") as file:
        return file.read()

seeds, *rest = read_file("Day5-IfYouGiveASeedAFertilizer.txt").split("\n\n")
seeds = list(map(lambda x: int(x), seeds.split(":")[1].split()))


for part in rest:
    intervals = []
    for l in part.split('\n')[1:]:
        intervals.append(list(map(lambda x: int(x), l.split())))

    new_seeds = []
    for seed in seeds:
        for start_src, start_dst, increment in intervals: # 50 98 2
            if start_dst <= seed < start_dst + increment:
                new_seeds.append(seed - start_dst + start_src)
                break
        else:
            new_seeds.append(seed)
    seeds = new_seeds

print(min(seeds))


