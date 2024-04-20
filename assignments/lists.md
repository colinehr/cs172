# Assignment: Lists

This assignment is meant to give you practice implementing some standard data structures and their associated algorithms.

## Description

You will define two classes, `ArrayList` and `LinkedList`. Each of these must implement the methods listed below. Your classes must pass the tests in the corresponding test classes `test_array_list.py` and `test_linked_list.py`, and must implement the abstract base class `AbstractList` found in `abstract_list.py`. *(Note: links to files will be added tomorrow morning when I get on campus.)*

| **Method**                                    | **Description**                                                                                                                                                                                                                             |
|-----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `append(self, item: object)`                  | Add an item to the end of the list (similar to pushing for stacks).                                                                                                                                                                         |
| `clear(self)`                                 | Remove all items from the list.                                                                                                                                                                                                             |
| `extend(self, iterable: Iterable)`            | Extend the list by appending all the items from the iterable. (Note: the only thing you can assume about the `iterable` variable is that you can iterate through its items with a `for` loop.)                                              |
| `index_of(self, item: object)`                | Return the index in the list of the first item whose value is equal to `item`. Raises a `ValueError` if there is no such item.                                                                                                              |
| `insert(self, index: int, item: object)`      | Insert an item at a given position. The first argument is the index of the element before which to insert, so `a.insert(0, x)` inserts at the front of the list, and `a.insert(len(a), x)` is equivalent to `a.append(x)`.                  |
| `pop(self, index: int = None) -> object`      | Remove the item at the given position in the list, and return it. If no index is specified, `a.pop()` removes and returns the last item in the list. It raises an `IndexError` if the list is empty or the index is outside the list range. |
| `__str__(self) -> str`                        | Return a string representing the content of the list.                                                                                                                                                                                       |
| `__eq__(self, other) -> bool`                 | Return `True` if the lists are equal.                                                                                                                                                                                                       |
| `__len__(self) -> int`                        | Return the number of items in the list.                                                                                                                                                                                                     |
| `__getitem__(self, index: int) -> object`     | Return the item at position `index` in the list.                                                                                                                                                                                            |
| `__setitem__(self, index: int, item: object)` | Replace the element at position `index` with `item`.                                                                                                                                                                                        |
| `__contains__(self, item: object) -> bool`    | Return `True` if the list contains the item.                                                                                                                                                                                                |
| `__iter__(self) -> Iterator`                  | Return an iterator for the content of the list.                                                                                                                                                                                             |

The orders of the amortized running times of your methods must be as follows:

| **Method**                                    | **ArrayList** | **LinkedList** |
|-----------------------------------------------|---------------|----------------|
| `append(self, item: object)`                  | $O(1)$        | $O(n)$         |
| `clear(self)`                                 | $O(1)$        | $O(1)$         |
| `extend(self, iterable: Iterable)`            | $O(n)$*       | $O(n)$*        |
| `index_of(self, item: object)`                | $O(n)$        | $O(n)$         |
| `insert(self, index: int, item: object)`      | $O(1)$        | $O(n)$         |
| `pop(self, index: int = None) -> object`      | $O(1)$        | $O(n)$         |
| `__str__(self) -> str`                        | $O(n)$        | $O(n)$         |
| `__eq__(self, other) -> bool`                 | $O(n)$        | $O(n)$         |
| `__len__(self) -> int`                        | $O(1)$        | $O(n)$         |
| `__getitem__(self, index: int) -> object`     | $O(1)$        | $O(n)$         |
| `__setitem__(self, index: int, item: object)` | $O(1)$        | $O(n)$         |
| `__contains__(self, item: object) -> bool`    | $O(n)$        | $O(n)$         |
| `__iter__(self) -> Iterator`                  | $O(1)$        | $O(1)$         |

*For the `extend` method you are allowed to iterate through both the list and the `iterable` variable.

We will talk about what this means on Monday, but essentially
- $O(1)$ means the function will take the same amount of time to run no matter how many items are in your list, i.e. no looping through your list! The one exception is in your `ArrayList`
- $O(n)$ means the function can take more time depending on how many items are in your list, i.e. you are allowed to loop through your list or call other functions that loop through your list.

A variable is an `Iterable` if it implements the `__iter__` method, and an `Iterator` if it implements the methods `__iter__` and `__next__`. You can specify these types in the signatures of your methods by importing their names from the `collections.abc` package:
```python
from collections.abc import Iterable, Iterator
```
See the [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable) and [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator) sections of the `collections.abc` packge documentation for more information.

There is no `main` program to run here. You are simply implementing data structures that could be used in other programs.

## Hints

- You may reuse any part of the `Stack` or `Queue` code that we have written in class or that appears on Pythonorama (see [Stacks](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/stacks.md) and [Queues](https://github.com/alainkaegi/pythonorama/blob/main/data_structures/queues.md)). But otherwise you are meant to write these classes yourself, not copy them from the Internet or delegate the work to an existing library.

- For the `ArrayList` implementation, you are encouraged to use the `Array` class from the [`array_cs2.py`](https://github.com/colinehr/cs172/blob/main/code/array_cs2.py) file linked here on my GitHub and import it with
```python
from array_cs2 import Array
```

- You don't have to write docstrings.

- The `pop(self, index: int = None)` method expands the method we defined for stacks by allowing the user to specify an optional integer which will pop the element at that index rather than the end of the list. That means that if `pop` is called with no arguments (for example `a.pop()`) the `index` variable will be `None`, and the method should pop the last element and return it in that case. 

- After all your tests but the last (`test_implements_abstractlist`) pass, you can edit your class to implement `AbstractList` by writing
```python
from abstract_list import AbstractList

class LinkedList(AbstractList):
    ...
```
This will give an error unless all the required methods outlined above are defined, so only do this once you're done with everything else!

## What To Hand In

Hand in your classes `array_list.py` and `linked_list.py`. Don’t forget to sign your work!