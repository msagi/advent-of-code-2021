# https://adventofcode.com/2021/day/22
import re

"""
This challenge cannot be solved with brute force within reasonable time, due to the x,y,z boundaries 
set too wide, it takes extremely long to apply each 'boot command' to the whole 3D space.

However, some cubes are switched on/off in a group, not one by one. If we create a 'shrunk' 3D space
where one 'pixel' of this shrunk space maps to a group of cubes in the REAL 3D space which are switching 
on/of TOGETHER, then we only need to iterate through this shrunk 3D space which is significantly faster.

We need to keep track of the 'distance shrunk' for each group because this is different group by group. 
We will need this distance to calculate how many REAL cubes we have ON after executing the 
'booting command sequence' in 'shrunk' space.
"""

line_pattern = \
    re.compile("([a-z]+) x=(-?[0-9]+)..(-?[0-9]+),y=(-?[0-9]+)..(-?[0-9]+),z=(-?[0-9]+)..(-?[0-9]+)")


def translate_real_to_shrunk(coordinates):
    # create a 'shrunk' map where similarly behaving cubes are clubbed
    # so real 3D space coordinates of 1, 11, 15, 31
    # will be mapped to 'shrunk' space coordinates of 0, 1, 2, 3

    # to be able to calculate distances, coordinates needs to be sorted
    coordinates = sorted(coordinates)

    real_to_shrunk_coordinate_map = {}
    shrunk_coordinate_real_size_map = {}

    for i in range(len(coordinates)):
        # map real World boundary coordinates to 'shrunk' coordinates
        real_to_shrunk_coordinate_map[coordinates[i]] = i
        if i+1 < len(coordinates):
            # calculate the number of real World cubes this single 'shrunk' coordinate represents
            shrunk_coordinate_real_size_map[i] = coordinates[i + 1] - coordinates[i]
    return real_to_shrunk_coordinate_map, shrunk_coordinate_real_size_map


def solve(input_file: str):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()

    # parse input
    commands = []
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
        command = [on, x1, x2, y1, y2, z1, z2]
        commands.append(command)
        print("{}, x={}..{}, y={}..{},z={}..{}".format('on' if on else 'off', x1, x2, y1, y2, z1, z2))
    print("parse:OK")

    # for a real space with commands UP [1..10] and UP [15..30]
    # it looks like UP [1..10], DOWN [11..14], UP [15..30]
    # which can be written in the form of "COMMAND (<start_coordinate>, <number_of_cubes_switching_together>)
    # e.g. UP (1,10) , DOWN (11,4) , UP (15,16)
    # so boundary markers will be at 1, 11, 15, 31
    # and lengths will be 10, 4, 16, 0
    # note: to get the boundaries right, the 2nd coordinates of each dimension need to be adjusted by 1
    x_bounds = set()
    y_bounds = set()
    z_bounds = set()
    for on, x1, x2, y1, y2, z1, z2 in commands:
        x_bounds.add(x1)
        x_bounds.add(x2 + 1)
        y_bounds.add(y1)
        y_bounds.add(y2 + 1)
        z_bounds.add(z1)
        z_bounds.add(z2 + 1)

    # create a 'shrunk' map where similarly behaving cubes are clubbed
    # so read space coordinates of 1, 11, 15, 31
    # will be mapped to 'shrunk' space coordinates of 0, 1, 2, 3
    x_bounds, x_sizes = translate_real_to_shrunk(x_bounds)
    y_bounds, y_sizes = translate_real_to_shrunk(y_bounds)
    z_bounds, z_sizes = translate_real_to_shrunk(z_bounds)

    # create the 'shrunk' 3D space with all coordinates turned off
    shrunk_space = [[[False for z in range(len(z_bounds))] for y in range(len(y_bounds))] for x in range(len(x_bounds))]
    # go through each rules and do the switch on/off in 'shrunk' space
    for on, x1, x2, y1, y2, z1, z2 in commands:
        for x in range(x_bounds[x1], x_bounds[x2 + 1]):  # note: adjust 2nd coordinates again to hit the right boundary
            for y in range(y_bounds[y1], y_bounds[y2 + 1]):
                for z in range(z_bounds[z1], z_bounds[z2 + 1]):
                    shrunk_space[x][y][z] = on
    # 'shrunk' space switching done

    # map each 'shrunk' space coordinate to the real space number of cubes it represents
    result = 0
    for x in range(len(x_bounds)):
        for y in range(len(y_bounds)):
            for z in range(len(z_bounds)):
                if shrunk_space[x][y][z]:  # if 'shrunk' space coordinate is turned on
                    x_size = x_sizes[x]
                    y_size = y_sizes[y]
                    z_size = z_sizes[z]
                    result += x_size * y_size * z_size

    print(result)
    print("solve:OK")


solve("22/input.txt")  # 1217808640648260
print("OK")
