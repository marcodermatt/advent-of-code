import sys


def val_or_max(x, y):
    if x < 0 or y < 0:
        return sys.maxsize
    try:
        return big_dp[y][x] or sys.maxsize
    except IndexError:
        return sys.maxsize


def new_val(x, y):
    val = dp[y % size][x % size] + x // size + y // size
    return val if val < 10 else val % 10 + 1


with open("input.txt") as f:
    dp = [[int(i) for i in line.strip()] for line in f.readlines()]

size = len(dp)
full_size = size * 5
big_dp = [[0] * full_size for i in range(full_size)]

big_dp[full_size - 1][full_size - 1] = new_val(full_size - 1, full_size - 1)

for y in range(full_size - 1, - 1, - 1):
    for x in range(full_size - 1, -1, -1):
        if x == y == full_size - 1:
            continue
        big_dp[y][x] = min(val_or_max(x + 1, y), val_or_max(x, y + 1)) + new_val(x, y)

for i in range(4):
    for y in range(full_size - 1, - 1, - 1):
        for x in range(full_size - 1, -1, -1):
            if x == y == full_size - 1:
                continue
            big_dp[y][x] = min(val_or_max(x + 1, y), val_or_max(x, y + 1), val_or_max(x - 1, y), val_or_max(x, y - 1)) + new_val(x, y)

print(min(big_dp[0][1], big_dp[1][0]))
