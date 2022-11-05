from SUDOKU.BOARD.HELPERS.Coordinates import Coordinates
from SUDOKU.BOARD.HELPERS.Markup import Markup
from SUDOKU.BOARD.HELPERS.Value import Value
from SUDOKU.CONFIG.Constants import ALL_POSSIBILITIES_SET, BOARD_DIMENSION


class Cell:
    """
    This Class keeps track of Sudoku CELL information:
     - value
     - markup
     - coordinates
    Can keep track of a LINE or a COLUMN coordinate
    Can give information about the BLOCK in which the Cell is contained
    """
    def __init__(self, value=None, coordinates=None):
        try:
            self.check(value)
        except:
            self._value = Value(None)
            self._markup = Markup()
            try:
                self._coordinates = Coordinates((coordinates.line, coordinates.column))
            except:
                self._coordinates = Coordinates(None)
            else:
                self._coordinates = Coordinates((coordinates.line, coordinates.column))
        else:
            self._value = Value(value)
            self._markup = Markup()
            self._markup.value.clear()
            try:
                self._coordinates = Coordinates((coordinates.line, coordinates.column))
            except:
                self._coordinates = Coordinates(None)
            else:
                self._coordinates = Coordinates((coordinates.line, coordinates.column))

    @property
    def value(self):
        """
        VALUE
        """
        return self._value

    @property
    def markup(self):
        """
        MARKUP
        """
        return self._markup

    @property
    def coordinates(self):
        """
        COORDINATES
        """
        return self._coordinates

    def fill_value(self, value=None):
        try:
            self.check(value)
        except:
            self._value.clear()
            self._markup.reset()
        else:
            self._value.from_int(value)
            self._markup.discard_all()

    def fill_markup(self, markup):
        self._markup = markup

    def fill_coordinates(self, coordinates):
        self._coordinates = coordinates

    def clear_cell(self):
        """
        CLEAR CELL
        """
        self._value = Value(None)
        self._markup.reset()

    def check(self, value):
        """
        CHECK THE CELL VALUE
        """
        if value not in ALL_POSSIBILITIES_SET:
            raise Exception(f"Value not in range")

    def __str__(self):
        return f"C[{self.coordinates.line},{self.coordinates.column}]({self.value})"

    def __repr__(self):
        return f"{self.value}" if self.value is not None else f"0"

    def __call__(self):
        if self.value is None:
            return 0
        else:
            return self.value()

    def __eq__(self, other):
        return (self.value == other.value) and (self.coordinates == other.coordinates)