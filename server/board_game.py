from constants import CellState

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
        # self.board = [["BW"[(i+j+size%2+1) % 2] for i in range(size)] for j in range(size)]
        self.board = [[BoardCell("BW"[(i+j+size%2+1) % 2], CellState.EMPTY) for i in range(size)] for j in range(size)]

             
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
        
