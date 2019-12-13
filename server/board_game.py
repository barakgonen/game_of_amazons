class BoardGame:
    def __init__(self, size):
        self.board = [[]]
        self.board = [["BW"[(i+j+size%2+1) % 2] for i in range(size)] for j in range(size)]
             
    def print_board(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[i])):
                print self.board[i][j],
            print ""
        
