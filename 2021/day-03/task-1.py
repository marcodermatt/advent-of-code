with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

input_len = len(data)
number_len = len(data[0])

print(f"{input_len=} {number_len=}")

bit_count = [0] * number_len
for line in data:
    for i in range(number_len):
        bit_count[i] += int(line[i])

gamma_rate = epsilon_rate = ""
gamma_rate = gamma_rate.join(["0" if bit_count[i] <= input_len//2 else "1" for i in range(number_len)])
epsilon_rate = epsilon_rate.join(["1" if gamma_rate[i] == "0" else "0" for i in range(number_len)])

print(f"{gamma_rate=} {epsilon_rate=}")
print(int(gamma_rate, 2) * int(epsilon_rate, 2))


