import logging
import copy

class GameManager:
    def __init__(self, black_player, white_player, turn_validator, board_game, blocking_manager, available_steps_manager):
        self.black_player = black_player
        self.white_player = white_player
        self.turn_validator = turn_validator
        self.board_game = copy.deepcopy(board_game)
        self.blocking_manager = blocking_manager
        self.available_steps_manager = available_steps_manager

    def run_single_turn(self, player):
        if player.kind == "Person":
            # validate this is the correct amazona
            amazon_to_move = player.get_amazon_to_move()  # must have input validation!
            is_amazon_valid = self.board_game.is_white_amazon(amazon_to_move.y, amazon_to_move.x)
            while not is_amazon_valid:
                amazon_to_move = player.get_amazon_to_move()  # must have input validation!
                is_amazon_valid = self.board_game.is_white_amazon(amazon_to_move.y, amazon_to_move.x)

            current_player_move = player.make_move()
            is_move_valid = self.turn_validator.is_step_valid(self.board_game, amazon_to_move, current_player_move)
            while not is_move_valid:
                current_player_move = player.make_move()
                is_move_valid = self.turn_validator.is_step_valid(self.board_game, amazon_to_move, current_player_move)
            self.board_game.update_move(amazon_to_move, current_player_move, player.color)
            current_player_shoot = player.shoot_blocking_rock()
            is_shooting_valid = self.turn_validator.is_shoot_valid(self.board_game, current_player_move, current_player_shoot)
            while not is_shooting_valid:
                current_player_shoot = player.shoot_blocking_rock()
                is_shooting_valid = self.turn_validator.is_shoot_valid(self.board_game, current_player_move, current_player_shoot)
            if self.board_game.shoot_blocking_rock(current_player_shoot):
                self.blocking_manager.get_rock()
                print(amazon_to_move.to_string() + current_player_move.to_string() + "/" + current_player_shoot.to_string())
            else:
                logging.error("<run_single_turn()> Error. we decieded we can shoot blocking rock, but update failed")
        elif player.kind == "AI":
            self.board_game = copy.deepcopy(player.make_move(self.board_game.current_board))
        else:
            raise RuntimeError("Un-recognized player plays")


    def is_there_reason_to_play(self, player):
        if self.blocking_manager.are_blocks_available():
            players_amazons = self.board_game.current_board.get_players_positions(player.get_color())
            moves_for_player = self.available_steps_manager.get_available_moves_for_player(self.board_game.current_board, players_amazons)
            if len(moves_for_player) > 0:
                return True
        return False

    def run_round(self):
        # if there are rocks, self.blocking_manager.get_rock() need to check it after every turn
        if self.is_there_reason_to_play(self.white_player):
            self.run_single_turn(self.white_player)
            logging.info("<run_round()> " + self.white_player.get_name() + " made successfull move!")
            if self.is_there_reason_to_play(self.black_player):
                self.run_single_turn(self.black_player)
                logging.info("<run_round()> " + self.black_player.get_name() + " made successfull move!")
                return True
        logging.warning("<run_round()> No more options available, stopping the game")
        return False

    def run_game(self):
        # first step, initialize queens on the board
        is_game_still_run = self.run_round()
        while is_game_still_run:
            self.board_game.print_board()
            is_game_still_run = self.run_round()
        logging.info("<run_game()> game is over, according to board's state, need to define the winner")
        number_of_possible_moves_for_white = self.available_steps_manager.get_available_moves_for_player(self.board_game.current_board, self.board_game.get_white_amazons())
        number_of_possible_moves_for_black = self.available_steps_manager.get_available_moves_for_player(self.board_game.current_board, self.board_game.get_black_amazons())
        if number_of_possible_moves_for_white > number_of_possible_moves_for_black:
            print("<run_game()> White has won! Congrats")
            return 2
        elif number_of_possible_moves_for_black > number_of_possible_moves_for_white:
            print("<run_game()> Black has won! Congrats")
            return 1
        else:
            print("<run_game()> There is a tie.. it means it's a bug since there ")
            return 0
