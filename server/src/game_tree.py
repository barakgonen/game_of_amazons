import math
import random

import numpy
import logging

from server.src.board_game import BoardGame
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
                 current_board_game,
                 is_black_player,
                 blocking_rocks_manager,
                 searching_depth,
                 available_steps_manager,
                 turn_validator):
        self.current_board_game = current_board_game
        self.is_black_player = is_black_player
        self.blocking_rocks_manager = blocking_rocks_manager
        self.searching_depth = searching_depth
        self.available_steps_manager = available_steps_manager
        self.turn_validator = turn_validator
        self.root = GameNode(current_board_game,
                             self.is_black_player,
                             self.available_steps_manager)
                             # self.turn_validator,
                             # self.is_black_player)
        # Generate all possible moves for me and blocking rock shots
        self.move_to_do = None
        self.generate_my_amazons_next_possible_move_and_shot()

    def minimax(self, current_state, depth, is_maximizing, alpha, beta, is_black_player):
        if depth == 2:
            return current_state.get_calculated_result(), current_state
        else:
            print("Working in depth: " + str(depth))
        if is_black_player:
            playing_player_amazons = self.root.get_black_amazons()
            oponents_amazons = self.root.get_white_amazons()
        else:
            playing_player_amazons = self.root.get_white_amazons()
            oponents_amazons = self.root.get_black_amazons()
        if is_maximizing:
            best = (float("-inf"), current_state)
            for amazona in playing_player_amazons:
                print("BARAK IM MAXIMIZER, need to find best for me!")
                for optional_state in generate_possible_board_states_for_amazona(self.current_board_game.get_size(),
                                                                                  current_state,
                                                                                  amazona,
                                                                                  self.available_steps_manager.get_available_moves_set_for_amazon(self.current_board_game, amazona),
                                                                                  self.blocking_rocks_manager,
                                                                                  self.available_steps_manager):
                    val = self.minimax(optional_state, depth+1, not is_maximizing, alpha, beta, not is_black_player)
                    if best[0] <= val[0]:
                        best = val
                    alpha = max(alpha, best[0])

                    # alpha beta pruning
                    if beta <= alpha:
                        print("PRUNING BRO")
                        break
            return best
        else:
            best = float("inf"), current_state
            for amazona in playing_player_amazons:
                print("BARAK IM MAXIMIZER, need to find best for me!")
                for optional_board in generate_possible_board_states_for_amazona(self.current_board_game.get_size(),
                                                                                  current_state,
                                                                                  amazona,
                                                                                  self.available_steps_manager.get_available_moves_set_for_amazon(self.current_board_game, amazona),
                                                                                  self.blocking_rocks_manager,
                                                                                  self.available_steps_manager):
                    val = self.minimax(optional_board, depth+1, not is_maximizing, alpha, beta, not is_black_player)
                    if val[0] <= best[0]:
                        best = val
                    beta = min(beta, best[0])

                    # alpha beta pruning
                    if beta <= alpha:
                        print("PRUNING BRO")
                        break
            return best

    def generate_my_amazons_next_possible_move_and_shot(self):
        is_maximizer = True
        available_playing_states = []
        playing_player_amazons = []
        oponents_amazons = []
        origin_number_of_root_childs = 0

        start_time = int(round(time.time() * 1000))
        if self.is_black_player:
            playing_player_amazons = self.root.get_black_amazons()
            oponents_amazons = self.root.get_white_amazons()
        else:
            playing_player_amazons = self.root.get_white_amazons()
            oponents_amazons = self.root.get_black_amazons()

        self.move_to_do = self.minimax(self.root, self.searching_depth, True, float("-inf"), float("+inf"), self.is_black_player)

        # for amazona in playing_player_amazons:
        #     available_playing_states = generate_possible_board_states_for_amazona(self.current_board_game.get_size(),
        #                                                                           self.root,
        #                                                                           amazona,
        #                                                                           self.available_steps_manager.get_available_moves_set_for_amazon(self.current_board_game, amazona),
        #                                                                           self.blocking_rocks_manager,
        #                                                                           self.available_steps_manager)
        #     for state in available_playing_states:
        #         self.root.addChildNode(state)
        #         origin_number_of_root_childs += 1
        #     del available_playing_states

        # I know how to reduce calculations of avalable steps for player, doing it by saving list of tuples of available movements for amazons [(from, [to])] and each time move just one key, from, and calculate for it.. you are king
        #         We must normalize received results
        # for c in range(0, 15):
        #     self.__print_board(random.randrange(0, len(self.root.children), 1))

        # self.normalize_results(.25, 1, 1)

        # for i in range(0, 15):
        #     self.__print_board(random.randrange(0, len(self.root.children)))

        # self.root.children = self.get_best_n_moves(10)
        #
        # end_time = int(round(time.time() * 1000))
        # total_time_milliseconds = end_time - start_time
        # logging.info("<generate_my_amazons_next_possible_move_and_shot()> TOOK JUST: ", str(total_time_milliseconds))

        # counter = 0
        # Recalculating
        # results_lst = []
        #
        # for move in self.root.children:
        #     move.remove_score()
        #     # CALL MINIMAX WITH THIS STATE
        #     evaluated_state = EvaluationThread(origin_number_of_root_childs,
        #                                        move,
        #                                        not self.is_black_player,
        #                                        not is_maximizer,
        #                                        self.searching_depth,
        #                                        self.blocking_rocks_manager,
        #                                        self.available_steps_manager,
        #                                        self.current_board_game.get_size())
        #     calculated_score = evaluated_state.execute_evaluation()
        #     results_lst.append(calculated_score)
        # for i in range(0, len(self.root.children)):
        #     if ((results_lst[i])[0])[1].get_black_amazons() != self.root.children[i].get_black_amazons():
        #         logging.error("<generate_my_amazons_next_possible_move_and_shot()> Incosistant index")
        #     else:
        #         self.root.children[i].calculated_result = ((results_lst[i])[0])[0]
        # logging.info(
        #     "<generate_my_amazons_next_possible_move_and_shot()> Finished calculating oponents min moves, "
        #     "now need to return my max of min")
        end_time = int(round(time.time() * 1000))
        total_time_milliseconds = end_time - start_time
        logging.info("<generate_my_amazons_next_possible_move_and_shot()> TOOK JUST: ", str(total_time_milliseconds))

    def get_next_move(self):
        return self.move_to_do[1]

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

    # Private method to print random generated board to make sure it works as expected
    def __print_board(self, index):
        print('BOARD IS: of index ' + str(index))
        game_node = self.root.children[index]
        board = BoardGame(self.current_board_game.get_size(), False, game_node.get_white_amazons(),
                          game_node.get_black_amazons(), game_node.get_blocking_rocks())
        board.print_board()
