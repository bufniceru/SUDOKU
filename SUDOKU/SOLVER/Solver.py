from SUDOKU.BOARD.BoardManager import BoardManager
from SUDOKU.STRATEGIES.Strategies import Strategies


class Solver:
    def __init__(self, board: str):
        self.board = BoardManager(board)
        self.strategies = Strategies(self.board)

    def simple_elimination(self):
        """
        SIMPLE ELIMINATION PROCEDURE
        """
        for empty_cell in self.board.scan_empty_cells():
            empty_cell.markup_discard_neighbours()

    def solve(self):
        self.strategies.iterate()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass