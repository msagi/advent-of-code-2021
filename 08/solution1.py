# https://adventofcode.com/2021/day/8

# load file
infile = open('08/input.txt', 'r')
lines = infile.readlines()
infile.close()

# parse input
answer = 0
unique_number_of_segments_lengths = [2, 4, 3, 7]

for line in lines:
    line = line.strip()
    print("line: {}".format(line))
    line_parts = line.split(' | ')
    unique_signal_patterns = line_parts[0].split(' ')
    four_digit_output_value = line_parts[1].split(' ')
    for value in four_digit_output_value:
        output_value_length = len(value)
        if output_value_length in unique_number_of_segments_lengths:
            answer += 1

print(answer)  # 365
print("OK")
