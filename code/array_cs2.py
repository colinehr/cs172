# type: ignore
class Array:
    """A C-like array structure.
    
    Arrays are intended to imitate C arrays. This means that many operations with
    collections that are normally supported in Python, such as slicing or negative
    indices, are not supported here. Arrays cannot be resized once they are created.
    """
    _data: list

    def __init__(self, capacity: int):
        """Initialize an array with a given capacity.
        
        Upon creation, each element of the array is initialized to None.
        
        Args:
            capacity: the maximum number of items that can be held in the array
        """
        self._data = [None] * capacity

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index: int) -> object:
        if not isinstance(index, int):
            raise TypeError('Array indices must be integers, not ' + str(type(index)))
        if index < 0 or index >= len(self):
            raise IndexError('Array index out of range')
        return self._data[index]

    def __setitem__(self, index: int, value: object):
        if not isinstance(index, int):
            raise TypeError('Array indices must be integers, not ' + str(type(index)))
        if index < 0 or index >= len(self):
            raise IndexError('Array index out of range')
        self._data[index] = value

    def __repr__(self):
        return repr(self._data)

    def __str__(self):
        return str(self._data)
