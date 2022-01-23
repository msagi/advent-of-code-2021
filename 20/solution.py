# https://adventofcode.com/2021/day/20


def get_pixel_number(arr, r, c, rows, cols, edge_value):
    coordinates = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                   (r, c - 1), (r, c), (r, c + 1),
                   (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
    bin_number = 0
    for rr, cc in coordinates:
        value = edge_value
        if 0 <= rr < rows and 0 <= cc < cols:
            value = arr[rr][cc]
        bin_number = (bin_number * 2) + value
    return bin_number


def solve(input_file: str):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()

    # parse input
    algorithm = lines[0].strip()
    lines.pop(0)  # pop algorithm
    lines.pop(0)  # pop empty line
    arr = []
    for line in lines:
        line = line.strip()
        line_values = [1 if char == '#' else 0 for char in line]
        arr.append(line_values)
    arr_rows = len(arr)
    arr_cols = len(arr[0])

    expand_by = 1

    arr2 = [[0 for cols in range(arr_cols + (2 * expand_by))] for rows in range(arr_rows + (2 * expand_by))]
    r_offset = expand_by
    c_offset = expand_by
    for r in range(arr_rows):
        for c in range(arr_cols):
            arr2[r + r_offset][c + c_offset] = arr[r][c]
    arr = arr2
    arr_rows = len(arr)
    arr_cols = len(arr[0])

    # solve
    for i in range(1, 51):
        edge_value = arr[0][0]
        edge_value_number = get_pixel_number(arr, 0, 0, arr_rows, arr_cols, arr[0][0])
        new_edge_value = 0 if algorithm[edge_value_number] == '.' else 1
        arr2 = [[new_edge_value for cols in range(arr_cols + (2 * expand_by))] for rows in range(arr_rows + (2 * expand_by))]
        r_offset = expand_by
        c_offset = expand_by
        for r in range(arr_rows):
            for c in range(arr_cols):
                bin_number = get_pixel_number(arr, r, c, arr_rows, arr_cols, edge_value)
                assert bin_number < 512
                pixel_value = 0
                if algorithm[bin_number] == '#':
                    pixel_value = 1
                arr2[r + r_offset][c + c_offset] = pixel_value
        arr = arr2
        arr_rows = len(arr)
        arr_cols = len(arr[0])
        if i in [2, 50]:
            result = 0
            for r in range(arr_rows):
                for c in range(arr_cols):
                    if expand_by <= r < arr_rows - expand_by and expand_by <= c < arr_cols - expand_by:
                        if arr2[r][c] == 1:
                            result += 1
            print('enhanced {}x times: {} pixels lit'.format(i, result))
    print("solve:OK")


print("sample")
solve("20/sample_input.txt")  # 2x -> 35, 50x -> 3351
print("real")
solve("20/input.txt")  # 2x -> 5464, 50x -> 19228
print("OK")
