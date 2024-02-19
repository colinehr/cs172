# Take two lists and return a list of all elements that appear in both lists.
# The resulting list should have no duplicates.
# Example: [1, 2, 3] and [3, 4, 1] will return [1, 3] (or [3, 1])
def matches(l1: list, l2: list) -> list:
    result = []
    i = 0
    while i < len(l1):
        if l1[i] in l2 and l1[i] not in result:
            result.append(l1[i])
        i += 1
    return result


a = [1, 2, 3, 3]
b = [3, 4, 1, 3]
print(matches(a, b))
