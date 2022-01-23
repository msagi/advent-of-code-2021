# https://adventofcode.com/2021/day/7
import sys


# load file
infile = open('07/input.txt', 'r')
lines = infile.readlines()
infile.close()


def get_fuel_spent(arr, target):
    fuel = 0
    for i in arr:
        fuel += abs(i - target)
    return fuel


# parse input
positions = []
position_values = lines[0]
for position_value in position_values.strip().split(','):
    positions.append(int(position_value))

# get input boundaries
position_min = min(positions)
position_max = max(positions)

# brute force calculate optimal position
optimal_position = position_max + 1
answer = sys.maxsize
for i in range(position_min, position_max + 1):
    fuel_required = get_fuel_spent(positions, i)
    if fuel_required < answer:
        optimal_position = i
        answer = fuel_required

print("optimal position: {}, total fuel required: {}".format(optimal_position, answer))  # 336701
print("OK")
