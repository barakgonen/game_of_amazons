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
        amazon_to_move = player.get_amazon_to_move()  # must have input validation!
        if (player.color == "BLACK"):
            is_amazon_valid = self.board_game.is_black_amazon(
                amazon_to_move.y, amazon_to_move.x)
        else:
            is_amazon_valid = self.board_game.is_white_amazon(
                amazon_to_move.y, amazon_to_move.x)
        while (not is_amazon_valid):
            amazon_to_move = player.get_amazon_to_move()  # must have input validation!
            if (player.color == "BLACK"):
                is_amazon_valid = self.board_game.is_black_amazon(
                    amazon_to_move.y, amazon_to_move.x)
            else:
                is_amazon_valid = self.board_game.is_white_amazon(
                    amazon_to_move.y, amazon_to_move.x)

        current_player_move = player.make_move()
        is_move_valid = self.turn_validator.is_step_valid(
            amazon_to_move, current_player_move)
        while (not is_move_valid):
            current_player_move = player.make_move()
            is_move_valid = self.turn_validator.is_step_valid(
                amazon_to_move, current_player_move)
        self.board_game.update_move(
            amazon_to_move, current_player_move, player.color)
        current_player_shoot = player.shoot_blocking_rock()
        is_shooting_valid = self.turn_validator.is_shoot_valid(
            current_player_move, current_player_shoot)
        while (not is_shooting_valid):
            current_player_shoot = player.shoot_blocking_rock()
            is_shooting_valid = self.turn_validator.is_shoot_valid(
                current_player_move, current_player_shoot)
        self.board_game.shoot_blocking_rock(current_player_shoot)
        self.blocking_manager.get_rock()
        self.board_game.print_board()

    def is_there_reason_to_play(self, player):
        if (self.blocking_manager.are_blocks_available() and
                self.turn_validator.is_there_are_available_mooves_for_player(player)):
            return True
        return False

    def run_round(self):
        # if there are rocks , self.blocking_manager.get_rock() need to check it after every turn shoul
        if self.is_there_reason_to_play(self.white_player):
            self.run_single_turn(self.white_player)
            print (self.white_player.get_name() + " made successfull move!")
            if self.is_there_reason_to_play(self.black_player):
                self.run_single_turn(self.black_player)
                print (self.black_player.get_name() +
                       " made successfull move!")
                return True
        print "<run_round()> no more options to play!"
        return False

    def run_game(self):
        # first step, initialize queens on the board
        is_game_still_run = self.run_round()
        while (is_game_still_run):
            is_game_still_run = self.run_round()
        print("<run_game()> game is over, according to board's state, need to define the winner")
        number_of_possible_moves_for_white = self.board_game.get_white_available_mooves()
        number_of_possible_moves_for_black = self.board_game.get_black_available_mooves()
        if (number_of_possible_moves_for_white > number_of_possible_moves_for_black):
            print ("<run_game()> White has won! Congrats")
        elif (number_of_possible_moves_for_black > number_of_possible_moves_for_white):
            print("<run_game()> Black has won! Congrats!")
        else:
            print("<run_game()> There is a tie.. it means it's a bug since there ")
