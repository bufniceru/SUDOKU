from functools import singledispatchmethod

from SUDOKU.CONFIG.Constants import ALL_POSSIBILITIES_SET


class Value:
    """
    This Class keeps track of the value of a Sudoku Cell
    """
    @singledispatchmethod
    def __init__(self):
        """
        Constructor Void
        """

    @__init__.register(type(None))
    def _from_none(self, value: type(None)):
        """
        Constructor from None
        """
        self._value = bytearray()

    @__init__.register(int)
    def _from_int(self, value: int):
        """
        Constructor from Int
        """
        self._value = bytearray()
        self.from_int(value)

    @__init__.register(str)
    def _from_str(self, value: str):
        """
        Constructor from Str
        """
        self._value = bytearray()
        self.from_str(value)

    @property
    def value(self):
        """
        Value
        """
        if len(self._value) == 0:
            return None
        else:
            return int.from_bytes(bytes(self._value), 'big', signed=False)

    def from_int(self, value: int):
        """
        Fill The Content from Int
        """
        try:
            self.check(value)
        except:
            pass
        else:
            self._value.extend(value.to_bytes(1, 'big', signed=False))

    def from_str(self, value: str):
        """
        Fill The Content from Str
        """
        try:
            int_value = self.check(int(value))
        except:
            pass
        else:
            self._value.extend(int(value) .to_bytes(1, 'big', signed=False))

    def clear(self):
        """
        Clear Content
        """
        self._value.clear()

    @staticmethod
    def check(value) -> bool:
        """
        Check Value
        """
        try:
            value not in ALL_POSSIBILITIES_SET
        except:
            raise Exception(f"Value not suitable")
            return False
        else:
            if value not in ALL_POSSIBILITIES_SET:
                raise Exception(f"Value not in range")
            return True

    def __str__(self) -> str:
        if self.value is None:
            return f"{0}"
        else:
            return f"{self.value}"

    def __call__(self) -> int:
        if self.value is None:
            return 0
        else:
            return self.value