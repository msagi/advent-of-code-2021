# https://adventofcode.com/2021/day/11


def increase_energy_level(arr, arr_len_x, arr_len_y, increase_step):
    for x in range(arr_len_x):
        for y in range(arr_len_y):
            arr[x][y] += increase_step


def flash_octopus(arr, arr_len_x, arr_len_y, x, y):
    if arr[x][y] <= 9:  # no flash for this octopus
        return 0
    arr[x][y] = -1  # register that this octopus has JUST flashed
    number_of_flashes = 1
    x_coords = [x-1, x, x+1]
    y_coords = [y-1, y, y+1]
    for x_coord in x_coords:
        for y_coord in y_coords:
            if 0 <= x_coord < arr_len_x and 0 <= y_coord < arr_len_y:
                if -1 == arr[x_coord][y_coord]:  # this neighbour has been flashed BEFORE
                    continue
                arr[x_coord][y_coord] += 1
                number_of_flashes += flash_octopus(arr, arr_len_x, arr_len_y, x_coord, y_coord)  # cascade flashing
    return number_of_flashes


def flash(arr, arr_len_x, arr_len_y):
    number_of_flashes = 0
    for x in range(arr_len_x):
        for y in range(arr_len_y):
            number_of_flashes += flash_octopus(arr, arr_len_x, arr_len_y, x, y)
    return number_of_flashes


def clean_up(arr, arr_len_x, arr_len_y):
    for x in range(arr_len_x):
        for y in range(arr_len_y):
            if arr[x][y] == -1:
                arr[x][y] = 0


def dump_arr(arr, arr_len_x, arr_len_y):
    for y in range(arr_len_y):
        print(arr[y])


# load file
infile = open('11/input.txt', 'r')
lines = infile.readlines()
infile.close()

arr = []
# parse input
for line in lines:
    line = line.strip()
    line_values = [int(char) for char in line]
    arr.append(line_values)
arr_len_x = len(arr[0])
arr_len_y = len(arr)
arr_size = arr_len_x * arr_len_y
dump_arr(arr, arr_len_x, arr_len_y)

max_step = 100
answer = 0
for step in range(max_step):
    increase_energy_level(arr, arr_len_x, arr_len_y, 1)
    number_of_flashes = flash(arr, arr_len_x, arr_len_y)
    clean_up(arr, arr_len_x, arr_len_y)
    answer += number_of_flashes
print(answer)  # 1749
print('OK')
