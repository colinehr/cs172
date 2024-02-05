# Takes a list of integers and returns their sum
def sum(l: list[int]) -> int:
    i = 0
    result = 0
    while i < len(l):
        result = result + l[i]
        i = i + 1
    return result

# Takes a list of integers and returns their average (mean)
def mean(l: list[int]) -> float:
    return sum(l) / len(l)


def median(l: list[int]) -> float:
    l.sort()
    if len(l) % 2 == 1:     # odd length case
        middle_index = (len(l) - 1) // 2    # force integer division
        return l[middle_index]
    else:                   # even length case
        index1 = len(l) // 2 - 1
        index2 = len(l) // 2
        return (l[index1] + l[index2]) / 2

l = []
number = input("Give me a number: ")
while number != "":
    l.append(int(number))
    number = input("Give me another number: ")
print(median(l))