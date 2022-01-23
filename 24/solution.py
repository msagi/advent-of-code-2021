"""
After reviewing the input algorithm, the following observations taken:
- x is reset to 0 for each input digit -> there is no need to track x value in between digits
- y is reset to 0 for each input digit -> there is no need to track y value in between digits
- z is NEVER negative -> starts as 0 and never goes below it
- z mostly is increasing. z ONLY decreases when Z[i] = 26 and z //= 26 -> z will only reach zero if we seek to run on
    this z //= 26 condition every time it is possible (via choosing the input digit)

See algo_analysis.txt and alu_code.py for details
"""

#     0   1   2   3   4   5   6   7   8   9   10  11   12  13
Z = [ 1,  1,  1, 26,  1,  1,  1, 26, 26,  1,  26, 26,  26, 26]  # copied from the algorithm: z = z // Z[i] (line #5)
X = [14, 12, 11, -4, 10, 10, 15, -9, -9, 12, -15, -7, -10,  0]  # copied from the algorithm: x = x + X[i] (line #6)
Y = [ 7,  4,  8,  1,  5, 14, 12, 10,  5,  7,   6,  8,   4,  6]  # copied from the algorithm: y = y + Y[i] (line #16)


def search(i, z, w, number, digits):
    i += 1  # go to next digit

    if i == 14:  # we are over the 14 digits (starting 0 indexed)
        if z == 0:  # z to be 0 is the solution we are looking for
            return number  # we are searching in a monotonic order -> first match is the solution
        return None  # if z is not 0 -> this is not our number

    x = z % 26 + X[i]

    # the only chance for z = 0 in the end if we always do z // 26 where possible, otherwise z grow too big
    if Z[i] == 26:  # this is time when the algo can do z // 26
        if 1 <= x <= 9:  # we have the chance to do z // 26 because it depends on 'w'
            if w != x:
                return None  # 'w' will not trigger z // 26 -> 'w' is not our digit
        else:
            return None  # no 'w' can trigger z // 26 -> 'w' is not our digit

    # calculate new z
    z //= Z[i]
    if w != x:
        z *= 26
        z += w + Y[i]

    number = number * 10 + w  # move to the next digit and track the whole number
    for digit in digits:
        hit = search(i, z, digit, number, digits)
        if hit:
            return hit
    return None


def solve(digits):
    for digit in digits:
        hit = search(-1, 0, digit, 0, digits)
        if hit:
            return hit


# part 1
solution1 = solve([9, 8, 7, 6, 5, 4, 3, 2, 1])
print(solution1)  # 29599469991739
# part 2
solution2 = solve([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(solution2)  # 17153114691118
