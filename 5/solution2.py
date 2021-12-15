FILENAME = "input"

d = {}

def cmp(a,b):
    return (a > b) - (a < b)

def points_between(x1, x2, y1, y2):
    x_dir = cmp(x2,x1)
    y_dir = cmp(y2,y1)
    points = max(x1 - x2, x2 - x1, y1 - y2, y2 - y1) + 1

    return [f"{x1 + (i*x_dir)},{y1 + (i*y_dir)}" for i in range(points)]

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