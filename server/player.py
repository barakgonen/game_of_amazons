import random
from point import Point

class Player:
    def __init__(self, name):
        self.name = name
        print ("Creating an instance of Player, name is: " + name)

    def get_name(self):
        return self.name

class ComputerPlayer(Player):
    def __init__(self, name):
        self.name = name
        # self.movesCalculator = movesCalculator
    def make_move(self):
        algo_move = self.calculate_next_move()
        print "This is algorithm turn, " + algo_move.to_string()
        return ""

    def calculate_next_move(self):
        x = random.randrange(0, 60, 1)
        y = random.randrange(0, 60, 1)
        return Point(x, y)

class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
    def make_move(self):
        human_move = self.calculate_next_move()
        print "This is human turn, my turn is: " + human_move.to_string()
        return ""

    def calculate_next_move(self):
        x = input("Enter x: ") 
        y = input("Enter y: ")
        return Point(x, y) 