# https://adventofcode.com/2021/day/10


def get_syntax_error_score(line, i):
    error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    stack = []
    open_characters = ['{', '(', '[', '<']
    close_characters = ['}', ')', ']', '>']
    for c in line:
        if c in open_characters:
            stack.append(c)
        elif c in close_characters:
            close_characters_index = close_characters.index(c)
            expected_open_characters = open_characters[close_characters_index]
            if stack[-1] == expected_open_characters:
                stack.pop()
            else:
                score = error_score[c]
                print("line {}: got {} but expected {}, error score: {}, line: {}".format(i, c, stack[-1], score, line))
                return score
    print("line {}: OK".format(i))
    return 0


def solve(file_name):
    # load file
    infile = open(file_name, 'r')
    lines = infile.readlines()
    infile.close()

    arr = []
    # parse input
    for line in lines:
        line = line.strip()
        line_values = [char for char in line]
        arr.append(line_values)

    score = 0
    for i in range(len(arr)):
        score += get_syntax_error_score(arr[i], i)
    return score


answer = solve("10/input.txt")
print(answer)  # 388713
print("OK")
