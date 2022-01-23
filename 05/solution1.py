# https://adventofcode.com/2021/day/5

import re

line_pattern = re.compile("([0-9]+),([0-9]+) -> ([0-9]+),([0-9]+)\n")

# load file
infile = open('05/input.txt', 'r')
lines = infile.readlines()
infile.close()

# parse input
vents = []
for line in lines:
    m = line_pattern.match(line)
    if not m:
        print("invalid line: '{}'".format(line))
        exit(-1)
    vent = [min(int(m.group(1)), int(m.group(3))),
            min(int(m.group(2)), int(m.group(4))),
            max(int(m.group(1)), int(m.group(3))),
            max(int(m.group(2)), int(m.group(4)))]
    vents.append(vent)
print("input parsed")

# identify map dimensions
max_x = 0
max_y = 0
for vent in vents:
    max_vent_x = max(vent[0], vent[2])
    if max_vent_x > max_x:
        max_x = max_vent_x
    max_vent_y = max(vent[1], vent[3])
    if max_vent_y > max_y:
        max_y = max_vent_y
print("map dimensions calculated: x:{}, y:{}".format(max_x, max_y))

# generate map
vents_map = []
for y in range(0, max_y + 1):
    vents_map_row = []
    for x in range(0, max_x + 1):
        vents_map_row.append(0)
    vents_map.append(vents_map_row)

for vent in vents:
    if vent[0] == vent[2]:
        # horizontal vent
        print("adding horizontal vent to map: vent:'{},{} -> {},{}'".format(vent[0],vent[1],vent[2],vent[3]))
        for i in range(vent[1], vent[3] + 1):
            vents_map[i][vent[0]] += 1
    elif vent[1] == vent[3]:
        # vertical vent
        print("adding vertical vent to map: vent:'{},{} -> {},{}'".format(vent[0],vent[1],vent[2],vent[3]))
        for i in range(vent[0], vent[2] + 1):
            vents_map[vent[1]][i] += 1
    else:
        # do nothing
        print("skipping diagonal vent to map: vent:'{},{} -> {},{}'".format(vent[0],vent[1],vent[2],vent[3]))
        continue

# find overlaps
answer = 0
for y in range(0, max_y + 1):
    for x in range(0, max_x + 1):
        if vents_map[y][x] > 1:
            answer += 1

print(answer)  # 6564
