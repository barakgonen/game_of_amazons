from server.src.next_state_generation_utils import generate_possible_states_for_amazona_from_game_node
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
                 turn_validator):
        self.origin_number_of_nodes_from_root = origin_number_of_nodes_from_root
        self.current_game_state = current_board_game
        self.is_black_player = is_black_player
        self.is_maximizer = is_maximizer
        self.max_depth = max_depth
        self.blocking_rocks_manager = blocking_rocks_manager
        self.available_steps_manager = available_steps_manager
        self.turn_validator = turn_validator

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
            return random.uniform(1.0, 15.0,), game_state
        if is_maximizer:
            return self.__get_max(depth)
        else:
            return self.__get_min(depth)

    def __get_max(self, depth):
        best_move = (float("-inf"), self.current_game_state)

        for move in self.generate_my_amazons_next_possible_move_and_shot():
            calculated_move = self.__minimax(move, False, depth)
            if best_move[0] <= calculated_move[0]:
                best_move = calculated_move
        return best_move

    def __get_min(self, depth):
        worst_move = (float("inf"), self.current_game_state)
        depth += 1
        my_counter = 0
        for move in self.generate_my_amazons_next_possible_move_and_shot():
            my_counter += 1
            score = self.__minimax(move, True, depth)
            if score[0] <= worst_move[0]:
                worst_move = score
        return worst_move

    def generate_my_amazons_next_possible_move_and_shot(self):
        available_playing_states_to_return = []
        playing_player_amazons = []

        if self.is_black_player:
            playing_player_amazons = self.current_game_state.get_black_amazons()
        else:
            playing_player_amazons = self.current_game_state.get_white_amazons()
        for amazona in playing_player_amazons:
            available_playing_states = generate_possible_states_for_amazona_from_game_node(self.current_game_state,
                                                                                           amazona,
                                                                                           self.blocking_rocks_manager,
                                                                                           self.available_steps_manager,
                                                                                           self.turn_validator)
            available_playing_states_to_return.extend(available_playing_states)
        return available_playing_states_to_return


