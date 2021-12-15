FILENAME = "input"

with open(FILENAME) as f:
    x = 0
    y = 0

    for line in f:
        instructions = line.split()
        direction = instructions[0]
        distance = int(instructions[1])
        if (direction == "forward"):
            x += distance
        elif (direction == "down"):
            y += distance
        elif (direction == "up"):
            y -= distance

    print(f"[{x},{y}]")
    print(x*y)