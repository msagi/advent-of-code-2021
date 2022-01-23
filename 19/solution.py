# https://adventofcode.com/2021/day/19
import itertools

#
# pseudocode
#
# read all scanner inputs
# for all scanner inputs, generate all the 24 variations (due to the scanner rotation or facing direction)
# for all scanners (pick 2 scanners: SA, SB where SA is in the absolute co-ordinate system)
#   for all co-ordinate pair from SA and SB
#     calculate DELTA in between the co-ordinate pair (SA[i] and SB[j])
#     apply delta to all other co-ordinates in SB with counting of matches
#     if matches >= 12 then this is a MATCH,
#       align coordinates of SB to absolute co-ordinate system
#       save scanner's position and orientation
# once all scanners have their position and orientation, with their coordinates transformed
#   to the absolute coordinate system, merge the beacon co-ordinates to one list
#   and count unique beacons

MIN_OVERLAPS_NEEDED = 12


def is_match(s1, s2) -> bool:
    for c1 in range(len(s1)):
        for c2 in range(len(s2)):
            matches = 0
            delta = (
                s1[c1][0] - s2[c2][0],
                s1[c1][1] - s2[c2][1],
                s1[c1][2] - s2[c2][2])  # pick one beacon from both sonars and calculate difference
            s2shifted = s2.copy()  # translate sonar 2 beacon locations with this difference 
            for i in range(len(s2shifted)):
                s2shifted[i] = (
                    s2shifted[i][0] + delta[0],
                    s2shifted[i][1] + delta[1],
                    s2shifted[i][2] + delta[2])
                if s2shifted[i] in s1:
                    matches += 1  # count the matching beacons after this translation in between sonar 1 and 2
                    if matches >= MIN_OVERLAPS_NEEDED:  # enough beacons match -> these sonars overlap
                        return delta  # return the translation vector
    return None  # not enough match in between sonar 1 and 2 beacons translated using any beacon combinations


def generate_orientations():
    # note: this generates 48 orientations but
    # challenge talks about there is only 24 (?!)
    orientations = []
    for x_direction in (-1, 1):  # x direction, 2x, flip
        for y_direction in (-1, 1):  # y direction, 2x, flip
            for z_direction in (-1, 1):  # z direction, 2x, flip
                for permutations in itertools.permutations(range(3)):  # 6x, rotate
                    orientations.append(permutations + (x_direction, y_direction, z_direction))
    return orientations


def apply_orientation(coord, orientation):
    x_permutation, y_permutation, z_permutation, x_direction, y_direction, z_direction = orientation
    coord2 = [None] * 3
    coord2[x_permutation] = coord[0] * x_direction
    coord2[y_permutation] = coord[1] * y_direction
    coord2[z_permutation] = coord[2] * z_direction
    return tuple(coord2)


def is_aligned(s1, s2, orientations):
    # calculate all orientation for s2 coordinates
    for orientation in orientations:  # for all orientation
        # calculate "oriented" coordinates for s2 sensor
        s2oriented = []
        for coord in s2:
            s2oriented.append(apply_orientation(coord, orientation))
        # check if s2 "oriented" coordinates can be matched with s1
        delta = is_match(s1, s2oriented)
        if delta is not None:  # if match found
            return orientation, delta
    # no match at all
    return None


def transform(s, orientation, delta):
    for i in range(len(s)):
        rotated_coordinate = apply_orientation(s[i], orientation)
        aligned_coordinate = (
            rotated_coordinate[0] + delta[0],
            rotated_coordinate[1] + delta[1],
            rotated_coordinate[2] + delta[2])
        s[i] = aligned_coordinate


def solve(input_file: str):
    # load file
    infile = open(input_file, 'r')
    scanners_data = infile.read().strip().split('\n\n')
    infile.close()

    scanners = []
    for scanner_data in scanners_data:
        scanner = []
        scanner_data_lines = scanner_data.split('\n')
        scanner_data_lines.pop(0)  # header
        for line in scanner_data_lines:
            coordinates = line.strip().split(',')
            assert len(coordinates) == 3
            coordinate = (int(coordinates[0]), int(coordinates[1]), int(coordinates[2]))
            scanner.append(coordinate)
        scanners.append(scanner)
    print("parse:OK")

    orientations = generate_orientations()

    scanner_locations = [None] * len(scanners)  # store identified scanner locations here
    scanner_locations[0] = ((0, 0, 0), (0, 1, 2, 1, 1, 1))  # use scanner #0 as absolute zero
    scanner_blacklist = []

    while not all(scanner_locations):
        for i in range(len(scanners)):
            if scanner_locations[i] is None:  # we won't be able to calculate absolute delta, orientation without this
                continue
            for j in range(len(scanners)):
                if i == j:  # do not match the scanner with itself
                    continue
                if scanner_locations[j] is not None:  # this scanner has been located, no need to do it again
                    continue
                if (scanners[i], scanners[j]) in scanner_blacklist:  # these two does not match
                    print("skipped blacklisted scanner combination: {} and {}".format(i, j))
                    continue
                print("checking if scanner {} and {} have at least {} matching beacons...".format(i, j, MIN_OVERLAPS_NEEDED))
                match = is_aligned(scanners[i], scanners[j], orientations)
                if match is not None:
                    orientation, delta = match
                    print("match found: sonar#{} and sonar#{}, with delta: {} and orientation: {}".format(i, j, delta, orientation))
                    transform(scanners[j], orientation, delta)
                    scanner_locations[j] = match
                    break
                else:  # these two scanners do not match after all orientations and shifts -> never try these again
                    scanner_blacklist.append((scanners[i], scanners[j]))

    # iterate through all scanner coordinates and count uniques
    global_scanner = []
    for i in range(len(scanners)):
        global_scanner += scanners[i]
    unique_beacons = list(set(global_scanner))
    print("number of unique beacons: {}".format(len(unique_beacons)))  # 430

    max_distance = 0
    for s1 in range(len(scanner_locations)):
        for s2 in range(len(scanner_locations)):
            if s1 == s2:
                continue
            l1 = scanner_locations[s1][1]
            l2 = scanner_locations[s2][1]
            manhattan_distance = abs(l1[0] - l2[0]) + abs(l1[1] - l2[1]) + abs(l1[2] - l2[2])
            max_distance = max(manhattan_distance, max_distance)
    print("largest Manhattan distance: {}".format(max_distance))  # 11860
    print("solve:OK")


solve("19/input.txt")
print("OK")
