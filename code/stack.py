import abc

class Stack(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def push(self, var: object):
        pass

    @abc.abstractmethod
    def pop(self) -> object:
        pass
