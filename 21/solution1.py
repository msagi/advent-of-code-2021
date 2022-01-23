# https://adventofcode.com/2021/day/21


def solve(input_file: str):
    # load file
    infile = open(input_file, 'r')
    lines = infile.readlines()
    infile.close()

    # parse input
    arr = []
    for line in lines:
        position = int(line.strip().split(': ')[1])
        arr.append(position)
    print("parse:OK")

    starting_positions = arr.copy()
    player_positions = arr.copy()
    player_scores = [0 for i in range(len(arr))]
    die = 0
    number_of_die_rolls = 0
    while max(player_scores) < 1000:
#        if number_of_die_rolls == 24:
#            break
        for player in range(2):
            player_steps = []
            for steps in range(3):
                die += 1
                while die > 100:
                    die -= 100
                number_of_die_rolls += 1
                player_steps.append(die)
            player_positions[player] += sum(player_steps)
            while player_positions[player] > 10:
                player_positions[player] -= 10
            player_scores[player] += player_positions[player]
            print("player {} rolls {} and moves to space {} for a total score of {}.".format(1 + player, player_steps, player_positions[player], player_scores[player]))
            if player_scores[player] >= 1000:
                break

    print("player scores: {}, die rolled {}x times".format(player_scores, number_of_die_rolls))
    print("answer: {}".format(min(player_scores) * number_of_die_rolls))
    print("solve:OK")


solve("21/input.txt")  # 1073709
print("OK")
