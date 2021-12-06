with open("input.txt") as f:
    initial = list(map(int, f.read().split(",")))

print(f"{initial=}")
population = [0]*9

for i in initial:
    population[i] += 1

print(f"{population=}")
for _ in range(80):
    temp = population[0]
    for i in range(8):
        population[i] = population[i+1]
    population[6] += temp
    population[8] = temp
print(sum(population))