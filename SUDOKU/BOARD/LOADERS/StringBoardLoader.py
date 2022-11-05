from SUDOKU.BOARD.Board import Board
from SUDOKU.BOARD.HELPERS.Coordinates import Coordinates
from SUDOKU.CONFIG.Constants import ALL_POSSIBILITIES_SET


class StringBoardCreator:
    @staticmethod
    def create_board(problem_string):
        problem_string = problem_string.replace('.', '0')
        board = Board()
        for board_line, line in enumerate([problem_string[i:i + 9] for i in range(0, len(problem_string), 9)]):
            for board_column, char in enumerate(line):
                if int(char) in ALL_POSSIBILITIES_SET:
                    board.cell(Coordinates((board_line + 1, board_column + 1))).fill_value(int(char))
        return board
