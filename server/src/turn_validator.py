
from common_funcs import  get_col_index, get_raw_index
from point import Point
from constant import CellState
import logging

class TurnValidator:
    def __init__(self, game_board):
        self.game_board = game_board

    def is_horizontal_valid_movement(self, orig_x, orig_y, dest_x, dest_y):
        is_valid_movement = (orig_y == dest_y) and orig_x != dest_x
        if (is_valid_movement):
            # should iterate all xs and see that cells are clear
            if (orig_x < dest_x):
                # moving to the right
                for x in range (ord(orig_x) - ord('A') + 1, ord(dest_x) - ord('A') + 1):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(orig_y, chr(x + ord('A')))
                    else:
                        break
            else:
                # moving to the left
                for x in reversed(range(ord(dest_x) - ord('A'), ord(orig_x) - ord('A'))):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(orig_y, chr(x + ord('A')))
                    else:
                        break
        return is_valid_movement
    
    def is_vertical_valid_movement(self, orig_x, orig_y, dest_x, dest_y):
        is_valid_movement = (orig_x == dest_x) and orig_y != dest_y
        if (is_valid_movement):
            # should iterate all ys and see that cells are clear
            if (orig_y > dest_y):
                # moving down
                for y in reversed(range(dest_y, orig_y)):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(y, orig_x)
                    else:
                        break
            else:
                # moving up
                for y in range (orig_y + 1, dest_y + 1):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(y, orig_x)
                    else:
                        break
        return is_valid_movement
    
    def is_diagonal_valid_movement(self, orig_x, orig_y, dest_x, dest_y):
        if (orig_x != dest_x and orig_y != dest_y):
            if (orig_x > dest_x):
                if (orig_y > dest_y):
                # orig_x > dest_x and orig_y> dest_y
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != dest_x)) 
                        and ((0 <= orig_y) and (orig_y != dest_y)) 
                        and is_route_ok):
                            orig_x = chr(ord(orig_x) - 1)
                            orig_y -= 1
                            is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
                else:
                    # orig_x > dest_x and orig_y < dest_y
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != dest_x)) 
                        and ((0 <= orig_y) and (orig_y != dest_y))
                        and is_route_ok):
                            orig_x = chr(ord(orig_x) - 1)
                            orig_y += 1
                            is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
            else:
                # orig_x < dest_x moving right
                if (orig_y > dest_y):
                    # orig_x < dest_x and orig_y > dest_y moving right and down, 135deg. SouthEast
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != ord(dest_x))) 
                            and ((0 <= orig_y) and (orig_y != dest_y))
                            and is_route_ok):
                                orig_x = chr(1 + ord(orig_x))
                                orig_y -= 1
                                is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
                else: 
                    # orig_x < dest_x and orig_y < dest_y moving up and right, 45 deg. NorthEast
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != dest_x)) 
                        and ((0 <= orig_y) and (orig_y != dest_y))
                        and is_route_ok):
                                orig_x = chr(1 + ord(orig_x))
                                orig_y += 1
                                is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
            if (orig_x == dest_x and orig_y == dest_y and is_route_ok):
                return True
        else:   
            return False
    
    def is_movement_leagal(self, current_pos, desired_pos):
        board_size = self.game_board.get_size()
        try:
            destination_x = get_col_index(desired_pos.get_x(), board_size)
            destination_y = get_raw_index(desired_pos.get_y(), board_size)

            if (destination_x < board_size and destination_y < board_size):
                if (self.is_horizontal_valid_movement(current_pos.get_x(), current_pos.get_y(), desired_pos.get_x(), desired_pos.get_y())
                    or self.is_vertical_valid_movement(current_pos.get_x(), current_pos.get_y(), desired_pos.get_x(), desired_pos.get_y()) 
                    or self.is_diagonal_valid_movement(current_pos.get_x(), current_pos.get_y(), desired_pos.get_x(), desired_pos.get_y())):
                    return True
        
        except (IndexError, KeyError) as err:
            print (err)

        return False
            
    def is_step_valid(self, current_pos, desired_pos):
        if (self.is_movement_leagal(current_pos, desired_pos)):
            print ("<TurnValidator::is_step_valid()> Player wants to move to: {" + str(desired_pos.get_x()) + ", " + str(desired_pos.get_y()) + "}")
            return True
        else:
            print "<TurnValidator::is_step_valid()> step_is_invalid"
            return False

    def is_horizontal_valid_shooting(self, orig_x, orig_y, dest_x, dest_y):
        is_valid_movement = (orig_y == dest_y) and orig_x != dest_x
        if (is_valid_movement):
            # should iterate all xs and see that cells are clear
            if (orig_x < dest_x):
                # moving to the right
                for x in range (ord(orig_x) - ord('A') + 1, ord(dest_x) - ord('A') + 1):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(orig_y, chr(x + ord('A')))
                    else:
                        break
            else:
                # moving to the left
                for x in reversed(range(ord(dest_x) - ord('A'), ord(orig_x) - ord('A'))):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(orig_y, chr(x + ord('A')))
                    else:
                        break
        return is_valid_movement
    
    def is_vertical_valid_shooting(self, orig_x, orig_y, dest_x, dest_y):
        is_valid_movement = (orig_x == dest_x) and orig_y != dest_y
        if (is_valid_movement):
            # should iterate all ys and see that cells are clear
            if (orig_y > dest_y):
                # moving down
                for y in reversed(range(dest_y, orig_y)):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(y, orig_x)
                    else:
                        break
            else:
                # moving up
                for y in range (orig_y + 1, dest_y + 1):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(y, orig_x)
                    else:
                        break
        return is_valid_movement
    
    def is_diagonal_valid_shooting(self, orig_x, orig_y, dest_x, dest_y):
        if (orig_x != dest_x and orig_y != dest_y):
            if (orig_x > dest_x):
                # moving W
                if (orig_y > dest_y):
                    # moving SW
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != dest_x)) 
                        and ((0 <= orig_y) and (orig_y != dest_y)) 
                        and is_route_ok):
                            orig_x = chr(ord(orig_x) - 1)
                            orig_y -= 1
                            is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
                else:
                    # moving NW
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != dest_x)) 
                        and ((0 <= orig_y) and (orig_y != dest_y))
                        and is_route_ok):
                            orig_x = chr(ord(orig_x) - 1)
                            orig_y += 1
                            is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
            else:
                # moving E
                if (orig_y > dest_y):
                    # moving SE
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != ord(dest_x))) 
                            and ((0 <= orig_y) and (orig_y != dest_y))
                            and is_route_ok):
                                orig_x = chr(1 + ord(orig_x))
                                orig_y -= 1
                                is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
                else: 
                    # moving NE
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != dest_x)) 
                        and ((0 <= orig_y) and (orig_y != dest_y))
                        and is_route_ok):
                                orig_x = chr(1 + ord(orig_x))
                                orig_y += 1
                                is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
            if (orig_x == dest_x and orig_y == dest_y and is_route_ok):
                return True
        else:   
            return False
    
    def is_shooting_leagal(self, amazona_pos, target_pos):
        board_size = self.game_board.get_size()
        try:
            origin_x = get_col_index(amazona_pos.get_x(), board_size)
            origin_y = get_raw_index(amazona_pos.get_y(), board_size)
            destination_x = get_col_index(target_pos.get_x(), board_size)
            destination_y = get_raw_index(target_pos.get_y(), board_size)

            if (destination_x < board_size and destination_y < board_size):
                if (self.is_horizontal_valid_shooting(amazona_pos.x, amazona_pos.y, target_pos.x, target_pos.y)
                    or self.is_vertical_valid_shooting(amazona_pos.x, amazona_pos.y, target_pos.x, target_pos.y) 
                    or self.is_diagonal_valid_shooting(amazona_pos.x, amazona_pos.y, target_pos.x, target_pos.y)):
                    return True
        
        except (IndexError, KeyError) as err:
            print (err)

        return False
    
    def is_shoot_valid(self, amazona_pos, target_pos):
        if (self.is_shooting_leagal(amazona_pos, target_pos)):
            print ("<TurnValidator::is_shoot_valid()> Player wants to shoot to: {" + str(target_pos.get_x()) + ", " + str(target_pos.get_y()) + "}")
            return True
        else:
            print "<TurnValidator::is_shoot_valid()> shoot"
            return False

    def can_move_n_up(self, amazona, i):
        return self.is_step_valid(amazona,
                                  Point(amazona.x, amazona.y + i))

    def can_move_n_down(self, amazona, i):
        return self.is_step_valid(amazona,
                                  Point(amazona.x, amazona.y - i))

    def can_move_n_right(self, amazona, i):
        return self.is_step_valid(amazona, Point(chr(ord(amazona.get_x()) + i), amazona.y))

    def can_move_n_left(self, amazona, i):
        return self.is_step_valid(amazona, Point(chr(ord(amazona.get_x()) - i), amazona.y))

    def can_move_n_horizontaly_up_right(self, amazona, i):
        return self.is_step_valid(amazona, Point(chr(ord(amazona.get_x()) + i), amazona.y + i))

    def can_move_n_horizontaly_up_left(self, amazona, i):
        return self.is_step_valid(amazona, Point(chr(ord(amazona.get_x()) - i), amazona.y + i))

    def can_move_n_horizontaly_down_right(self, amazona, i):
        return self.is_step_valid(amazona, Point(chr(ord(amazona.get_x()) + i), amazona.y - i))

    def can_move_n_horizontaly_down_left(self, amazona, i):
        return self.is_step_valid(amazona, Point(chr(ord(amazona.get_x()) - i), amazona.y - i))

    def is_amazona_has_valid_step(self, amazona):
        for i in range(1, self.game_board.get_size()):
            if (self.can_move_n_up(amazona, i) or
                self.can_move_n_down(amazona, i) or
                self.can_move_n_right(amazona, i) or
                self.can_move_n_left(amazona, i) or
                self.can_move_n_horizontaly_up_right(amazona, i) or
                self.can_move_n_horizontaly_up_left(amazona, i) or
                self.can_move_n_horizontaly_down_right(amazona, i) or
                self.can_move_n_horizontaly_down_left(amazona, i)):
                return True
        return False

    def is_there_are_available_mooves_for_player(self, player_color):
        players_position = self.game_board.get_players_positions(player_color)
        for amazona in players_position:
            if self.is_amazona_has_valid_step(amazona):
                return True
        return False