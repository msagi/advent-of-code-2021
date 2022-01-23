# https://adventofcode.com/2021/day/14

from collections import Counter

"""Due to the 40x steps to be calculated for Part 2, an entirely new algorithm is needed.

Every XY slice of the whole polymer, with an XY -> Z rule, the slice will be transformed to 
two slices, such as XZ and ZY.
Note: This will double all character counts in the polymer, except the very last one 
(which will not have rule applied therefore stay as is) and we will correct this very last 
character count at the very end of the calculation.
"""

def process(counter, rule_map):
    counter2 = Counter()  # e.g. for 'XY -> Z' case
    for key in counter:  # key = XY
        value = counter[key]  # value = count of XY in the polymer
        rule_char = rule_map[key]  # rule_char = Z
        key1 = key[0] + rule_char  # key1 = XZ
        key2 = rule_char + key[1]  # key2 = ZY
        counter2[key1] += value  # add previous count of XY to the count of XZ
        counter2[key2] += value  # add previous count of XY to the count of ZY
    return counter2


def solve(input_file):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()

    # initial polymer
    polymer = lines[0].strip()

    # count the character pairs in the template
    counter = Counter()
    for i in range(len(polymer) - 1):
        pair = polymer[i] + polymer[i + 1]
        counter[pair] += 1

    # parse rules
    rule_map = {}
    for r in range(2, len(lines)):
        line = lines[r].strip()
        pair, element = line.split(' -> ')
        rule_map[pair] = element

    # run the iterations
    for i in range(40):
        counter = process(counter, rule_map)

    # calculate result
    element_counter = Counter()
    for key in counter:
        value = counter[key]
        key1 = key[0]
        element_counter[key1] += value
    # since we counted only the first character of the key,
    # we will miss the last character of the original polimer,
    # so adding it here
    element_counter[polymer[-1]] += 1

    max_count = max(element_counter.values())
    min_count = min(element_counter.values())
    return max_count - min_count


print(solve('14/sample_input.txt'))  # 2188189693529
print(solve('14/input.txt'))  # 3318837563123
print("OK")
