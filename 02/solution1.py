# https://adventofcode.com/2021/day/2

import re

line_pattern = re.compile("([a-z]+) ([0-9]+)\n")

infile = open('02/input.txt', 'r')
lines = infile.readlines()
infile.close()

position = 0
depth = 0
for line in lines:
    m = line_pattern.match(line)
    if not m:
        exit(-1)
    instruction = str(m.group(1))
    amount = int(m.group(2))
    if instruction == 'forward':
        position += amount
    elif instruction == 'down':
        depth += amount
    elif instruction == 'up':
        depth -= amount
print(position*depth)  # 1451208

