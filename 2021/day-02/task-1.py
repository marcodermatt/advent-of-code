with open("input.txt") as f:
    data = f.readlines()

x = z = 0

for line in data:
    direction, value = line.split()
    value = int(value)

    match direction:
        case "forward":
            x += value
        case "down":
            z += value
        case "up":
            z -= value

print(x*z)


