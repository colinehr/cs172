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

| Source ↓ / Target → | `bool` | `int` | `float` | `str` |
|--------------------:|--------|-------|---------|-------|
| `bool`              |        |       |         |       |
| `int`               |        |       |         |       |
| `float`             |        | Cuts off the decimal part.      |         |       |
| `str`               |        |       |         |       |

## Further reading
- [Python Documentation &mdash; Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Pythonorama &mdash; Built-in Types](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/built_in_types.md)