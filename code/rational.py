# create a class called Rational which represents a fraction of integers
# properties should be:
#   - numerator (int)
#   - denominator (int)
# methods should be:
#   - a + b, a - b, a * b, a / b, abs(a), str(a), a == b
#   - a < b, a > b (__lt__ and __gt__)
# write tests for Rational

import math         # use math.gcd(a, b)


class Rational:
    _numerator: int
    _denominator: int

    def __init__(self, n: int, d: int):
        self._numerator = n
        self._denominator = d