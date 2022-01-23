# https://adventofcode.com/2021/day/22

import re

line_pattern = \
    re.compile("([a-z]+) x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)")


def initialise(arr, status, x1, x2, y1, y2, z1, z2):
    x1 = max(-50, x1)
    x2 = min(50, x2)
    y1 = max(-50, y1)
    y2 = min(50, y2)
    z1 = max(-50, z1)
    z2 = min(50, z2)
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                    arr[x + 50][y + 50][z + 50] = status


def count(arr, x1=-50, x2=50, y1=-50, y2=50, z1=-50, z2=50):
    result = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                    if arr[x + 50][y + 50][z + 50]:
                        result += 1
    return result


def solve(input_file: str):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()

    # parse input
    arr = [[[False for z in range(101)] for y in range(101)] for x in range(101)]
    for line in lines:
        line = line.strip()
        m = line_pattern.match(line)
        if not m:
            exit(-1)
        on = str(m.group(1)) == 'on'
        x1 = int(m.group(2))
        x2 = int(m.group(3))
        y1 = int(m.group(4))
        y2 = int(m.group(5))
        z1 = int(m.group(6))
        z2 = int(m.group(7))
        print("{}, x={}..{}, y={}..{},z={}..{}".format('on' if on else 'off', x1, x2, y1, y2, z1, z2))
        initialise(arr, on, x1, x2, y1, y2, z1, z2)
    print("parse:OK")

    c = count(arr)
    print("Number of active cubes: {}".format(c))
    print("solve:OK")


solve("22/input.txt")  # 652209
print("OK")
