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
        self.move_to_do = self.__minimax(self.root, 0, True, float("-inf"), float("+inf"), self.is_black_player)
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

    def __minimax(self, current_state, depth, is_maximizing, alpha, beta, is_black_player):
        if depth == self.searching_depth:
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
                for optional_state in generate_possible_board_states_for_amazona(self.current_board_game.get_size(),
                                                                                 current_state,
                                                                                 amazona,
                                                                                 self.available_steps_manager.get_available_moves_set_for_amazon(
                                                                                     self.current_board_game,
                                                                                     amazona),
                                                                                 self.blocking_rocks_manager,
                                                                                 self.available_steps_manager):
                    val = self.__minimax(optional_state, depth + 1, not is_maximizing, alpha, beta,
                                       not is_black_player)
                    if best[0] <= val[0]:
                        best = val
                    alpha = max(alpha, best[0])

                    # alpha beta pruning
                    if beta <= alpha:
                        print("Preform pruning!, cutoff")
                        break
            return best
        else:
            best = float("inf"), current_state
            for amazona in playing_player_amazons:
                for optional_board in generate_possible_board_states_for_amazona(self.current_board_game.get_size(),
                                                                                 current_state,
                                                                                 amazona,
                                                                                 self.available_steps_manager.get_available_moves_set_for_amazon(
                                                                                     self.current_board_game,
                                                                                     amazona),
                                                                                 self.blocking_rocks_manager,
                                                                                 self.available_steps_manager):
                    val = self.__minimax(optional_board, depth + 1, not is_maximizing, alpha, beta,
                                       not is_black_player)
                    if val[0] <= best[0]:
                        best = val
                    beta = min(beta, best[0])

                    # alpha beta pruning
                    if beta <= alpha:
                        print("Preform pruning!, cutoff")
                        break
            return best
