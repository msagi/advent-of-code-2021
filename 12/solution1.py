# https://adventofcode.com/2021/day/12

# load file
infile = open('12/input.txt', 'r')
lines = infile.readlines()
infile.close()

# parse input
paths = {}
for line in lines:
    line = line.strip()
    path = line.split('-')
    a = path[0]
    b = path[1]
    if a not in paths:
        paths[a] = []
    paths[a].append(b)
    if b not in paths:
        paths[b] = []
    paths[b].append(a)


def explore(paths, current, target):
    if current == target:
        return 1
    # get where to go from here
    if current not in paths:  # dead end
        return 0
    next_steps = paths[current]
    next_paths = paths.copy()
    # if we cannot pass this step twice then remove from map
    if current.islower():
        next_paths.pop(current, None)
    total = 0
    for next_step in next_steps:
        total += explore(next_paths, next_step, target)
    return total


answer = explore(paths, 'start', 'end')
print(answer)  # 4775
print('OK')
