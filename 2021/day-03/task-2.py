with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]

number_len = len(data[0])

bit_count = 0
result = data

for i in range(number_len):
    for line in result:
        bit_count += int(line[i])
    most_common_bit = "0" if bit_count < len(result)/2 else "1"
    bit_count = 0
    result = [line for line in result if line[i] == most_common_bit]
    print(f"{result=}")
    if len(result) == 1:
        break
oxygen_rating = int(result[0], 2)

result = data
for i in range(number_len):
    for line in result:
        bit_count += int(line[i])
    most_common_bit = "0" if bit_count < len(result)/2 else "1"
    bit_count = 0
    result = [line for line in result if line[i] != most_common_bit]
    print(f"{result=}")
    if len(result) == 1:
        break

co2_rating = int(result[0], 2)
print(oxygen_rating*co2_rating)

