from server.src.common_funcs import get_raw_index, get_col_index
from server.src.point import Point


class AvailableStepsManger:
    def __init__(self):
        pass

    # Assuming public funcs gets amazons on matrix
    def get_available_moves_to_the_north(self, current_board_game, amazona, distance=None):
        return self.__get_available_moves_to_the_north(current_board_game,
                                                       (get_raw_index(amazona.get_y(), current_board_game.get_size()), get_col_index(amazona.get_x(), current_board_game.get_size())))

    def get_available_moves_to_the_south(self, current_board_game, amazona, distance=None):
        return self.__get_available_moves_to_the_south(current_board_game,
                                                       (get_raw_index(amazona.get_y(), current_board_game.get_size()),
                                                        get_col_index(amazona.get_x(), current_board_game.get_size())))

    def get_available_moves_to_the_east(self, current_board_game, amazona, distance=None):
        return self.__get_available_moves_to_the_east(current_board_game,
                                                      (get_raw_index(amazona.get_y(), current_board_game.get_size()),
                                                       get_col_index(amazona.get_x(), current_board_game.get_size())))

    def get_available_moves_to_the_west(self, current_board_game, amazona, distance=None):
        return self.__get_available_moves_to_the_west(current_board_game,
                                                      (get_raw_index(amazona.get_y(), current_board_game.get_size()),
                                                       get_col_index(amazona.get_x(), current_board_game.get_size())))

    def get_available_moves_to_NE(self, current_board_game, amazona, distance=None):
        return self.__get_available_moves_to_NE(current_board_game,
                                                (get_raw_index(amazona.get_y(), current_board_game.get_size()),
                                                 get_col_index(amazona.get_x(), current_board_game.get_size())))

    def get_available_moves_to_NW(self, current_board_game, amazona, distance=None):
        return self.__get_available_moves_to_NW(current_board_game,
                                                (get_raw_index(amazona.get_y(), current_board_game.get_size()),
                                                 get_col_index(amazona.get_x(), current_board_game.get_size())))

    def get_available_moves_to_SE(self, current_board_game, amazona, distance=None):
        return self.__get_available_moves_to_SE(current_board_game,
                                                (get_raw_index(amazona.get_y(), current_board_game.get_size()),
                                                 get_col_index(amazona.get_x(), current_board_game.get_size())))

    def get_available_moves_to_SW(self, current_board_game, amazona, distance=None):
        return self.__get_available_moves_to_SW(current_board_game,
                                                (get_raw_index(amazona.get_y(), current_board_game.get_size()),
                                                 get_col_index(amazona.get_x(), current_board_game.get_size())))

    # Assuming private funcs gets indexes on matrix
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

    def get_available_moves_set_for_amazon(self, current_board_game, amazona, distance=None):
        uniq_moves_for_amazona = set()
        available_moves_for_amazona = self.__get_available_moves_to_the_north(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_the_south(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_the_east(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_the_west(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_NE(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_NW(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_SE(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.__get_available_moves_to_SW(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)

        return list(uniq_moves_for_amazona)

    def get_number_of_available_moves_for_player(self, current_board_game, queens_coordinates):
        total_available_mooves = set()
        for queen_pos in queens_coordinates:
            total_available_mooves.update(self.get_available_moves_set_for_amazon(current_board_game, queen_pos))
        return len(total_available_mooves)

    # def get_available_mooves_for_player(self, current_board_game, player_color):
    #     players_position = current_board_game.get_players_positions(player_color)
    #     total_available_mooves = set()
    #     for amazona in players_position:
    #         total_available_mooves.update(self.get_available_moves_set_for_amazon(current_board_game, amazona))
    #     return len(total_available_mooves)

    # def get_available_states_for_player(self, board_size, white_amazons_pos, black_amazons_pos, blocking_lst,
    #                                     player_color):
    #     current_board_game = BoardGame(board_size, white_amazons_pos, black_amazons_pos, blocking_lst)
    #     players_position = current_board_game.get_players_positions(player_color)
    #     total_available_mooves = set()
    #     for amazona in players_position:
    #         total_available_mooves.update(self.get_available_moves_set_for_amazon(current_board_game, amazona))
    #     del current_board_game
    #     return total_available_mooves
    #

    def get_available_moves_in_distance(self, current_board_game, queens_pos, distance):
        total_moves_in_distance = set()
        for amazona in queens_pos:
            total_moves_in_distance.update(
                self.get_available_moves_set_for_amazon(current_board_game, amazona, distance))
        return total_moves_in_distance
