with open("input.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]

vals = {')': 1, ']': 2, '}': 3, '>': 4}
match_char = {'(': ')', '[': ']', '{': '}', '<': '>'}

counter = 0
scores = []
for line in data:
    stack = []
    while len(line) > 0:
        val = line.pop(0)
        if val in vals:
            if match_char[stack.pop()] != val:
                stack = []
                break
        else:
            stack.append(val)
    if len(stack) > 0:
        score = 0
        while len(stack) > 0:
            score *= 5
            score += vals[match_char[stack.pop()]]
        scores.append(score)
scores.sort()
print(scores[len(scores)//2])

