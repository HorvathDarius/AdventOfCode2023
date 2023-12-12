cache = {}

def count(cfg, nums):
    if cfg == "":
        return 1 if nums == () else 0

    if nums == ():
        return 0 if "#" in cfg else 1

    key = (cfg, nums)

    if key in cache:
        return cache[key]

    result = 0

    if cfg[0] in ".?":
        result += count(cfg[1:], nums)

    if cfg[0] in "#?":
        if nums[0] <= len(cfg) and "." not in cfg[:nums[0]] and (nums[0] == len(cfg) or cfg[nums[0]] != "#"):
            result += count(cfg[nums[0] + 1:], nums[1:])

    cache[key] = result
    return result


total = 0
counter = 0
for line in open("Day12-HotSprings.txt"):
    print(counter)
    counter += 1
    cfg, nums = line.split()
    new_cfg = ""
    for i in range(5):
        new_cfg += cfg + "?"
    new_cfg = new_cfg[:-1]
    new_nums = ""
    for i in range(5):
        new_nums += nums + ","
    new_nums = new_nums[:-1]

    new_nums = tuple(map(int, new_nums.split(',')))
    total += count(new_cfg, new_nums)

print(total)
