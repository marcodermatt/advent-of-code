with open("input.txt") as f:
    positions = list(map(int, f.read().split(",")))

fuel_costs = [0]*max(positions)
for crab in positions:
    for i in range(max(positions)):
        fuel_costs[i] += abs(crab-i)

print(min(fuel_costs))