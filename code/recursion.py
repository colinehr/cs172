def population(initial: int, years: int) -> float:
    if years == 0:
        return initial
    return 1.1 * population(initial, years - 1)


# the number of ways to choose k items from a set of n items
# compute using Pascal's Triangle
def choose(n: int, k: int) -> int:
    if n == 0:
        return 1
    if k == 0:
        return 1
    if k == n:
        return 1
    return choose(n - 1, k - 1) + choose(n - 1, k)


def str_length(string: str) -> int:
    if string == "":
        return 0
    return 1 + str_length(string[:-1])


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
    pass


move3("A", "C", "B")
