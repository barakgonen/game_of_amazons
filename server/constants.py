from enum import Enum

SMALL_BOARD_SIZE = 6
LARGE_BOARD_SIZE = 10
NUMBER_OF_ROCKS_IN_SMALL_BOARD = 32
NUMBER_OF_ROCKS_IN_LARGE_BOARD = 92

COLUMNS_ARRAY = ["","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

class CellState(Enum):
    EMPTY = "E" # for empty
    BLOCKED = "*" # for blocked
    WHITE_AMAZON = "w" # for white amazon
    BLACK_AMAZON = "b" # for black_amazon

    def __str__(self):
        return str(self.value)