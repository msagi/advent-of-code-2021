# https://adventofcode.com/2021/day/16
import numpy as np
import sys

MAX_INT = sys.maxsize

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
    v = s[o:o + l]
    return int(v, 2)


def is_all_zeros(s, o):
    for c in range(o, len(s)):
        if s[c] != '0':
            return False
    return True


def parse_packet(bits, offset, max_packets_to_parse):
    packets_parsed = 0
    operands = []
    while (not is_all_zeros(bits, offset)) and packets_parsed < max_packets_to_parse:  # while there is a header
        # get 3 bits = version
        version = get_bits_as_numbers(bits, offset, 3)
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
                number_bits += bits[offset:offset + 4]
                offset += 4
            number = int(number_bits, 2)
            operands.append(number)
            packets_parsed += 1
        else:  # operator packets
            numbers = []
            operator_length_id = get_bits_as_numbers(bits, offset, 1)
            offset += 1
            if operator_length_id == 0:
                sub_packets_length = get_bits_as_numbers(bits, offset, 15)
                offset += 15
                _, packet_operands = parse_packet(bits[offset:offset + sub_packets_length], 0, MAX_INT)
                offset += sub_packets_length
                packets_parsed += 1
            else:
                assert operator_length_id == 1
                number_of_sub_packets = get_bits_as_numbers(bits, offset, 11)
                offset += 11
                packet_offset, packet_operands = parse_packet(bits[offset:], 0, number_of_sub_packets)
                offset += packet_offset
                packets_parsed += 1
            if type_id == 0:  # 'sum'
                operands.append(sum(packet_operands))
            elif type_id == 1:  # 'product'
                operands.append(int(np.prod(packet_operands)))
            elif type_id == 2:  # 'minimum'
                operands.append(min(packet_operands))
            elif type_id == 3:  # 'maximum'
                operands.append(max(packet_operands))
            elif type_id == 5:  # 'greater than'
                assert len(packet_operands) == 2
                if packet_operands[0] > packet_operands[1]:
                    operands.append(1)
                else:
                    operands.append(0)
            elif type_id == 6:  # 'less than'
                assert len(packet_operands) == 2
                if packet_operands[0] < packet_operands[1]:
                    operands.append(1)
                else:
                    operands.append(0)
            elif type_id == 7:  # 'equal to'
                assert len(packet_operands) == 2
                if packet_operands[0] == packet_operands[1]:
                    operands.append(1)
                else:
                    operands.append(0)
            else:
                exit(-1)

        # there CAN be some extra 0s at the end due to the HEXA representation -> when parsed to bit stream
    return offset, operands


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

_, result = parse_packet(bits, 0, MAX_INT)
print(result[0])  # 101501020883
print("OK")
