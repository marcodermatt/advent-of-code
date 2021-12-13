with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

points = set()
folds = []
for line in lines:
    if ',' in line:
        points.add((int(line.split(',')[0]), int(line.split(',')[1])))
    elif '=' in line:
        folds.append(line.split()[2].split('='))

val = int(folds[0][1])
points = {(val - (p[0] - val), p[1]) if p[0] > val else p for p in points}
print(len(points))

