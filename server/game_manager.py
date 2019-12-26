from constants import LARGE_BOARD_SIZE, SMALL_BOARD_SIZE

class GameManager:
    def __init__(self, black_player, white_player, turn_validator, board_game, blocking_manager):
        self.black_player = black_player
        self.white_player = white_player
        self.turn_validator = turn_validator
        self.board_game = board_game
        self.blocking_manager = blocking_manager

    def run_single_turn(self, player):
        # validate this is the correct amazona
        amazon_to_move = player.get_amazon_to_move() # must have input validation!
        if (player.color == "BLACK"):
            is_amazon_valid = self.board_game.is_black_amazon(amazon_to_move.y, amazon_to_move.x)
        else:
            is_amazon_valid = self.board_game.is_white_amazon(amazon_to_move.y, amazon_to_move.x)
        while (not is_amazon_valid):
            amazon_to_move = player.get_amazon_to_move() # must have input validation!
            if (player.color == "BLACK"):
                is_amazon_valid = self.board_game.is_black_amazon(amazon_to_move.y, amazon_to_move.x)
            else:
                is_amazon_valid = self.board_game.is_white_amazon(amazon_to_move.y, amazon_to_move.x)
    
        current_player_move = player.make_move()
        is_move_valid = self.turn_validator.is_step_valid(amazon_to_move, current_player_move)
        while (not is_move_valid):
            current_player_move = player.make_move()
            is_move_valid = self.turn_validator.is_step_valid(amazon_to_move, current_player_move)
        self.board_game.update_move(amazon_to_move, current_player_move, player.color)
        self.board_game.print_board()
            
    def run_round(self):
        self.run_single_turn(self.white_player)
        print (self.white_player.get_name() + " made successfull move!")
        self.run_single_turn(self.black_player)
        print (self.black_player.get_name() + " made successfull move!")

    def run_game(self):
        # first step, initialize queens on the board
        while (True):
            self.run_round()