# https://adventofcode.com/2021/day/6

# load file
infile = open('06/sample_input.txt', 'r')
lines = infile.readlines()
infile.close()


def spawn(arr):
    arr_len = len(arr)
    for i in range(0, arr_len):
        if arr[i] == 0:
            arr[i] = 7
            arr.append(9)


def age(arr):
    for i in range(0, len(arr)):
        arr[i] -= 1


# parse input
line = lines[0]
population = [int(numeric_string) for numeric_string in line.split(",")]

for day in range(0, 80):
    spawn(population)
    age(population)

print(len(population))  # 5934
