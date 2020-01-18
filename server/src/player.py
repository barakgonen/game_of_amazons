import random
from point import Point

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print ("Creating an instance of Player, name is: " + self.name + ", color is: " + self.color)

    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

class ComputerPlayer(Player):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        # self.movesCalculator = movesCalculator
    def make_move(self):
        algo_move = self.calculate_next_move()
        print "This is algorithm turn, " + algo_move.to_string()
        return ""

    def calculate_next_move(self):
        list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        b=random.randint(0,5)
        x = str(list1[b])
        y = random.randint(1, 6)
        return Point(x, y)

    def get_amazon_to_move(self):
        return self.calculate_next_move()

class HumanPlayer(Player):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_move(self):
        human_move = self.calculate_next_move()
        print "<make_move()> This is human turn, my turn is: " + human_move.to_string()
        return human_move

    def calculate_next_move(self):
        x = str(raw_input("Enter x (horizontal,  capital letter): "))[0]
        if x.islower():
            x = x.upper()[0]
        while not x: 
            x = str(raw_input("Enter x (horizontal,  capital letter): "))[0]
            if x.islower():
                x = x.upper[0]
        y = input("Enter y (vertical,): number")
        while not y:
            y = input("Enter y (vertical,): number")
        return Point(x, y)

    def get_amazon_to_move(self):
        x = str(raw_input("Enter x (horizontal,  capital letter): "))[0]
        if x.islower():
            x = x.upper()[0]
        while not x: 
            x = str(raw_input("Enter x (horizontal,  capital letter): "))[0]
            if x.islower():
                x = x.upper[0]
        y = input("Enter y (vertical,): number")
        while not y:
            y = input("Enter y (vertical,): number")
        return Point(x, y)

    def shoot_blocking_rock(self):
        print "<Human_Player::shoot_blocking_rock()> Select position to throw blocking rock"
        x = str(raw_input("Enter x (horizontal,  capital letter): "))[0]
        if x.islower():
            x = x.upper()[0]
        while not x: 
            x = str(raw_input("Enter x (horizontal,  capital letter): "))[0]
            if x.islower():
                x = x.upper[0]
        y = input("Enter y (vertical,): number")
        while not y:
            y = input("Enter y (vertical,): number")
        return Point(x, y)