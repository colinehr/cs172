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


print(choose(4, 2))