
from common_funcs import  get_col_index, get_raw_index

class TurnValidator:
    def __init__(self, game_board):
        self.game_board = game_board

    def is_horizontal_valid_movement(self, orig_x, orig_y, dest_x, dest_y):
        is_valid_movement = (orig_y == dest_y) and orig_x != dest_x
        if (is_valid_movement):
            # should iterate all xs and see that cells are clear
            if (orig_x > dest_x):
                # moving to the left
                for x in range (dest_x, orig_x):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(orig_y, x)
                    else:
                        break
            else:
                # moving to the right
                for x in range (orig_x + 1, dest_x + 1):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(orig_y, x)
                    else:
                        break
        return is_valid_movement
    
    def is_vertical_valid_movement(self, orig_x, orig_y, dest_x, dest_y):
        is_valid_movement = (orig_x == dest_x) and orig_y != dest_y
        if (is_valid_movement):
            # should iterate all ys and see that cells are clear
            if (orig_y > dest_y):
                # moving up
                for y in range (dest_y, orig_y):
                    if is_valid_movement:
                        is_valid_movement = self.game_board.is_free_cell(y, orig_x)
                    else:
                        break
            else:
                # moving down
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
                            orig_x -= 1
                            orig_y -= 1
                            is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
                else: 
                    # orig_x > dest_x and orig_y < dest_y
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != dest_x)) 
                        and ((0 <= orig_y) and (orig_y != dest_y))
                        and is_route_ok):
                            orig_x -= 1
                            orig_y += 1
                            is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
            else:
                # orig_x < dest_x
                if (orig_y > dest_y):
                    # orig_x < dest_x and orig_y > dest_y
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != dest_x)) 
                        and ((0 <= orig_y) and (orig_y != dest_y))
                        and is_route_ok):
                            orig_x += 1
                            orig_y -= 1
                            is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
                else: 
                    # orig_x < dest_x and orig_y < dest_y
                    is_route_ok = True
                    while (((0 <= orig_x) and (orig_x != dest_x)) 
                        and ((0 <= orig_y) and (orig_y != dest_y))
                        and is_route_ok):
                            orig_x += 1
                            orig_y += 1
                            is_route_ok = self.game_board.is_free_cell(orig_y, orig_x)
            if (orig_x == dest_x and orig_y == dest_y and is_route_ok):
                return True
        return False    
    
    def is_movement_leagal(self, current_pos, desired_pos):
        board_size = self.game_board.get_size()
        try:
            origin_x = get_col_index(current_pos.get_x(), board_size)
            origin_y = get_raw_index(current_pos.get_y(), board_size)
            destination_x = get_col_index(desired_pos.get_x(), board_size)
            destination_y = get_raw_index(desired_pos.get_y(), board_size)

            if (destination_x < board_size and destination_y < board_size):
                if (self.is_horizontal_valid_movement(origin_x, origin_y, destination_x, destination_y)
                    or self.is_vertical_valid_movement(origin_x, origin_y, destination_x, destination_y) 
                    or self.is_diagonal_valid_movement(origin_x, origin_y, destination_x, destination_y)):
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

    def is_amazon_exists(self, pos):
        try:
            origin_x = get_raw_index(pos.get_y(), self.game_board.get_size())
            origin_y = get_col_index(pos.get_x(), self.game_board.get_size())
            return self.game_board              
        except IndexError as err:
            print (err)
            return False
        