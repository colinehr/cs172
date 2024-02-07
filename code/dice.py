# Write a program that makes 10000 dice rolls
# Each dice roll is the sum of two six-sided dice
# Prints how many times each result occurs

import random


def roll(sides: int, num_dice: int) -> int:
    # Return an integer that is the sum of the dice thrown
    pass


counts = [0] * 13
i = 0
while i < 10000:
    roll = random.randint(1, 6) + random.randint(1, 6)
    counts[roll] += 1
    i += 1
print(counts)

# Modify this to give a more human-friendly output (bonus: give percents)