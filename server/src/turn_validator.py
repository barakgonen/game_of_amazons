import logging
from server.src.common_funcs import get_col_index, get_raw_index


class TurnValidator:
    def is_horizontal_movement_valid(self, game_board, orig_x, orig_y, dest_x, dest_y):
        is_valid_movement = (orig_y == dest_y) and orig_x != dest_x
        if is_valid_movement:
            # should iterate all xs and see that cells are clear
            if orig_x < dest_x:
                # moving to the EAST
                for x in range(orig_x + 1, dest_x + 1):
                    if is_valid_movement:
                        is_valid_movement = game_board.is_free_cell(orig_y, x)
                    else:
                        break
            else:
                # moving to the WEST
                for x in reversed(range(dest_x, orig_x)):
                    if is_valid_movement:
                        is_valid_movement = game_board.is_free_cell(orig_y, x)
                    else:
                        break
        return is_valid_movement

    def is_vertical_movement_valid(self, game_board, orig_x, orig_y, dest_x, dest_y):
        is_valid_movement = (orig_x == dest_x) and orig_y != dest_y
        if is_valid_movement:
            # should iterate all ys and see that cells are clear
            if orig_y < dest_y:
                # moving SOUTH
                for y in range(orig_y + 1, dest_y + 1):
                    if is_valid_movement:
                        is_valid_movement = game_board.is_free_cell(y, orig_x)
                    else:
                        break
            else:
                # moving NORTH
                for y in reversed(range(dest_y, orig_y)):
                    if is_valid_movement:
                        is_valid_movement = game_board.is_free_cell(y, orig_x)
                    else:
                        break
        return is_valid_movement

    def is_diagonal_movement_valid(self, game_board, orig_x, orig_y, dest_x, dest_y):
        if orig_x != dest_x and orig_y != dest_y:
            if orig_x < dest_x:
                # moving E
                if dest_y < orig_y:
                    # moving NE
                    is_route_ok = True
                    while 0 <= orig_x < dest_x and 0 <= dest_y < orig_y and is_route_ok:
                        orig_x += 1
                        orig_y -= 1
                        is_route_ok = game_board.is_free_cell(orig_y, orig_x)
                else:
                    # moving SE
                    is_route_ok = True
                    while 0 <= orig_x < dest_x and 0 <= orig_y < dest_y and is_route_ok:
                        orig_x += 1
                        orig_y += 1
                        is_route_ok = game_board.is_free_cell(orig_y, orig_x)
            else:
                # moving W
                if orig_y < dest_y:
                    # moving Sw
                    is_route_ok = True
                    while 0 <= dest_x < orig_x and 0 <= orig_y < dest_y and is_route_ok:
                        orig_x -= 1
                        orig_y += 1
                        is_route_ok = game_board.is_free_cell(orig_y, orig_x)
                else:
                    # moving NW
                    is_route_ok = True
                    while 0 <= dest_x < orig_x and 0 <= dest_y < orig_y and is_route_ok:
                        orig_x -= 1
                        orig_y -= 1
                        is_route_ok = game_board.is_free_cell(orig_y, orig_x)
            if orig_x == dest_x and orig_y == dest_y and is_route_ok:
                return True
        else:
            return False

    def __is_path_valid(self, game_board, src_x, src_y, dst_x, dst_y):
        # Now we are sure src and dst are valid potential points
        logging.debug("<TurnValidator::is_path_valid()> Player wants to move to: {" + str(dst_x) + ", " + str(dst_y)
                      + "}")
        if (self.is_horizontal_movement_valid(game_board, src_x, src_y, dst_x, dst_y)
            or self.is_vertical_movement_valid(game_board, src_x, src_y, dst_x, dst_y)
            or self.is_diagonal_movement_valid(game_board, src_x, src_y, dst_x, dst_y)):
            return True
        return False

    def is_step_valid(self, game_board, src, dst):
        # first stage, is to verify weather current_pos exists, and desired pos exists
        try:
            board_size = game_board.get_size()
            src_x = get_col_index(src.get_x(), board_size)
            src_y = get_raw_index(src.get_y(), board_size)
            if 0 <= src_x < board_size and 0 <= src_y < board_size:
                dst_x = get_col_index(dst.get_x(), board_size)
                dst_y = get_raw_index(dst.get_y(), board_size)
                if 0 <= dst_x <= board_size and 0 <= dst_y <= board_size:
                    if self.__is_path_valid(game_board, src_x, src_y, dst_x, dst_y):
                        return True
        except IndexError as e:
            logging.error("<TurnValidator::is_step_valid() Caught exception: " + str(e))
        logging.error("<TurnValidator::is_step_valid()> step_is_invalid")
        return False

    def is_shoot_valid(self, game_board, src, dst):
        # first stage, is to verify weather current_pos exists, and desired pos exists
        try:
            board_size = game_board.get_size()
            src_x = get_col_index(src.get_x(), board_size)
            src_y = get_raw_index(src.get_y(), board_size)
            if 0 <= src_x < board_size and 0 <= src_y < board_size:
                dst_x = get_col_index(dst.get_x(), board_size)
                dst_y = get_raw_index(dst.get_y(), board_size)
                if 0 <= dst_x <= board_size and 0 <= dst_y <= board_size:
                    if self.__is_path_valid(game_board, src_x, src_y, dst_x, dst_y):
                        return True
        except IndexError as e:
            logging.error("<TurnValidator::is_shoot_valid() Caught exception: " + str(e))
        logging.error("<TurnValidator::is_shoot_valid()> step_is_invalid")
        return False

    def is_valid_horizontal_movement(self, src, dst):
        return (src.get_y() == dst.get_y()) and (src.get_x() != dst.get_x())

    def is_valid_vertical_movement(self, src, dst):
        return (src.get_y() != dst.get_y()) and (src.get_x() == dst.get_x())

    def is_valid_diagonal_movement(self, src, dst):
        orig_x = src.get_x()
        orig_y = src.get_y()
        dest_x = dst.get_x()
        dest_y = dst.get_y()
        if orig_x != dest_x and orig_y != dest_y:
            if orig_x > dest_x:
                # moving W
                if orig_y > dest_y:
                    # moving SW
                    is_route_ok = True
                    while (((ord('A') <= ord(orig_x)) and (orig_x != dest_x))
                           and ((0 <= orig_y) and (orig_y != dest_y))):
                        orig_x = chr(ord(orig_x) - 1)
                        orig_y -= 1
                else:
                    # moving NW
                    while (((ord('A') <= ord(orig_x)) and (orig_x != dest_x))
                           and ((0 <= orig_y) and (orig_y != dest_y))):
                        orig_x = chr(ord(orig_x) - 1)
                        orig_y += 1
            else:
                # moving E
                if orig_y > dest_y:
                    # moving SE
                    while (((ord('A') <= ord(orig_x)) and (orig_x != ord(dest_x)))
                           and ((0 <= orig_y) and (orig_y != dest_y))):
                        orig_x = chr(1 + ord(orig_x))
                        orig_y -= 1
                else:
                    # moving NE
                    while (((ord('A') <= ord(orig_x)) and (orig_x != dest_x))
                           and ((0 <= orig_y) and (orig_y != dest_y))):
                        orig_x = chr(1 + ord(orig_x))
                        orig_y += 1
            if orig_x == dest_x and orig_y == dest_y:
                return True
        else:
            return False

    def is_legal_move(self, opponent_amazona, possible_move):
        # if we got here, it means possible_move does not intersects with another quenns or blocking rocks,
        # thus we just have to validate if the movement is ok
        try:
            if (self.is_valid_horizontal_movement(opponent_amazona, possible_move)
                    or self.is_valid_vertical_movement(opponent_amazona, possible_move)
                    or self.is_valid_diagonal_movement(opponent_amazona, possible_move)):
                return True
        except (IndexError, KeyError) as err:
            print(err)

        return False
