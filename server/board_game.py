from constants import CellState, SMALL_BOARD_SIZE, LARGE_BOARD_SIZE, COLUMNS_ARRAY
from common_funcs import get_col_index, get_raw_index
from point import Point

class BoardCell:
    def __init__(self, color, state):
        self.color = color
        self.state = state

    def get_cell_color(self):
        return str(self.color)

    def get_cell_state(self):
        return str(self.state)

class BoardGame:
    def __init__(self, size):
        self.size = size
        self.board = [[BoardCell("BW"[(i+j+size%2+1) % 2], CellState.EMPTY) for i in range(size)] for j in range(size)]
        print ("<BoardGame::BoardGame()> Placing amazons in the board")
        try:
            if (self.size == LARGE_BOARD_SIZE):
                self.board[get_raw_index(7, self.size)][get_col_index('A', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(10, self.size)][get_col_index('D', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(10, self.size)][get_col_index('G', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(7, self.size)][get_col_index('J', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(4, self.size)][get_col_index('A', self.size)].state = CellState.WHITE_AMAZON
                self.board[get_raw_index(1, self.size)][get_col_index('D', self.size)].state = CellState.WHITE_AMAZON
                self.board[get_raw_index(1, self.size)][get_col_index('G', self.size)].state = CellState.WHITE_AMAZON
                self.board[get_raw_index(4, self.size)][get_col_index('J', self.size)].state = CellState.WHITE_AMAZON
  
            elif(self.size == SMALL_BOARD_SIZE):
                self.board[get_raw_index(4, self.size)][get_col_index('A', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(3, self.size)][get_col_index('F', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(1, self.size)][get_col_index('C', self.size)].state = CellState.WHITE_AMAZON
                self.board[get_raw_index(6, self.size)][get_col_index('D', self.size)].state = CellState.WHITE_AMAZON
        except IndexError as err:
            print (err)
        
    def print_board(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                print "| " + self.board[i][j].get_cell_color() + " ",
            print "\n"
            for j in range(0, len(self.board[i])):
                print "| " + self.board[i][j].get_cell_state() + " ",
            print "\n________________________________________________"
    
    def get_size(self):
        print ("<BoardGame::get_size()> Returning size of the board. size is: " + str(self.size))
        return self.size

    def is_free_cell(self, raw, col):
        return self.board[get_raw_index(raw, self.size)][get_col_index(col, self.size)].state == CellState.EMPTY
    
    def is_black_amazon(self, raw, col):
        return self.board[get_raw_index(raw, self.size)][get_col_index(col, self.size)].state == CellState.BLACK_AMAZON
    
    def is_white_amazon(self, raw, col):
        return self.board[get_raw_index(raw, self.size)][get_col_index(col, self.size)].state == CellState.WHITE_AMAZON
    
    def update_move(self, amazon_to_update, new_position, amazon_color):
        # input validation
        if ((amazon_color == "BLACK" and self.is_black_amazon(amazon_to_update.y, amazon_to_update.x))
            or (amazon_color == "WHITE") and self.is_white_amazon(amazon_to_update.y, amazon_to_update.x)):
            self.board[get_raw_index(new_position.y, self.size)][get_col_index(new_position.x, self.size)].state = self.board[get_raw_index(amazon_to_update.y, self.size)][get_col_index(amazon_to_update.x, self.size)].state
            self.board[get_raw_index(amazon_to_update.y, self.size)][get_col_index(amazon_to_update.x, self.size)].state = CellState.EMPTY
            print "<update_move()> move updated successfully!"
        else:
            print "<update_move()> something went wrong dude"
        
    # this is the final function called, after validations
    def shoot_blocking_rock(self, rock_target_pos):
        if (self.board[get_raw_index(rock_target_pos.y, self.size)][get_col_index(rock_target_pos.x, self.size)].state == CellState.EMPTY):
            self.board[get_raw_index(rock_target_pos.y, self.size)][get_col_index(rock_target_pos.x, self.size)].state = CellState.BLOCKED
        else:
            raise IndexError("Trying to shoot to non-empty cell")
    
    def get_players_positions(self, cell_state):
        players_pos = []
        # iterate as you get input A,1 or 1,A...
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                if cell_state == CellState.BLACK_AMAZON:
                    if self.is_black_amazon(i, COLUMNS_ARRAY[j]):
                        players_pos.append(Point(COLUMNS_ARRAY[j], i))
                elif cell_state == CellState.WHITE_AMAZON:    
                    if self.is_white_amazon(i, COLUMNS_ARRAY[j]):
                        players_pos.append(Point(COLUMNS_ARRAY[j], i))
                else:
                    raise IndexError("BARAK YOU GOT A BUG!")
        return players_pos

    def get_number_of_available_mooves(self, player_color):
        players_position = self.get_players_positions(player_color)
        # for amazona in players_position:
        #     if self.is_amazona_has_valid_step(amazona):
        #         return True
        return 4

    def get_black_available_mooves(self):
        return self.get_number_of_available_mooves(CellState.BLACK_AMAZON)

    def get_white_available_mooves(self):
        return self.get_number_of_available_mooves(CellState.WHITE_AMAZON)