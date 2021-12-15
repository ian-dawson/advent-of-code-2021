FILENAME = "input"

with open(FILENAME) as f:
    count = 0
    previous = None

    lines = f.read().splitlines()

    for index, line in enumerate(lines):
        if (index + 2 < len(lines)):
            current = int(line) + int(lines[index+1]) + int(lines[index+2])
            if previous is not None:
                if current > previous:
                    count += 1
            previous = current

    print(count)