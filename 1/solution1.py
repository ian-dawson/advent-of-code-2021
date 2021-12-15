FILENAME = "input"

with open(FILENAME) as f:
    count = 0
    previous = None

    for line in f:
        current = int(line)
        if previous is not None:
            if current > previous:
                count += 1
        previous = current

    print(count)