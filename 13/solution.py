# https://adventofcode.com/2021/day/13

from collections import Counter
import re


def fold_along_y(arr, arr_rows, arr_cols, row:int):
    r_to = row
    for r_from in range(row + 1, arr_rows):
        r_to -= 1
        for c in range(arr_cols):
            if arr[r_from][c] == '#':
                arr[r_to][c] = '#'
                arr[r_from][c] = ' '


def fold_along_x(arr, arr_rows, arr_cols, col:int):
    c_to = col
    for c_from in range(col + 1, arr_cols):
        c_to -= 1
        for r in range(arr_rows):
            if arr[r][c_from] == '#':
                arr[r][c_to] = '#'
                arr[r][c_from] = ' '


def solve(input_file):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()

    # parse input
    coordinates = []
    arr_rows = 0
    arr_cols = 0
    line_index = 0
    while True:
        line = lines[line_index].strip()
        line_index += 1
        if line == "":
            break
        line_coordinates = line.split(',')
        c = int(line_coordinates[0])
        if c > arr_cols:
            arr_cols = c
        r = int(line_coordinates[1])
        if r > arr_rows:
            arr_rows = r
        line_values = (int(r), int(c))
        coordinates.append(line_values)
    arr_rows += 1
    arr_cols += 1
    arr = [[' ' for col in range(arr_cols)] for row in range(arr_rows)]

    for coordinate in coordinates:
        arr[coordinate[0]][coordinate[1]] = '#'

    line_pattern = re.compile("fold along ([xy])=([0-9]+)")
    instruction_counter = 0
    for instruction_index in range(line_index, len(lines)):
        instruction_counter += 1
        instruction = lines[instruction_index].strip()
        m = line_pattern.match(instruction)
        if not m:
            exit(-1)
        dimension = str(m.group(1))
        amount = int(m.group(2))
        if dimension == 'y':
            fold_along_y(arr, arr_rows, arr_cols, amount)
        elif dimension == 'x':
            fold_along_x(arr, arr_rows, arr_cols, amount)
        else:
            exit(-2)
        if instruction_counter == 1:
            count = sum(row.count('#') for row in arr)
            print("count #: {}".format(count))    

    code = ''
    for i in range(6):
        code_line = ''.join(arr[i])
        code += code_line[:40] + '\n'
    print(code)


solve('13/input.txt')  # Part 1 -> 775, Part 2 -> REUPUPKR
print("OK")
