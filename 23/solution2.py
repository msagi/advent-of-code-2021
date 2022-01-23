# https://adventofcode.com/2021/day/23
import sys
from copy import deepcopy

"""
Note: Amphipods => Crabs, I can't stand writing it so many times with typos
"""
# room indexes (positions) on the hallway
ROOM_POSITION = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
# the energy cost for each step for the various types of crabs
ENERGY_COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def is_target_room_ready_for_crab(crab, rooms):
    # returns True if the room is empty or has only designated type of crabs
    crab_target_room = rooms[crab]
    for position in crab_target_room:
        if position is not None and position != crab:
            return False
    return True


def is_crab_able_to_move_to_target_room(crab_hallway_position, state):
    # returns True if designated room is ready for crab and there is clear path for the crab to move to the room

    hallway, rooms = state
    crab = hallway[crab_hallway_position]

    if not is_target_room_ready_for_crab(crab, rooms):
        return False

    # check if there is clear path from crab position to target room
    target_room_position = ROOM_POSITION[crab]
    is_path_clear = True
    if target_room_position < crab_hallway_position:
        for position in range(target_room_position, crab_hallway_position):
            if hallway[position] is not None:
                is_path_clear = False
                break
    else:
        assert target_room_position != crab_hallway_position
        for position in range(crab_hallway_position + 1, target_room_position + 1):
            if hallway[position] is not None:
                is_path_clear = False
                break
    return is_path_clear


def move_crab_to_target_room(crab_hallway_position, state):
    # note: only call this function if the crab can move to the target room
    hallway, rooms = state
    crab = hallway[crab_hallway_position]
    target_room_position = ROOM_POSITION[crab]
    steps_to_final_position = abs(target_room_position - crab_hallway_position)
    target_room = rooms[crab]
    room_position = 0
    for position in range(len(target_room)):
        if target_room[position] is None:
            room_position = position
    steps_to_final_position += (room_position + 1)
    energy_cost = steps_to_final_position * ENERGY_COST[crab]
    # create new state: copy current state and move crab
    new_hallway = list(hallway)
    new_rooms = deepcopy(rooms)
    new_hallway[crab_hallway_position] = None
    new_rooms[crab][room_position] = crab
    return energy_cost, (new_hallway, new_rooms)


def is_simulation_complete(state):
    hallway, rooms = state
    for target_crab, room in rooms.items():
        for position in range(len(room)):
            if room[position] != target_crab:
                return False
    return True


def get_first_crab_to_move_from_room(room_target_crab, rooms):
    room = rooms[room_target_crab]
    # room is 'healthy' if there is nothing to move
    is_room_healthy = True
    for position in range(len(room)):
        crab = room[position]
        if crab is not None and crab != room_target_crab:
            is_room_healthy = False
            break
    if is_room_healthy:  # no move out from this room
        return None, -1
    for position in range(len(room)):
        crab = room[position]
        if crab is not None:
            return crab, position


def is_crab_able_to_move_to_hallway(start_room_id, target_hallway_position, state):
    hallway, rooms = state
    # crab cannot move to above any room
    if target_hallway_position in [2, 4, 6, 8]:
        return False
    # crab cannot move to an already occupied position
    if hallway[target_hallway_position] is not None:
        return False
    crab_hallway_position = ROOM_POSITION[start_room_id]
    is_path_clear = True
    if crab_hallway_position < target_hallway_position:
        for position in range(crab_hallway_position, target_hallway_position + 1):
            if hallway[position] is not None:
                is_path_clear = False
                break
    else:
        assert crab_hallway_position != target_hallway_position
        for position in range(target_hallway_position, crab_hallway_position + 1):
            if hallway[position] is not None:
                is_path_clear = False
                break
    return is_path_clear


def move_crab_from_target_room(crab, start_room_id, position_in_start_room, target_crab_hallway_position, state):
    # note: only call this function if the crab can move to the target room
    crab_hallway_position = ROOM_POSITION[start_room_id]
    steps_to_final_position = abs(crab_hallway_position - target_crab_hallway_position)
    steps_to_final_position += (position_in_start_room + 1)

    energy_cost = steps_to_final_position * ENERGY_COST[crab]

    # create new state: copy current state and move crab
    hallway, rooms = state
    new_hallway = list(hallway)
    new_rooms = deepcopy(rooms)
    new_hallway[target_crab_hallway_position] = crab
    new_rooms[start_room_id][position_in_start_room] = None
    return energy_cost, (new_hallway, new_rooms)


MEMO = {}  # memoization dictionary


def simulate(state):
    hallway, rooms = state

    if is_simulation_complete(state):  # no more steps
        return 0

    key = (tuple((room_id, tuple(room)) for room_id, room in rooms.items()), tuple(hallway))

    if key in MEMO:
        return MEMO[key]

    # try move any crabs to final state first (if possible)
    for hallway_position in range(len(hallway)):
        if hallway[hallway_position] is not None:
            if is_crab_able_to_move_to_target_room(hallway_position, state):
                energy_cost, new_state = move_crab_to_target_room(hallway_position, state)
                # clear crab from hallway and check if other crabs can now move to target position
                hallway[hallway_position] = None
                return energy_cost + simulate(new_state)

    minimal_energy_required = sys.maxsize

    # try move crabs which need to move
    for start_room_id, room in rooms.items():
        crab_to_move, position_in_start_room = get_first_crab_to_move_from_room(start_room_id, rooms)
        if crab_to_move is None:
            continue
        for target_hallway_position in range(len(hallway)):
            if is_crab_able_to_move_to_hallway(start_room_id, target_hallway_position, state):
                energy_cost, new_state = move_crab_from_target_room(crab_to_move, start_room_id, position_in_start_room, target_hallway_position, state)
                total_cost = energy_cost + simulate(new_state)
                minimal_energy_required = min(total_cost, minimal_energy_required)

    MEMO[key] = minimal_energy_required
    return minimal_energy_required


def solve():
    # parse input
    hallway = [None for i in range(11)]
    rooms = {'A': ['D', 'D'],  # 19019
             'B': ['B', 'A'],
             'C': ['C', 'B'],
             'D': ['C', 'A']}
#    rooms = {'A': ['D', 'D', 'D', 'D'],  # 47533
#             'B': ['B', 'C', 'B', 'A'],
#             'C': ['C', 'B', 'A', 'B'],
#             'D': ['C', 'A', 'C', 'A']}
    print("parse:OK")

    result = simulate((hallway, rooms))
    print(result)
    print("solve:OK")


solve()
print("OK")
