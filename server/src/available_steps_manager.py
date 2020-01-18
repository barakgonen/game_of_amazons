from point import Point

class AvailableStepsManger:
    def __init__(self, board_game, movement_validator):
        self.board_game = board_game
        self.movement_validator = movement_validator

    def get_number_of_available_moves_to_the_north(self, amazona):
        valid_path = True
        index = 1
        number_of_available_moves = 0
        while (valid_path and amazona.get_y() + index <= self.board_game.get_size()):
            valid_path = self.movement_validator.is_movement_leagal(amazona,
                                                        Point(amazona.get_x(), amazona.get_y() + index))
            if (valid_path):
                number_of_available_moves += 1
                index += 1
        return number_of_available_moves

    def get_number_of_available_moves_to_the_south(self, amazona):
        valid_path = True
        index = 1
        number_of_available_moves = 0
        while (valid_path and amazona.get_y() - index >= 0):
            valid_path = self.movement_validator.is_movement_leagal(amazona,
                                                        Point(amazona.get_x(), amazona.get_y() - index))
            if (valid_path):
                number_of_available_moves += 1
                index += 1
        return number_of_available_moves

    def get_number_of_available_moves_to_the_east(self, amazona):
        valid_path = True
        index = 1
        number_of_available_moves = 0
        while (valid_path and (ord(amazona.get_x()) - ord('A') + index) <= self.board_game.get_size()):
            valid_path = self.movement_validator.is_movement_leagal(amazona,
                                                        Point(chr(ord(amazona.get_x()) + index), amazona.get_y()))
            if (valid_path):
                number_of_available_moves += 1
                index += 1
        return number_of_available_moves

    def get_number_of_available_moves_to_the_west(self, amazona):
        valid_path = True
        index = 1
        number_of_available_moves = 0
        while (valid_path and (ord(amazona.get_x()) - ord('A') - index) >= 0):
            valid_path = self.movement_validator.is_movement_leagal(amazona,
                                                        Point(chr(ord(amazona.get_x()) - index), amazona.get_y()))
            if (valid_path):
                number_of_available_moves += 1
                index += 1
        return number_of_available_moves

    def get_number_of_available_moves_to_NE(self, amazona):
        valid_path = True
        index = 1
        number_of_available_moves = 0
        
        while ((0 <= (ord(amazona.get_x()) - ord('A')) and ((ord(amazona.get_x()) - ord('A') + index) <= self.board_game.get_size())) 
                and (amazona.get_y() + index) <= self.board_game.get_size()
                and valid_path):
                    valid_path = self.movement_validator.is_movement_leagal(amazona,
                                            Point(chr(index + ord(amazona.get_x())), amazona.get_y() + index))
                    if (valid_path):
                        number_of_available_moves += 1
                        index += 1
        return number_of_available_moves

    def get_number_of_available_moves_to_NW(self, amazona):
        valid_path = True
        index = 1
        number_of_available_moves = 0
        
        while (0 <= (ord(amazona.get_x()) - ord('A') - index)
                and (amazona.get_y() + index <= self.board_game.get_size())
                and valid_path):
                    valid_path = self.movement_validator.is_movement_leagal(amazona,
                                            Point(chr(ord(amazona.get_x()) - index), amazona.get_y() + index))
                    if (valid_path):
                        number_of_available_moves += 1
                        index += 1
        return number_of_available_moves

    def get_number_of_available_moves_to_SE(self, amazona):
        valid_path = True
        index = 1
        number_of_available_moves = 0
        
        while ((0 <= (ord(amazona.get_x()) - ord('A')) and ((ord(amazona.get_x()) - ord('A') + index) <= self.board_game.get_size())) 
                and 0 <= (amazona.get_y() - index)
                and valid_path):
                    valid_path = self.movement_validator.is_movement_leagal(amazona,
                                            Point(chr(index + ord(amazona.get_x())), amazona.get_y() - index))
                    if (valid_path):
                        number_of_available_moves += 1
                        index += 1
        return number_of_available_moves

    def get_number_of_available_moves_to_SW(self, amazona):
        valid_path = True
        index = 1
        number_of_available_moves = 0
        
        while (0 <= (ord(amazona.get_x()) - ord('A') - index)
                and (0 <= amazona.get_y() - index)
                and valid_path):
                    valid_path = self.movement_validator.is_movement_leagal(amazona,
                                            Point(chr(ord(amazona.get_x()) - index), amazona.get_y() - index))
                    if (valid_path):
                        number_of_available_moves += 1
                        index += 1
        return number_of_available_moves

    def count_available_moves(self, amazona):
        available_moves_for_amazona = 0
        available_moves_for_amazona += self.get_number_of_available_moves_to_the_north(amazona)
        available_moves_for_amazona += self.get_number_of_available_moves_to_the_south(amazona)
        available_moves_for_amazona += self.get_number_of_available_moves_to_the_east(amazona)
        available_moves_for_amazona += self.get_number_of_available_moves_to_the_west(amazona)
        available_moves_for_amazona += self.get_number_of_available_moves_to_NE(amazona)
        available_moves_for_amazona += self.get_number_of_available_moves_to_NW(amazona)
        available_moves_for_amazona += self.get_number_of_available_moves_to_SE(amazona)
        available_moves_for_amazona += self.get_number_of_available_moves_to_SW(amazona)
        return available_moves_for_amazona

    def get_number_of_available_mooves(self):
        return 0

    def get_number_of_available_mooves_for_player(self, player_color):
        players_position = self.board_game.get_players_positions(player_color)
        total_available_mooves = 0
        for amazona in players_position:
            total_available_mooves += self.count_available_moves(amazona)
        return total_available_mooves
