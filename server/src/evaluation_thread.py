from server.src.next_state_generation_utils import generate_possible_board_states_for_amazona
from server.src.point import Point
import random

class EvaluationThread:
    """ Instance running in different thread to calculate new tree branch
    """
    def __init__(self,
                 origin_number_of_nodes_from_root,
                 current_board_game,
                 is_black_player,
                 is_maximizer,
                 max_depth,
                 blocking_rocks_manager,
                 available_steps_manager,
                 board_size):
        self.origin_number_of_nodes_from_root = origin_number_of_nodes_from_root
        self.current_game_state = current_board_game
        self.is_black_player = is_black_player
        self.is_maximizer = is_maximizer
        self.max_depth = max_depth
        self.blocking_rocks_manager = blocking_rocks_manager
        self.available_steps_manager = available_steps_manager
        self.board_size = board_size

    def run_minimax(self):
        return self.__minimax(self.current_game_state, self.is_maximizer, 0)

    def execute_evaluation(self):
        depthA = 1
        depthB = 0

        if self.origin_number_of_nodes_from_root < 50:
            depthA = 3
            depthB = 2
        elif self.origin_number_of_nodes_from_root < 500:
            depthA = 2
            depthB = 1
        # elif self.origin_number_of_nodes_from_root < 500:
        #     depthA = 2
        #     depthB = 1

        # minimaxA = self.minimax(1, 2, mobility_heuristic, True, False, depthA)
        # minimaxB = self.minimax(1, 2, move_counter_heuristic, True, False, depthB)
        minimaxA = self.run_minimax()
        minimaxB = 223
        return [minimaxA, minimaxB]

# this func should be call with the same parameters passed to GameTree::generate_next_moves because
# it generate next moves
    def __minimax(self, game_state, is_maximizer, depth):
        if depth == self.max_depth:   # OR THIS IS THE END OF THE GAME
            return game_state.calculated_result, game_state
        if is_maximizer:
            return self.__get_max(depth)
        else:
            return self.__get_min(depth)

    def __get_max(self, depth):
        beta = (float("-inf"), self.current_game_state)
        depth += 1
        for move in self.generate_my_amazons_next_possible_move_and_shot():
            calculated_move = self.__minimax(move, False, depth)
            if beta[0] <= calculated_move[0]:
                beta = calculated_move
        return beta

    def __get_min(self, depth):
        alpha = (float("inf"), self.current_game_state)
        depth += 1
        for move in self.generate_my_amazons_next_possible_move_and_shot():
            score = self.__minimax(move, True, depth)
            if score[0] <= alpha[0]:
                alpha = score
        return alpha

    def generate_my_amazons_next_possible_move_and_shot(self):
        available_playing_states_to_return = []
        playing_player_amazons = []

        if self.is_black_player:
            playing_player_amazons = self.current_game_state.get_black_amazons()
            amazons_moves_dictionary = self.current_game_state.black_available_moves
        else:
            playing_player_amazons = self.current_game_state.get_white_amazons()
            amazons_moves_dictionary = self.current_game_state.white_available_moves

        for amazona in playing_player_amazons:
            available_playing_states = generate_possible_board_states_for_amazona(self.board_size,
                                                                                  self.current_game_state,
                                                                                  amazona,
                                                                                  amazons_moves_dictionary[amazona],
                                                                                  self.blocking_rocks_manager,
                                                                                  self.available_steps_manager)
            available_playing_states_to_return.extend(available_playing_states)
        return available_playing_states_to_return


