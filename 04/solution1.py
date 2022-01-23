# https://adventofcode.com/2021/day/4

import re

line_pattern = re.compile("([0-9]+)[ ]+([0-9]+)[ ]+([0-9]+)[ ]+([0-9]+)[ ]+([0-9]+)")


def get_bingo_board(arr, index):
    # define a 5x5 bingo board array
    board = []
    for board_i in range(5):
        m = line_pattern.match(arr[index + board_i])
        if not m:
            print("invalid line: {}, index: {}".format(arr[index + board_i], index + board_i))
            exit(-1)
        board_row = []
        for board_j in range(5):
            value = [m.group(board_j + 1), False]   # each value is the number and flag if drawn
            board_row.append(value)
        board.append(board_row)
    return board


def mark_number_drawn(boards, n):
    for board in boards:
        for board_row in range(5):
            for board_col in range(5):
                if board[board_row][board_col][0] == n:
                    board[board_row][board_col][1] = True


def get_winner_board_index(boards):
    for board_index in range(len(boards)):  # for each board
        board = boards[board_index]
        # check for bingo in rows
        for board_row in range(5):
            numbers_drawn_found = 0
            for board_col in range(5):
                if board[board_row][board_col][1]:
                    numbers_drawn_found += 1
            if numbers_drawn_found == 5:  # all 5 numbers have been drawn in the row
                # the board is a winner
                return board_index
        # check for bingo columns
        for board_col in range(5):
            numbers_drawn_found = 0
            for board_row in range(5):
                if board[board_row][board_col][1]:
                    numbers_drawn_found += 1
            if numbers_drawn_found == 5:  # all 5 numbers have been drawn in the column
                # the board is a winner
                return board_index
    # no winner
    return -1


def get_winner_board_score(boards, board_index):
    score = 0
    board = boards[board_index]
    for board_row in range(5):
        for board_col in range(5):
            if not board[board_row][board_col][1]:
                score += int(board[board_row][board_col][0])
    return score


# load file
infile = open('04/input.txt', 'r')
lines = infile.readlines()
infile.close()

# remove tailing \n
for i in range(len(lines)):
    lines[i] = lines[i].strip()

# parse input: bingo boards
bingo_boards = []
i = 2
while i < len(lines):
    bingo_boards.append(get_bingo_board(lines, i))
    i += 6

# parse input: numbers drawn
numbers_drawn = lines[0].split(',')

answer = 0
for number in numbers_drawn:
    mark_number_drawn(bingo_boards, number)
    winner_board_index = get_winner_board_index(bingo_boards)
    if winner_board_index != -1:
        winner_board_score = get_winner_board_score(bingo_boards, winner_board_index)
        print("winner board is #{}, score: {}, last drawn number: {}".format(winner_board_index, winner_board_score, number))
        answer = winner_board_score * int(number)
        break

print(answer)  # 58838