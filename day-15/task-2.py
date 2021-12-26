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
big_dp = [[0] * size * 5 for i in range(size * 5)]

big_dp[size * 5 - 1][size * 5 - 1] = new_val(size * 5 - 1, size * 5 - 1)
x = size * 5 - 2
y = size * 5 - 1
while y >= 0:
    while x >= 0:
        risk = new_val(x, y)
        min_n = sys.maxsize
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            neighbour = val_or_max(x + dx, y + dy)
            min_n = min(min_n, neighbour)
        current_val = min_n + risk
        big_dp[y][x] = current_val
        for dx, dy in ((0, 1), (1, 0)):
            neighbour = val_or_max(x + dx, y + dy)
            if neighbour != sys.maxsize:
                neighbour_risk = new_val(x + dx, y + dy)
                if neighbour - neighbour_risk > current_val:
                    big_dp[y + dy][x + dx] = current_val + neighbour_risk
                    x += dx
                    y += dy
                    break
        x -= 1
    x = size * 5 - 1
    y -= 1

print(min(big_dp[0][1], big_dp[1][0]))
