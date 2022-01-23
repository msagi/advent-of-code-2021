# https://adventofcode.com/2021/day/10


def complete_line_score(arr):
    print("arr: {}".format(arr))

    total_score = 0
    while len(arr) > 0:
        total_score *= 5
        c = arr.pop()
        if c == '(':
            total_score += 1
        elif c == '[':
            total_score += 2
        elif c == '{':
            total_score += 3
        elif c == '<':
            total_score += 4
        else:
            exit(-1)
    print("total score: {}".format(total_score))
    return total_score


def get_line_to_complete(arr):
    stack = []
    open_characters = ['{', '(', '[', '<']
    close_characters = ['}', ')', ']', '>']
    for c in arr:
        if c in open_characters:
            stack.append(c)
        elif c in close_characters:
            close_characters_index = close_characters.index(c)
            expected_open_characters = open_characters[close_characters_index]
            if stack[-1] == expected_open_characters:
                stack.pop()
            else:
                return []
    return stack


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

    lines_to_complete = []
    for a in arr:
        line_to_complete = get_line_to_complete(a)
        if len(line_to_complete) > 0:
            lines_to_complete.append(line_to_complete)

    scores = []
    for a in lines_to_complete:
        scores.append(complete_line_score(a))
    scores = sorted(scores)
    print(scores)
    return scores[int((len(scores) / 2))]


answer = solve("10/input.txt")
print(answer)  # 3539961434
print("OK")
