with open("input.txt") as f:
    template = f.readline().strip()
    f.readline()
    substitutions = {line.split()[0]: line.split()[2] for line in f.readlines()}

pairs = {}
for i in range(len(template) - 1): pairs.update({template[i:i + 2]: pairs.get(template[i:i + 2], 0) + 1})
for step in range(40):
    new_pairs = {}
    for pair, val in pairs.items():
        if pair in substitutions:
            sub = substitutions[pair]
            pair_one = pair[0] + sub
            pair_two = sub + pair[1]
            new_pairs.update({pair_one: new_pairs.get(pair_one, 0) + val, pair_two: new_pairs.get(pair_two, 0) + val})
    pairs = new_pairs

counts = {template[-1]: 1}
for pair, val in pairs.items():
    counts[pair[0]] = counts.get(pair[0], 0) + val
print(max(counts.values())-min(counts.values()))
