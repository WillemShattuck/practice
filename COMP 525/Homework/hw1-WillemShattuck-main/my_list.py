"""
Date: Feb 19
Name:Willem Shattuck
Sources:
"""


class MyList:

    """
    noop
    """

    def __init__(self):

        self._thelist = [None] * 4
        self._used = 0
        self._size = 4

    def append(self, item):
        """
        Adds item to the end of the list
        TODO: resize list when necessary
        """

        self._thelist[self._used] = item
        self._used += 1

    def pop(self):
        """
        If the list is emtpy, return None.
        Otherwise, return item at end of list and decrement used. 
        """

    def at(self, index):
        """
        If index is in bounds (0 - used), return the value
        at the index.  Otherwise, return IndexError 
        """

        return IndexError

    def index(self, value):
        """
        Returns index of value if value is found;
        otherwise, ValueError
        """

        # REWRITE this without enumerate!
        for i, n in enumerate(self._thelist):
            if value == n:
                return i
            
        return ValueError

    def insert(self, index, value):
        """
        Inserts value at index if index is in bounds (0 - used)
        Otherwise, returns IndexError
        The value inserted does not overwrite the existing 
        value; instead, existing values are moved over.  You 
        might have to increase the size of the array to do this.
        """

    def __len__(self) -> int:
        return self._used

    def __str__(self):

        v = "["

        for i in range(0, self._used):
            v += str(self._thelist[i])

        v += "]"

        return v




