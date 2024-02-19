# Let user input a space-separated list of instructions
# All instructions are either: F (forward), L (turn left), R (turn right)
# Print the position of the turtle after it follows the instructions
# Assume the turtle begins by facing in the positive x direction

import math
import turtle


s = input("Direct the turtle: ")
instructions = s.split(" ")

x = 0
y = 0
direction = 0       # degrees from positive x-axis

i = 0
while i < len(instructions):
    if instructions[i] == "F":
        x = x + math.cos(direction * math.pi/180)
        y = y + math.sin(direction * math.pi/180)
        turtle.forward(100)
    elif instructions[i] == "L":
        direction = direction + 90
        turtle.left(90)
    elif instructions[i] == "R":
        direction = direction - 90
        turtle.right(90)
    i += 1

x = int(round(x, 0))
y = int(round(y, 0))
print("(" + str(x) + ", " + str(y) + ")")


turtle.done()