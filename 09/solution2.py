# https://adventofcode.com/2021/day/9

# load file
infile = open('09/input.txt', 'r')
lines = infile.readlines()
infile.close()


def get_point_value(arr, i_x, i_y, max_x, max_y):
    max_value = 9223372036854775807
    if i_x < 0:
        return max_value
    if i_y < 0:
        return max_value
    if i_x > max_x:
        return max_value
    if i_y > max_y:
        return max_value
    return arr[i_x][i_y]


def get_low_point_value(arr, x, y, max_x, max_y):
    value = arr[x][y]
    if get_point_value(arr, x - 1, y, max_x, max_y) <= value:
        return -1
    if get_point_value(arr, x + 1, y, max_x, max_y) <= value:
        return -1
    if get_point_value(arr, x, y - 1, max_x, max_y) <= value:
        return -1
    if get_point_value(arr, x, y + 1, max_x, max_y) <= value:
        return -1
    return value


def is_valid_coordinate(arr, i_x, i_y, max_x, max_y):
    if i_x < 0:
        return False
    if i_y < 0:
        return False
    if i_x > max_x:
        return False
    if i_y > max_y:
        return False
    if arr[i_x][i_y] >= 9:
        return False
    return True


def get_basin_size(arr, x, y, max_x, max_y):
    size = 1
    arr[x][y] = 10
    if is_valid_coordinate(arr, x - 1, y, max_x, max_y):
        size += get_basin_size(arr, x - 1, y, max_x, max_y)
    if is_valid_coordinate(arr, x + 1, y, max_x, max_y):
        size += get_basin_size(arr, x + 1, y, max_x, max_y)
    if is_valid_coordinate(arr, x, y - 1, max_x, max_y):
        size += get_basin_size(arr, x, y - 1, max_x, max_y)
    if is_valid_coordinate(arr, x, y + 1, max_x, max_y):
        size += get_basin_size(arr, x, y + 1, max_x, max_y)
    return size


# parse input
heatmap = []
for line in lines:
    line = line.strip()
    line_chars = [int(char) for char in line]
    heatmap.append(line_chars)
len_x = len(heatmap) - 1
len_y = len(heatmap[0]) - 1

low_points = []
for i in range(len(heatmap)):
    for j in range(len(heatmap[i])):
        low_point_value = get_low_point_value(heatmap, i, j, len_x, len_y)
        if low_point_value > -1:
            low_points.append([i, j])

# iterate through all low points
basin_sizes = []
for low_point in low_points:
    i = low_point[0]
    j = low_point[1]
    print("low point: {},{}".format(i, j))
    basin_size = get_basin_size(heatmap, i, j, len_x, len_y)
    basin_sizes.append(basin_size)

sorted_basin_sizes = sorted(basin_sizes, key=int, reverse=True)

print(sorted_basin_sizes[0] * sorted_basin_sizes[1] * sorted_basin_sizes[2])  # 858494
print("OK")
