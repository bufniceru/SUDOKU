class SimpleElimination:
    name = "SIMPLE ELIMINATION"

    def __init__(self, board):
        self.board = board
        self.found_cell = None

    @property
    def trigger(self):
        return True

    def iterate(self):
        for empty_cell in self.board.scan_empty_cells():
            empty_cell.markup_discard_neighbours()

