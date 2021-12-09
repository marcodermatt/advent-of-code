with open("input.txt") as f:
    data = [[int(cell) for cell in line.strip()] for line in f.readlines()]

max_y = len(data)
max_x = len(data[0])
count = 0
for y in range(max_y):
    for x in range(max_x):
        val = data[y][x]
        if ((x == 0 or data[y][x - 1] > val) and (x == max_x - 1 or data[y][x + 1] > val) and
                (y == 0 or data[y - 1][x] > val) and (y == max_y - 1 or data[y + 1][x] > val)):
            count += val + 1

print(count)