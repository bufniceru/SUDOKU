from SUDOKU.CONFIG.Constants import ALL_POSSIBILITIES_SET


class Markup:
    """
    This Class keeps track of the markup of a Sudoku Cell
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
        self._value = value

    def discard(self, number):
        self._value.discard(number)

    def discard_all(self):
        self._value.clear()

    def reset(self):
        self._value = set(ALL_POSSIBILITIES_SET)

    def __str__(self):
        return f"{self.value}"
