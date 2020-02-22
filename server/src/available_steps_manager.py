from point import Point

class AvailableStepsManger:
    def __init__(self, movement_validator=None):
        self.movement_validator = movement_validator

    def get_available_moves_to_the_north(self, current_board_game, amazona, distance=None):
        valid_path = True
        index = 1
        available_moves = []
        while (valid_path and amazona.get_y() + index <= current_board_game.get_size()):
            next_step = Point(amazona.get_x(), amazona.get_y() + index)
            valid_path = self.movement_validator.is_movement_leagal(current_board_game, amazona, next_step)
            if (valid_path):
                available_moves.append(next_step)
            if (distance is not None):
                if (distance <= index):
                    break
            index += 1
        return available_moves

    def get_available_moves_to_the_south(self, current_board_game, amazona, distance=None):
        valid_path = True
        index = 1
        available_moves = []
        while (valid_path and amazona.get_y() - index >= 0):
            next_step = Point(amazona.get_x(), amazona.get_y() - index)
            valid_path = self.movement_validator.is_movement_leagal(current_board_game, amazona, next_step)
            if (valid_path):
                available_moves.append(next_step)
            if (distance is not None):
                if (distance <= index):
                    break
            index += 1
        return available_moves

    def get_available_moves_to_the_east(self, current_board_game, amazona, distance=None):
        valid_path = True
        index = 1
        available_moves = []
        while (valid_path and (ord(amazona.get_x()) - ord('A') + index) <= current_board_game.get_size()):
            next_step = Point(chr(ord(amazona.get_x()) + index), amazona.get_y())
            valid_path = self.movement_validator.is_movement_leagal(current_board_game, amazona, next_step)
            if (valid_path):
                available_moves.append(next_step)
            if (distance is not None):
                if (distance <= index):
                    break
            index += 1
        return available_moves

    def get_available_moves_to_the_west(self, current_board_game, amazona, distance=None):
        valid_path = True
        index = 1
        available_moves = []
        while (valid_path and (ord(amazona.get_x()) - ord('A') - index) >= 0):
            next_step = Point(chr(ord(amazona.get_x()) - index), amazona.get_y())
            valid_path = self.movement_validator.is_movement_leagal(current_board_game, amazona, next_step)
            if (valid_path):
                available_moves.append(next_step)
            if (distance is not None):
                if (distance <= index):
                    break
            index += 1
        return available_moves

    def get_available_moves_to_NE(self, current_board_game, amazona, distance=None):
        valid_path = True
        index = 1
        available_moves = []
        while ((0 <= (ord(amazona.get_x()) - ord('A')) and ((ord(amazona.get_x()) - ord('A') + index) <= current_board_game.get_size())) 
            and (amazona.get_y() + index) <= current_board_game.get_size()
            and valid_path):
                next_step = Point(chr(index + ord(amazona.get_x())), amazona.get_y() + index)
                valid_path = self.movement_validator.is_movement_leagal(current_board_game, amazona, next_step)
                if (valid_path):
                    available_moves.append(next_step)
                if (distance is not None):
                    if (distance <= index):
                        break                
                index += 1
        return available_moves

    def get_available_moves_to_NW(self, current_board_game, amazona, distance=None):
        valid_path = True
        index = 1
        available_moves = []
        while (0 <= (ord(amazona.get_x()) - ord('A') - index)
            and (amazona.get_y() + index <= current_board_game.get_size())
            and valid_path):
                next_step = Point(chr(ord(amazona.get_x()) - index), amazona.get_y() + index)
                valid_path = self.movement_validator.is_movement_leagal(current_board_game, amazona, next_step)
                if (valid_path):
                    available_moves.append(next_step)
                if (distance is not None):
                    if (distance <= index):
                        break
                index += 1
        return available_moves

    def get_available_moves_to_SE(self, current_board_game, amazona, distance=None):
        valid_path = True
        index = 1
        available_moves = []
        while ((0 <= (ord(amazona.get_x()) - ord('A')) and ((ord(amazona.get_x()) - ord('A') + index) <= current_board_game.get_size())) 
            and 0 <= (amazona.get_y() - index)
            and valid_path):
                next_step = Point(chr(index + ord(amazona.get_x())), amazona.get_y() - index)
                valid_path = self.movement_validator.is_movement_leagal(current_board_game, amazona, next_step)
                if (valid_path):
                    available_moves.append(next_step)
                if (distance is not None):
                    if (distance <= index):
                        break
                index += 1
        return available_moves

    def get_available_moves_to_SW(self, current_board_game, amazona, distance=None):
        valid_path = True
        index = 1
        available_moves = []
        while (0 <= (ord(amazona.get_x()) - ord('A') - index)
            and (0 <= amazona.get_y() - index)
            and valid_path):
                next_step = Point(chr(ord(amazona.get_x()) - index), amazona.get_y() - index)
                valid_path = self.movement_validator.is_movement_leagal(current_board_game, amazona, next_step)
                if (valid_path):
                    available_moves.append(next_step)
                if (distance is not None):
                    if (distance <= index):
                        break
                index += 1
        return available_moves

    def get_available_moves_set_for_amazon(self, current_board_game, amazona, distance=None):
        uniq_moves_for_amazona = set()
        available_moves_for_amazona = self.get_available_moves_to_the_north(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_the_south(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_the_east(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_the_west(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_NE(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_NW(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_SE(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_SW(current_board_game, amazona, distance)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        
        return uniq_moves_for_amazona

    def get_number_of_available_mooves(self):
        return 0

    def get_number_of_available_mooves_for_player(self, current_board_game, player_color):
        players_position = current_board_game.get_players_positions(player_color)
        total_available_mooves = set()
        for amazona in players_position:
            total_available_mooves.update(self.get_available_moves_set_for_amazon(current_board_game, amazona))
        return len(total_available_mooves)

    def get_available_mooves_in_distance(self, current_board_game, player_color, distance):
        players_position = current_board_game.get_players_positions(player_color)
        total_moves_in_distance = set()
        for amazona in players_position:
            total_moves_in_distance.update(self.get_available_moves_set_for_amazon(current_board_game, amazona, distance))
        return total_moves_in_distance
        