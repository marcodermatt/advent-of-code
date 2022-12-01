import sys


def val_or_max(x, y):
    try:
        return dp[y][x]
    except IndexError:
        return sys.maxsize


with open("input.txt") as f:
    dp = [[int(i) for i in line.strip()] for line in f.readlines()]

size = len(dp)

for y in range(size - 1, -1, -1):
    for x in range(size - 1, -1, -1):
        if x == y == size - 1:
            continue
        dp[y][x] += min(val_or_max(x, y + 1), val_or_max(x + 1, y))

print(min(dp[0][1], dp[1][0]))
