class GameManager:
    def __init__(self, p1, p2, turn_validator):
        self.player1 = p1
        self.player2 = p2
        self.turn_validator = turn_validator

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
        while (True):
            self.run_round()