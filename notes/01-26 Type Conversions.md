# Type Conversions

## Definitions
An *explicit cast* is an intentional conversion from one type to another. The name of each type can be used as a function to perform the conversion. The conversion methods defined for casts throw away information in a reasonable way. For instance, casting a `float` to an `int` discards the fractional part by rounding towards zero (i.e., truncation).

An *implicit cast* is a conversion that happens automatically by Python in certain situations.
For example, in the code
```python
4 + 3.5
```
the `4` will be implicitly converted into a `float` and then added to `3.5` using regular `float` addition. Another example is the `print()` function, which will automatically convert whatever is given to it into a `str`. In the case of something like
```python
print(3.14159)
```
Python will convert the number `3.14159` into the string `'3.14159'` before printing.

## Table of type conversions

| Target →<br>Source ↓ | `bool`                                                           | `int`                                                                                               | `float`                                                                                                  | `str`                                                            |
|----------------------|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| `bool`               |                                                                  | `True` becomes `1`, `False` becomes `0`                                                             | `True` becomes `1.0`, `False` becomes `0.0`                                                              | Turns it into its string representation<br>`str(True) == 'True'` |
| `int`                | `0` becomes `False`, otherwise `True`<br>`bool(573) == True`     |                                                                                                     | Adds 0.0<br>`float(4) == 4.0`                                                                            | Turns it into its string representation<br>`str(5) == '5'`       |
| `float`              | `0.0` becomes `False`, otherwise `True`<br>`bool(3.142) == True` | Cuts off ("truncates") the decimal part<br>`int(-2.718) == -2`                                      |                                                                                                          | Turns it into its string representation<br>`str(6.28) == '6.28'` |
| `str`                | `''` becomes `False`, otherwise `True`<br>`bool("Hi!") == True`  | If the string "looks like" an integer, converts it, otherwise gives an Error<br>`int("312") == 312` | If the string "looks like" a decimal, converts it, otherwise gives an Error<br>`float("2.718") == 2.718` |                                                                  |

## Further reading
- [Python Documentation &mdash; Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Pythonorama &mdash; Built-in Types](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/built_in_types.md)