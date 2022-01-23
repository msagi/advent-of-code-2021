# https://adventofcode.com/2021/day/16
import sys

MAX_INT = sys.maxsize

hex_to_bin_map0 = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1]
}
hex_to_bin_map = {
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


def get_bits_as_numbers(s, o, l):
    v = s[o:o+l]
    return int(v, 2)


def is_all_zeros(s, o):
    for c in range(o, len(s)):
        if s[c] != '0':
            return False
    return True


def parse_packet(bits, offset, max_packets_to_parse, versions):
    packets_parsed = 0
    while (not is_all_zeros(bits, offset)) and packets_parsed < max_packets_to_parse:  # while there is a header
        # get 3 bits = version
        version = get_bits_as_numbers(bits, offset, 3)
        versions.append(version)
        offset += 3
        # get 3 bits = type_id
        type_id = get_bits_as_numbers(bits, offset, 3)
        offset += 3
        # if type_id == 4 then this is a literal value
        if type_id == 4:  # literal value packet
            # get all the next 5 bits...
            #  if the first bit of the 5 bit group is 1 then this is a group of 4 bits of the number
            #  if the first bit of the 5 bit group is 0 then this is the LAST group of 4 bits of the number
            last_group = False
            number_bits = ''
            while not last_group:
                last_group = (get_bits_as_numbers(bits, offset, 1) == 0)
                offset += 1
                number_bits += bits[offset:offset+4]
                offset += 4
            number = int(number_bits, 2)
            packets_parsed += 1
        else:  # operator packets
            operator_length_id = get_bits_as_numbers(bits, offset, 1)
            offset += 1
            if operator_length_id == 0:
                sub_packets_length = get_bits_as_numbers(bits, offset, 15)
                offset += 15
                parse_packet(bits[offset:offset+sub_packets_length], 0, MAX_INT, versions)
                offset += sub_packets_length
                packets_parsed += 1
            else:
                assert operator_length_id == 1
                number_of_sub_packets = get_bits_as_numbers(bits, offset, 11)
                offset += 11
                offset += parse_packet(bits[offset:], 0, number_of_sub_packets, versions)
                packets_parsed += 1
        # there CAN be some extra 0s at the end due to the HEXA representation -> when parsed to bit stream
    return offset


# load file
infile = open('16/input.txt', 'r')
lines = infile.readlines()
infile.close()

# parse input
line = lines[0].strip()
# convert hexa to bitstream
bits = ""
for c in line:
    bits += hex_to_bin_map[c]

versions = []
parse_packet(bits, 0, MAX_INT, versions)
print(sum(versions))  # 977

print("OK")
