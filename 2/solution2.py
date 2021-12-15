FILENAME = "input"

with open(FILENAME) as f:
    x = 0
    y = 0
    aim = 0

    for line in f:
        direction, units = line.split()
        units = int(units)
        if (direction == "forward"):
            x += units
            y += units*aim
        elif (direction == "down"):
            aim += units
        elif (direction == "up"):
            aim -= units

    print(f"[{x},{y}]")
    print(x*y)