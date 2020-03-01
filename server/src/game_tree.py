import time
import logging
from operator import attrgetter

from server.src.game_node import GameNode
from server.src.board_game import BoardGame
from server.src.next_state_generation_utils import generate_possible_board_states_for_amazona


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
        self.move_to_do = None
        # Generate all possible moves for me and blocking rock shots
        self.generate_my_amazons_next_possible_move_and_shot()

    def generate_my_amazons_next_possible_move_and_shot(self):
        start_time = int(round(time.time() * 1000))
        self.move_to_do = self.alpha_beta_search(self.root, self.is_black_player, 0)
        end_time = int(round(time.time() * 1000))
        total_time_milliseconds = end_time - start_time
        logging.info("<generate_my_amazons_next_possible_move_and_shot()> TOOK JUST: ", str(total_time_milliseconds))

    def get_next_move(self):
        return self.move_to_do[1].current_board

    # Private method to print random generated board to make sure it works as expected
    def __print_board(self, index):
        print('BOARD IS: of index ' + str(index))
        game_node = self.root.children[index]
        board = BoardGame(self.current_board_game.get_size(), False, game_node.get_white_amazons(),
                          game_node.get_black_amazons(), game_node.get_blocking_rocks())
        board.print_board()


    def __bla(self, current_state, is_black_player):
        available_playing_states_to_return = []
        playing_player_amazons = []

        if is_black_player:
            playing_player_amazons = current_state.get_black_amazons()
        else:
            playing_player_amazons = current_state.get_white_amazons()
        for amazona in playing_player_amazons:
            available_playing_states = generate_possible_board_states_for_amazona(self.current_board_game.get_size(),
                                                                                  current_state,
                                                                                  amazona,
                                                                                  self.available_steps_manager.get_available_moves_set_for_amazon(self.current_board_game, amazona),
                                                                                  self.blocking_rocks_manager,
                                                                                  self.available_steps_manager)
            available_playing_states_to_return.extend(available_playing_states)
        return available_playing_states_to_return

    def __get_max(self, current_state, depth, alpha, beta, is_black_player):
        if depth == self.searching_depth:
            # current_state.calculate_heuristics()
            return current_state.get_calculated_result(), current_state
        depth += 1
        best_move = (float("-inf"), self.current_board_game)

        for move in self.__bla(current_state, is_black_player):
            move.calculate_heuristics()
            # printing val

            color = "B" if is_black_player else "W"
            print("MAX_" + str(depth) + "_" + str(move.get_calculated_result()) + "_" +color)
            calculated_move = self.__get_min(move, depth, alpha, beta, not is_black_player)
            if best_move[0] < calculated_move[0]:
                best_move = calculated_move
                if beta <= best_move[0]:
                    print("Performing pruning, a b cutoff since: " + str(beta) + "<=" + str(alpha) + str(depth))
                    return calculated_move
                alpha = max(alpha, best_move[0])
        return best_move

    def __get_min(self, current_state, depth, alpha, beta, is_black_player):
        if depth == self.searching_depth:
            return current_state.get_calculated_result(), current_state
        worst_move = (float("inf"), self.current_board_game)
        depth += 1
        for move in self.__bla(current_state, is_black_player):
            color = "B" if is_black_player else "W"
            print("MIN_" + str(depth) + "_" + str(move.get_calculated_result()) + "_" +color)
            move.calculate_heuristics()
            calculated_move = self.__get_max(move, depth, alpha, beta, not is_black_player)
            if calculated_move[0] < worst_move[0]:
                worst_move = calculated_move
                if beta <= alpha:
                    print("Performing pruning, a b cutoff since: " + str(beta) + "<=" + str(alpha) + ", current depth: " + str(depth))
                    return calculated_move
                beta = min(beta, worst_move[0])

        return worst_move

    def alpha_beta_search(self, current_game_state, is_black_player, depth):
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors = self.__bla(current_game_state, is_black_player)
        best_state = None
        number_of_branches_scanned = 0
        for state in successors:
            start_time = int(round(time.time() * 1000))
            value = self.min_value(state, best_val, beta, depth + 1, not is_black_player)
            if value > best_val:
                best_val = value
                best_state = state
            number_of_branches_scanned += 1
            end_time = int(round(time.time() * 1000))
            total = end_time - start_time
            print("Time for depth search is: " + str(total) + "ms")
            print("Number of branches: " + str(number_of_branches_scanned) + " out of: " + str(len(successors)))
        return best_state

    def min_value(self, current_state, alpha, beta, depth, is_black_player):
        if depth == self.searching_depth:
            return current_state.get_calculated_result()
        infinity = float('inf')
        value = infinity

        successors = self.__bla(current_state, is_black_player)
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta, depth + 1, not is_black_player))
            if value <= alpha:
                return value
            beta = min(beta, value)

        return value

    def max_value(self, current_state, alpha, beta, depth, is_black_player):
        if depth == self.searching_depth:
            return current_state.get_calculated_result()
        infinity = float('inf')
        value = -infinity

        successors = self.__bla(current_state, is_black_player)
        for state in successors:
            value = max(value, self.min_value(state, alpha, beta, depth + 1, not is_black_player))
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def __minimax(self, current_state, depth, is_maximizing, alpha, beta, is_black_player):
        # print("!!!!!!!!!!!!!!!!!!!11Minimax runs in depth of: " + str(depth))
        if depth == self.searching_depth:
            return current_state.get_calculated_result(), current_state
        if is_maximizing:
            return self.__get_max(current_state, depth, alpha, beta, is_black_player)
        else:
            return self.__get_min(current_state, depth, alpha, beta, is_black_player)

        #
        # if is_black_player:
        #     playing_player_amazons = self.root.get_black_amazons()
        #     oponents_amazons = self.root.get_white_amazons()
        # else:
        #     playing_player_amazons = self.root.get_white_amazons()
        #     oponents_amazons = self.root.get_black_amazons()
        #
        # possible_game_states = []
        # for amazona in playing_player_amazons:
        #     for optional_state in generate_possible_board_states_for_amazona(self.current_board_game.get_size(),
        #                                                                      current_state,
        #                                                                      amazona,
        #                                                                      self.available_steps_manager.get_available_moves_set_for_amazon(
        #                                                                          self.current_board_game,
        #                                                                          amazona),
        #                                                                      self.blocking_rocks_manager,
        #                                                                      self.available_steps_manager):
        #         possible_game_states.append(optional_state)
        # best_value = (float('-inf'), current_state) if is_maximizing else (float('inf'), current_state)
        # for game_state in possible_game_states:
        #     eval_res = self.__minimax(game_state, depth + 1, not is_maximizing, alpha, beta, not is_black_player)
        #     if is_maximizing and best_value[0] < eval_res[0]:
        #         best_value = eval_res
        #         alpha = max(alpha, best_value[0])
        #         if beta <= alpha:
        #             print("Preform pruning!, cutoff")
        #             break
        #     elif not is_maximizing and best_value[0] > eval_res[0]:
        #         best_value = eval_res
        #         beta = min(beta, best_value[0])
        #         if beta <= alpha:
        #             print("Preform pruning!, cutoff")
        #             break
        # return best_value

        # if is_maximizing:
        #     best = (float("-inf"), current_state)
        #     for amazona in playing_player_amazons:
        #         for optional_state in generate_possible_board_states_for_amazona(self.current_board_game.get_size(),
        #                                                                          current_state,
        #                                                                          amazona,
        #                                                                          self.available_steps_manager.get_available_moves_set_for_amazon(
        #                                                                              self.current_board_game,
        #                                                                              amazona),
        #                                                                          self.blocking_rocks_manager,
        #                                                                          self.available_steps_manager):
        #             val = self.__minimax(optional_state, depth + 1, not is_maximizing, alpha, beta,
        #                                not is_black_player)
        #             if best[0] <= val[0]:
        #                 best = val
        #                 alpha = max(alpha, best[0])
        #                 # alpha beta pruning
        #                 if beta <= alpha:
        #                     print("Preform pruning!, cutoff")
        #                     break
        #     return best
        # else:
        #     best = float("inf"), current_state
        #     for amazona in playing_player_amazons:
        #         for optional_board in generate_possible_board_states_for_amazona(self.current_board_game.get_size(),
        #                                                                          current_state,
        #                                                                          amazona,
        #                                                                          self.available_steps_manager.get_available_moves_set_for_amazon(
        #                                                                              self.current_board_game,
        #                                                                              amazona),
        #                                                                          self.blocking_rocks_manager,
        #                                                                          self.available_steps_manager):
        #             val = self.__minimax(optional_board, depth + 1, not is_maximizing, alpha, beta,
        #                                not is_black_player)
        #             if val[0] <= best[0]:
        #                 best = val
        #                 beta = min(beta, best[0])
        #                 # alpha beta pruning
        #                 if beta <= alpha:
        #                     print("Preform pruning!, cutoff")
        #                     break
        #     return best
    def __get_best_n_moves(self, num, results):
        if num > len(results):
            num = len(results)
        return sorted(results, key=attrgetter('calculated_result'), reverse=True)[:num]

    def __get_worst_n_moves(self, num, results):
        if num > len(results):
            num = len(results)
        return sorted(results, key=attrgetter('calculated_result'), reverse=False)[:num]
