# https://adventofcode.com/2021/day/1

infile = open('01/input.txt', 'r')
numbers = infile.readlines()
infile.close()

previous_sum = -1

number_of_increases = 0
for i in range(len(numbers) - 2):
    current_sum = 0
    for j in range(3):
        current_sum += int(numbers[i + j])
    if previous_sum == -1:
        previous_sum = current_sum
        continue
    if current_sum > previous_sum:
        number_of_increases += 1
    previous_sum = current_sum

print(number_of_increases)  # 1748
