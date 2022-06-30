"""Counter module"""

class Counter:
    """Counter class
    >>> c=Counter()
    >>> c.counter=10
    >>> c.counter
    10
    """

    def __init__(self, start=0):
        self._counter = start

    @property
    def counter(self):
        """get counter value"""
        self._counter += 1
        return self._counter

    @counter.setter
    def counter(self, value):
        """change counter value"""
        if value > 0:
            self._counter = value
        else:
            raise ValueError('Value below or equal zero')
        if self._counter > 999:
            self._counter = 0

    def __str__(self):
        return f'counter={self._counter}'

    def __repr__(self):
        return f'{self._counter}'


if __name__ == "__main__":  # pragma: no cover, don't test main
    # Exporatory tests
    # c = Counter()
    # Counter.counter_list()

    # print(c)
    # c.counter = 12
    # assert c.counter == 12
    # print(c)
    
    import doctest
    doctest.testmod()
