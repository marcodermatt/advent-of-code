def pop_bits(bits, n):
    return int(bits[:n], 2), bits[n:]

def parse_packet(bits):
    version, bits = pop_bits(bits, 3)
    packet_type, bits = pop_bits(bits, 3)
    if packet_type == 4:
        literal = ''
        prefix = 1
        while prefix:
            prefix, bits = pop_bits(bits, 1)
            literal_part, bits = bits[:4], bits[4:]
            literal += literal_part
        result = int(literal, 2)
    else:
        l_type, bits = pop_bits(bits, 1)
        vals = []
        if l_type == 0:
            sub_packet_length, bits = pop_bits(bits, 15)
            current_len = len(bits)
            while current_len - len(bits) < sub_packet_length:
                sub_result, bits = parse_packet(bits)
                vals.append(sub_result)
        else:
            n_packets, bits = pop_bits(bits, 11)
            for i in range(n_packets):
                sub_result, bits = parse_packet(bits)
                vals.append(sub_result)

        match packet_type:
            case 0:
                result = sum(vals)
            case 1:
                result = vals[0]
                for val in vals[1:]:
                    result *= val
            case 2:
                result = min(vals)
            case 3:
                result = max(vals)
            case 5:
                result = 1 if vals[0] > vals[1] else 0
            case 6:
                result = 1 if vals[0] < vals[1] else 0
            case 7:
                result = 1 if vals[0] == vals[1] else 0
    return result, bits

hex_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
with open("input.txt") as f:
    bit_string = ''.join(hex_map[c] for c in f.readline())

result, _ = parse_packet(bit_string)
print(result)


