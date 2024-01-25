# The parameter weekday is True if it is a weekday, and the parameter vacation is True
# if we are on vacation. We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.
def sleep_in(weekday: bool, vacation: bool) -> bool:
    pass


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each
# is smiling. We are in trouble if they are both smiling or if neither of them is
# smiling. Return True if we are in trouble.
def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:
    pass


# Given two int values, return their sum. Unless the two values are the same, then
# return double their sum.
def sum_double(a: int, b: int) -> int:
    pass


# Given an int n, return the absolute difference between n and 21, except return double
# the absolute difference if n is over 21.
def diff21(n: int) -> int:
    pass


# We have a loud talking parrot. The "hour" parameter is the current hour time in the
# range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or
# after 20. Return True if we are in trouble.
def parrot_trouble(talking: bool, hour: int) -> bool:
    pass


# Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.
def makes10(a: int, b: int) -> bool:
    pass


# Given an int n, return True if it is within 10 of 100 or 200.
# Note: abs(num) computes the absolute value of a number.
def near_hundred(n: int) -> bool:
    pass


# Given a non-empty str and an int n, return a new str where the character at index n
# has been removed. The value of n will be a valid index of a character in the original
# str (i.e. n will be in the range 0..len(string) inclusive).
def missing_char(string: str, index: int) -> str:
    pass


# Given a str, return a new str where the first and last chars have been exchanged.
def front_back(string: str) -> str:
    pass


# Given a str, we'll say that the front is the first 3 chars of the str. If the str
# length is less than 3, the front is whatever is there. Return a new str which is
# 3 copies of the front.
def front3(string: str) -> str:
    pass


# Given a str, take the last character and return a new str with the last character
# added at the front and back, so "cat" yields "tcatt". The original str will be length
# 1 or more.
def back_around(string: str) -> str:
    pass


# Return True if the given non-negative number is a multiple of 3 or a multiple of 5.
# Use the % "mod" operator.
def or35(n: int) -> bool:
    pass


# Given a str, take the first 2 characters and return the str with the 2 characters
# added at both the front and back, so "kitten" yields "kikittenki". If the str length
# is less than 2, use whatever characters are there.
def front22(string: str) -> str:
    pass


# Given a str, return True if the str starts with "hi" and False otherwise.
def start_hi(string: str) -> bool:
    pass


# Given two temperatures, return True if one is less than 0 and the other is greater
# than 100.
def icy_hot(temp1: int, temp2: int) -> bool:
    pass


# We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 3 int
# values, return True if one or more of them are teen.
def has_teen(a: int, b: int, c: int) -> bool:
    pass


# We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 2 int
# values, return True if one or the other is teen, but not both.
def lone_teen(a: int, b: int) -> bool:
    pass


# Given a str, if the string "del" appears starting at index 1, return a str
# where that "del" has been deleted. Otherwise, return the string unchanged.
def del_del(string: str) -> str:
    pass


# Return True if the given str begins with "mix", except the 'm' can be anything, so
# "pix", "9ix" .. all count.
def mix_start(string: str) -> bool:
    pass


# Given a string, return a string made of the first 2 characters (if present), however
# include first character only if it is 'o' and include the second only if it is 'z',
# so "ozymandias" yields "oz".
def start_oz(string: str) -> str:
    pass


# Given three int values, a b c, return the largest. Do not use the max() function.
def int_max(a: int, b: int, c: int) -> int:
    pass


# Given 2 int values, return whichever value is nearest to the value 10, or return 0 in
# the event of a tie. Note that abs(n) returns the absolute value of a number.
def close10(a: int, b: int) -> int:
    pass


# Given 2 int values, return True if they are both in the range 30..40 inclusive, or
# they are both in the range 40..50 inclusive.
def in3050(a: int, b: int) -> bool:
    pass


# Given 2 positive int values, return the larger value that is in the range 10..20
# inclusive, or return 0 if neither is in that range.
def max1020(a: int, b: int) -> int:
    pass


# Return True if the given str contains between 1 and 3 'e' characters.
def string_e(string: str) -> bool:
    pass


# Given two non-negative int values, return True if they have the same last digit, such
# as with 27 and 57.
def last_digit(a: int, b: int) -> bool:
    pass


# Given a str, return a new str where the last 3 characters are now in upper case. If
# the str has less than 3 characters, uppercase whatever is there. Note that
# "hello".upper() returns the uppercase version of the string "hello".
def end_up(string: str) -> str:
    pass


# Given a non-empty str and an int n, return the str made starting with character 0,
# and then every nth character of the str. So if n is 3, use character 0, 3, 6, ... and
# so on. n is 1 or more.
def every_nth(string: str, n: int) -> str:
    pass
