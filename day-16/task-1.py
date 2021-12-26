def pop_bits(bits, n):
    return int(bits[:n], 2), bits[n:]

def parse_packet_and_sum_versions(bits):
    version, bits = pop_bits(bits, 3)
    packet_type, bits = pop_bits(bits, 3)
    if packet_type == 4:
        while int(bits[0]):
            _, bits = pop_bits(bits, 5)
        _, bits = pop_bits(bits, 5)
    else:
        l_type, bits = pop_bits(bits, 1)
        if l_type == 0:
            sub_packet_length, bits = pop_bits(bits, 15)
            current_len = len(bits)
            while current_len - len(bits) < sub_packet_length:
                sub_sum, bits = parse_packet_and_sum_versions(bits)
                version += sub_sum
        else:
            n_packets, bits = pop_bits(bits, 11)
            for i in range(n_packets):
                sub_sum, bits = parse_packet_and_sum_versions(bits)
                version += sub_sum
    return version, bits

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

version_sum, _ = parse_packet_and_sum_versions(bit_string)
print(version_sum)


