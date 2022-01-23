# https://adventofcode.com/2021/day/17

# SAMPLE
# target area: x=20..30, y=-10..-5
target_x = [20, 30]
target_y = [-10, -5]
# velocity ranges to probe brute force (start by big enough values then tweak it down based on the printed value range)
velocity_range_x = [0, 40]
velocity_range_y = [-30, 1000]
steps_range = 25  # we conclude if we hit or miss after this amount of steps

# INPUT
# target area: x=144..178, y=-100..-76
target_x = [144, 178]
target_y = [-100, -76]
# velocity ranges to probe brute force
velocity_range_x = [0, 350]
velocity_range_y = [-101, 100]
steps_range = 200  # we conclude if we hit or miss after this amount of steps


total_max_y = 0
hit_counter = 0

# guide values to calibrate ranges
total_max_steps_to_hit = 0
range_y_min = 999999
range_y_max = 0

for x in range(velocity_range_x[0], velocity_range_x[1]):
    for y in range(velocity_range_y[0], velocity_range_y[1]):
        hit = False
        probe_x = 0
        probe_y = 0
        velocity_x = x
        velocity_y = y
        y = y
        probe_max_y = 0
        hit = False
        for steps in range(steps_range):
            # new coordinates
            probe_x += velocity_x
            probe_y += velocity_y
            probe_max_y = max(probe_y, probe_max_y)
            # update velocities with drag
            if velocity_x > 0:
                velocity_x -= 1
            if velocity_x < 0:
                velocity_x += 1
            velocity_y -= 1
            if target_x[0] <= probe_x <= target_x[1] and target_y[0] <= probe_y <= target_y[1]:  # hit the target
                hit = True
                total_max_steps_to_hit = max(steps, total_max_steps_to_hit)
                range_y_min = min(y, range_y_min)
                range_y_max = max(y, range_y_max)
                break
        if hit:
            hit_counter += 1
            total_max_y = max(total_max_y, probe_max_y)
            print("x={}, y={}, velocity_range_min_y={}, velocity_range_max_y={}, total_max_steps_to_hit={}, total_max_y={}"
                  .format(x, y, range_y_min, range_y_max, total_max_steps_to_hit, total_max_y))

print("part 1: highest y position reached whilst hitting the target: {}".format(total_max_y))  # 4950
print("part 2: number of distinct initial velocity values hit the target: {}".format(hit_counter))  # 1477
print("OK")
