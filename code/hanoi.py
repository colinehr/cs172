# Goal: give moves to solve the Tower of Hanoi puzzle for varying numbers of disks
# Example: https://www.mathsisfun.com/games/towerofhanoi.html

def move1(source: str, destination: str):
    print("Move from peg " + source + " to peg " + destination)


def move2(source: str, destination: str, other: str):
    move1(source, other)
    move1(source, destination)
    move1(other, destination)


# write a function which gives the solution for the Tower of Hanoi puzzle
# for 3 disks (using move1 and move2)
def move3(source: str, destination: str, other: str):
    move2(source, other, destination)
    move1(source, destination)
    move2(other, destination, source)


# write a function which gives the solution for the Tower of Hanoi puzzle
# with the number of disks given (you can use move1)
def move(disks: int, source: str, destination: str, other: str):
    if disks == 1:
        move1(source, destination)
        return                      # leave the function
    move(disks - 1, source, other, destination)
    move1(source, destination)
    move(disks - 1, other, destination, source)


move(4, "A", "C", "B")