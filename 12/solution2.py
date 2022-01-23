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


def explore(paths, current, target, is_twice_chance_used, label, journeys):
    if label == "":
        label = current
    else:
        label += ",{}".format(current)

    if current == target:
        journeys.append(label)
        return 1
    # get where to go from here
    if current not in paths:  # dead end
        return 0
    next_steps = paths[current]
    next_paths = paths.copy()
    total = 0
    # if we cannot pass this step twice then remove from map
    if current.islower():
        if current in ['start', 'end']:
            next_paths.pop(current, None)
            for next_step in next_steps:
                total += explore(next_paths, next_step, target, is_twice_chance_used, label, journeys)
        else:
            if is_twice_chance_used:
                next_paths.pop(current, None)
                for next_step in next_steps:
                    total += explore(next_paths, next_step, target, True, label, journeys)
            else:
                # leave it
                for next_step in next_steps:
                    total += explore(next_paths, next_step, target, True, label, journeys)
                # remove it
                next_paths.pop(current, None)
                for next_step in next_steps:
                    total += explore(next_paths, next_step, target, False, label, journeys)
    else:
        for next_step in next_steps:
            total += explore(next_paths, next_step, target, is_twice_chance_used, label, journeys)
    return total


journeys = []
result = explore(paths, 'start', 'end', False, "", journeys)
journeys = sorted(journeys)

deduped = []
counter = 0
for journey in journeys:
    if counter == 0:
        deduped.append(journey)
        counter += 1
    if counter > 0 and journey != deduped[-1]:
        deduped.append(journey)

answer = len(deduped)  
print(answer)  # 152480
print('OK')
