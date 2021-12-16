import multiprocessing

FILENAME = "input"
DAYS = 256

# The "more cores" approach - a bit faster, but not enough

def grow(fish_list):
    day = 0
    while day < DAYS:
        new_fish = []
        for index, fish in enumerate(fish_list):
            if fish == 0:
                fish_list[index] = 6
                new_fish.append(8)
            else:
                fish_list[index] -= 1
        day += 1
        fish_list.extend(new_fish)
        print(f"After {day} days: {len(fish_list)} fish")
    return fish_list

with open(FILENAME) as f:
    current_fish = [int(x) for x in f.readline().split(",")]
    group_num = multiprocessing.cpu_count()
    fish_groups = [[] for i in range(group_num)]

    for index, i in enumerate(current_fish):
        if index % group_num == index:
            fish_groups[index] = [i]
        else:
            fish_groups[index % group_num].append(i)
    
    with multiprocessing.Pool(processes=group_num) as pool:
        result = 0
        for i in pool.imap_unordered(grow, fish_groups):
            result += len(i)
        print(f"total: {result}")