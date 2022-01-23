# https://adventofcode.com/2021/day/9
import sys

infile = open('09/input.txt', 'r')
lines = infile.readlines()
infile.close()


def get_point_value(arr, i_x, i_y, max_x, max_y):
    max_value = sys.maxsize
    if i_x < 0:
        return max_value
    if i_y < 0:
        return max_value
    if i_x > max_x:
        return max_value
    if i_y > max_y:
        return max_value
    return arr[i_x][i_y]


def get_low_point_value(arr, x, y):
    value = arr[x][y]
    max_x = len(arr) - 1
    max_y = len(arr[x]) - 1
    if get_point_value(arr, x - 1, y, max_x, max_y) <= value:
        return -1
    if get_point_value(arr, x + 1, y, max_x, max_y) <= value:
        return -1
    if get_point_value(arr, x, y - 1, max_x, max_y) <= value:
        return -1
    if get_point_value(arr, x, y + 1, max_x, max_y) <= value:
        return -1
    return value


heatmap = []

# parse input
for line in lines:
    line = line.strip()
    line_chars = [int(char) for char in line]
    heatmap.append(line_chars)

answer = 0
for i in range(len(heatmap)):
    for j in range(len(heatmap[i])):
        low_point_value = get_low_point_value(heatmap, i, j)
        if low_point_value > -1:
            print("low point: {},{}".format(i, j))
            answer += (1 + low_point_value)

print(answer)  # 594
print("OK")
