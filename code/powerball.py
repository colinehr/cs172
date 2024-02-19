# Let user submit their "lottery ticket"
# Generate a random draw and check how many matches there are

import random


numbers = [52, 34, 1, 64, 12]
powerball = 17


draw = []
i = 0
while i < 5:
    draw.append(random.randint(1, 69))
    i += 1
draw.append(random.randint(1, 26))

print(draw)
