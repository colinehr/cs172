# Project: Lines of Action
This is a programming project. You may work with another person, but you should submit your own code. Please specify any additional people you work with upon submission.

## Overview
You will implement a two-player version of the board game Connect Four. The rules are available [online](https://en.wikipedia.org/wiki/Connect_Four), but essentially:
- Players take turns placing one of their tokens in a column,
- Pieces can only be played on the bottom-most empty slot in a column (i.e. the tokens are being "dropped" from top to bottom)
- The player who connects four of their pieces horizontally, vertically, or diagonally wins.

You should implement the standard version with 7 columns and 6 rows.

Your version does not need to be fancy, but it must:

- Have a graphic user interface similar to the Minesweeper game we developed in class.
- Prohibit illegal moves. (e.g. when a column is full)
- Detect when the game is over and who has won (it is much easier to display this information on the console, using print statements, rather than displaying it graphically).
- Be fully object-oriented.

You are implementing a game for two human players; you do not have to write an artificially intelligent opponent.

## Hints
The design is up to you, but here's one reasonable option:

![](connectfour.drawio.svg)

Don't go overboard creating objects. Even though pieces are physical "objects," it's simpler to represent the board as a two-dimensional array of, say, chars, with the entry at each location indicating whether it is red, yellow, or vacant.

Break down complicated methods, separate control from data, and take advantage of existing data structures.

## Rubric

- **Excellent (E):** The work exceeds the expectations of the assignment. Deep understanding of the concepts is evident. There are no nontrivial errors. Your code is readable, well-structured, and well-written. Code is cleanly divided into appropriately named classes and functions, and input and output types for functions are given. Each function, class, and file has a docstring written for it, and other more complicated parts of the code are explained with comments. For each function or method, enough tests have been written to ensure functionality (including corner cases), and all tests pass. This work could be used as an in-class example.
- **Meets Expectations (M):** Understanding of the concepts is evident. Code is correct and understandable. The logic of the code is broken up into classes and functions, and each function has tests, but some revision or expansion is needed. No additional instruction is needed.
- **Revision Needed (R):** Program appears to be functional, but little to no tests have been written. There may be some bugs still left in the code. The logic of the code is difficult to follow; classes aren't used, or there aren't enough functions, or the functions/classes are not breaking up the code in a logical way. The code shows only partial understanding of concepts and needs further work or more review.
- **Not Assessable (N):** The code does not work or does not satisfy the program specification. There is not enough to accurately assess understanding of concepts and code writing ability. Or, there are simply too many mistakes to justify correcting each one separately.

## What To Hand In

Hand in all of your `.py` files including tests.

Include your name and any other people you worked with in the `__author__` variable at the top of your code. For example, if I worked with Alain, the first line of my code would be
```python
__author__ = "Colin Ehr and Alain Kägi"
```
