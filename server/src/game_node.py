import copy
import random
import time


# TODO: add is_game_over func
from server.src.common_funcs import get_col_index, get_raw_index
from server.src.point import Point


# This class represents a node in the game tree
class GameNode:
    def __init__(self,
                 board_size,
                 turn_validator,
                 white_amazons_pos,
                 black_amazons_pos,
                 blocking_lst,
                 available_steps_manager,
                 is_black_player):
        self.children = []
        self.is_black_player = is_black_player
        self.board_size = board_size
        self.turn_validator = turn_validator
        self.white_amazons_pos = copy.deepcopy(white_amazons_pos)
        self.black_amazons_pos = copy.deepcopy(black_amazons_pos)
        self.blocking_lst = copy.deepcopy(blocking_lst)
        self.available_steps_manager = available_steps_manager
        self.scores_arr = []
        self.calculated_result = 0
        self.calculate_heuristics()

    """ Node within the game tree
    """
    def remove_score(self):
        self.scores_arr = []
        self.calculated_result = 0

    def set_score(self, index, val):
        self.scores_arr[index] = val

    def get_scores_arr(self):
        return self.scores_arr

    def calculate_heuristics(self):
        random_heuristic_res = self.calculate_random_heuristic()
#        mobility_heuristic_res = self.calculate_mobility_heuristic()
#        move_count_heuristic_res = self.calculate_move_count_heuristic()
        mobility_heuristic_res = 1
        move_count_heuristic_res = 1
        self.scores_arr.append(random_heuristic_res)
        self.scores_arr.append(mobility_heuristic_res)
        self.scores_arr.append(move_count_heuristic_res)
        self.calculated_result = random_heuristic_res + mobility_heuristic_res + move_count_heuristic_res

    def addChildNode(self, node):
        self.children.append(node)

    def calculate_move_count_heuristic(self):
        return self._calculate_moves_differences()

    def calculate_random_heuristic(self):
        return random.randrange(1, 10, 1)

    def calculate_mobility_heuristic(self):
        return random.randrange(1, 10, 1)
        # I will define mobility as the ability to move on the board.
        # start_time = int(round(time.time() * 1000))
        # mobility_res = self.__calculate_mobility()
        # end_time = int(round(time.time() * 1000))
        # took = end_time - start_time
        # return mobility_res

    def _calculate_moves_differences(self):
        white_steps = self.available_steps_manager.get_available_states_for_player(self.board_size,
                                                                                   self.white_amazons_pos,
                                                                                   self.black_amazons_pos,
                                                                                   self.blocking_lst, "WHITE")
        black_available_steps = self.available_steps_manager.get_available_states_for_player(self.board_size,
                                                                                             self.white_amazons_pos,
                                                                                             self.black_amazons_pos,
                                                                                             self.blocking_lst, "BLACK")
        if self.is_black_player:
            # BLACK PLAYER PLAYS, means opponent is white
            oponent_available_steps = len(white_steps) * -1
            num_of_available_steps_for_me = len(black_available_steps)
        else:
            # WHITE PLAYER PLAYS, means opponent is black
            oponent_available_steps = len(black_available_steps) * -1
            num_of_available_steps_for_me = len(white_steps)
        return num_of_available_steps_for_me + oponent_available_steps