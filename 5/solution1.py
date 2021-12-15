FILENAME = "input"

d = {}

def points_between(x1, x2, y1, y2):
    if x1 == x2:
        y_coords = sorted([y1, y2])
        return [f"{x1},{y_coords[0] + i}" for i in range(y_coords[1] - y_coords[0] + 1)]
    elif y1 == y2:
        x_coords = sorted([x1, x2])
        return [f"{x_coords[0] + i},{y1}" for i in range(x_coords[1] - x_coords[0] + 1)]
    else:
        return []

with open(FILENAME) as f:
    for line in f:
        line = line.strip()
        start, end = line.split(" -> ")
        x1, y1 = [int(i) for i in start.split(",")]
        x2, y2 = [int(i) for i in end.split(",")]
    
        coords = points_between(x1, x2, y1, y2)

        for coord in coords:
            d[coord] = d.get(coord, 0) + 1
      
    print(len([count for count in d.values() if count >= 2]))