import copy
import math
import numpy
import logging

from server.src.evaluation_thread import EvaluationThread
from server.src.game_node import GameNode
from server.src.next_state_generation_utils import generate_possible_board_states_for_amazona
from server.src.point import Point
from datetime import datetime
from operator import attrgetter
import time


class GameTree:
    """ The Game tree from current position
    """

    def __init__(self,
                 white_amazons_position,
                 black_amazons_position,
                 blocking_rocks_position,
                 board_size,
                 player_color,
                 searching_distance,
                 blocking_rocks_manager,
                 searching_depth,
                 available_steps_manager,
                 turn_validator):
        self.white_amazons_position = white_amazons_position
        self.black_amazons_position = black_amazons_position
        self.blocking_rocks_position = blocking_rocks_position
        self.board_size = board_size
        self.playing_player_color = player_color
        self.searching_distance = searching_distance
        self.blocking_rocks_manager = blocking_rocks_manager
        self.searching_depth = searching_depth
        self.available_steps_manager = available_steps_manager
        self.turn_validator = turn_validator
        self.root = GameNode(self.board_size,
                             self.turn_validator,
                             self.white_amazons_position,
                             self.black_amazons_position,
                             self.blocking_rocks_position,
                             self.available_steps_manager,
                             self.playing_player_color == "BLACK")
        # Generate all possible moves for me and blocking rock shots
        self.generate_my_amazons_next_possible_move_and_shot()

    def generate_my_amazons_next_possible_move_and_shot(self):
        is_maximizer = True
        available_playing_states = []
        playing_player_amazons = []
        oponents_amazons = []

        start_time = int(round(time.time() * 1000))
        if self.playing_player_color == "WHITE":
            playing_player_amazons = self.white_amazons_position
            oponents_amazons = self.black_amazons_position
        else:
            playing_player_amazons = self.black_amazons_position
            oponents_amazons = self.white_amazons_position

        for amazona in playing_player_amazons:
            available_playing_states = generate_possible_board_states_for_amazona(self.board_size,
                                                                                  amazona,
                                                                                  self.playing_player_color,
                                                                                  self.white_amazons_position,
                                                                                  self.black_amazons_position,
                                                                                  self.blocking_rocks_position,
                                                                                  self.available_steps_manager,
                                                                                  self.blocking_rocks_manager,
                                                                                  self.turn_validator)
            for state in available_playing_states:
                self.root.addChildNode(state)
            del available_playing_states

        origin_number_of_root_childs = len(self.root.children)

        # We must normalize received results
        self.normalize_results(.25, 1, 1)
        self.root.children = self.get_best_n_moves(10)

        end_time = int(round(time.time() * 1000))
        total_time_milliseconds = end_time - start_time
        logging.info("<generate_my_amazons_next_possible_move_and_shot()> TOOK JUST: ", str(total_time_milliseconds))

        # counter = 0
        is_maximizer = not is_maximizer
        # Recalculating
        results_lst = []
        for move in self.root.children:
            move.remove_score()
            if self.playing_player_color == "WHITE":
                # CALL MINIMAX WITH THIS STATE
                evaluated_state = EvaluationThread(origin_number_of_root_childs,
                                                   move,
                                                   True,
                                                   is_maximizer,
                                                   self.searching_depth,
                                                   "BLACK",
                                                   self.blocking_rocks_manager)
                calculated_score = evaluated_state.execute_evaluation()
                results_lst.append(calculated_score)
            elif self.playing_player_color == "BLACK":
                # CALL MINIMAX WITH THIS STATE
                evaluated_state = EvaluationThread(origin_number_of_root_childs,
                                                   move,
                                                   False,
                                                   is_maximizer,
                                                   self.searching_depth,
                                                   "WHITE",
                                                   self.blocking_rocks_manager)
                calculated_score = evaluated_state.execute_evaluation()
                results_lst.append(calculated_score)

        for i in range(0, len(self.root.children)):
            if ((results_lst[i])[0])[1].black_amazons_pos != self.root.children[i].black_amazons_pos:
                logging.error("<generate_my_amazons_next_possible_move_and_shot()> Incosistant index")
            else:
                self.root.children[i].calculated_result = ((results_lst[i])[0])[0]
        logging.info("<generate_my_amazons_next_possible_move_and_shot()> "
                     "Finished calculating oponents min moves, now need to return my max of min")

        end_time = int(round(time.time() * 1000))
        total_time_milliseconds = end_time - start_time
        logging.info("<generate_my_amazons_next_possible_move_and_shot()> TOOK JUST: ", str(total_time_milliseconds))

    def get_next_move(self):
        return self.get_best_n_moves(1)[0]

    def normalize_results(self, *weights):
        if len(self.root.children) < 1:
            pass
        for i in range(0, len(
                self.root.children[0].get_scores_arr())):  # should be number of heiuristics, length of hiuristics list
            self.normalize_result(i, weights[i])  # hope it works

    def normalize_result(self, i, weight):
        max_result = 0
        for move in self.root.children:
            _score = math.fabs(move.get_scores_arr()[i])
            max_result = max(_score, max_result)
        for move in self.root.children:
            normalized_score = int(
                ((math.fabs(move.get_scores_arr()[i] / max_result)) *  # get ratio of score to max score
                 (100 * weight) *  # scale score
                 numpy.sign(move.get_scores_arr()[i]))  # put correct sign
            )
            move.set_score(i, normalized_score)

    def get_best_n_moves(self, num):
        if num > len(self.root.children):
            num = len(self.root.children)
        return sorted(self.root.children, key=attrgetter('calculated_result'), reverse=True)[:num]
