from SUDOKU.CONFIG.Constants import ALL_POSSIBILITIES_SET


class Markup:
    """
    This Class keeps track of the markup of a Sudoku Cell
    A Markup contains all possible values that can be place in a Cell
    at a given time as the Solving process take place due to the Strategies
    """
    def __init__(self):
        self._value = set(ALL_POSSIBILITIES_SET)

    @property
    def value(self):
        """
        VALUE
        """
        return self._value

    def fill(self, value):
        """
        Here value can be assigned dirrectly
        """
        self._value = value

    def discard(self, number):
        """
        Here a number si eliminated from value
        """
        self._value.discard(number)

    def discard_all(self):
        """
        Here value is emptyed as a set
        """
        self._value.clear()

    def reset(self):
        """
        Here value is reset to its initial value with all numbers possible
        """
        self._value = set(ALL_POSSIBILITIES_SET)

    def __str__(self):
        return f"{self.value}"

    def __eq__(self, other):
        return self.value == other.value
