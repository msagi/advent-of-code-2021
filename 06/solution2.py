# https://adventofcode.com/2021/day/6

# load file
infile = open('06/input.txt', 'r')
lines = infile.readlines()
infile.close()


def process_day(pop):
    # get number of spawning today
    number_of_spawning = pop[0]
    # age the population
    for i in range(1, 9):
        pop[i - 1] = pop[i]
    # add spawns
    pop[8] = number_of_spawning
    # reset spawning ones
    pop[6] += number_of_spawning


# parse input
line = lines[0]
population_input = [int(numeric_string) for numeric_string in line.split(",")]

# create calc array [0..8]
population = [0] * 9

# count sort input to array
for i in range(len(population_input)):
    population[population_input[i]] += 1

# iterate and update
for i in range(256):
    process_day(population)

print(sum(population))  # 1634946868992
