# https://adventofcode.com/2021/day/11
import sys
import matrix

def flash_octopus(arr, rows, cols, r, c):
    if arr[r][c] <= 9:  # no flash for this octopus
        return 0
    arr[r][c] = -1  # register that this octopus has JUST flashed
    flashes = 1
    neighbours = matrix.get_all_neighbours(r, c, rows, cols)
    for rr, cc in neighbours:
        if -1 == arr[rr][cc]:  # this neighbour has been flashed BEFORE
            continue
        arr[rr][cc] += 1
        flashes += flash_octopus(arr, rows, cols, rr, cc)  # cascade flashing
    return flashes


def flash(arr, rows, cols):
    flashes = 0
    for r in range(rows):
        for c in range(cols):
            flashes += flash_octopus(arr, rows, cols, r, c)
    return flashes


def clean_up(arr, rows, cols):
    for r in range(rows):
        for c in range(cols):
            if arr[r][c] == -1:
                arr[r][c] = 0


def dump_arr(arr, rows, cols):
    for row in range(rows):
        print(arr[row])


# load file
infile = open('11/input.txt', 'r')
lines = infile.readlines()
infile.close()

# parse input
arr = []
for line in lines:
    line = line.strip()
    line_values = [int(char) for char in line]
    arr.append(line_values)
arr_rows = len(arr)
arr_cols = len(arr[0])
arr_size = arr_rows * arr_cols

dump_arr(arr, arr_rows, arr_cols)

max_step = sys.maxsize
total_number_of_flashes = 0
answer = 0
for step in range(max_step):
    matrix.arr_add(arr, arr_rows, arr_cols, 1)
    number_of_flashes = flash(arr, arr_rows, arr_cols)
    if number_of_flashes == arr_size:
        answer = 1 + step
        break
    clean_up(arr, arr_rows, arr_cols)
    total_number_of_flashes += number_of_flashes
print(answer)  # 285
print('OK')