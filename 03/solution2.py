# https://adventofcode.com/2021/day/3


def get_most_common_value(arr, index):
    ones = 0
    zeros = 0
    for item in arr:
        if item[index] == '1':
            ones += 1
        elif item[index] == '0':
            zeros += 1
        else:
            exit(-1)
    if zeros > ones:
        return 0
    elif zeros < ones:
        return 1
    else:
        return -1


def filter_by_value(arr, index, value):
    result = []
    for item in arr:
        if item[index] == value:
            result.append(item)
    return result



infile = open('03/input.txt', 'r')
lines = infile.readlines()
infile.close()
line_length = len(lines[0].strip())


# calculate o2 generator settings
i = 0
while len(lines) > 1:
    print("number of lines: {}, i: {}".format(len(lines), i))
    most_common = get_most_common_value(lines, i)
    if most_common == 0:
        lines = filter_by_value(lines, i, '0')
    elif most_common == 1:
        lines = filter_by_value(lines, i, '1')
    else:
        lines = filter_by_value(lines, i, '1')
    i += 1

print("number of lines: {}, i: {}".format(len(lines), i))
o2_generator_rating = lines[0]
print("O2 generator rating: {}".format(o2_generator_rating))

# calculate co2 scrubber settings
infile = open('03/input.txt', 'r')
lines2 = infile.readlines()
infile.close()

i = 0
while len(lines2) > 1:
    print("number of lines: {}, i: {}".format(len(lines2), i))
    most_common = get_most_common_value(lines2, i)
    if most_common == 0:
        lines2 = filter_by_value(lines2, i, '1')
    elif most_common == 1:
        lines2 = filter_by_value(lines2, i, '0')
    else:
        lines2 = filter_by_value(lines2, i, '0')
    i += 1

print("number of lines: {}, i: {}".format(len(lines2), i))
co2_scrubber_rating = lines2[0]
print("CO2 scrubber rating: {}".format(co2_scrubber_rating))

print(int(o2_generator_rating, 2) * int(co2_scrubber_rating, 2))  # 2981085

