from SUDOKU.BOARD.Cell import Cell
from SUDOKU.BOARD.HELPERS.Coordinates import Coordinates
from SUDOKU.CONFIG.Constants import BOARD_DIMENSION


class StringBoard:
    """
    This Class is an interface between a string representation of a Sudoku game
    and the Cells contained in the Board
    """
    def __init__(self, string):
        self.string = string

    def cell(self, line, column):
        """
        Returns an empty Cell with the given Coordinates
        Both line and colum can have values from 1 to 9 (not 0 to 8)
        """
        char = self.string[StringBoard.index(line - 1, column - 1)]
        return Cell(int(char) if char.isdigit() else 0, Coordinates((line, column)))

    @staticmethod
    def index(line, column):
        """
        Translates from the cell coordinates to string index
        """
        return line * BOARD_DIMENSION + column