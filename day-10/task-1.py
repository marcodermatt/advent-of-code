with open("input.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]

vals = {')': 3, ']': 57, '}': 1197, '>': 25137}
match_char = {'(': ')', '[': ']', '{': '}', '<': '>'}

counter = 0
for line in data:
    stack = []
    while len(line) > 0:
        val = line.pop(0)
        if val in vals:
            if match_char[stack.pop()] != val:
                counter += vals[val]
                break
        else:
            stack.append(val)
print(counter)

