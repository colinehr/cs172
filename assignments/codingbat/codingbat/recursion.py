# Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1.
# Compute the result recursively (without loops).
def factorial(n: int) -> int:
    pass


# We have a number of bunnies and each bunny has two big floppy ears. We want to
# compute the total number of ears across all the bunnies recursively (without loops or
# multiplication).
def bunny_ears(bunnies: int) -> int:
    pass


# The fibonacci sequence is a famous bit of mathematics, and it happens to have a
# recursive definition. The first two values in the sequence are 0 and 1 (essentially 2
# base cases). Each subsequent value is the sum of the previous two values, so the
# whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive
# fibonacci(n) method that returns the nth fibonacci number, with n=0 representing the
# start of the sequence.
def fibonacci(n: int) -> int:
    pass


# We have triangle made of blocks. The topmost row has 1 block, the next row down has 2
# blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or
# multiplication) the total number of blocks in such a triangle with the given number
# of rows.
def triangle(n: int) -> int:
    pass


# Given a non-negative int n, return the sum of its digits recursively (no loops). 
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while integer
# division (//) by 10 removes the rightmost digit (126 // 10 is 12).
def sum_digits(n: int) -> int:
    pass


# Given a non-negative int n, return the count of the occurrences of 7 as a digit, so
# for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost
# digit (126 % 10 is 6), while integer division (//) by 10 removes the rightmost digit
# (126 // 10 is 12).
def count7(n: int) -> int:
    pass


# Given base and n that are both 1 or more, compute recursively (no loops) the value of
# base to the n power, so power_n(3, 2) is 9 (3 squared).
def power_n(base: int, n: int) -> int:
    pass


# Given a string, compute recursively (no loops) the number of lowercase "x" in the
# string.
def count_x(string: str) -> int:
    pass


# Given a string, compute recursively (no loops) the number of times lowercase "hi"
# appears in the string.
def count_hi(string: str) -> int:
    pass


# Given a string, compute recursively (no loops) a new string where all the lowercase
# 'x's have been changed to 'y's.
def change_xy(string: str) -> str:
    pass


# Given a string, compute recursively a new string where all the 'x's have been removed.
def no_x(string: str) -> str:
    pass


# Given an array of ints, compute recursively the number of times that the value 11
# appears in the part of the array that begins at the given index. 
def count_11(l: list[int]) -> int:
    pass


# Given a string, compute recursively a new string where all the adjacent characters
# are now separated by a "*". (For example, "hello" becomes "h*e*l*l*o")
def all_star(string: str) -> str:
    pass


# Given a string, compute recursively a new string where identical characters that are
# adjacent in the original string are separated from each other by a "*". (For example,
# "hello" becomes "hel*lo")
def pair_star(string: str) -> str:
    pass


# Given a string, return recursively a "cleaned" string where adjacent characters that
# are the same have been reduced to a single char. So "yyzzza" yields "yza".
def string_clean(string: str) -> str:
    pass


# Given a string that contains a single pair of parenthesis, compute recursively a new
# string made of only of the parenthesis and their contents, so "xyz(abc)123" yields
# "(abc)".
def paren_bit(string: str) -> str:
    pass


# Given a string, return True if it is a nesting of zero or more pairs of parenthesis,
# like "(())" or "((()))". Suggestion: check the first and last chars, and then recur
# on what's inside them.
def nest_parens(string: str) -> bool:
    pass


# Given a string and a non-empty substring sub, compute recursively the number of times
# that sub appears in the string, without the sub strings overlapping.
def str_count(string: str, sub: str) -> int:
    pass


# Given a string and a non-empty substring sub, compute recursively the largest
# substring which starts and ends with sub and return its length.
def str_dist(string: str, sub: str) -> int:
    pass
