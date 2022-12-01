with open("input.txt") as f:
    data = f.readlines()

x = z = aim = 0

for line in data:
    direction, value = line.split()
    value = int(value)

    match direction:
        case "forward":
            x += value
            z += value * aim
        case "down":
            aim += value
        case "up":
            aim -= value

print(x*z)


