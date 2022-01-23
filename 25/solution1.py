# https://adventofcode.com/2021/day/25
from copy import copy, deepcopy


def move_east(arr, rows, cols):
    move = False
    arr2 = deepcopy(arr)
    for r in range(rows):
        for c in range(cols):
            if arr[r][c] == '>':  # if 'east' facing sea cucumber
                c2 = (c + 1) % cols
                if arr[r][c2] == '.':  # the place to move 'east' is free
                    arr2[r][c2] = '>'
                    arr2[r][c] = '.'
                    move = True
    return move, arr2


def move_south(arr, rows, cols):
    move = False
    arr2 = deepcopy(arr)
    for r in range(rows):
        r2 = (r + 1) % rows
        for c in range(cols):
            if arr[r][c] == 'v':  # if 'south' facing sea cucumber
                if arr[r2][c] == '.':  # the place to move 'south' is free
                    arr2[r2][c] = 'v'
                    arr2[r][c] = '.'
                    move = True
    return move, arr2


def print_state(step, arr, rows, cols):
    state = ''
    if step == 0:
        state += 'Initial state:\n'
    elif step == 1:
        state += 'After 1 step:\n'
    else:
        state += 'After {} steps:\n'.format(step)
    for r in range(rows):
        for c in range(cols):
            state += arr[r][c]
        state += '\n'
    print(state)


def solve(input_file: str):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()

    # parse input
    arr = []
    for line in lines:
        line = line.strip()
        line_values = [char for char in line]
        arr.append(line_values)
    arr_rows = len(arr)
    arr_cols = len(arr[0])
    print("parse:OK")
    print_state(0, arr, arr_rows, arr_cols)

    moving = True
    step = 0
    while moving:
        east_move, arr = move_east(arr, arr_rows, arr_cols)
        south_move, arr = move_south(arr, arr_rows, arr_cols)
        moving = east_move or south_move
        step += 1
#        if step in [1, 2, 3, 4, 5, 10, 20, 30, 40, 50, 55, 56, 57, 58]:
#            print_state(step, arr, arr_rows, arr_cols)
    print("solve:OK")
    return step


answer = solve("25/input.txt")
print(answer)  # 308
print("OK")
