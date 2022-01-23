# https://adventofcode.com/2021/day/3

infile = open('03/input.txt', 'r')
lines = infile.readlines()
infile.close()

number_of_lines = 0
number_of_ones = []
for line in lines:
    # initialize counter array
    if len(number_of_ones) == 0:
        number_of_ones = [0 for i in range(len(line.strip()))]
    for i in range(len(line)):
        if line[i] == '1':
            number_of_ones[i] += 1
    number_of_lines += 1

gamma_rate = ''
epsilon_rate = ''
for i in range(len(number_of_ones)):
    if number_of_ones[i] > (number_of_lines / 2):
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print(gamma_rate)
print(epsilon_rate)
print(int(gamma_rate, 2) * int(epsilon_rate, 2))  # 3309596
