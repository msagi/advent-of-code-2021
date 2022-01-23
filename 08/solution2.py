# https://adventofcode.com/2021/day/8
from itertools import permutations

# load file
infile = open('08/input.txt', 'r')
lines = infile.readlines()
infile.close()

TOP = 0
TOP_LEFT = 1
TOP_RIGHT = 2
MIDDLE = 3
BOTTOM_LEFT = 4
BOTTOM_RIGHT = 5
BOTTOM = 6


def get_digit_patterns_for_segments(segments_map):
    digits = []
    zero = "{}{}{}{}{}{}".format(
        segments_map[TOP],
        segments_map[TOP_LEFT],
        segments_map[TOP_RIGHT],
        segments_map[BOTTOM_LEFT],
        segments_map[BOTTOM_RIGHT],
        segments_map[BOTTOM]
    )
    one = "{}{}".format(
        segments_map[TOP_RIGHT],
        segments_map[BOTTOM_RIGHT]
    )
    two = "{}{}{}{}{}".format(
        segments_map[TOP],
        segments_map[TOP_RIGHT],
        segments_map[MIDDLE],
        segments_map[BOTTOM_LEFT],
        segments_map[BOTTOM]
    )
    three = "{}{}{}{}{}".format(
        segments_map[TOP],
        segments_map[TOP_RIGHT],
        segments_map[MIDDLE],
        segments_map[BOTTOM_RIGHT],
        segments_map[BOTTOM]
    )
    four = "{}{}{}{}".format(
        segments_map[TOP_LEFT],
        segments_map[TOP_RIGHT],
        segments_map[MIDDLE],
        segments_map[BOTTOM_RIGHT]
    )
    five = "{}{}{}{}{}".format(
        segments_map[TOP],
        segments_map[TOP_LEFT],
        segments_map[MIDDLE],
        segments_map[BOTTOM_RIGHT],
        segments_map[BOTTOM]
    )
    six = "{}{}{}{}{}{}".format(
        segments_map[TOP],
        segments_map[TOP_LEFT],
        segments_map[MIDDLE],
        segments_map[BOTTOM_LEFT],
        segments_map[BOTTOM_RIGHT],
        segments_map[BOTTOM]
    )
    seven = "{}{}{}".format(
        segments_map[TOP],
        segments_map[TOP_RIGHT],
        segments_map[BOTTOM_RIGHT]
    )
    eight = "{}{}{}{}{}{}{}".format(
        segments_map[TOP],
        segments_map[TOP_LEFT],
        segments_map[TOP_RIGHT],
        segments_map[MIDDLE],
        segments_map[BOTTOM_LEFT],
        segments_map[BOTTOM_RIGHT],
        segments_map[BOTTOM]
    )
    nine = "{}{}{}{}{}{}".format(
        segments_map[TOP],
        segments_map[TOP_LEFT],
        segments_map[TOP_RIGHT],
        segments_map[MIDDLE],
        segments_map[BOTTOM_RIGHT],
        segments_map[BOTTOM]
    )
    digits.append(''.join(sorted(zero)))
    digits.append(''.join(sorted(one)))
    digits.append(''.join(sorted(two)))
    digits.append(''.join(sorted(three)))
    digits.append(''.join(sorted(four)))
    digits.append(''.join(sorted(five)))
    digits.append(''.join(sorted(six)))
    digits.append(''.join(sorted(seven)))
    digits.append(''.join(sorted(eight)))
    digits.append(''.join(sorted(nine)))
    return digits


# prepare data
sorted_lines = []
for line in lines:
    line = line.strip()
    line_parts = line.split(' | ')
    unique_signal_patterns = line_parts[0].split(' ')
    four_digit_output_value = line_parts[1].split(' ')
    line_values = unique_signal_patterns + four_digit_output_value
    sorted_line_values = []
    for line_value in line_values:
        sorted_line_values.append(''.join(sorted(line_value)))
    sorted_lines.append(sorted_line_values)

possible_digit_permutations = [''.join(p) for p in permutations('abcdefg')]
possible_number_digit_configurations = []
for possible_digit_permutation in possible_digit_permutations:
    possible_number_digit_configurations.append(get_digit_patterns_for_segments(possible_digit_permutation))

# process input
answer = 0
for number_patterns in sorted_lines:
    print("line: {}".format(number_patterns))
    for possible_number_digit_configuration_values in possible_number_digit_configurations:
        match = True
        for number_pattern in number_patterns:
            if number_pattern not in possible_number_digit_configuration_values:
                match = False
                break
        if match:
            line_result = ''
            for i in range(10, 14):
                line_result += str(possible_number_digit_configuration_values.index(number_patterns[i]))
            print("entry value: {}, configuration: {}".format(line_result, possible_number_digit_configuration_values))
            answer += int(line_result)

print(answer)  # 975706
print("OK")
