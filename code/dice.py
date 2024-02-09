# Write a program that makes 10000 dice rolls
# Each dice roll is the sum of two six-sided dice
# Prints how many times each result occurs

import random


def roll(sides: int, num_dice: int) -> int:
    # Return an integer that is the sum of the dice thrown
    rolls = []
    i = 0
    while i < num_dice:
        rolls.append(random.randint(1, sides))
        i += 1
    return sum(rolls)


number_of_dice = 3

counts = [0] * (number_of_dice * 6 + 1)
i = 0
while i < 10000:
    throw = roll(6, number_of_dice)
    counts[throw] += 1
    i += 1

i = number_of_dice
while i < len(counts):
    print(str(i) + ": " + str(counts[i]))
    i += 1