from constants import CellState, SMALL_BOARD_SIZE, LARGE_BOARD_SIZE
from common_funcs import get_col_index, get_raw_index

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
        if (self.size == LARGE_BOARD_SIZE):
            self.board[get_raw_index(7, self.size)][get_col_index('A')].state = CellState.BLACK_AMAZON
            self.board[get_raw_index(10, self.size)][get_col_index('D')].state = CellState.BLACK_AMAZON
            self.board[get_raw_index(10, self.size)][get_col_index('G')].state = CellState.BLACK_AMAZON
            self.board[get_raw_index(7, self.size)][get_col_index('J')].state = CellState.BLACK_AMAZON
            self.board[get_raw_index(4, self.size)][get_col_index('A')].state = CellState.WHITE_AMAZON
            self.board[get_raw_index(1, self.size)][get_col_index('D')].state = CellState.WHITE_AMAZON
            self.board[get_raw_index(1, self.size)][get_col_index('G')].state = CellState.WHITE_AMAZON
            self.board[get_raw_index(4, self.size)][get_col_index('J')].state = CellState.WHITE_AMAZON
  
        elif(self.size == SMALL_BOARD_SIZE):
            self.board[get_raw_index(4, self.size)][get_col_index('A')].state = CellState.BLACK_AMAZON
            self.board[get_raw_index(3, self.size)][get_col_index('F')].state = CellState.BLACK_AMAZON
            self.board[get_raw_index(1, self.size)][get_col_index('C')].state = CellState.WHITE_AMAZON
            self.board[get_raw_index(6, self.size)][get_col_index('D')].state = CellState.WHITE_AMAZON
             
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

    def is_route_empty(self, current_pos, desired_pos):
        print "<BoardGame::is_route_empty()> Need to check wether all the way from current_pos to desired_pos is_empty and that the road stands the rules"

    

    def is_movement_va
