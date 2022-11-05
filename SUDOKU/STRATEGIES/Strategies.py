from SUDOKU.STRATEGIES.NAKED_SINGLE.NakedSingle import NakedSingle
from SUDOKU.STRATEGIES.SIMPLE_ELIMINATION.SimpleElimination import SimpleElimination


class Strategies:
    def __init__(self, board):
        self.board = board
        self._naked_single = NakedSingle(board)
        self._simple_elimination = SimpleElimination(board)

    @property
    def naked_single(self):
        return self._naked_single

    @property
    def simple_elimination(self):
        return self._simple_elimination

    def iterate(self):
        for strategy_str in self.get_strategies():
            strategy = self.__dict__['_' + strategy_str]
            if strategy.trigger:
                print(f'APPLING [{strategy_str.upper()}]')
                strategy.iterate()

    @classmethod
    def get_strategies(cls):
        """
        GET THE PROPERTY LIST IN CREATION ORDER OF THE MESSAGE
        """
        strategies_list = list([p for p in cls.__dict__ if isinstance(getattr(cls, p), property)])
        return strategies_list
