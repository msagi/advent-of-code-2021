# https://adventofcode.com/2021/day/14
from collections import Counter
import re
import sys

line_pattern = re.compile("([A-Z]{2}) -> ([A-Z])\n")


def process(template, map):
    template2 = []
    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        template2.append(template[i])
        template2.append(map[pair])
    template2.append(template[len(template) - 1])
    return template2


def solve(input_file):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()

    template = lines[0].strip()

    map = {}
    # parse input
    for r in range(2, len(lines)):
        line = lines[r]
        m = line_pattern.match(line)
        if not m:
            exit(-1)
        pair = str(m.group(1))
        element = str(m.group(2))
        map[pair] = element

    for i in range(10):
        template = process(template, map)

    counts = Counter(template).most_common()
    _, max_count = counts[0]
    _, min_count = counts[-1]

    return max_count - min_count

print(solve('14/sample_input.txt'))  # 1588
print(solve('14/input.txt'))  # 2587
print("OK")
