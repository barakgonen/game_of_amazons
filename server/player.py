class Player:
    def __init__(self, name):
        self.name = name
        print ("Creating an instance of Player, name is: " + name)

class ComputerPlayer(Player):
    def __init__(self, name):
        self.name = name
        # self.movesCalculator = movesCalculator
    def make_move(self):
        print ("This is algorithm turn, my name is: " + self.name)

class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
    def make_move(self):
        print ("This is human turn, my name is: " + self.name)