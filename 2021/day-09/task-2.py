def count_region(x, y):
    data[y][x] = True
    size = 1
    if x != 0 and not data[y][x - 1]:
       size += count_region(x - 1, y)
    if x != max_x - 1 and not data[y][x + 1]:
        size += count_region(x + 1, y)
    if y != 0 and not data[y - 1][x]:
        size += count_region(x, y - 1)
    if y != max_y - 1 and not data[y + 1][x]:
        size += count_region(x, y + 1)
    return size

with open("input.txt") as f:
    data = [[cell == '9' for cell in line.strip()] for line in f.readlines()]

max_y = len(data)
max_x = len(data[0])
regions = []
for y in range(max_y):
    for x in range(max_x):
        if not data[y][x]:
            size = count_region(x, y)
            regions.append(size)

out = 1
for i in range(3):
    out *= max(regions)
    regions.remove(max(regions))
print(out)