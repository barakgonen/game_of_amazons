import random

class TurnValidator:
    def is_step_valid(self, move, game_board):
        val = random.randrange(0, 100000000, 1) # this should be with the board according to amazons game rules
        if (val % 2 == 0):
            print "is_step_valid, step is valid"
            return True
        else:
            print "step_is_invalid"
            return False
    
    def validate_move(self, move, board_game):
        if (self.is_step_valid(move, board_game)):
          return True
        else:
            print "Step is invalid"
            return False
