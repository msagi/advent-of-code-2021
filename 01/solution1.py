# https://adventofcode.com/2021/day/1

infile = open('01/input.txt', 'r')
numbers = infile.readlines()
infile.close()

previous_measurement = -1
number_of_increases = 0
for i in range(len(numbers)):
    current_measurement = int(numbers[i])
    if previous_measurement == -1:
        previous_measurement = current_measurement
        continue
    if current_measurement > previous_measurement:
        number_of_increases += 1
    previous_measurement = current_measurement

print(number_of_increases)  # 1722
