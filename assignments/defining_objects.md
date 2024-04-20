# Assignment: Defining Objects
This assignment is meant to give you practice defining objects.

You will define two classes:

- `Vector`, which has two attribute variables `_x` and `_y`
- `Starship`, which has three attribute variables `_name`, `_position`, and `_velocity`

Each class should be written in proper object-oriented style, including:

- Instance variables and methods
- One or more initializers
- Getters using `@property`
- `__str__` and `__eq__` methods
- `__add__`, `__sub__`, and `__mul__` methods as required
- Any other methods required by the tests (see below)
- A docstring comment associated with each method

The specification for these classes is given in the form of two pytest test files,[`test_vector.py`](test_vector.py) and [`test_starship.py`](test_starship.py). You'll have to examine these to determine what methods you need and what they're supposed to do.

Note that there is no main program to run here. You're just defining classes that might be used in other programs, such as games or control systems for actual spacecraft. Don't worry, it's just rocket science!

# Hints
Make sure `Vector` is finished (passing all tests) before starting on `Starship`.

For each class, first write enough of the class so that the test compiles. Methods don't have to do anything yet; leave them empty or with `pass` if they are supposed to return something. Once you can run the tests, work through the tests in the order they appear in the test file, doing whatever is necessary to pass each one.

There are no loops or recursion required to complete these classes; if you're using those, you're working too hard.

# What To Hand In
Hand in your classes `vector.py` and `starship.py`. Don’t forget to sign your work!
