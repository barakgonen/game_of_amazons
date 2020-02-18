from point import Point

class AvailableStepsManger:
    def __init__(self, board_game, movement_validator):
        self.board_game = board_game
        self.movement_validator = movement_validator

    def get_available_moves_to_the_north(self, amazona, depth=None):
        valid_path = True
        index = 1
        available_moves = []
        while (valid_path and amazona.get_y() + index <= self.board_game.get_size()):
            next_step = Point(amazona.get_x(), amazona.get_y() + index)
            valid_path = self.movement_validator.is_movement_leagal(amazona, next_step)
            if (valid_path):
                available_moves.append(next_step)
            if (depth is not None):
                if (depth <= index):
                    break
            index += 1
        return available_moves

    def get_available_moves_to_the_south(self, amazona, depth=None):
        valid_path = True
        index = 1
        available_moves = []
        while (valid_path and amazona.get_y() - index >= 0):
            next_step = Point(amazona.get_x(), amazona.get_y() - index)
            valid_path = self.movement_validator.is_movement_leagal(amazona, next_step)
            if (valid_path):
                available_moves.append(next_step)
            if (depth is not None):
                if (depth <= index):
                    break
            index += 1
        return available_moves

    def get_available_moves_to_the_east(self, amazona, depth=None):
        valid_path = True
        index = 1
        available_moves = []
        while (valid_path and (ord(amazona.get_x()) - ord('A') + index) <= self.board_game.get_size()):
            next_step = Point(chr(ord(amazona.get_x()) + index), amazona.get_y())
            valid_path = self.movement_validator.is_movement_leagal(amazona, next_step)
            if (valid_path):
                available_moves.append(next_step)
            if (depth is not None):
                if (depth <= index):
                    break
            index += 1
        return available_moves

    def get_available_moves_to_the_west(self, amazona, depth=None):
        valid_path = True
        index = 1
        available_moves = []
        while (valid_path and (ord(amazona.get_x()) - ord('A') - index) >= 0):
            next_step = Point(chr(ord(amazona.get_x()) - index), amazona.get_y())
            valid_path = self.movement_validator.is_movement_leagal(amazona, next_step)
            if (valid_path):
                available_moves.append(next_step)
            if (depth is not None):
                if (depth <= index):
                    break
            index += 1
        return available_moves

    def get_available_moves_to_NE(self, amazona, depth=None):
        valid_path = True
        index = 1
        available_moves = []
        while ((0 <= (ord(amazona.get_x()) - ord('A')) and ((ord(amazona.get_x()) - ord('A') + index) <= self.board_game.get_size())) 
            and (amazona.get_y() + index) <= self.board_game.get_size()
            and valid_path):
                next_step = Point(chr(index + ord(amazona.get_x())), amazona.get_y() + index)
                valid_path = self.movement_validator.is_movement_leagal(amazona, next_step)
                if (valid_path):
                    available_moves.append(next_step)
                if (depth is not None):
                    if (depth <= index):
                        break                
                index += 1
        return available_moves

    def get_available_moves_to_NW(self, amazona, depth=None):
        valid_path = True
        index = 1
        available_moves = []
        while (0 <= (ord(amazona.get_x()) - ord('A') - index)
            and (amazona.get_y() + index <= self.board_game.get_size())
            and valid_path):
                next_step = Point(chr(ord(amazona.get_x()) - index), amazona.get_y() + index)
                valid_path = self.movement_validator.is_movement_leagal(amazona, next_step)
                if (valid_path):
                    available_moves.append(next_step)
                if (depth is not None):
                    if (depth <= index):
                        break
                index += 1
        return available_moves

    def get_available_moves_to_SE(self, amazona, depth=None):
        valid_path = True
        index = 1
        available_moves = []
        while ((0 <= (ord(amazona.get_x()) - ord('A')) and ((ord(amazona.get_x()) - ord('A') + index) <= self.board_game.get_size())) 
            and 0 <= (amazona.get_y() - index)
            and valid_path):
                next_step = Point(chr(index + ord(amazona.get_x())), amazona.get_y() - index)
                valid_path = self.movement_validator.is_movement_leagal(amazona, next_step)
                if (valid_path):
                    available_moves.append(next_step)
                if (depth is not None):
                    if (depth <= index):
                        break
                index += 1
        return available_moves

    def get_available_moves_to_SW(self, amazona, depth=None):
        valid_path = True
        index = 1
        available_moves = []
        while (0 <= (ord(amazona.get_x()) - ord('A') - index)
            and (0 <= amazona.get_y() - index)
            and valid_path):
                next_step = Point(chr(ord(amazona.get_x()) - index), amazona.get_y() - index)
                valid_path = self.movement_validator.is_movement_leagal(amazona, next_step)
                if (valid_path):
                    available_moves.append(next_step)
                if (depth is not None):
                    if (depth <= index):
                        break
                index += 1
        return available_moves

    def get_available_moves_set_for_amazon(self, amazona, depth=None):
        uniq_moves_for_amazona = set()
        available_moves_for_amazona = self.get_available_moves_to_the_north(amazona, depth)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_the_south(amazona, depth)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_the_east(amazona, depth)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_the_west(amazona, depth)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_NE(amazona, depth)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_NW(amazona, depth)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_SE(amazona, depth)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        available_moves_for_amazona = self.get_available_moves_to_SW(amazona, depth)
        for move in available_moves_for_amazona:
            uniq_moves_for_amazona.add(move)
        
        return uniq_moves_for_amazona

    def get_number_of_available_mooves(self):
        return 0

    def get_number_of_available_mooves_for_player(self, player_color):
        players_position = self.board_game.get_players_positions(player_color)
        total_available_mooves = set()
        for amazona in players_position:
            total_available_mooves.update(self.get_available_moves_set_for_amazon(amazona))
        return len(total_available_mooves)

    def get_available_mooves_in_depth(self, player_color, depth):
        players_position = self.board_game.get_players_positions(player_color)
        total_moves_in_depth = set()
        for amazona in players_position:
            total_moves_in_depth.update(self.get_available_moves_set_for_amazon(amazona, depth))
        return total_moves_in_depth
        