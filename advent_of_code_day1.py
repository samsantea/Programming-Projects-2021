# Advent of Code 2021 Day 1

# Open file using f as the name for it
# Destroys f variable after done
with open("./data/input-day1.txt") as f:
    depths = []

    for line in f:
        # Add the INTEGER to a list of depth
        depths.append(int(line))

# Part One

larger = 0

for i in range(len(depths)):
    if depths[i] > depths[i-1]:
        larger += 1

print(larger)

# Part Two

all_sums = []

for i in range(len(depths)):
    if not i + 2 >= 2000:
        x = i + 1
        y = i + 2
        depths_sum = depths[i] + depths[x] + depths[y]
        all_sums.append(depths_sum)

sum_larger = 0

for i in range(len(all_sums)):
    if all_sums[i] > all_sums[i - 1]:
        sum_larger += 1

print(sum_larger)

# Both work! Yay!