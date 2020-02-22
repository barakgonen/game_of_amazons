import copy
import random
import numpy as np
from point import Point
from game_tree import GameTree

class Player:
    def __init__(self, name, color, current_board_game):
        self.name = name
        self.color = color
        self.board_game = current_board_game
        print ("Creating an instance of Player, name is: " + self.name + ", color is: " + self.color)

    def get_name(self):
        return self.name
    
    def get_color(self):
        return self.color

# This class implements my AI Functionality, it has it's own implementation of make_move func, which calculates the next best move to do
class ComputerPlayer(Player):
    def __init__(self, name, color, available_steps_manager, searching_distance, blocking_rocks_manager, searching_depth):
        self.name = name
        self.color = color
        self.available_steps_manager = available_steps_manager
        self.searching_distance = searching_distance
        self.blocking_rocks_manager = blocking_rocks_manager
        self.searching_depth = searching_depth
        
    def make_move(self, current_board_game):
        # Building GameTree from current board, each level below level 1 represents game state
        game_tree = GameTree(current_board_game, 
                             self.color, 
                             self.searching_distance, 
                             self.available_steps_manager, 
                             self.blocking_rocks_manager, 
                             self.searching_depth)
        return game_tree.get_next_move()

    def calculate_next_move(self):
        list1=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        b=random.randint(0,5)
        x = str(list1[b])
        y = random.randint(1, 6)
        return Point(x, y)

    def get_amazon_to_move(self):
        return self.calculate_next_move()

class HumanPlayer(Player):
    def __init__(self, name, color, board_game=None):
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