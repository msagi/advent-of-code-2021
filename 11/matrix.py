
def create_array(rows, cols, default):
    """
    Create a new array with given dimensions and default value
    :param rows: The number of rows of the array
    :param cols: The number of columns of the array
    :param default: The default cell value
    :return: The newly created array
    """
    arr = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(default)
        arr.append(row)
    return arr


def create_3d_array(x, y, z, default):
    """
    Create a new array with given dimensions and default value
    :param x: The X dim of the array
    :param y: The Y dim of the array
    :param z: The Z dim of the array
    :param default: The default cell value
    :return: The newly created array
    """
    x_d = []
    for x_i in range(x):
        y_d = []
        for y_i in range(y):
            z_d = []
            for z_i in range(z):
                z_d.append(default)
            y_d.append(z_d)
        x_d.append(y_d)
    return x_d


def get_up_down_left_right_neighbours(r, c, rows, cols):
    """
    Return the up, down, left, right (valid) neighbours of a matrix coordinate
    :param r: row value of the coordinate
    :param c: column value of the coordinate
    :param rows: number of rows in the matrix
    :param cols: number of columns in the matrix
    :return: the up, down, left, right (valid) neighbours of a matrix coordinate
    """
    all = [(r - 1, c),
           (r + 1, c),
           (r, c - 1), (r, c + 1)]
    valid = []
    for rr, cc in all:
        if 0 <= rr < rows and 0 <= cc < cols:
            valid.append((rr, cc))
    return valid


def get_down_neighbour(r, c, rows, cols):
    """
    Return the down (valid) neighbour of a matrix coordinate
    :param r: row value of the coordinate
    :param c: column value of the coordinate
    :param rows: number of rows in the matrix
    :param cols: number of columns in the matrix
    :return: the down (valid) neighbour of a matrix coordinate
    """
    if 0 <= r + 1 < rows:
        return r + 1, c
    return None


def get_right_neighbour(r, c, rows, cols):
    """
    Return the right (valid) neighbour of a matrix coordinate
    :param r: row value of the coordinate
    :param c: column value of the coordinate
    :param rows: number of rows in the matrix
    :param cols: number of columns in the matrix
    :return: the right (valid) neighbour of a matrix coordinate
    """
    if 0 <= c + 1 < cols:
        return r, c + 1
    return None


def get_diagonal_neighbours(r, c, rows, cols):
    """
    Return the (valid) diagonal (top-left, top-right, bottom-left, bottom-right) neighbours of a matrix coordinate
    :param r: row value of the coordinate
    :param c: column value of the coordinate
    :param rows: number of rows in the matrix
    :param cols: number of columns in the matrix
    :return: the (valid) diagonal (top-left, top-right, bottom-left, bottom-right) neighbours of a matrix coordinate
    """
    all = [(r - 1, c - 1), (r - 1, c + 1),
           (r + 1, c - 1), (r + 1, c + 1)]
    valid = []
    for rr, cc in all:
        if 0 <= rr < rows and 0 <= cc < cols:
            valid.append((rr, cc))
    return valid


def get_all_neighbours(r, c, rows, cols):
    """
    Return the (valid) (top-left, top, top-right, left, right, bottom-left, bottom, bottom-right) neighbours
    of a matrix coordinate
    :param r: row value of the coordinate
    :param c: column value of the coordinate
    :param rows: number of rows in the matrix
    :param cols: number of columns in the matrix
    :return: the (valid) (top-left, top, top-right, left, right, bottom-left, bottom, bottom-right) neighbours
    """
    all = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
           (r, c - 1), (r, c + 1),
           (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]
    valid = []
    for rr, cc in all:
        if 0 <= rr < rows and 0 <= cc < cols:
            valid.append((rr, cc))
    return valid


def get_diagonal45_coordinates(arr, rows, cols):
    diagonals = []
    # top-left triangle
    for r in range(rows):
        c = 0
        d = []
        while r >= 0:
            d.append((r, c))
            r -= 1
            c += 1
        diagonals.append(d)
    # bottom-right triangle
    for c in range(1, cols):
        r = rows - 1
        d = []
        while c < cols:
            d.append((r, c))
            r -= 1
            c += 1
        diagonals.append(d)
    return diagonals


def arr_add(arr, rows, cols, amount):
    """
    Add to each item in the matrix
    :param arr: the matrix
    :param rows: number of rows in the matrix
    :param cols: number of columns in the matrix
    :param amount: the amount to add to each item
    :return: n/a
    """
    for r in range(rows):
        for c in range(cols):
            arr[r][c] += amount


def walk_through(arr, rows, cols):
    """
    Walk through all items of given array
    :param arr: the matrix
    :param rows: number of rows in the matrix
    :param cols: number of columns in the matrix
    :return: n/a
    """
    for r in range(rows):
        for c in range(cols):
            print(arr[r][c])
