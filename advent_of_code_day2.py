# Advent of Code 2021 Day 2

horizontal_pos = 0
depth = 0

with open("./data/input-day2.txt") as f:
    movements = []

    for line in f:
        movements.append(line)

# Part One

for movement in movements:
    if movement.startswith("forward"):
        horizontal_pos += int(movement.strip("forward "))
    elif movement.startswith("down"):
        depth += int(movement.strip("down "))
    elif movement.strip("up"):
        depth -= int(movement.strip("up "))

print(horizontal_pos * depth)

# Part Two

horizontal_pos = 0
depth = 0
aim = 0

for movement in movements:
    if movement.startswith("down"):
        aim += int(movement.strip("down "))
    elif movement.startswith("up"):
        aim -= int(movement.strip("up "))
    elif movement.startswith("forward"):
        horizontal_pos += int(movement.strip("forward "))
        depth += aim * int(movement.strip("forward "))

print(horizontal_pos * depth)

# Both work! Woohoo