import copy
from game_node import GameNode
from point import Point
from datetime import datetime
from board_game import BoardGame

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
                 available_steps_manager):
        self.white_amazons_position = white_amazons_position
        self.black_amazons_position = black_amazons_position
        self.blocking_rocks_position = blocking_rocks_position
        self.board_size = board_size
        self.playing_player_color = player_color
        self.searching_distance = searching_distance
        self.blocking_rocks_manager = blocking_rocks_manager
        self.searching_depth = searching_depth
        self.available_steps_manager = available_steps_manager
        self.root = GameNode(self.board_size, white_amazons_position, black_amazons_position, self.blocking_rocks_position, self.available_steps_manager)
        # Generate all possible moves for me and blocking rock shots
        self.generate_my_amazons_next_possible_move_and_shot(self.playing_player_color)
        print "BARAL"
    
    def generate_possible_board_states_for_amazona(self, amazona, searching_depth, player_color, current_white_amazons, current_black_amazons, current_blocking_rocks_pos):
        available_states_for_amazona = []
        available_steps_for_amazona = self.available_steps_manager.get_available_moves_for_amazona(self.board_size, current_white_amazons, current_black_amazons, current_blocking_rocks_pos, player_color, amazona)
        for available_move in available_steps_for_amazona:
            players_current_pos = []
            available_throwing_rocks_options = []
            if player_color == "BLACK":
                players_current_pos = copy.deepcopy(current_black_amazons)
                players_current_pos.remove(amazona)
                players_current_pos.append(available_move)
                available_throwing_rocks_options = self.blocking_rocks_manager.generate_available_throwing_options(self.board_size, current_white_amazons, players_current_pos, current_blocking_rocks_pos, available_move, self.searching_distance)
            elif player_color == "WHITE":
                players_current_pos = copy.deepcopy(current_white_amazons)
                players_current_pos.remove(amazona)
                players_current_pos.append(available_move)
                available_throwing_rocks_options = self.blocking_rocks_manager.generate_available_throwing_options(self.board_size, players_current_pos, current_black_amazons, current_blocking_rocks_pos, available_move, self.searching_distance)
            else:
                raise ValueError("Invalid player color")
            for available_throwing_option in available_throwing_rocks_options:
                throwing_option = copy.deepcopy(current_blocking_rocks_pos)
                throwing_option.append(available_throwing_option)
                if player_color == "BLACK":
                    turn_game_node = GameNode(self.board_size, current_white_amazons, players_current_pos, throwing_option, self.available_steps_manager)    
                elif player_color == "WHITE":
                    turn_game_node = GameNode(self.board_size, players_current_pos, current_black_amazons, throwing_option, self.available_steps_manager)
                for depth in range(1, searching_depth):
                    if depth % 2 != 0:
                        for oponent_amazona in current_white_amazons:
                            available_states_for_oponent_amazona_amazona = self.generate_possible_board_states_for_amazona(oponent_amazona, searching_depth - 1, "WHITE", current_white_amazons, players_current_pos, throwing_option)
                            for available_state in available_states_for_oponent_amazona_amazona:
                                turn_game_node.addChildNode(available_state)
                available_states_for_amazona.append(turn_game_node)
                del throwing_option
            del players_current_pos
        return available_states_for_amazona

    def generate_my_amazons_next_possible_move_and_shot(self, color):
        start_time = datetime.now()
        if color == "WHITE":
            for amazona in self.white_amazons_position:
                available_stetes_for_amazona = self.generate_possible_board_states_for_amazona(amazona, self.searching_depth, color, self.white_amazons_position, self.black_amazons_position, self.blocking_rocks_position)
                for state in available_stetes_for_amazona:
                    self.root.addChildNode(state)
                del available_stetes_for_amazona
        elif color == "BLACK":
            for amazona in self.black_amazons_position:
                available_stetes_for_amazona = self.generate_possible_board_states_for_amazona(amazona, self.searching_depth, color, self.white_amazons_position, self.black_amazons_position, self.blocking_rocks_position)
                for state in available_stetes_for_amazona:
                    self.root.addChildNode(state)
                del available_stetes_for_amazona
        end_time = datetime.now()   
        total_time = end_time - start_time
        print("TOOK JUST: ", str(total_time.seconds) + "." + str(total_time.microseconds) + " seconds" + " number of nodes in depth 1 is: " + str(len(self.root.children)))

    def get_next_move(self):
        return Point("x", 2)