from array_cs2 import Array
from stack import Stack

class ArrayStack(Stack):
    _a: Array
    _n: int

    def __init__(self):
        self._a = Array(1)
        self._n = 0

    def push(self, var: object):
        if len(self._a) == self._n:
            # create a new array with double capacity
            new_a = Array(self._n * 2)
            # copying current array into new array
            i = 0
            while i < self._n:
                new_a[i] = self._a[i]
                i += 1
            self._a = new_a
        # add var to next empty spot
        self._a[self._n] = var
        self._n += 1

    def pop(self) -> object:
        var = self._a[self._n - 1]
        self._a[self._n - 1] = None
        self._n -= 1
        if len(self._a) >= 2 * self._n:
            # create a new array with half capacity
            new_a = Array(self._n)
            # copying current array into new array
            i = 0
            while i < self._n:
                new_a[i] = self._a[i]
                i += 1
            self._a = new_a
        return var

stack = ArrayStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
print(stack.pop())
print(stack.pop())
stack.push(6)
print(stack.pop())
print(stack.pop())
