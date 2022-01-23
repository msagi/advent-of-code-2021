# https://adventofcode.com/2021/day/7
import sys


# load file
infile = open('07/input.txt', 'r')
lines = infile.readlines()
infile.close()


def get_fuel_requirements(pos_max):
    fuel_requirements = [-1] * (pos_max + 1)
    fuel_requirement = 0
    for i in range(len(fuel_requirements)):
        fuel_requirement += i
        fuel_requirements[i] = fuel_requirement
    return fuel_requirements


def get_fuel_spent(arr, target, requirements):
    fuel = 0
    for i in arr:
        fuel += requirements[abs(i - target)]
    return fuel


# parse input
positions = []
position_values = lines[0]
for position_value in position_values.strip().split(','):
    positions.append(int(position_value))

# get input boundaries
position_min = min(positions)
position_max = max(positions)
fuel_requirements = get_fuel_requirements(position_max)

# brute force calculate optimal position
optimal_position = position_max + 1
answer = sys.maxsize
for i in range(position_min, position_max + 1):
    fuel_required = get_fuel_spent(positions, i, fuel_requirements)
    if fuel_required < answer:
        optimal_position = i
        answer = fuel_required

print("optimal position: {}, total fuel required: {}".format(optimal_position, answer))  # 95167302
print("OK")
