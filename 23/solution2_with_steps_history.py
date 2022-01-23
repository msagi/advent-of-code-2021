# https://adventofcode.com/2021/day/23
import copy
import sys
from copy import deepcopy

"""
Note: Amphipods => Crabs, I can't stand writing it so many times with typos
"""
# room indexes (positions) on the hallway
ROOM_POSITION = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
# the energy cost for each step for the various types of crabs
ENERGY_COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}


def is_target_room_ready_for_crab(crab: chr, rooms: dict) -> bool:
    """Check if the target room is ready to receive the crab.
        The room is ready if there are only empty positions or has only designated type of crabs

        Args:
            crab (chr): The crab (type).
            rooms (dict): The state of the rooms.

        Returns:
            bool: True if the target room is ready to receive the crab, False otherwise.
        """
    crab_target_room = rooms[crab]
    for position in crab_target_room:
        if position is not None and position != crab:
            return False
    return True


def is_crab_able_to_move_to_target_room(crab_hallway_position: int, state: tuple) -> bool:
    """Check if the crab is able to move to its target room.

        Args:
            crab_hallway_position (int): the (zero indexed) position of the crab in the hallway
            state (tuple): the current state of the hallway and crab rooms

        Returns:
            bool: True if the crab can move to its target room, False otherwise
        """
    hallway, rooms = state
    crab = hallway[crab_hallway_position]

    if not is_target_room_ready_for_crab(crab, rooms):
        return False

    # check if there is clear path from crab position to target room
    target_room_position = ROOM_POSITION[crab]
    is_path_clear = True
    move_range_from = min(target_room_position, crab_hallway_position)
    move_range_to = max(target_room_position, crab_hallway_position)
    for position in range(move_range_from, move_range_to + 1):
        if position == crab_hallway_position:
            continue
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


def is_simulation_complete(state: tuple) -> bool:
    """Check if simulation has reached end state.

        Args:
            state (tuple): The current simulation state.

        Returns:
            bool: True if simulation is complete, False otherwise
        """
    hallway, rooms = state
    for target_crab, room in rooms.items():
        for position in range(len(room)):
            if room[position] != target_crab:
                return False
    return True


def get_first_crab_to_move_from_room(room_id: chr, rooms: dict) -> tuple:
    """Get the crab to move out from given room.

        Args:
            room_id (chr): The target crab for the room.
            rooms (dict): The rooms in current simulation state.

        Returns:
            tuple: The crab and its room position if there is a crab to move. None, -1 otherwise.
        """
    room = rooms[room_id]
    # room is 'healthy' if there is nothing to move
    is_room_healthy = True
    for position in range(len(room)):
        crab = room[position]
        if crab is not None and crab != room_id:
            is_room_healthy = False
            break
    if is_room_healthy:  # no move out from this room
        return (None, -1)
    for position in range(len(room)):
        crab = room[position]
        if crab is not None:
            return (crab, position)


def is_crab_able_to_move_to_hallway(start_room_id, target_hallway_position, state):
    hallway, rooms = state
    # crab cannot move to above any room
    if target_hallway_position in [2, 4, 6, 8]:
        return False
    # crab cannot move to an already occupied position
    if hallway[target_hallway_position] is not None:
        return False
    crab_room_in_hallway_position = ROOM_POSITION[start_room_id]
    is_path_clear = True
    move_range_from = min(target_hallway_position, crab_room_in_hallway_position)
    move_range_to = max(target_hallway_position, crab_room_in_hallway_position)
    for position in range(move_range_from, move_range_to + 1):
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


def get_state_str(start_cost, move_cost, state):
    hallway, rooms = state
    status = ''
    status += '#############\n'
    hallway_line = '#'
    for crab in hallway:
        hallway_line += crab if crab is not None else '.'
    hallway_line += '# {} + {} = {}\n'.format(start_cost, move_cost, start_cost + move_cost)
    status += hallway_line
    for position in range(len(rooms['A'])):
        if position == 0:
            room_line = '###'
        else:
            room_line = '  #'
        for room_id in ['A', 'B', 'C', 'D']:
            crab = rooms[room_id][position]
            room_line += crab if crab is not None else '.'
            room_line += '#'
        if position == 0:
            room_line += '##\n'
        else:
            room_line += '  \n'
        status += room_line
    status += '  #########  \n\n'
    return status


def print_state(total_energy, energy, state):
    print(get_state_str(total_energy, energy, state))


def get_chain_str(chain):
    s = ''
    start_cost = 0
    for move_cost, next_state in chain:
        s += get_state_str(start_cost, move_cost, next_state)
        start_cost += move_cost 
    return s


def print_chain(chain):
    print(get_chain_str(chain))


def get_key_for_state(state) -> str:
    hallway, rooms = state
    return (tuple((room_id, tuple(room)) for room_id, room in rooms.items()), tuple(hallway))


MEMO = {}  # memoization dictionary

def simulate(state):
    hallway, rooms = state

    if is_simulation_complete(state):  # no more steps
        return 0, []

    key = get_key_for_state(state)

    if key in MEMO:
        return MEMO[key]

    # try to move any crabs already in the hallway to their target room first (if possible)
    for hallway_position in range(len(hallway)):  # check all positions in hallway
        if hallway[hallway_position] is not None:  # if there is a crab in the current position
            if is_crab_able_to_move_to_target_room(hallway_position, state):
                move_cost, next_state = move_crab_to_target_room(hallway_position, state)
                chain_cost, chain = simulate(next_state)
                total_cost = move_cost + chain_cost
                total_chain = copy.deepcopy(chain)
                total_chain.insert(0, [move_cost, next_state])
                return total_cost, total_chain

    minimal_total_cost = sys.maxsize
    minimal_total_cost_chain = []

    # try to move crabs which can move out
    for start_room_id, room in rooms.items():
        crab_to_move, position_in_start_room = get_first_crab_to_move_from_room(start_room_id, rooms)
        if crab_to_move is None:
            continue
        for target_hallway_position in range(len(hallway)):
            if is_crab_able_to_move_to_hallway(start_room_id, target_hallway_position, state):
                move_cost, next_state = move_crab_from_target_room(crab_to_move, start_room_id, position_in_start_room, target_hallway_position, state)
                chain_cost, chain = simulate(next_state)
                total_cost = move_cost + chain_cost
                total_chain = copy.deepcopy(chain)
                total_chain.insert(0, [move_cost, next_state])
                if total_cost < minimal_total_cost:
                    minimal_total_cost = total_cost
                    minimal_total_cost_chain = total_chain
    # memoize before returning values so we won't have to calculate minimal energy from this state again
    # note: memoization starts from the end and goes backwards!
    MEMO[key] = minimal_total_cost, minimal_total_cost_chain
    return minimal_total_cost, minimal_total_cost_chain


def solve():
    # parse input
    hallway = [None for i in range(11)]
#    rooms = {'A': ['D', 'D'],  # 19019
#             'B': ['B', 'A'],
#             'C': ['C', 'B'],
#             'D': ['C', 'A']}
    rooms = {'A': ['D', 'D', 'D', 'D'],  # 47533
             'B': ['B', 'C', 'B', 'A'],
             'C': ['C', 'B', 'A', 'B'],
             'D': ['C', 'A', 'C', 'A']}
    print("parse:OK")

    start_state = (hallway, rooms)
    minimal_total_cost, minimal_total_cost_chain = simulate(start_state)
    minimal_total_cost_chain.insert(0, [0, start_state])
    print_chain(minimal_total_cost_chain)
    print(minimal_total_cost)
    print("solve:OK")


solve()
print("OK")
