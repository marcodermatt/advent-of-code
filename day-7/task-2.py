with open("small-input.txt") as f:
    positions = list(map(int, f.read().split(",")))

fuel_costs = [0]*max(positions)
for crab in positions:
    for i in range(max(positions)):
        distance = abs(crab-i)
        fuel_costs[i] += (distance * (distance + 1))//2

print(min(fuel_costs))