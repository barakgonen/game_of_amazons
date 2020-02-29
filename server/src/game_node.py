import copy
import random
import time


# TODO: add is_game_over func
from server.src.common_funcs import get_col_index, get_raw_index
from server.src.point import Point


# This class represents a node in the game tree
class GameNode:
    def __init__(self,
                 current_board,
                 turn_validator,
                 available_steps_manager,
                 is_black_player):
        self.current_board = copy.deepcopy(current_board)
        self.turn_validator = turn_validator
        self.is_black_player = is_black_player
        self.available_steps_manager = available_steps_manager
        self.is_black_player = is_black_player
        self.scores_arr = []
        self.children = []
        self.winner = ""
        self.is_game_over = False
        self.calculated_result = 0
        self.calculate_heuristics()
        self.__set_calculated_results()

    """ Node within the game tree
    """
    def is_black_player_plays(self):
        return self.is_black_player

    def get_board_size(self):
        return self.current_board.get_size()

    def get_white_amazons(self):
        return self.current_board.get_players_positions("WHITE")

    def get_black_amazons(self):
        return self.current_board.get_players_positions("BLACK")

    def get_blocking_rocks(self):
        return self.current_board.get_blocking_rocks()

    def get_available_steps_for_amazona(self, amazona):
        return self.available_steps_manager.get_available_moves_set_for_amazon(self.current_board, amazona)

    def get_calculated_result(self):
        sum = 0.0
        for res in self.scores_arr:
            sum += res
        return sum

    def remove_score(self):
        self.scores_arr = []
        self.calculated_result = 0

    def set_score(self, index, val):
        self.scores_arr[index] = val

    def get_scores_arr(self):
        return self.scores_arr

    def reset_results(self):
        self.scores_arr = []

    def __set_calculated_results(self):
        for res in self.scores_arr:
            self.calculated_result += res

    def calculate_heuristics(self):
        self.scores_arr.append(self.__calculate_random_heuristic())
        self.scores_arr.append(self.__calculate_mobility())
        self.scores_arr.append(self._calculate_moves_differences())


    def addChildNode(self, node):
        self.children.append(node)

    def calculate_move_count_heuristic(self):
        return self._calculate_moves_differences()

    def _calculate_moves_differences(self):
        white_steps = self.available_steps_manager.get_number_of_available_mooves_for_player(self.current_board,
                                                                                             "WHITE")
        black_steps = self.available_steps_manager.get_number_of_available_mooves_for_player(self.current_board,
                                                                                             "BLACK")
        if self.is_black_player:
            # BLACK PLAYER PLAYS, means opponent is white
            oponent_available_steps = white_steps * -1
            num_of_available_steps_for_me = black_steps
            if oponent_available_steps == 0 and num_of_available_steps_for_me != 0:
                self.winner = "BLACK"
                self.is_game_over = True
            elif oponent_available_steps != 0 and num_of_available_steps_for_me == 0:
                self.winner = "WHITE"
                self.is_game_over = True
        else:
            # WHITE PLAYER PLAYS, means opponent is black
            oponent_available_steps = black_steps * -1
            num_of_available_steps_for_me = white_steps
            if oponent_available_steps != 0 and num_of_available_steps_for_me == 0:
                self.winner = "BLACK"
                self.is_game_over = True
            elif oponent_available_steps == 0 and num_of_available_steps_for_me != 0:
                self.winner = "WHITE"
                self.is_game_over = True
        return num_of_available_steps_for_me + oponent_available_steps

    def __calculate_random_heuristic(self):
        return random.randrange(1, 10, 1)

    def __calculate_mobility(self):
        if self.is_black_player:
            return len(self.available_steps_manager.get_available_mooves_in_distance(self.current_board, "BLACK", 1))
        else:
            return len(self.available_steps_manager.get_available_mooves_in_distance(self.current_board, "WHITE", 1))

    def calculate_mobility_heuristic(self):
        mobility_res = self.__calculate_mobility()
        return mobility_res