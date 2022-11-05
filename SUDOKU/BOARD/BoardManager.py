from SUDOKU.BOARD.Board import Board
from SUDOKU.BOARD.HELPERS.Coordinates import Coordinates
from SUDOKU.BOARD.WorkingCell import WorkingCell
from SUDOKU.CONFIG.Constants import BOARD_DIMENSION


class BoardManager(Board):
    """
    This Class involves some solving logic in addition to a Simple BOARD.
    It needs a Current CELL that scan the BOARD for different purposes.
    """
    def __init__(self, board=None):
        Board.__init__(self)
        if board is not None:
            self.board = board.board
        self.current_cell = WorkingCell(self, self.cell(Coordinates((1,1))))
        # self.current_cell.move(self.cell(Coordinates(1,1)))

    def find_first_empty_cell(self):
        """
        First Empty Cell is returned if found
        If there is no Cell found then the Sudoku is Solved.
        """
        for cell in self.scan_empty_cells():
            return cell
        else:
            return None

    def find_first_naked_single(self):
        """
        First Naked Single Cell is returned if found
        """
        for cell in self.scan_empty_cells():
            if len(cell.markup.value) == 1:
                return cell
        else:
            return None

    def scan_empty_cells(self):
        """
        Scan the Board for empty cell
        """
        for cell in self.scan_cells():
            if cell.value.value is None:
                self.current_cell = WorkingCell(self, self.cell(Coordinates((cell.coordinates.line, cell.coordinates.column))))
                yield self.current_cell

    def scan_non_empty_cells(self):
        """
        Scan the Board for non empty cell
        """
        for cell in self.scan_cells():
            if cell.value.value is not None:
                yield cell

    def scan_cells(self):
        """
        Scan the Board for all cell
        Line by Line, Column by Column
        """
        for line_no in range(1, BOARD_DIMENSION + 1):
            for column_no in range(1, BOARD_DIMENSION + 1):
                yield self.cell(Coordinates((line_no, column_no)))
