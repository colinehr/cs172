# Let user input a space-separated list of instructions
# All instructions are either: F (forward), L (turn left), R (turn right)
# Print the position of the turtle after it follows the instructions
# Assume the turtle begins by facing in the positive x direction

s = input("Direct the turtle: ")
instructions = s.split(" ")

x = 0
y = 0
direction = ???

i = 0
while i < len(instructions):
    if instructions[i] == "F":
        # do something
    elif instructions[i] == "L":
        # do something
    elif instructions[i] == "R":
        # do something