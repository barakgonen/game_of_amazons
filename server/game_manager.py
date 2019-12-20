from constants import LARGE_BOARD_SIZE, SMALL_BOARD_SIZE 

class GameManager:
    def __init__(self, p1, p2, turn_validator, board_game, blocking_manager):
        self.player1 = p1
        self.player2 = p2
        self.turn_validator = turn_validator
        self.board_game = board_game
        self.blocking_manager = blocking_manager

    def run_single_turn(self, player):
        current_player_move = player.make_move()
        is_move_valid = self.turn_validator.validate_move(current_player_move)
        while (not is_move_valid):
            current_player_move = player.make_move()
            is_move_valid = self.turn_validator.validate_move(current_player_move)
            
    def run_round(self):
        self.run_single_turn(self.player1)
        print (self.player1.get_name() + " made successfull move!")
        self.run_single_turn(self.player2)
        print (self.player2.get_name() + " made successfull move!")

    def run_game(self):
        # first step, initialize queens on the board
        board_size = self.board_game.get_size()
        print ("<GameManager::run_game()> Size of board game is:" + str(board_size))
        print ("<GameManager::run_game()> Placing amazons in the board")
        # if (board_size == LARGE_BOARD_SIZE):


        # elif(board_size == SMALL_BOARD_SIZE):

        while (True):
            self.run_round()