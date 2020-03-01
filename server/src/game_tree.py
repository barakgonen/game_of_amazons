import time
import logging

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
        self.alpha_beta_search(self.root, self.is_black_player, 0)
        end_time = int(round(time.time() * 1000))
        total_time_milliseconds = end_time - start_time
        logging.info("<generate_my_amazons_next_possible_move_and_shot()> TOOK JUST: ", str(total_time_milliseconds))

    def get_next_move(self):
        return self.move_to_do

    # Private method to print random generated board to make sure it works as expected
    def __print_board(self, index):
        print('BOARD IS: of index ' + str(index))
        game_node = self.root.children[index]
        board = BoardGame(self.current_board_game.get_size(), False, game_node.get_white_amazons(),
                          game_node.get_black_amazons(), game_node.get_blocking_rocks())
        board.print_board()

    def __get_successors(self, current_state, is_black_player):
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

    def alpha_beta_search(self, current_game_state, is_black_player, depth):
        current_player_players = []
        if is_black_player:
            current_player_players = current_game_state.get_black_amazons()
        else:
            current_player_players = current_game_state.get_white_amazons()
        infinity = float('inf')
        best_val = -infinity
        beta = infinity

        successors = self.__get_successors(current_game_state, is_black_player)
        for state in successors:
            value = self.min_value(state, best_val, beta, depth + 1, not is_black_player)
            if value > best_val:
                best_val = value
                self.move_to_do = state
        pos_at_the_end = []
        if is_black_player:
            pos_at_the_end = self.move_to_do.get_black_amazons()
        else:
            pos_at_the_end = self.move_to_do.get_white_amazons()
        moved_amazon = list(set(current_player_players) - set(pos_at_the_end))

    def min_value(self, current_state, alpha, beta, depth, is_black_player):
        if depth == self.searching_depth:
            return current_state.get_calculated_result()
        print("--------------Looking for min in depth of: " + str(depth))
        infinity = float('inf')
        value = infinity

        successors = self.__get_successors(current_state, is_black_player)
        for state in successors:
            value = min(value, self.max_value(state, alpha, beta, depth + 1, not is_black_player))
            if value <= alpha:
                print("Performed a b pruning, since: " + str(value) + "<=" + str(alpha))
                return value
            beta = min(beta, value)

        return value

    def max_value(self, current_state, alpha, beta, depth, is_black_player):
        if depth == self.searching_depth:
            return current_state.get_calculated_result()
        print("--------------Looking for max in depth of: " + str(depth))
        infinity = float('inf')
        value = -infinity

        successors = self.__get_successors(current_state, is_black_player)
        for state in successors:
            value = max(value, self.min_value(state, alpha, beta, depth + 1, not is_black_player))
            if value >= beta:
                print("Performed a b pruning, since: " + str(value) + ">=" + str(beta))
                return value
            alpha = max(alpha, value)
        return value
