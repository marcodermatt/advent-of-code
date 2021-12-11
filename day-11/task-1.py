def flash_octopuses(x, y):
    count = 1
    data[y][x][1] = True
    if x != 0:
        if not data[y][x - 1][1]:
            data[y][x - 1][0] += 1
            if data[y][x - 1][0] > 9:
                count += flash_octopuses(x - 1, y)
        if y != 0 and not data[y - 1][x - 1][1]:
            data[y - 1][x - 1][0] += 1
            if data[y - 1][x - 1][0] > 9:
                count += flash_octopuses(x - 1, y - 1)
        if y != max_y - 1 and not data[y + 1][x - 1][1]:
            data[y + 1][x - 1][0] += 1
            if data[y + 1][x - 1][0] > 9:
                count += flash_octopuses(x - 1, y + 1)
    if x != max_x - 1:
        if not data[y][x + 1][1]:
            data[y][x + 1][0] += 1
            if data[y][x + 1][0] > 9:
                count += flash_octopuses(x + 1, y)
        if y != 0 and not data[y - 1][x + 1][1]:
            data[y - 1][x + 1][0] += 1
            if data[y - 1][x + 1][0] > 9:
                count += flash_octopuses(x + 1, y - 1)
        if y != max_y - 1 and not data[y + 1][x + 1][1]:
            data[y + 1][x + 1][0] += 1
            if data[y + 1][x + 1][0] > 9:
                count += flash_octopuses(x + 1, y + 1)
    if y != 0 and not data[y - 1][x][1]:
        data[y - 1][x][0] += 1
        if data[y - 1][x][0] > 9:
            count += flash_octopuses(x, y - 1)
    if y != max_y - 1 and not data[y + 1][x][1]:
        data[y + 1][x][0] += 1
        if data[y + 1][x][0] > 9:
            count += flash_octopuses(x, y + 1)
    return count

with open("input.txt") as f:
    data = [[[int(cell), False] for cell in line.strip()] for line in f.readlines()]

max_y = len(data)
max_x = len(data[0])

count = 0
for i in range(100):
    for y in range(max_y):
        for x in range(max_x):
            data[y][x][0] += 1

    for y in range(max_y):
        for x in range(max_x):
            if not data[y][x][1] and data[y][x][0] > 9:
                count += flash_octopuses(x, y)

    for y in range(max_y):
        for x in range(max_x):
            if data[y][x][1]:
                data[y][x][0] = 0
                data[y][x][1] = False



print(count)

