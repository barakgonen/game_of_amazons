import copy
import random
import time


# TODO: add is_game_over func
from server.src.common_funcs import get_col_index, get_raw_index
from server.src.point import Point


# This class represents a node in the game tree
class GameNode:
    def __init__(self,
                 board_game,
                 is_black_player,
                 available_steps_manager):
        self.current_board = copy.deepcopy(board_game)
        self.white_amazons = self.current_board.get_players_positions("WHITE")
        self.black_amazons = self.current_board.get_players_positions("BLACK")
        self.blocking_rocks = self.current_board.get_blocking_rocks()
        self.is_black_player = is_black_player
        self.available_steps_manager = available_steps_manager
        self.white_available_moves = self.available_steps_manager.get_available_moves_for_player(self.current_board,
                                                                                                 self.white_amazons)
        self.black_available_moves = self.available_steps_manager.get_available_moves_for_player(self.current_board,
                                                                                                 self.black_amazons)
        self.children = []
        self.calculated_result = 0
        self.winner = ""
        self.is_game_over = False
        self.calculate_heuristics()

    """ Node within the game tree
    """
    def addChildNode(self, node):
        self.children.append(node)

    def is_black_player_plays(self):
        return self.is_black_player

    def get_white_amazons(self):
        return self.white_amazons

    def get_black_amazons(self):
        return self.black_amazons

    def get_blocking_rocks(self):
        return self.blocking_rocks

    def get_calculated_result(self):
        return self.calculated_result

    def remove_score(self):
        self.calculated_result = 0

    def reset_results(self):
        self.calculated_result = 0

    def print_board(self):
        self.current_board.print_board()

    def calculate_heuristics(self):
        self.calculated_result = self.__calculate_random_heuristic() + \
                                 self.__calculate_mobility() + \
                                 self._calculate_moves_differences()

    def __calculate_random_heuristic(self):
        return random.randrange(1, 10, 1)

    def calculate_move_count_heuristic(self):
        return self._calculate_moves_differences()

    def _calculate_moves_differences(self):
        white_steps = 0
        for direction in self.white_available_moves:
            white_steps += len(direction)

        black_steps = 0
        for direction in self.black_amazons:
            black_steps += len(direction)

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

    def calculate_mobility_heuristic(self):
        return self.__calculate_mobility()

    def __calculate_mobility(self):
        black_available_moves = len(self.available_steps_manager.get_available_moves_in_distance(self.current_board,
                                                                                      self.black_amazons, 1))
        white_available_moves = len(self.available_steps_manager.get_available_moves_in_distance(self.current_board,
                                                                                      self.white_amazons, 1))
        if self.is_black_player:
            return black_available_moves + -1 * white_available_moves
        else:
            return -1 * black_available_moves + white_available_moves