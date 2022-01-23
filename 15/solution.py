# https://adventofcode.com/2021/day/15
import heapq


def copy_arr(target, source, source_rows, source_cols, target_row, target_col, offset):
    for r in range(source_rows):
        for c in range(source_cols):
            rr = target_row + r
            cc = target_col + c
            v = source[r][c] + offset
            while v > 9:
                v -= 9
            target[rr][cc] = v


def solve(multiplier):
    # load file
    infile = open('15/input.txt', 'r')
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

    if (multiplier > 1):
        arr2 = []
        for r in range(arr_rows * multiplier):
            row = []
            for c in range(arr_cols * multiplier):
                row.append(-1)
            arr2.append(row)
        for ri in range(multiplier):
            for ci in range(multiplier):
                copy_arr(arr2, arr, arr_rows, arr_cols, ri * arr_rows, ci * arr_cols, ri + ci)
        arr = arr2
        arr_rows = len(arr)
        arr_cols = len(arr[0])

    # create a same size risk array
    risk_arr = [[-1 for cols in range(arr_cols)] for rows in range(arr_rows)]

    # Dijkstra algo: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#/media/File:Dijkstra_Animation.gif
    start = (0, 0, 0)  # distance, r, c
    HQ = []
    heapq.heappush(HQ, start)

    while HQ:
        (total_min_risk, r, c) = heapq.heappop(HQ)
        risk = total_min_risk + arr[r][c]
        if risk_arr[r][c] == -1 or risk_arr[r][c] > risk:
            risk_arr[r][c] = risk
            neighbours = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]  # up, down, left, right
            for rr, cc in neighbours:
                if 0 <= rr < arr_rows and 0 <= cc < arr_cols:
                    heapq.heappush(HQ, (risk_arr[r][c], rr, cc))
    return risk_arr[arr_rows - 1][arr_cols - 1] - risk_arr[0][0]


print(solve(1))  # part 1: 824
print(solve(5))  # part 2: 3063
print("OK")

