# https://adventofcode.com/2021/day/21

MEMO = {}


def roll(space1, score1, space2, score2):
    if score1 >= 21:
        return 1, 0  # one win for player 1
    if score2 >= 21:
        return 0, 1  # one win for player 2
    if (space1, score1, space2, score2) in MEMO:
        return MEMO[(space1, score1, space2, score2)]  # we already know this status

    win = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                die_value = d1 + d2 + d3
                new_space1 = space1 + die_value
                while new_space1 > 10:
                    new_space1 -= 10
                new_score1 = score1 + new_space1
                win2, win1 = roll(space2, score2, new_space1, new_score1)  # switch players! switched players will return switched wins -> switch it again
                win = (win[0] + win1, win[1] + win2)
                MEMO[(space1, score1, space2, score2)] = win  # save status to avoid calculating it again
    return win


def solve(input_file: str):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()
    # parse input
    arr = []
    for line in lines:
        position = int(line.strip().split(': ')[1])
        arr.append(position)
    print("parse:OK")

    wins = roll(arr[0], 0, arr[1], 0)
    print("player wins: {}, winner: {}".format(wins, max(wins)))  # 148747830493442
    print("solve:OK")


solve("21/input.txt")
print("OK")
