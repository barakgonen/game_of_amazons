import copy
import random

# This class represents a node in the game tree
class GameNode:
    """ Node within the game tree
    """
    def __init__(self, board_size, white_amazons_pos, black_amazons_pos, blocking_lst, available_steps_manager):
        self.children = []
        self.board_size = board_size
        self.white_amazons_pos = copy.deepcopy(white_amazons_pos)
        self.black_amazons_pos = copy.deepcopy(black_amazons_pos)
        self.blocking_lst = copy.deepcopy(blocking_lst)
        self.available_steps_manager = available_steps_manager
        # self.black_moves = len(available_steps_manager.get_available_states_for_player(board_size, self.white_amazons_pos, self.black_amazons_pos, self.blocking_lst, "BLACK"))
        # self.white_moves = len(available_steps_manager.get_available_states_for_player(board_size, self.white_amazons_pos, self.black_amazons_pos, self.blocking_lst, "WHITE"))

        ### TODO: CALCULATE HEURISTICS - RANDOM HEIURISTIC, MOVE-COUNT HEIURISTIC & MOBILITY HEIURISTIC
        return
        
    def addChildNode(self, node):
        self.children.append(node)