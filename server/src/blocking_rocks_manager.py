from server.src.constants import Constants
import logging
from server.src.point import Point
from server.src.board_game import BoardGame


class BlockingRocksManager:
    def __init__(self, board_size, movement_validator):
        if board_size == Constants.SMALL_BOARD_SIZE:
            self.available_rocks = Constants.NUMBER_OF_ROCKS_IN_SMALL_BOARD
        elif board_size == Constants.LARGE_BOARD_SIZE:
            self.available_rocks = Constants.NUMBER_OF_ROCKS_IN_LARGE_BOARD
        self.movement_validator = movement_validator

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

    def __get_available_moves_to_the_north(self, current_board_game, src, distance=None):
        valid_path = True
        index = 1
        available_moves = []

        if 0 <= src[1] < current_board_game.get_size() and 0 <= src[0] < current_board_game.get_size():
            dst_x = src[1]
            dst_y = src[0] - index
            while valid_path and 0 <= dst_y:
                valid_path = current_board_game.is_free_cell(dst_y, dst_x)
                if valid_path:
                    available_moves.append((dst_y, dst_x))
                else:
                    break
                if distance is not None:
                    if distance <= index:
                        break
                index += 1
                dst_y -= 1
        return available_moves

    def __get_available_moves_to_the_south(self, current_board_game, src, distance=None):
        valid_path = True
        index = 1
        available_moves = []

        if 0 <= src[1] < current_board_game.get_size() and 0 <= src[0] < current_board_game.get_size():
            dst_x = src[1]
            dst_y = src[0] + index
            while valid_path and 0 <= dst_y < current_board_game.get_size():
                valid_path = current_board_game.is_free_cell(dst_y, dst_x)
                if valid_path:
                    available_moves.append((dst_y, dst_x))
                else:
                    break
                if distance is not None:
                    if distance <= index:
                        break
                index += 1
                dst_y = src[0] + index
        return available_moves

    def __get_available_moves_to_the_east(self, current_board_game, src, distance=None):
        valid_path = True
        index = 1
        available_moves = []

        if 0 <= src[1] < current_board_game.get_size() and 0 <= src[0] < current_board_game.get_size():
            dst_x = src[1] + index
            dst_y = src[0]
            while valid_path and dst_x < current_board_game.get_size():
                valid_path = current_board_game.is_free_cell(dst_y, dst_x)
                if valid_path:
                    available_moves.append((dst_y, dst_x))
                else:
                    break
                if distance is not None:
                    if distance <= index:
                        break
                index += 1
                dst_x = src[1] + index
        return available_moves

    def __get_available_moves_to_the_west(self, current_board_game, src, distance=None):
        valid_path = True
        index = 1
        available_moves = []

        if 0 <= src[1] < current_board_game.get_size() and 0 <= src[0] < current_board_game.get_size():
            dst_x = src[1] - index
            dst_y = src[0]
            while valid_path and 0 <= dst_x:
                valid_path = current_board_game.is_free_cell(dst_y, dst_x)
                if valid_path:
                    available_moves.append((dst_y, dst_x))
                else:
                    break
                if distance is not None:
                    if distance <= index:
                        break
                index += 1
                dst_x = src[1] - index
        return available_moves

    def __get_available_moves_to_NE(self, current_board_game, src, distance=None):
        valid_path = True
        index = 1
        available_moves = []

        if 0 <= src[1] < current_board_game.get_size() and 0 <= src[0] < current_board_game.get_size():
            dst_x = src[1] + index
            dst_y = src[0] - index
            while valid_path and 0 <= dst_y:
                if 0 <= dst_x < current_board_game.get_size() and 0 <= dst_y < current_board_game.get_size():
                    valid_path = current_board_game.is_free_cell(dst_y, dst_x)
                    if valid_path:
                        available_moves.append((dst_y, dst_x))
                    else:
                        break
                    if distance is not None:
                        if distance <= index:
                            break
                    index += 1
                    dst_x = src[1] + index
                    dst_y = src[0] - index
                else:
                    break
        return available_moves

    def __get_available_moves_to_NW(self, current_board_game, src, distance=None):
        valid_path = True
        index = 1
        available_moves = []

        if 0 <= src[1] < current_board_game.get_size() and 0 <= src[0] < current_board_game.get_size():
            dst_x = src[1] - index
            dst_y = src[0] - index
            while valid_path and 0 <= dst_y:
                if 0 <= dst_x < current_board_game.get_size() and 0 <= dst_y < current_board_game.get_size():
                    valid_path = current_board_game.is_free_cell(dst_y, dst_x)
                    if valid_path:
                        available_moves.append((dst_y, dst_x))
                    else:
                        break
                    if distance is not None:
                        if distance <= index:
                            break
                    index += 1
                    dst_x = src[1] - index
                    dst_y = src[0] - index
                else:
                    break
        return available_moves

    def __get_available_moves_to_SE(self, current_board_game, src, distance=None):
        valid_path = True
        index = 1
        available_moves = []

        if 0 <= src[1] < current_board_game.get_size() and 0 <= src[0] < current_board_game.get_size():
            dst_x = src[1] + index
            dst_y = src[0] + index
            while valid_path and 0 <= dst_y:
                if 0 <= dst_x < current_board_game.get_size() and 0 <= dst_y < current_board_game.get_size():
                    valid_path = current_board_game.is_free_cell(dst_y, dst_x)
                    if valid_path:
                        available_moves.append((dst_y, dst_x))
                    else:
                        break
                    if distance is not None:
                        if distance <= index:
                            break
                    index += 1
                    dst_x = src[1] + index
                    dst_y = src[0] + index
                else:
                    break
        return available_moves

    def __get_available_moves_to_SW(self, current_board_game, src, distance=None):
        valid_path = True
        index = 1
        available_moves = []

        if 0 <= src[1] < current_board_game.get_size() and 0 <= src[0] < current_board_game.get_size():
            dst_x = src[1] - index
            dst_y = src[0] + index
            while valid_path and 0 <= dst_y:
                if 0 <= dst_x < current_board_game.get_size() and 0 <= dst_y < current_board_game.get_size():
                    valid_path = current_board_game.is_free_cell(dst_y, dst_x)
                    if valid_path:
                        available_moves.append((dst_y, dst_x))
                    else:
                        break
                    if distance is not None:
                        if distance <= index:
                            break
                    index += 1
                    dst_x = src[1] - index
                    dst_y = src[0] + index
                else:
                    break
        return available_moves

    # # need to pass current_board since it checks the state of an optional tmp board
    def get_available_positions_to_throw_blocking_rock_for_amazona(self, current_board_game, throw_pos):
        uniq_moves_for_amazona = set()
        available_moves_for_amazona = self.__get_available_moves_to_the_north(current_board_game, throw_pos)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_the_south(current_board_game, throw_pos)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_the_east(current_board_game, throw_pos)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_the_west(current_board_game, throw_pos)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_NE(current_board_game, throw_pos)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_NW(current_board_game, throw_pos)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_SE(current_board_game, throw_pos)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_SW(current_board_game, throw_pos)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)

        return uniq_moves_for_amazona

    def generate_available_throwing_options(self, board_game, throwing_from):
        return list(self.get_available_positions_to_throw_blocking_rock_for_amazona(board_game, throwing_from))
