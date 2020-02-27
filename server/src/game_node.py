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
        self.scores_arr.append(self.calculate_mobility_heuristic())
        # self.scores_arr.append(self.calculate_move_count_heuristic())
        self.scores_arr.append(random_heuristic_res)
        self.calculated_result += random_heuristic_res

    def addChildNode(self, node):
        self.children.append(node)

    def get_number_of_moves_for_player(self, is_black):
        moves_counter = 0
        oponent_amazonas = []
        my_amazons = []

        if is_black:
            # BLACK PLAYER PLAYS, means opponent is white
            oponent_amazonas = self.white_amazons_pos
            my_amazons = self.black_amazons_pos
        else:
            # WHITE PLAYER PLAYS, means opponent is black
            oponent_amazonas = self.black_amazons_pos
            my_amazons = self.white_amazons_pos

        for amazon in my_amazons:
            for dst_x in range(0, self.board_size):
                for dst_y in range(0, self.board_size):
                    destination_amazon = Point(chr(dst_x + ord('A')), dst_y)
                    if destination_amazon not in my_amazons:
                        if destination_amazon not in oponent_amazonas:
                            if destination_amazon not in self.blocking_lst:
                                for throw_x in range(0, self.board_size):
                                    for throw_y in range(0, self.board_size):
                                        throw_target = Point(chr(throw_x + ord('A')), throw_y)
                                        if self.turn_validator.is_legal_move(destination_amazon, throw_target):
                                            moves_counter += 1
        return moves_counter

    def calculate_move_count_heuristic(self):
        return self.get_number_of_moves_for_player(self.is_black_player) \
               - self.get_number_of_moves_for_player(not self.is_black_player)

    def calculate_random_heuristic(self):
        # return random.randrange(1, 10, 1)
        return random.randrange(1, 1000, 1)

    def calculate_mobility_heuristic(self):
        start_time = int(round(time.time() * 1000))
        blu = self.calculate_opponent_mobility()
        bla = self.calculate_player_mobility()
        end_time = int(round(time.time() * 1000))
        took = end_time - start_time
        return bla + blu

    def calculate_opponent_mobility(self):
        score = 0
        oponent_amazonas = []
        my_amazons = []

        if self.is_black_player:
            # BLACK PLAYER PLAYS, means opponent is white
            oponent_amazonas = self.white_amazons_pos
            my_amazons = self.black_amazons_pos
        else:
            # WHITE PLAYER PLAYS, means opponent is black
            oponent_amazonas = self.black_amazons_pos
            my_amazons = self.white_amazons_pos

        for opponent_amazona in oponent_amazonas:
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    if "A" <= chr(dx + ord(opponent_amazona.get_x())) <= chr(ord("A") + self.board_size):
                        if 1 <= dy <= self.board_size:
                            possible_move = Point(chr(dx + ord(opponent_amazona.get_x())),
                                                            int(opponent_amazona.get_y() + dy))
                            if possible_move not in my_amazons:
                                if possible_move not in oponent_amazonas:
                                    if possible_move not in self.blocking_lst:
                                        if self.turn_validator.is_legal_move(opponent_amazona, possible_move):
                                            score -= 1
        return score

    def calculate_player_mobility(self):
        score = 0
        oponent_amazonas = []
        my_amazons = []

        if self.is_black_player:
            # BLACK PLAYER PLAYS, means opponent is white
            oponent_amazonas = self.white_amazons_pos
            my_amazons = self.black_amazons_pos
        else:
            # WHITE PLAYER PLAYS, means opponent is black
            oponent_amazonas = self.black_amazons_pos
            my_amazons = self.white_amazons_pos

        for opponent_amazona in oponent_amazonas:
            for dx in range(-2, 3):
                for dy in range(-2, 3):
                    possible_move = Point(chr(dx + ord(opponent_amazona.get_x())), int(opponent_amazona.get_y() + dy))
                    if (ord('A') <= ord(possible_move.get_x())) <= self.board_size:
                        if 1 <= possible_move.get_y() <= self.board_size:
                            if possible_move not in my_amazons:
                                if possible_move not in oponent_amazonas:
                                    if possible_move not in self.blocking_lst:
                                        if self.turn_validator.is_legal_move(opponent_amazona, possible_move):
                                            score += 1
        return score
