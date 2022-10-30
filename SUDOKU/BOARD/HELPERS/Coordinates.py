from functools import singledispatchmethod

from SUDOKU.CONFIG.Constants import ALL_POSSIBILITIES_SET


class Coordinates:
    """
    This Class keeps track of the coordinates:
     - line
     - column
    of a Sudoku Cell
    Can keep track of a LINE coordinate or a COLUMN coordinate
    Can give information about the BLOCK in which the Cell is contained
    """
    @singledispatchmethod
    def __init__(self):
        """
        Constructor Void
        """

    @__init__.register(type(None))
    def _from_none(self, coordinates: type(None)):
        """
        Constructor from None
        """
        self._line = bytearray()
        self._column = bytearray()

    @__init__.register(tuple)
    def _from_tuple(self, coordinates: tuple):
        """
        Constructor from Tuple
        """
        self._line = bytearray()
        self.line_from_int(coordinates[0])
        self._column = bytearray()
        self.column_from_int(coordinates[1])

    @property
    def line(self):
        """
        Line
        """
        if len(self._line) == 0:
            return None
        else:
            return int.from_bytes(bytes(self._line), 'big', signed=False)

    @property
    def column(self):
        """
        Column
        """
        if len(self._column) == 0:
            return None
        else:
            return int.from_bytes(bytes(self._column), 'big', signed=False)

    def line_from_int(self, line: int = None):
        """
        Fill The Line from Int
        """
        try:
            self.check(line)
        except:
            pass
        else:
            self._line.extend(line.to_bytes(1, 'big', signed=False))

    def column_from_int(self, column: int = None):
        """
        Fill The Column from Int
        """
        try:
            self.check(column)
        except:
            pass
        else:
            self._column.extend(column.to_bytes(1, 'big', signed=False))

    @property
    def block_line_start(self):
        """
        BLOCK LINE START
        """
        return ((self.line - 1) // 3) * 3

    @property
    def block_line_finish(self):
        """
        BLOCK LINE FINISH
        """
        return self.block_line_start + 3

    @property
    def block_column_start(self):
        """
        BLOCK COLUMN START
        """
        return ((self.column - 1) // 3) * 3

    @property
    def block_column_finish(self):
        """
        BLOCK COLUMN FINISH
        """
        return self.block_column_start + 3

    @staticmethod
    def check(element):
        """
        CHECK THE LINE OR COLUMN NUMBER
        for DataType, Value and Range
        """
        try:
            element not in ALL_POSSIBILITIES_SET
        except:
            raise Exception(f"Value not suitable")
            return False
        else:
            if element not in ALL_POSSIBILITIES_SET:
                raise Exception(f"Value not in range")
            return True

    def __str__(self):
        line_str = '_' if self.line is None else self.line
        column_str = '_' if self.column is None else self.column
        return f"({line_str}:{column_str})"