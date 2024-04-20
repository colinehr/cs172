# Assignment: Rational Number Objects

This assignment is intended to give you more practice with designing, implementing, and testing a class.

Please define a class `Rational` that represents a fraction of integers (a.k.a. a rational number). Your class should implement at least the following API:

| **client operation** | **special method**         | **description**                                                |
|----------------------|----------------------------|----------------------------------------------------------------|
| `Rational(n, d)`     | `__init__(self, n, d)`     | a new `Rational` object with numerator `n` and denominator `d` |
| `x.numerator`        |                            | the numerator of `x`                                           |
| `x.denominator`      |                            | the numerator of `x`                                           |
| `x.is_integer()`     |                            | can `x` be written as a single integer?                        |
| `x + y`              | `__add__(self, other)`     | sum of `x` and `y`                                             |
| `x - y`              | `__sub__(self, other)`     | difference of `x` and `y`                                      |
| `x * y`              | `__mul__(self, other)`     | product of `x` and `y`                                         |
| `x / y`              | `__truediv__(self, other)` | quotient of `x` and `y`                                        |
| `-x`                 | `__neg__(self)`            | negation of `x`                                                |
| `abs(x)`             | `__abs__(self)`            | absolute value of `x`                                          |
| `round(x)`           | `__round__(self)`          | integer closest to `x`                                         |
| `float(x)`           | `__float__(self)`          | float representation of `x`                                    |
| `str(x)`             | `__str__(self, other)`     | string representation of `x`                                   |
| `x == y`             | `__eq__(self, other)`      | is `x` equal to `y`?                                           |
| `x < y`              | `__lt__(self, other)`      | is `x` less than `y`?                                          |
| `x <= y`             | `__le__(self, other)`      | is `x` less than or equal to `y`?                              |
| `x > y`              | `__gt__(self, other)`      | is `x` greater than `y`?                                       |
| `x >= y`             | `__ge__(self, other)`      | is `x` greater than or equal to `y`?                           |

Additionally, you should write a test function for each method you write. The tests should ensure that the method works, including corner cases. For example, to test `abs`, you should check both the positive case and the negative case. You will be graded partly on the comprehensiveness of your tests, but don't go overboard.

If the denominator of a `Rational` is ever 0, a `ValueError` should be raised with an appropriate error message. 

**Bonus:** For the arithmetic operations, also handle the case where `other` is an `int`, and for the comparison operations, also handle the cases where `other` is an `int` or a `float`. To check if a variable is a certain type, use the `isinstance()` function:
```python
def __add__(self, other) -> "Rational":
    if isinstance(other, float):
        # other is a float
    else:
        # assume other is a Rational
```

## Hints

The `math` module has a function `math.gcd()` which finds the greatest common divisor of two integers. This can be helpful when implementing your class.

Think hard about the possible corner cases. For example, when should two rational numbers be equal?

## How to Turn In

Turn in your code `rational.py` and your test file `test_rational.py`. Make sure to sign your work!