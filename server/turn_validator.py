import random

class TurnValidator:
    def __init__(self, game_board):
        self.game_board = game_board

    def is_step_valid(self, move):
        val = random.randrange(0, 100000000, 1) # this should be with the board according to amazons game rules
        if (val % 2 == 0):
            print "is_step_valid, step is valid"
            return True
        else:
            print "step_is_invalid"
            return False
    
    def validate_move(self, move):
        if (self.is_step_valid(move)):
          return True
        else:
            print "Step is invalid"
            return False
