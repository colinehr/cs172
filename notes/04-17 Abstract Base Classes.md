# Abstract Base Classes

Consider the following two class definitions:

```python
class Circle:
    _radius: float

    def __init__(self, radius: float):
        self._radius = radius

    def area(self) -> float:
        return self._radius * self._radius

    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

class Rectangle:
    _length: float
    _width: float

    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def area(self) -> float:
        return self._length * self._width

    def perimeter(self) -> float:
        return (2 * self._length) + (2 * self._width)
```

While both the `Circle` class and `Rectangle` class represent different shapes, they have multiple methods in common, namely `area()` and `perimeter()`. If, for example, we had a list containing some circles and some rectangles, we could calculate their combined area with the following code:
```python
shape_list = [Circle(5), Rectangle(2, 3)]
total_area = 0
for shape in shape_list:
    total_area += shape.area()
```
Because both `Circle` and `Rectangle` have an `area()` method, this code works no matter which type each element of `shape_list` is. It can be useful to group together classes that have similar behavior, and Python offers a formal way to do this, by defining the common methods within an *abstract base class*: 

```python
import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self) -> float:
        pass

    @abc.abstractmethod
    def perimeter(self) -> float:
        pass    
```
We tag each method with an `@abc.abstractmethod` decorator to specify that the `Shape` class will *not* actually have any code for these methods, but that any class that represents a shape should have those methods. The `Shape` class itself doesn't do anything; in fact, trying to instantiate a variable of type `Shape` results in a `TypeError`. However, this class allows us to specify *other* classes as `Shape`s, by putting it in parentheses by the class name:
```python
class Circle(Shape):
    ...

class Rectangle(Shape):
    ...
```
We say that `Circle` and `Rectangle` *implement the `Shape` base class*. We can then specify a function as being able to work with anything that implements `Shape`; for example, we could write our code that calculates the combined area of a list of shapes in the following way:
```python
def total_area(shape_list: list[Shape]) -> float:
    total = 0
    for shape in shape_list:
        total += shape.area()
    return total
```
This code makes it explicit that the input to the function should be a list of variables that all have `area()` and `perimeter()` methods. Python will always be smart enough to defer to the proper `area()` method for each individual shape in the list.

## Common ABCs

The [`collections.abc`](https://docs.python.org/3/library/collections.abc.html) module defines some abstract base classes that represent common types of data structures. For example, the [`Container`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container) abstract base class is used to specify that a class implements the `__contains__` method. The code that defines this looks something like:
```python
class Container(abc.ABC):
    @abc.abstractmethod
    def __contains__(self, item: object) -> bool:
        pass
```

The [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence) abstract base class defines the abstract methods `__getitem__` and `__len__`. It could be defined as follows:
```python
class Sequence(abc.ABC):
    @abc.abstractmethod
    def __getitem__(self, index: int) -> object:
        pass

    @abc.abstractmethod
    def __len__(self) -> int:
        pass

    def __contains__(self, item: object) -> bool:
        i = 0
        while i < len(self):
            if self[i] == item:
                return True
            i += 1
        return False
```
This code illustrates another purpose of ABCs: to allow a class that implements the abstract methods of an ABC to also *automatically* define other methods based off of the abstract methods. In this example, since we know the length of the `Sequence` as well as a way to go through its items in order, we can use those to automatically define a `__contains__` method for any classes that implement `Sequence`. The `__contains__` method is *not* an abstract method and is not decorated by the `@abc.abstractmethod` decorator, and thus does not need to be manually defined by any implementing class; it just gets it for free. Such a method is sometimes called a *mixin method*.

## Further Resources

- [The `abc` module documentation](https://docs.python.org/3/library/abc.html)