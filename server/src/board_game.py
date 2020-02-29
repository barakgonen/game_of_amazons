import numpy
import logging
import pandas as pd

from server.src.constants import Constants
from server.src.common_funcs import get_col_index, get_raw_index


class BoardGame:
    def __init__(self, size, points_ctor=False, white_amazons=None, black_amazons=None, blockers_pos=None):
        self.size = size
        self.board = numpy.zeros((self.size, self.size), dtype=numpy.int)

        if white_amazons is None and black_amazons is None and blockers_pos is None:
            logging.info("<BoardGame::BoardGame()> Placing amazons in the board. Board size is: " + str(size))
            try:
                if self.size == Constants.LARGE_BOARD_SIZE:
                    self.board[get_raw_index(7, self.size)][get_col_index('A', self.size)] = Constants.BLACK_AMAZON_VAL
                    self.board[get_raw_index(10, self.size)][get_col_index('D', self.size)] = Constants.BLACK_AMAZON_VAL
                    self.board[get_raw_index(10, self.size)][get_col_index('G', self.size)] = Constants.BLACK_AMAZON_VAL
                    self.board[get_raw_index(7, self.size)][get_col_index('J', self.size)] = Constants.BLACK_AMAZON_VAL
                    self.board[get_raw_index(4, self.size)][get_col_index('A', self.size)] = Constants.WHITE_AMAZON_VAL
                    self.board[get_raw_index(1, self.size)][get_col_index('D', self.size)] = Constants.WHITE_AMAZON_VAL
                    self.board[get_raw_index(1, self.size)][get_col_index('G', self.size)] = Constants.WHITE_AMAZON_VAL
                    self.board[get_raw_index(4, self.size)][get_col_index('J', self.size)] = Constants.WHITE_AMAZON_VAL

                elif self.size == Constants.SMALL_BOARD_SIZE:
                    self.board[get_raw_index(4, self.size)][get_col_index('A', self.size)] = Constants.BLACK_AMAZON_VAL
                    self.board[get_raw_index(3, self.size)][get_col_index('F', self.size)] = Constants.BLACK_AMAZON_VAL
                    self.board[get_raw_index(1, self.size)][get_col_index('C', self.size)] = Constants.WHITE_AMAZON_VAL
                    self.board[get_raw_index(6, self.size)][get_col_index('D', self.size)] = Constants.WHITE_AMAZON_VAL
            except IndexError as err:
                print(err)
        else:
            logging.info("<BoardGame::BoardGame()> setting the board for us")
            if points_ctor:
                self.__set_from_points(white_amazons, black_amazons, blockers_pos)
            else:
                self.__set_from_tuples(white_amazons, black_amazons, blockers_pos)

    def __set_from_tuples(self, white_amazons, black_amazons, blockers_pos):
        for white_amazon in white_amazons:
            self.board[white_amazon[0]][white_amazon[1]] = Constants.WHITE_AMAZON_VAL
        for black_amazon in black_amazons:
            self.board[black_amazon[0]][black_amazon[1]] = Constants.BLACK_AMAZON_VAL
        for blocker_pos in blockers_pos:
            self.board[blocker_pos[0]][blocker_pos[1]] = Constants.BLOCKED_CELL_VAL

    def __set_from_points(self, white_amazons, black_amazons, blockers_pos):
            for white_amazon in white_amazons:
                self.board[get_raw_index(white_amazon.y, self.size)][
                    get_col_index(white_amazon.x, self.size)] = Constants.WHITE_AMAZON_VAL
            for black_amazon in black_amazons:
                self.board[get_raw_index(black_amazon.y, self.size)][
                    get_col_index(black_amazon.x, self.size)] = Constants.BLACK_AMAZON_VAL
            for blocker_pos in blockers_pos:
                self.board[get_raw_index(blocker_pos.y, self.size)][
                    get_col_index(blocker_pos.x, self.size)] = Constants.BLOCKED_CELL_VAL

    def __eq__(self, other):
        if self.size == other.get_size():
            for i in range(0, len(self.board)):
                for j in range(0, len(self.board[i])):
                    if self.board[i][j] != other.board[i][j]:
                        return False
        else:
            return False
        return True

    def print_board(self):
        pf = pd.DataFrame(self.board, columns=Constants.COLUMNS_ARRAY[:self.size],
                          index=reversed(range(1, self.size + 1)))
        print(pf)

    def get_size(self):
        logging.debug("<get_size()> Returning size of the board. size is: " + str(self.size))
        return self.size

    def is_free_cell(self, raw, col):
        return self.board[raw][col] == Constants.EMPTY_CELL_VAL

    def is_black_amazon(self, raw, col):
        return self.board[get_raw_index(raw, self.size)][get_col_index(col, self.size)] == Constants.BLACK_AMAZON_VAL

    def is_white_amazon(self, raw, col):
        return self.board[get_raw_index(raw, self.size)][get_col_index(col, self.size)] == Constants.WHITE_AMAZON_VAL

    def update_move(self, amazon_to_update, new_position, amazon_color):
        # input validation
        if ((amazon_color == "BLACK" and self.is_black_amazon(amazon_to_update.y, amazon_to_update.x))
                or (amazon_color == "WHITE") and self.is_white_amazon(amazon_to_update.y, amazon_to_update.x)):
            self.board[get_raw_index(new_position.y, self.size)][get_col_index(new_position.x, self.size)] = \
                self.board[get_raw_index(amazon_to_update.y, self.size)][get_col_index(amazon_to_update.x, self.size)]
            self.board[get_raw_index(amazon_to_update.y, self.size)][
                get_col_index(amazon_to_update.x, self.size)] = Constants.EMPTY_CELL_VAL
            logging.debug("<update_move()> move updated successfully!")
            return True
        else:
            logging.error("<update_move()> Tried to move to non-empty spot. update failed")
            return False

    # this is the final function called, after validations
    def shoot_blocking_rock(self, rock_target_pos):
        if self.board[get_raw_index(rock_target_pos.y, self.size)][get_col_index(rock_target_pos.x, self.size)] == \
                Constants.EMPTY_CELL_VAL:
            self.board[get_raw_index(rock_target_pos.y, self.size)][get_col_index(rock_target_pos.x, self.size)] = \
                Constants.BLOCKED_CELL_VAL
            logging.debug("<shoot_blocking_rock()>, shooting is valid")
            return True
        else:
            logging.error("<shoot_blocking_rock()> Error, you tried to shoot to non-empty cell")
            return False

    def get_players_positions(self, player_color):
        cell_state = Constants.WHITE_AMAZON_VAL if player_color == "WHITE" else Constants.BLACK_AMAZON_VAL
        return list(zip(*numpy.where(self.board == cell_state)))

    def get_blocking_rocks(self):
        return list(zip(*numpy.where(self.board == Constants.BLOCKED_CELL_VAL)))
