import random
from common_funcs import  get_col_index, get_raw_index

class TurnValidator:
    def is_movement_leagal(self, current_pos, desired_pos):
        origin_x = get_raw_index(current_pos.get_y(), self.size)
        origin_y = get_col_index(current_pos.get_x())
        destination_y = get_raw_index(desired_pos.get_y(), self.size)
        destination_x = get_col_index(desired_pos.get_x())

    def is_step_valid(self, current_pos, desired_pos, game_board):
        if (self.is_movement_leagal(current_pos, desired_pos)):
            print ("<TurnValidator::is_step_valid()> Player wants to move to: {" + str(desired_pos.get_x()) + ", " + str(desired_pos.get_y()) + "}")
            if (game_board.is_route_empty(current_pos, desired_pos)):
                print "<TurnValidator::is_step_valid()> is_step_valid, step is valid"
                return True
        else:
            print "<TurnValidator::is_step_valid()> step_is_invalid"
            return False
        