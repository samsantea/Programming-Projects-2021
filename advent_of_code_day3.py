# Advent of Code 2021 Day 3

with open("./data/input-day3.txt") as f:
    diagnostic_report = []

    for line in f:
        diagnostic_report.append(line)

gamma_rate = ""
epsilon_rate = ""

one_bits = []
zero_bits = []

characters = len(diagnostic_report[0]) - 1

# Part 1

for i in range(characters):
    one_bits.append(0)
    zero_bits.append(0)

for number in diagnostic_report:
    for i in range(len(number)):
        if number[i] == "1":
            one_bits[i] += 1
        elif number[i] == "0":
            zero_bits[i] += 1

for i in range(len(one_bits)):
    if one_bits[i] > zero_bits[i]:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

print(int(gamma_rate, 2) * int(epsilon_rate, 2))