# https://adventofcode.com/2021/day/18


def parse(s) -> list[int]:
    """
    Parse the 'Snailfish number' string to a list of its components
    :param s: the 'Snailfish number'
    :return: the list of its components where numbers are casted to int while others are chars
    """
    items = []
    number = -1  # the number within the sequence can be double digit!
    for c in s:
        if c in '[':
            items.append(c)
        elif c in ',]':
            if number != -1:
                items.append(number)
                number = -1
            items.append(c)
        elif c in '0123456789':
            if number == -1:
                number = int(c)
            else:
                number *= 10
                number += int(c)
        else:
            exit(-1)
    return items


def explode(s) -> tuple:
    items = parse(s)

    depth = 0
    for i in range(len(items)):
        item = items[i]
        if item == '[':
            depth += 1
            if depth <= 4:
                continue
            # found the '[' of the pair which will explode
            left_value = items[i + 1]
            assert isinstance(left_value, int)
            separator = items[i + 2]
            assert separator == ','
            right_value = items[i + 3]
            assert isinstance(right_value, int)

            # find the first regular number on the left (if any)
            for li in range(i, 0, -1):
                if isinstance(items[li], int):
                    # and add left value to it
                    items[li] += left_value
                    break
            # find the first regular number on the right (if any)
            for ri in range(i + 4, len(items)):
                if isinstance(items[ri], int):
                    # and add left value to it
                    items[ri] += right_value
                    break
            # replace exploded pair with 0
            for j in range(5):
                items.pop(i)
            items.insert(i, 0)
            # return updated line
            new_line = ''.join([str(item) for item in items])
            return new_line, True
        elif item == ']':
            depth -= 1
        else:
            # we are
            pass
    # nothing to explode
    return s, False


def reduce(s) -> tuple:
    items = parse(s)

    for i in range(len(items)):
        item = items[i]
        if isinstance(item, int):
            value = item
            if value < 10:
                # this is not the right number to split
                continue
            # found the index of the number to split
            # remove the number
            items.pop(i)
            # add the split numbers
            left_item = value // 2
            right_item = (value + 1) // 2
            items.insert(i, ']')
            items.insert(i, right_item)
            items.insert(i, ',')
            items.insert(i, left_item)
            items.insert(i, '[')
            # return updated line
            new_line = ''.join([str(item) for item in items])
            return new_line, True
    return s, False


def evaluate(s1, s2):
    s = "[{},{}]".format(s1, s2)
    changed = True
    while changed:
        s, is_changed = explode(s)
        if is_changed:
            continue
        s, is_changed = reduce(s)
        if is_changed:
            continue
        changed = False
    return s


def get_magnitude(s) -> tuple:
    items = parse(s)

    for i in range(len(items)-2):
        item = items[i]
        if items[i] == '[' and isinstance(items[i + 1], int) and items[i + 2] == ',' and isinstance(items[i + 3], int) and items[i + 4] == ']':
            # this is a regular pair
            left_value = items[i + 1]
            right_value = items[i + 3]
            magnitude = 3 * left_value + 2 * right_value
            # replace pair with magnitude
            for j in range(5):
                items.pop(i)
            items.insert(i, magnitude)
            # return updated line
            new_line = ''.join([str(item) for item in items])
            return new_line, True
    return s, False


# load file
infile = open('18/input.txt', 'r')
lines = infile.readlines()
infile.close()

arr = []
for line in lines:
    arr.append(line.strip())

result = arr[0]
for i in range(1, len(arr)):
    result = evaluate(result, arr[i])

print(result)

while True:
    result, is_changed = get_magnitude(result)
    if not is_changed:
        break

print(result)  # 4480

print("OK")
