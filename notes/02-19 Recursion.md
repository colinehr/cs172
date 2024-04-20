# Recursion

Consider the following function, which calculates $2^n$ for some integer input $n$:
```python
def pow2(n: int) -> int:
    if n == 0:
        return 1
    return 2 * pow2(n - 1)
```
This function is interesting because it calls itself! This is allowed, and is a technique called *recursion*. A function that uses recursion is called a *recursive function*. It is leveraging the fact that $2^n = 2 \cdot 2^{n-1}$ when $n \ge 0$, and that $2^0 = 1$. The following example shows one way to think about how Python is able to run this, by substituting `2 * pow2(n - 1)` for `pow2(n)`, unless $n$ is 0 in which case we'll substitute `1` for `pow2(0)`:
```
pow2(3)
2 * pow2(2)
2 * (2 * pow2(1))
2 * (2 * (2 * pow2(0)))
2 * (2 * (2 * 1))
2 * (2 * 2)
2 * 4
8
```
Notice how Python builds up the expression until it gets to `pow2(0)` which becomes 1, at which point Python can simplify the expression starting from the end and working backwards. Looking at recursion this way, as a series of substitutions, is called the *substitution model*.

## The Anatomy of a Recursive Function

Every recursive function has a *base case* and a *recursive step*. It's easier to see this by example. Let's say we wanted to write a recursive function which finds the length of a string. The first question to ask is: what is the simplest possible string that we can find the length of? I would say this is definitely the empty string `""`, since its length is 0. Let's start our recursive function with our base case:
```python
def str_length(string: str) -> int:
    if string == "":
        return 0
    ...
```
The next question is: what if my string *isn't* `""`? Well, in that case it will have at least one character, so the length will be at least 1, plus the length of the string without the first character. So, if we know the length of the string without the first character, we can get the length of the whole string. We can complete our function with the recursive step:
```python
def str_length(string: str) -> int:
    if string == "":
        return 0
    return 1 + str_length[1:len(string)]
```
Does this work? Let's analyze it with the substitution model:
```
str_length("abc")
1 + str_length("bc")
1 + (1 + str_length("c"))
1 + (1 + (1 + str_length("")))
1 + (1 + (1 + 0))
1 + (1 + 1)
1 + 2
3
```
The function will return 3 for the string `"abc"`, which is the desired answer.

## Additional Reading

- [Sedgewick and Wayne &mdash; Recursion](https://introcs.cs.princeton.edu/java/23recursion/)
