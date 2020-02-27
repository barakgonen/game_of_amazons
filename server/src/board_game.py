from server.src.common_funcs import get_col_index, get_raw_index
from server.src.point import Point
import logging

from server.src.constants import Constants, CellState


class BoardCell:
    def __init__(self, color, state):
        self.color = color
        self.state = state

    def get_cell_color(self):
        return str(self.color)

    def get_cell_state(self):
        return str(self.state)


class BoardGame:
    def __init__(self, size, white_amazons=None, black_amazons=None, blockers_pos=None):
        self.size = size
        self.board = [[BoardCell("BW"[(i + j + size % 2 + 1) % 2], CellState.EMPTY) for i in range(size)] for j in
                      range(size)]
        if white_amazons is None and black_amazons is None and blockers_pos is None:
            logging.info("<BoardGame::BoardGame()> Placing amazons in the board. Board size is: " + str(size))
            try:
                if self.size == Constants.LARGE_BOARD_SIZE:
                    self.board[get_raw_index(7, self.size)][
                        get_col_index('A', self.size)].state = CellState.BLACK_AMAZON
                    self.board[get_raw_index(10, self.size)][
                        get_col_index('D', self.size)].state = CellState.BLACK_AMAZON
                    self.board[get_raw_index(10, self.size)][
                        get_col_index('G', self.size)].state = CellState.BLACK_AMAZON
                    self.board[get_raw_index(7, self.size)][
                        get_col_index('J', self.size)].state = CellState.BLACK_AMAZON
                    self.board[get_raw_index(4, self.size)][
                        get_col_index('A', self.size)].state = CellState.WHITE_AMAZON
                    self.board[get_raw_index(1, self.size)][
                        get_col_index('D', self.size)].state = CellState.WHITE_AMAZON
                    self.board[get_raw_index(1, self.size)][
                        get_col_index('G', self.size)].state = CellState.WHITE_AMAZON
                    self.board[get_raw_index(4, self.size)][
                        get_col_index('J', self.size)].state = CellState.WHITE_AMAZON

                elif (self.size == Constants.SMALL_BOARD_SIZE):
                    self.board[get_raw_index(4, self.size)][
                        get_col_index('A', self.size)].state = CellState.BLACK_AMAZON
                    self.board[get_raw_index(3, self.size)][
                        get_col_index('F', self.size)].state = CellState.BLACK_AMAZON
                    self.board[get_raw_index(1, self.size)][
                        get_col_index('C', self.size)].state = CellState.WHITE_AMAZON
                    self.board[get_raw_index(6, self.size)][
                        get_col_index('D', self.size)].state = CellState.WHITE_AMAZON
            except IndexError as err:
                print(err)
        else:
            logging.info("<BoardGame::BoardGame()> setting the board for us")
            for white_amazon in white_amazons:
                self.board[get_raw_index(white_amazon.y, self.size)][
                    get_col_index(white_amazon.x, self.size)].state = CellState.WHITE_AMAZON
            for black_amazon in black_amazons:
                self.board[get_raw_index(black_amazon.y, self.size)][
                    get_col_index(black_amazon.x, self.size)].state = CellState.BLACK_AMAZON
            for blocker_pos in blockers_pos:
                self.board[get_raw_index(blocker_pos.y, self.size)][
                    get_col_index(blocker_pos.x, self.size)].state = CellState.BLOCKED

    def __eq__(self, other):
        if (self.size == other.get_size()):
            for i in range(0, len(self.board)):
                for j in range(0, len(self.board[i])):
                    if self.board[i][j].state != other.board[i][j].state:
                        return False
        else:
            return False
        return True

    def print_board(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                print("| " + self.board[i][j].get_cell_color() + " ")
            print("\n")
            for j in range(0, len(self.board[i])):
                print("| " + self.board[i][j].get_cell_state() + " ")
            print("\n________________________________________________")

    def get_size(self):
        logging.debug("<get_size()> Returning size of the board. size is: " + str(self.size))
        return self.size

    def is_free_cell(self, raw, col):
        return self.board[get_raw_index(raw, self.size)][get_col_index(col, self.size)].state == CellState.EMPTY

    def is_black_amazon(self, raw, col):
        return self.board[get_raw_index(raw, self.size)][get_col_index(col, self.size)].state == CellState.BLACK_AMAZON

    def is_white_amazon(self, raw, col):
        return self.board[get_raw_index(raw, self.size)][get_col_index(col, self.size)].state == CellState.WHITE_AMAZON

    def update_move(self, amazon_to_update, new_position, amazon_color):
        # input validation
        if ((amazon_color == "BLACK" and self.is_black_amazon(amazon_to_update.y, amazon_to_update.x))
                or (amazon_color == "WHITE") and self.is_white_amazon(amazon_to_update.y, amazon_to_update.x)):
            self.board[get_raw_index(new_position.y, self.size)][get_col_index(new_position.x, self.size)].state = \
            self.board[get_raw_index(amazon_to_update.y, self.size)][get_col_index(amazon_to_update.x, self.size)].state
            self.board[get_raw_index(amazon_to_update.y, self.size)][
                get_col_index(amazon_to_update.x, self.size)].state = CellState.EMPTY
            logging.debug("<update_move()> move updated successfully!")
        else:
            logging.error("<update_move()> something went wrong dude")

    # this is the final function called, after validations
    def shoot_blocking_rock(self, rock_target_pos):
        if (self.board[get_raw_index(rock_target_pos.y, self.size)][
            get_col_index(rock_target_pos.x, self.size)].state == CellState.EMPTY):
            self.board[get_raw_index(rock_target_pos.y, self.size)][
                get_col_index(rock_target_pos.x, self.size)].state = CellState.BLOCKED
            logging.debug("<shoot_blocking_rock()>, shooting is valid")
            return True
        else:
            logging.error("<shoot_blocking_rock()> Error, you tried to shoot to non-empty cell")
            return False

    def get_players_positions(self, player_color):
        cell_state = CellState.WHITE_AMAZON if player_color == "WHITE" else CellState.BLACK_AMAZON
        players_pos = []
        # iterate as you get input A,1 or 1,A...
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                if cell_state == CellState.BLACK_AMAZON:
                    if self.is_black_amazon(i, Constants.COLUMNS_ARRAY[j]):
                        players_pos.append(Point(Constants.COLUMNS_ARRAY[j], i))
                elif cell_state == CellState.WHITE_AMAZON:
                    if self.is_white_amazon(i, Constants.COLUMNS_ARRAY[j]):
                        players_pos.append(Point(Constants.COLUMNS_ARRAY[j], i))
                else:
                    raise IndexError("BARAK YOU GOT A BUG!")
        return players_pos

    def get_blocking_rocks(self):
        blockers_pos = []
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.board[i][j].state == CellState.BLOCKED:
                    blockers_pos.append(Point(Constants.COLUMNS_ARRAY[j], i))
        return blockers_pos
