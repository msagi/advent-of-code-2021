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
    vent = []
    for i in range(1, 5):
        vent.append(int(m.group(i)))
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
for x in range(0, max_x + 1):
    vents_map_row = []
    for y in range(0, max_y + 1):
        vents_map_row.append(0)
    vents_map.append(vents_map_row)

for vent in vents:
    if vent[0] == vent[2]:
        # horizontal vent
        print("adding horizontal vent to map: vent:'{},{} -> {},{}'".format(vent[0],vent[1],vent[2],vent[3]))
        start_y = min(vent[1], vent[3])
        stop_y = max(vent[1], vent[3])
        for i in range(start_y, stop_y + 1):
            vents_map[vent[0]][i] += 1
    elif vent[1] == vent[3]:
        # vertical vent
        print("adding vertical vent to map: vent:'{},{} -> {},{}'".format(vent[0],vent[1],vent[2],vent[3]))
        start_x = min(vent[0], vent[2])
        stop_x = max(vent[0], vent[2])
        for i in range(start_x, stop_x + 1):
            vents_map[i][vent[1]] += 1
    else:
        # diagonal vent
        print("diagonal vent to map: vent:'{},{} -> {},{}'".format(vent[0],vent[1],vent[2],vent[3]))
        x = vent[0]
        y = vent[1]
        vents_map[x][y] += 1
        while x != vent[2] and y != vent[3]:
            if x < vent[2]:
                x += 1
            else:
                x -= 1
            if y < vent[3]:
                y += 1
            else:
                y -= 1
            vents_map[x][y] += 1

# find overlaps
answer = 0
for y in range(0, max_y + 1):
    for x in range(0, max_x + 1):
        if vents_map[x][y] > 1:
            answer += 1

print(answer)  # 19172
