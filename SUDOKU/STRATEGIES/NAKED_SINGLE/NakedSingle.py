class NakedSingle:
    name = "NAKED SINGLE"

    def __init__(self, board):
        self.board = board
        self.found_cell = None

    @property
    def trigger(self):
        self.found_cell = self.board.find_first_naked_single()
        return self.found_cell

    def iterate(self):
        if self.found_cell:
            self.found_cell.promote_naked_single()


