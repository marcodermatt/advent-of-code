with open("input.txt") as f:
    template = f.readline().strip()
    f.readline()
    substitutions = {line.split()[0]: line.split()[2] for line in f.readlines()}

for step in range(10):
    new_string = ''
    for i in range(len(template)-1):
        new_string += template[i] + substitutions.get(template[i:i+2], '')
    template = new_string + template[-1]

counts = set()
for element in set(template):
    counts.add(template.count(element))
counts = sorted(counts)
print(counts[-1] - counts[0])
