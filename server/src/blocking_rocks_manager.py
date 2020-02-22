from constants import Constants
import logging
from point import Point

class BlockingRocksManager:
    def __init__(self, board_size, movement_validator):
        if (board_size == Constants.SMALL_BOARD_SIZE):
            self.available_rocks = Constants.NUMBER_OF_ROCKS_IN_SMALL_BOARD
        elif (board_size == Constants.LARGE_BOARD_SIZE):
            self.available_rocks = Constants.NUMBER_OF_ROCKS_IN_LARGE_BOARD
        self.movement_validator = movement_validator

    def get_rock(self):
        if (self.available_rocks > 0):
            self.available_rocks -= 1
            logging.debug("<get_rock()> Returning available rock")
            return True
        else:
            logging.info("<get_rock()> There are not enough rocks... Game must over")
            return False

    def are_blocks_available(self):
        if (self.available_rocks > 0):
            logging.debug("<are_blocks_available()> blocks are available")
            return True
        else:
            logging.info("<are_blocks_available()> There are not enough rocks... Game must over")
            return False

    def get_throwing_options_to_the_north(self, amazona, current_board, distance=None):
        valid_path = True
        index = 1
        throwing_options = []
        while (valid_path and amazona.get_y() + index <= current_board.get_size()):
            next_step = Point(amazona.get_x(), amazona.get_y() + index)
            valid_path = self.movement_validator.is_movement_leagal(current_board, amazona, next_step)
            if (valid_path):
                throwing_options.append(next_step)
            if (distance is not None):
                if (distance <= index):
                    break
            index += 1
        return throwing_options

    def get_throwing_options_to_the_south(self, amazona, current_board, distance=None):
        valid_path = True
        index = 1
        throwing_options = []
        while (valid_path and amazona.get_y() - index >= 0):
            next_step = Point(amazona.get_x(), amazona.get_y() - index)
            valid_path = self.movement_validator.is_movement_leagal(current_board, amazona, next_step)
            if (valid_path):
                throwing_options.append(next_step)
            if (distance is not None):
                if (distance <= index):
                    break
            index += 1
        return throwing_options

    def get_throwing_options_to_the_east(self, amazona, current_board, distance=None):
        valid_path = True
        index = 1
        throwing_options = []
        while (valid_path and (ord(amazona.get_x()) - ord('A') + index) <= current_board.get_size()):
            next_step = Point(chr(ord(amazona.get_x()) + index), amazona.get_y())
            valid_path = self.movement_validator.is_movement_leagal(current_board, amazona, next_step)
            if (valid_path):
                throwing_options.append(next_step)
            if (distance is not None):
                if (distance <= index):
                    break
            index += 1
        return throwing_options

    def get_throwing_options_to_the_west(self, amazona, current_board, distance=None):
        valid_path = True
        index = 1
        throwing_options = []
        while (valid_path and (ord(amazona.get_x()) - ord('A') - index) >= 0):
            next_step = Point(chr(ord(amazona.get_x()) - index), amazona.get_y())
            valid_path = self.movement_validator.is_movement_leagal(current_board, amazona, next_step)
            if (valid_path):
                throwing_options.append(next_step)
            if (distance is not None):
                if (distance <= index):
                    break
            index += 1
        return throwing_options

    def get_throwing_options_to_NE(self, amazona, current_board, distance=None):
        valid_path = True
        index = 1
        throwing_options = []
        while ((0 <= (ord(amazona.get_x()) - ord('A')) and ((ord(amazona.get_x()) - ord('A') + index) <= current_board.get_size())) 
            and (amazona.get_y() + index) <= current_board.get_size()
            and valid_path):
                next_step = Point(chr(index + ord(amazona.get_x())), amazona.get_y() + index)
                valid_path = self.movement_validator.is_movement_leagal(current_board, amazona, next_step)
                if (valid_path):
                    throwing_options.append(next_step)
                if (distance is not None):
                    if (distance <= index):
                        break                
                index += 1
        return throwing_options

    def get_throwing_options_to_NW(self, amazona, current_board, distance=None):
        valid_path = True
        index = 1
        throwing_options = []
        while (0 <= (ord(amazona.get_x()) - ord('A') - index)
            and (amazona.get_y() + index <= current_board.get_size())
            and valid_path):
                next_step = Point(chr(ord(amazona.get_x()) - index), amazona.get_y() + index)
                valid_path = self.movement_validator.is_movement_leagal(current_board, amazona, next_step)
                if (valid_path):
                    throwing_options.append(next_step)
                if (distance is not None):
                    if (distance <= index):
                        break
                index += 1
        return throwing_options

    def get_throwing_options_to_SE(self, amazona, current_board, distance=None):
        valid_path = True
        index = 1
        throwing_options = []
        while ((0 <= (ord(amazona.get_x()) - ord('A')) and ((ord(amazona.get_x()) - ord('A') + index) <= current_board.get_size())) 
            and 0 <= (amazona.get_y() - index)
            and valid_path):
                next_step = Point(chr(index + ord(amazona.get_x())), amazona.get_y() - index)
                valid_path = self.movement_validator.is_movement_leagal(current_board, amazona, next_step)
                if (valid_path):
                    throwing_options.append(next_step)
                if (distance is not None):
                    if (distance <= index):
                        break
                index += 1
        return throwing_options

    def get_throwing_options_to_SW(self, amazona, current_board, distance=None):
        valid_path = True
        index = 1
        throwing_options = []
        while (0 <= (ord(amazona.get_x()) - ord('A') - index)
            and (0 <= amazona.get_y() - index)
            and valid_path):
                next_step = Point(chr(ord(amazona.get_x()) - index), amazona.get_y() - index)
                valid_path = self.movement_validator.is_movement_leagal(current_board, amazona, next_step)
                if (valid_path):
                    throwing_options.append(next_step)
                if (distance is not None):
                    if (distance <= index):
                        break
                index += 1
        return throwing_options

    # need to pass current_board since it checks the state of an optional tmp board
    def get_available_positions_to_throw_blocking_rock_for_amazona(self, current_board, throw_pos, distance):
        uniq_moves_for_amazona = set()
        throwing_options_for_amazona = self.get_throwing_options_to_the_north(throw_pos, current_board, distance)
        for move in throwing_options_for_amazona:
            uniq_moves_for_amazona.add(move)
        throwing_options_for_amazona = self.get_throwing_options_to_the_south(throw_pos, current_board, distance)
        for move in throwing_options_for_amazona:
            uniq_moves_for_amazona.add(move)
        throwing_options_for_amazona = self.get_throwing_options_to_the_east(throw_pos, current_board, distance)
        for move in throwing_options_for_amazona:
            uniq_moves_for_amazona.add(move)
        throwing_options_for_amazona = self.get_throwing_options_to_the_west(throw_pos, current_board, distance)
        for move in throwing_options_for_amazona:
            uniq_moves_for_amazona.add(move)
        throwing_options_for_amazona = self.get_throwing_options_to_NE(throw_pos, current_board, distance)
        for move in throwing_options_for_amazona:
            uniq_moves_for_amazona.add(move)
        throwing_options_for_amazona = self.get_throwing_options_to_NW(throw_pos, current_board, distance)
        for move in throwing_options_for_amazona:
            uniq_moves_for_amazona.add(move)
        throwing_options_for_amazona = self.get_throwing_options_to_SE(throw_pos, current_board, distance)
        for move in throwing_options_for_amazona:
            uniq_moves_for_amazona.add(move)
        throwing_options_for_amazona = self.get_throwing_options_to_SW(throw_pos, current_board, distance)
        for move in throwing_options_for_amazona:
            uniq_moves_for_amazona.add(move)
        
        return uniq_moves_for_amazona