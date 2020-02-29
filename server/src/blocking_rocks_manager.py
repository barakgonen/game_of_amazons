import logging
from server.src.constants import Constants


class BlockingRocksManager:
    def __init__(self, board_size, available_movements_manager):
        if board_size == Constants.SMALL_BOARD_SIZE:
            self.available_rocks = Constants.NUMBER_OF_ROCKS_IN_SMALL_BOARD
        elif board_size == Constants.LARGE_BOARD_SIZE:
            self.available_rocks = Constants.NUMBER_OF_ROCKS_IN_LARGE_BOARD
        self.available_movements_manager = available_movements_manager

    def get_rock(self):
        if self.available_rocks > 0:
            self.available_rocks -= 1
            logging.debug("<get_rock()> Returning available rock")
            return True
        else:
            logging.info("<get_rock()> There are not enough rocks... Game must over")
            return False

    def are_blocks_available(self):
        if self.available_rocks > 0:
            logging.debug("<are_blocks_available()> blocks are available")
            return True
        else:
            logging.info("<are_blocks_available()> There are not enough rocks... Game must over")
            return False

    def generate_available_throwing_options(self, board_game, throwing_from):
        return self.available_movements_manager.get_available_moves_set_for_amazon(board_game, throwing_from)
