FILENAME = "input"

DAYS = 80

with open(FILENAME) as f:
    current_fish = [int(x) for x in f.readline().split(",")]
    print(f"Initial state: {current_fish}")
    day = 0

    while day < DAYS:
        new_fish = []

        for index, fish in enumerate(current_fish):
            if fish == 0:
                current_fish[index] = 6
                new_fish.append(8)
            else:
                current_fish[index] -= 1
        current_fish.extend(new_fish)
        day += 1
        print(f"After {day} days: {len(current_fish)} fish")
