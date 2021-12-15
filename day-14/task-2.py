from collections import defaultdict, Counter

def substitute_and_count(depth):
    pair = ''.join(stack[:2])
    if pair in substitutions:
        if depth < 40:
            char = substitutions.get(pair)
            stack.insert(1, char)
            counts.update({char: counts[char] + 1})
            substitute_and_count(depth + 1)
            substitute_and_count(depth + 1)
        else:
            stack.pop(0)
    else:
        stack.pop(0)

with open("input.txt") as f:
    template = f.readline().strip()
    f.readline()
    substitutions = {line.split()[0]: line.split()[2] for line in f.readlines()}

stack = list(template)
depth = [0]
counts = defaultdict(lambda: 0)
counts.update(Counter(stack))
i = 0
while len(stack) > 1:
    i += 1
    print(i)
    substitute_and_count(0)

print(max(counts.values()) - min(counts.values()))
