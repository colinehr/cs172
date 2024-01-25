# Wed. 1/24 &mdash; Types and Variables

## What are types?

Every variable and value in Python (or any programming language) is stored in memory as a sequence of 1s and 0s. Because of this, Python needs to know how to convert the 1s and 0s into the actual value. Each variable has a *type* which dictates how to translate from 1s and 0s to the actual value, and also tells us what sorts of operations we can do with it.

## Main built-in types in Python
- `int` is used to represent integer values. If a number is of type `int`, it is an *exact* representation of the number. For example: `-2`, `7`, `65837`.
- `float` is used to represent decimal values. (it stands for "floating point" because the decimal point can move around) Many real numbers cannot be represented exactly since you can only hold a finite number of decimal places in a machine. Therefore it's possible for there to be rounding errors.
- `bool` has two possible values: `True` and `False`
- `str` represents sequences of characters. Note that unlike C there is no `char` type; everything is a string in Python.
- `list` represents arrays in Python. There are many differences between C arrays and Python lists that we will get into.

## Definitions

A *literal* is a representation of a data-type value.

An *operator* is a representation of an operation on some data type.

A *variable* is an entity that holds a data-type value.

## Some operators and examples of literals

| type    | operators                     | sample literal values           |
|---------|-------------------------------|---------------------------------|
| `int`   | `+` `-` `*` `**` `/` `//` `%` | `1` `-21` `2024`                |
| `float` | `+` `-` `*` `**` `/`          | `1.0` `3.1415` `-0.23`          |
| `bool`  | `and` `or` `not`              | `True` `False`                  |
| `str`   | `+` `*` `in`                  | `""` `"a"` `'abc'` `'Hello!\n'` |

## Variables

Each of the following lines of code defines a variable in Python:

```python
x = 1
pi = 3.1415
greeting = "Howdy!"
```

Notice that unlike in C, we don't have to explicitly say the type of the variable; it's inferred from context. In fact, we can even change the type of a variable after we declare it, so we are allowed to write

```python
var = 1
var = "Careful!"
```

In C we would get an error, but not so in Python. That being said, even though it doesn't give an error, it's best practice to make sure each variable's type is consistent throughout a program.

## Identifying the type of a variable

To get the type of a variable or literal, use the `type()` function. For literals, that looks like:

```python
type(1)         # int
type(1.0)       # float
type(1/3)       # float
type("Hi!")     # str
type(False)     # bool
```

And for variables it looks like:

```python
x = 3
type(x)         # int
```

## Further reading

- [Python Documentation &mdash; Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Pythonorama &mdash; Built-in Types](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/built_in_types.md)
- [Pythonorama &mdash; Operators](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/operators.md)
- [Pythonorama &mdash; Variables](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/variables.md)
- [Sedgewick, Wayne &mdash; Built-in Types of Data](https://introcs.cs.princeton.edu/python/12types/)