from stack import Stack


class EmptyStackError(Exception):
    pass


class EmptyQueueError(Exception):
    pass


class Node:
    _var: object
    _next: "Node"

    def __init__(self, var: object):
        self._var = var
        self._next = None


class OldStack:
    _first: Node

    def __init__(self):
        self._first = None

    def push(self, var: object):
        new_node = Node(var)
        if self._first is None:
            self._first = new_node
        else:
            # find the last node
            current_node = self._first
            while current_node._next is not None:
                current_node = current_node._next
            current_node._next = new_node
    
    def pop(self) -> object:
        # find the last node
        current_node = self._first
        previous_node = self._first
        while current_node._next is not None:
            previous_node = current_node
            current_node = current_node._next
        # unlink the last node
        previous_node._next = None
        # return the value of the last node
        return current_node._var
    

class LinkedStack(Stack):
    _first: Node

    def __init__(self):
        self._first = None

    def push(self, var: object):
        new_node = Node(var)
        new_node._next = self._first
        self._first = new_node

    def pop(self) -> object:
        if self._first is None:
            raise EmptyStackError("Can't pop from an empty Stack.")
        var = self._first._var
        self._first = self._first._next
        return var
    

class Queue:
    _first: Node
    _last: Node

    def __init__(self):
        self._first = None
        self._last = None

    def enqueue(self, var: object):
        new_node = Node(var)
        if self._last is None:
            self._last = new_node
            self._first = self._last
        else:
            self._last._next = new_node
            self._last = new_node

    def dequeue(self) -> object:
        if self._first is None:
            raise EmptyQueueError("Can't dequeue from an empty Queue.")
        var = self._first._var
        self._first = self._first._next
        if self._first is None:
            self._last = None
        return var


# I want to make a list of 1, 2, 4, 5
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(4)
queue.enqueue(5)

print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
print(queue.dequeue())  # 4
print(queue.dequeue())  # 5
print(queue.dequeue())  # error?

def make_stack() -> Stack:
    pass