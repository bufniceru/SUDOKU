import numpy as np

from SUDOKU.BOARD.Cell import Cell
from SUDOKU.BOARD.HELPERS.Coordinates import Coordinates
from SUDOKU.CONFIG.Constants import BOARD_INIT, BOARD_DIMENSION


class Board:
    """
    This Class keeps track of a Sudoku BOARD information:
     - values and markups of CELLS by coordinates
    Can give some Statistics
    """
    def __init__(self):
        self.board = None
        self.make_empty_board()

    def make_empty_board(self):
        self.board = np.array(BOARD_INIT)

        for line in range(0, BOARD_DIMENSION):
            for column in range(0, BOARD_DIMENSION):
                self.board[line][column] = Cell(None, Coordinates((line + 1, column + 1)))

    def cell(self, coordinates):
        return self.board[coordinates.line - 1][coordinates.column - 1]

    @property
    def validity(self):
        """
        Return True if grid is a valid Sudoku square, otherwise False.
        """
        return True

    @property
    def givens(self):
        """
        Returns the number of Given Cells in a Board
        """
        count = 0
        for cell in self.board.flatten():
            if cell.value.value is not None:
                count += 1
        return count

    @property
    def blanks(self):
        """
        Returns the number of Empty Cells in a Board
        """
        count = 0
        for cell in self.board.flatten():
            if cell.value.value is None:
                count += 1
        return count

    def how_many(self, value):
        """
        Returns the number of a Number Occurences
        """
        count = 0
        for cell in self.board.flatten():
            if cell.value.value == value:
                count += 1
        return count

    @property
    def line(self):
        return ''.join([f'{cell()}' for cell in self.board.flatten()])

    def __str__(self):
        return str(self.board)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass