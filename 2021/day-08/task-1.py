with open("input.txt") as f:
    data = [[len(entry) for entry in line.split()[11:]] for line in f.readlines()]

print(sum([sum([line.count(i) for i in (2, 3, 4, 7)]) for line in data]))