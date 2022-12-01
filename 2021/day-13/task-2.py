with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

points = set()
folds = []
for line in lines:
    if ',' in line:
        points.add((int(line.split(',')[0]), int(line.split(',')[1])))
    elif '=' in line:
        folds.append(line.split()[2].split('='))

for dir, val in folds:
    val = int(val)
    if dir == 'x':
        points = {(val - (p[0] - val), p[1]) if p[0] > val else p for p in points}
    if dir == 'y':
        points = {(p[0], val - (p[1] - val)) if p[1] > val else p for p in points}

max_x = max(points, key=lambda p: p[0])[0]
max_y = max(points, key=lambda p: p[1])[1]

for y in range(max_y + 1):
    row = ''
    for x in range(max_x + 1):
        if (x, y) in points:
            row += '#'
        else:
            row += '.'
    print(row)

