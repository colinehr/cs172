import math


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return d


def input_number() -> float:
    return float(input("What's the number? "))


x1 = input_number()
y1 = input_number()
x2 = input_number()
y2 = input_number()
x3 = input_number()
y3 = input_number()

d1 = distance(x1, y1, x2, y2)
d2 = distance(x2, y2, x3, y3)
d3 = distance(x3, y3, x1, y1)
print(d1 + d2 + d3)