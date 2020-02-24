# import os
# import json
# import requests
# import SocketServer
# import SimpleHTTPServer

# from src.constants import Constants
# from src.board_game import BoardGame
# from src.game_manager import GameManager
# from src.turn_validator import TurnValidator
# from src.player import ComputerPlayer, HumanPlayer
# from src.web_socket_adapter import WebSocketAdapter
# from src.blocking_rocks_manager import BlockingRocksManager

# def get_config():
#   configurationFile = ""
#   f = open('./config.json', "r")
#   for line in f:
#     configurationFile += line
#   f.close()
#   return configurationFile

# def run_server():
#   y = json.loads(get_config())
#   PORT = y["server-listening-port"]
#   Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
#   httpd = SocketServer.TCPServer(("", int(PORT)), Handler)
#   print "serving at port", PORT
#   httpd.serve_forever()

# def get_board_size():
#   is_input_valid = False
#   while (is_input_valid == False):
#     try:
#       board_size = int(input("Enter prefered board size: " + str(Constants.LARGE_BOARD_SIZE) + "^2 or: " + str(Constants.SMALL_BOARD_SIZE) + "^2"))
#     except Exception:
#         print "Your input is invalid.. please try again."
#         continue
#     if (board_size != Constants.LARGE_BOARD_SIZE and board_size != Constants.SMALL_BOARD_SIZE):
#       print "Your input is invalid.. please try again."
#     else:
#       is_input_valid = True
#       return board_size

# def main():
#   board_size = int(get_board_size())
#   board_game = BoardGame(board_size)
#   blocking_rocks_manager = BlockingRocksManager(board_size)

#   p1 = HumanPlayer("BARAK", "WHITE")
#   p2 = ComputerPlayer("ALGORITHM", "BLACK")
#   turn_validator = TurnValidator(board_game)

#   manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
#   manager.run_game()

# if __name__ == "__main__":
#     main()

# from ast import literal_eval
# import sys

# ##########################
# ######   MINI-MAX   ######
# ##########################

# # Think about this just on a game_tree... for now.
# # Can worry about how to actually generate that game tree, later.
# class MiniMax:
#     # print utility value of root node (assuming it is max)
#     # print names of all nodes visited during search
#     def __init__(self, game_tree):
#         self.game_tree = game_tree  # GameTree
#         self.root = game_tree.root  # GameNode
#         self.currentNode = None     # GameNode
#         self.successors = []        # List of GameNodes
#         return

#     def minimax(self, node):
#         # first, find the max value
#         best_val = self.max_value(node) # should be root node of tree

#         # second, find the node which HAS that max value
#         #  --> means we need to propagate the values back up the
#         #      tree as part of our minimax algorithm
#         successors = self.getSuccessors(node)
#         print "MiniMax:  Utility Value of Root Node: = " + str(best_val)
#         # find the node with our best move
#         best_move = None
#         for elem in successors:   # ---> Need to propagate values up tree for this to work
#             if elem.value == best_val:
#                 best_move = elem
#                 break

#         # return that best value that we've found
#         return best_move


#     def max_value(self, node):
#         print "MiniMax-->MAX: Visited Node :: " + node.Name
#         if self.isTerminal(node):
#             return self.getUtility(node)

#         infinity = float('inf')
#         max_value = -infinity

#         successors_states = self.getSuccessors(node)
#         # not sure how we signal to keep going down the tree
#         # except on tree nodes yet...
#         for state in successors_states:
#             # max_value = max(max_value, self.min_value(self.getSuccessors(state)))
#             max_value = max(max_value, self.min_value(state))
#         return max_value

#     def min_value(self, node):
#         print "MiniMax-->MIN: Visited Node :: " + node.Name
#         if self.isTerminal(node):
#             return self.getUtility(node)

#         infinity = float('inf')
#         min_value = infinity

#         successor_states = self.getSuccessors(node)
#         for state in successor_states:
#             # min_value = min(min_value, self.max_value(self.getSuccessors(state)))
#             min_value = min(min_value, self.max_value(state))
#         return min_value

#     #                     #
#     #   UTILITY METHODS   #
#     #                     #

#     # successor states in a game tree are the child nodes...
#     def getSuccessors(self, node):
#         assert node is not None
#         return node.children

#     # return true if the node has NO children (successor states)
#     # return false if the node has children (successor states)
#     def isTerminal(self, node):
#         assert node is not None
#         return len(node.children) == 0

#     def getUtility(self, node):
#         assert node is not None
#         return node.value


# ##########################
# ###### MINI-MAX A-B ######
# ##########################

# class AlphaBeta:
#     # print utility value of root node (assuming it is max)
#     # print names of all nodes visited during search
#     def __init__(self, game_tree):
#         self.game_tree = game_tree  # GameTree
#         self.root = game_tree.root  # GameNode
#         return

#     def alpha_beta_search(self, node):
#         infinity = float('inf')
#         best_val = -infinity
#         beta = infinity

#         successors = self.getSuccessors(node)
#         best_state = None
#         for state in successors:
#             value = self.min_value(state, best_val, beta)
#             if value > best_val:
#                 best_val = value
#                 best_state = state
#         print "AlphaBeta:  Utility Value of Root Node: = " + str(best_val)
#         print "AlphaBeta:  Best State is: " + best_state.Name
#         return best_state

#     def max_value(self, node, alpha, beta):
#         print "AlphaBeta-->MAX: Visited Node :: " + node.Name
#         if self.isTerminal(node):
#             return self.getUtility(node)
#         infinity = float('inf')
#         value = -infinity

#         successors = self.getSuccessors(node)
#         for state in successors:
#             value = max(value, self.min_value(state, alpha, beta))
#             if value >= beta:
#                 return value
#             alpha = max(alpha, value)
#         return value

#     def min_value(self, node, alpha, beta):
#         print "AlphaBeta-->MIN: Visited Node :: " + node.Name
#         if self.isTerminal(node):
#             return self.getUtility(node)
#         infinity = float('inf')
#         value = infinity

#         successors = self.getSuccessors(node)
#         for state in successors:
#             value = min(value, self.max_value(state, alpha, beta))
#             if value <= alpha:
#                 return value
#             beta = min(beta, value)

#         return value
#     #                     #
#     #   UTILITY METHODS   #
#     #                     #

#     # successor states in a game tree are the child nodes...
#     def getSuccessors(self, node):
#         assert node is not None
#         return node.children

#     # return true if the node has NO children (successor states)
#     # return false if the node has children (successor states)
#     def isTerminal(self, node):
#         assert node is not None
#         return len(node.children) == 0

#     def getUtility(self, node):
#         assert node is not None
#         return node.value


# #########################
# ###### GAME OBJECT ######
# #########################

# class Game:
#     def __init__(self):
#         self.initial_state = None
#         self.current_state = None
#         self.game_tree = None
#         # player(s) --> who's the player in the state
#         # successors(s) --> possible moves from current state
#         # result(a,s) --> the resulting state after action (a) is taken on state (s)
#         # terminal(s) --> returns true if state is a terminal state
#         # utility(s,p) --> the value function of state (s) for player (p)

#     def player(self, s):
#         # given a state, determine current player
#         # MAX or MIN
#         return None

#     def successors(self, s):
#         # Given a current state, return a list of successor states
#         return None

#     def result(self, a, s):
#         #
#         return None

#     def terminal(self, s):
#         return None

#     def utility(self, s, p):
#         return None




# ##########################
# ###### PARSE DATA ########
# ##########################
# def parse_data_as_list(fname):
#     with open(fname, "r") as f:
#         data_as_string = f.read()
#         print data_as_string
#         data_list = literal_eval(data_as_string)
#     return data_list


# class GameNode:
#     def __init__(self, name, value=0, parent=None):
#         self.Name = name      # a char
#         self.value = value    # an int
#         self.parent = parent  # a node reference
#         self.children = []    # a list of nodes

#     def addChild(self, childNode):
#         self.children.append(childNode)

# class GameTree:
#     def __init__(self):
#         self.root = None

#     def build_tree(self, data_list):
#         """
#         :param data_list: Take data in list format
#         :return: Parse a tree from it
#         """
#         self.root = GameNode(data_list.pop(0))
#         for elem in data_list:
#             self.parse_subtree(elem, self.root)

#     def parse_subtree(self, data_list, parent):
#         # base case
#         if type(data_list) is tuple:
#             # make connections
#             leaf_node = GameNode(data_list[0])
#             leaf_node.parent = parent
#             parent.addChild(leaf_node)
#             # if we're at a leaf, set the value
#             if len(data_list) == 2:
#                 leaf_node.value = data_list[1]
#             return

#         # recursive case
#         tree_node = GameNode(data_list.pop(0))
#         # make connections
#         tree_node.parent = parent
#         parent.addChild(tree_node)
#         for elem in data_list:
#             self.parse_subtree(elem, tree_node)

#         # return from entire method if base case and recursive case both done running
#         return

# ##########################
# #### MAIN ENTRY POINT ####
# ##########################

# def main():
#     filename = "C:\Users\barak\Documents\HaifaUniversity\AI\FinalProject\amazonsconfig.txt"
#     # filename = sys.argv[1]
#     print "------- CS1571 - ASSIGNMENT #02 -----------"
#     print "@author - Anthony (Tony) Poerio"
#     print "@email adp59@pitt.edu"
#     print '  ##############################'
#     print '  ########## PART I ############'
#     print '  ##############################\n'
#     print "FILENAME: " + filename
#     data_list = parse_data_as_list(filename)
#     data_tree = GameTree()
#     data_tree.build_tree(data_list)
#     print "\n\n----- MINIMAX SEARCH ------"
#     minimax = MiniMax(data_tree)
#     best_move = minimax.minimax(minimax.root)
#     alphabeta = AlphaBeta(data_tree)
#     print "\n\n----- ALPHA BETA PRUNING ------"
#     best_move_ab = alphabeta.alpha_beta_search(alphabeta.root)

# if __name__ == "__main__":
#     main()

# CS1571 -- Assignment #3: El Juego de las Amazonas in Python 2.7
# For more information about the game itself, please refer to:
#      http://en.wikipedia.org/wiki/Game_of_the_Amazons
#
# This file provides some basic support for you to develop your automatic Amazons player.
# It gives everyone a common starting point, and it will make it easier for us to set your players
# to play against each other. Therefore, you should NOT make any changes to the provided code unless
# directed otherwise. If you find a bug, please email me.

# This implementation includes two class definitions, some utility functions,
# and a function for a human player ("human").
# The two classes are:
# - The Amazons class: the main game controller
# - The Board class: contains info about the current board configuration.
#   It is through the Board class that the game controller
#   passes information to your player function.
# More details about these two classes are provided in their class definitions

# Your part: Write an automatic player function for the Game of the Amazons.
# * your automatic player MUST have your email userID as its function name (e.g., reh23)
# * The main game controller will call your function at each turn with
#   a copy of the current board as the input argument.  
# * Your function's return value should be your next move.
#   It must be expressed as a tuple of three tuples: e.g., ((0, 3), (1,3), (8,3)) 
#    - the start location of the queen you want to move (in row, column)
#    - the queen's move-to location,
#    - the arrow's landing location.
#   If you have no valid moves left, the function should return False.

# As usual, we won't spend much time on the user interface. 
# Updates of the game board are drawn with simple ascii characters.
#
# - Below is a standard initial board configuration:
#   * The board is a 10x10 grid. (It is advisable to use a smaller board during development/debugging)
#   * Each side has 4 queens. The white queens are represented as Q's; the black queens are represented as q's
#
#      a b c d e f g h i j
#   9  . . . q . . q . . . 
#   8  . . . . . . . . . . 
#   7  . . . . . . . . . . 
#   6  q . . . . . . . . q 
#   5  . . . . . . . . . . 
#   4  . . . . . . . . . . 
#   3  Q . . . . . . . . Q 
#   2  . . . . . . . . . . 
#   1  . . . . . . . . . . 
#   0  . . . Q . . Q . . . 
#
# - During a player's turn, one of the player's queens must be moved, then an arrow must be shot from the moved queen.
# - the arrow is represented as 'x'
# - neither the queens nor their arrows can move past another queen or an arrow
#
# - The objective of the game is to minimze your opponent's queens' movement.
# - The game technically ends when one side's queens have no more legal moves,
#   but the game practically ends when the queens from the two sides have been
#   segregated. We will just count up the territories owned by each side and
#   the side with the larger territory will be declared the winner

############################################
import copy, random, re, time, sys
from src.adp59_minimax import GameTree, AlphaBeta, Game

# The Amazons class controls the flow of the game.
# Its data include:
# * size -- size of board: assume it's <= 10
# * time_limit -- # of seconds a mchine is allowed to take (<30)
# * playerW -- name of the player function who'll play white
# * playerB -- name of the player function who'll play black
# * wqs -- initial positions of the white queens
# * bqs -- initial positions of the black queens
# * board -- current board configuration (see class def for Board)
# Its main functions are:
# * play: the main control loop of a game, which would:
#   - turn taking management: calls each auto player's minimax function (or "human")
#   - check for the validity of the player's move:
#     an auto player loses a turn if an invalid move is returned or if it didn't return a move in the alloted time  
#   - check for end game condition 
#   - declare the winner
# * update: this function tries out the move on a temporary board.
#   if the move is valid, the real board will be updated.
# * end_turn: just get the score from the board class

class Amazons:
    def __init__(self, fname):
        fin = open("C:\\Users\\barak\\Documents\\HaifaUniversity\\AI\\FinalProject\\amazonsconfig.txt", 'r')
        self.time_limit = int(fin.readline())
        self.size = int(fin.readline())
        self.playerW = fin.readline().strip()
        self.wqs = tuple(map(ld2rc,fin.readline().split()))
        self.playerB = fin.readline().strip()
        self.bqs  = tuple(map(ld2rc,fin.readline().split()))
        self.board = Board(self.size, self.wqs, self.bqs)

    def update(self, move):
        try:
            (src,dst,adst) = move
        except: return False

        # try out the move on a temp board        
        tmp_board = copy.deepcopy(self.board)
        if tmp_board.valid_path(src,dst):
            tmp_board.move_queen(src,dst)
            if tmp_board.valid_path(dst, adst):
                # the move is good. make the real board point to it
                tmp_board.shoot_arrow(adst)
                del self.board
                self.board = tmp_board
                return True
        # move failed. 
        del tmp_board
        return False

    def end_turn(self):
        return self.board.end_turn()

    def play(self):
        bPlay = True
        wscore = bscore = 0
        while (bPlay):
            for p in [self.playerW, self.playerB]:
                # send player a copy of the current board
                tmp_board = copy.deepcopy(self.board)
                tstart = time.clock()
                tmp_board.time_limit = tstart+self.time_limit
                move = eval("%s(tmp_board)"%p)
                tstop = time.clock()
                del tmp_board

                if move:
                    print p,": move:", [rc2ld(x) for x in move],"time:", tstop-tstart, "seconds"
                else: 
                    print p,"time:", tstop-tstart, "seconds"
                    # if move == False --> player resigned   
                    if self.board.bWhite:
                        (wscore, bscore) = (-1,0)
                    else: (wscore, bscore) = (0,-1)
                    bPlay = False
                    break

                # only keep clock for auto players
                if p != "human" and (tstop - tstart) > self.time_limit:
                    print p, ": took too long -- lost a turn"
                elif not self.update(move):
                    print p, ": invalid move", move, " lost a turn"

                # at the end of the turn, check whether the game ended
                # and update whether white is playing next
                (wscore, bscore) = self.end_turn()
                if wscore and bscore:
                    continue
                else:
                    bPlay = False
                    break
        # print final board
        self.board.print_board()
        if wscore == -1:
            print self.playerW,"(white) resigned.", self.playerB,"(black) wins"
        elif bscore == -1:
            print self.playerB,"(black) resigned.", self.playerW,"(white) wins"
        elif not wscore:
            print self.playerB,"(black) wins by a margin of",bscore
        else: print self.playerW, "(white) wins by a margin of",wscore
                
        
##############################################
# The Board class stores basic information about the game configuration.
# 
# NOTE: The amount of info stored in this class is kept to a minimal. This
# is on purpose. This is just set up as a way for the game controller to
# pass information to your automatic player. Although you cannot change
# the definition of the Board class, you are not constrained to use the
# Board class as your main state reprsentation. You can define your own
# State class and copy/transform from Board the info you need.

# The Board class contains the following data:
#  * config: the board configuration represented as a list of lists.
#    The assumed convention is (row, column) so config[0][1] = "b0"
#  * bWhite: binary indicator -- True if it's white's turn to play
#  * time_limit: deadline for when a move must be returned by
# The Board class supports the following methods:
#  * print_board: prints the current board configuration
#  * valid_path: takes two location tuples (in row, column format) and returns 
#    whether the end points describe a valid path (for either the queen or the arrow)
#  * move_queen: takes two location tuples (in row, column format)
#    and updates the board configuration to reflect the queen moving
#    from src to dst
#  * shoot_arrow: takes one location tuple (in row, column format)
#    and updates the board configuration to include the shot arrow
#  * end_turn: This function does some end of turn accounting: update whose
#    turn it is and determine whether the game ended
#  * count_areas: This is a helper function for end_turn. It figures out
#    whether we can end the game
class Board:
    def __init__(self, size, wqs, bqs):
        self.time_limit = None
        self.bWhite = True
        self.config = [['.' for c in range(size)] for r in range(size)]
        for (r,c) in wqs:
            self.config[r][c] = 'Q'
        for (r,c) in bqs:
            self.config[r][c] = 'q'
            
    def print_board(self):
        size = len(self.config)
        print ("     Black")
        tmp = "  "+" ".join(map(lambda x: chr(x+ord('a')),range(size)))
        print (tmp)
        for r in range(size-1, -1, -1):
            print r, " ".join(self.config[r]), r
        print (tmp)
        print ("     White\n")

    def valid_path(self, src, dst):
        (srcr, srcc) = src
        (dstr, dstc) = dst        

        srcstr = rc2ld(src)
        dststr = rc2ld(dst)

        symbol = self.config[srcr][srcc]
        if (self.bWhite and symbol != 'Q') or (not self.bWhite and symbol != 'q'):
            print "invalid move: cannot find queen at src:",srcstr
            return False

        h = dstr-srcr
        w = dstc-srcc
        if h and w and abs(h/float(w)) != 1: 
            print("invalid move: not a straight line")
            return False
        if not h and not w:
            print("invalid move: same start-end")
            return False

        if not h:
            op = (0, int(w/abs(w)))
        elif not w:
            op = (int(h/abs(h)),0)
        else:
            op = (int(h/abs(h)),int(w/abs(w)))

        (r,c) = (srcr,srcc)
        while (r,c) != (dstr, dstc):
            (r,c) = (r+op[0], c+op[1])
            if (self.config[r][c] != '.'):
                print "invalid move: the path is not cleared between",srcstr,dststr
                return False
        return True

    def move_queen(self, src, dst):
        self.config[dst[0]][dst[1]] = self.config[src[0]][src[1]]
        self.config[src[0]][src[1]] = '.'

    def shoot_arrow(self, dst):
        self.config[dst[0]][dst[1]] = 'x'

    def end_turn(self):
        # count up each side's territories
        (w,b) = self.count_areas()
        # if none of the queens of either side can move, the player who just
        # played wins, since that player claimed the last free space.
        if b == w and b == 0:
            if self.bWhite: w = 1
            else: b = 1
        # switch player
        self.bWhite = not self.bWhite
        return (w,b)

    # adapted from standard floodfill method to count each player's territories
    # - if a walled-off area with queens from one side belongs to that side
    # - a walled-off area with queens from both side is neutral
    # - a walled-off area w/ no queens is deadspace
    def count_areas(self):
        # replace all blanks with Q/q/n/-
        def fill_area(replace):
            count = 0
            for r in range(size):
                for c in range(size):
                    if status[r][c] == '.':
                        count+=1
                        status[r][c] = replace
            return count
        
        # find all blank cells connected to the seed blank at (seedr, seedc) 
        def proc_area(seedr,seedc):
            symbols = {} # keeps track of types of symbols encountered in this region
            connected = [(seedr,seedc)] # a stack for df traversal on the grid
            while connected:
                (r, c) = connected.pop()
                status[r][c] = '.'
                for ops in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    (nr, nc) = (r+ops[0], c+ops[1])
                    if nr < 0 or nr >= size or nc < 0 or nc >= size:
                        continue
                    # if it's a new blank, need to process it; also add to seen
                    if self.config[nr][nc] == '.' and status[nr][nc] == '?':
                        status[nr][nc] = '.'
                        connected.append((nr,nc))
                    # if it's a queen or an arrow; just mark as seen
                    elif self.config[nr][nc] != '.': 
                        status[nr][nc] = 'x'
                        symbols[self.config[nr][nc]] = 1

            if 'Q' in symbols and not 'q' in symbols: # area belongs to white
                return (fill_area('Q'), 0, 0)
            elif 'q' in symbols and not 'Q' in symbols: #area belongs to black
                return (0, fill_area('q'),0)
            elif 'q' in symbols and 'Q' in symbols: # area is neutral
                return (0, 0, fill_area('n'))
            else: # deadspace -- still have to fill but don't return its area value
                fill_area('-')
                return (0,0,0)

        size = len(self.config)
        # data structure for keeping track of seen locations
        status = [['?' for i in range(size)] for j in range(size)]
        wtot = btot = ntot = 0
        for r in range(size):
            for c in range(size):            
                # if it's an empty space and we haven't seen it before, process it
                if self.config[r][c] == '.' and status[r][c] == '?':
                    (w,b,n) = proc_area(r,c)
                    wtot += w
                    btot += b
                    ntot += n
                # if it's anything else, but we haven't seen it before, just mark it as seen and move on
                elif status[r][c] == '?':
                    status[r][c] = 'x'
                    
        if ntot == 0: # no neutral space left -- should end game
            if wtot > btot:
                return (wtot-btot, 0)
            else: return (0, btot-wtot)
        else: return (wtot+ntot, btot+ntot)

# utility functions:
# ld2rc -- takes a string of the form, letter-digit (e.g., "a3")
# and returns a tuple in (row, column): (3,0)
# rc2ld -- takes a tuple of the form (row, column) -- e.g., (3,0)
# and returns a string of the form, letter-digit (e.g., "a3")

def ld2rc(raw_loc):
    return (int(raw_loc[1]), ord(raw_loc[0])-ord('a'))
def rc2ld(tup_loc):
    return chr(tup_loc[1]+ord('a'))+str(tup_loc[0])

# get next move from a human player
# The possible return values are the same as an automatic player:
# Usually, the next move should be returned. It must be specified in the following format:
# [(queen-start-row, queen-start-col), (queen-end-row,queen-end-col), (arrow-end-row, arrow-end-col)]
# To resign from the game, return False

def human(board):

    board.print_board()

    if board.bWhite:
        print("You're playing White (Q)")
    else:
        print("You're playing Black (q)")

    print("Options:")
    print('* To move, type "<loc-from> <loc-to>" (e.g., "a3-d3")')
    print('* To resign, type "<return>"')
    while True: # loop to get valid queen move from human
        while True: # loop to check for valid input syntax first
            raw_move = raw_input("Input please: ").split()
            if not raw_move: # human resigned
                return False
            # if they typed "a3-d3"
            elif re.match("^[a-j][0-9]\-[a-j][0-9]$",raw_move[0]):
                break
            else: print str(raw_move),"is not a valid input format"
        (src, dst) = map(ld2rc, raw_move[0].split('-'))
        if board.valid_path(src, dst):
            board.move_queen(src, dst)
            break 

    board.print_board()
    print("Options:")
    print('* To shoot, type "<loc-to>" (e.g., "h3")')
    print('* To resign, type "<return>"')
    while True: # loop to get valid move from human
        while True: # loop to check for valid syntax first
            raw_move = raw_input("Input please: ").split()
            if not raw_move:
                return False
            if re.match("^[a-j][0-9]$",raw_move[0]):
                break
            else: print raw_move,"is not a valid input"
        adst = ld2rc(raw_move[0])
        if board.valid_path(dst,adst):
            return (src,dst,adst)

###################### Your code between these two comment lines ####################################
def adp59(board):
    # takes board state as an input arg
    board.print_board()

    # make a Game object so we can run our algorithms
    game = Game(board)

    # get the queen locations on the board itself
    queenLocations = game.getQueenLocations()  # DONE

    # get all possible places that this set of queens can move to
    allMoves = game.getAllFutureQueenLocations(queenLocations)  # DONE

    # get every possible moves, including arrow shots
    queen_moves = game.getAllMovesForQueens(allMoves)  #DONE

    # check which color we are playing
    playerWhite = board.bWhite

    # create a game tree given our current move set
    moveTree = GameTree(queen_moves, board, playerWhite)

    # set the game tree in our game object, so we can run search on it
    game.setGameTree(moveTree)

    # run an ALPHA-BETA MINIMAX search on the tree we've just created
    search = AlphaBeta(moveTree)

    # and find the best state from that search
    best_state = search.alpha_beta_search(moveTree.root)

    # if we have no best state, we have no valid moves, so return false
    if best_state is None:
        return False
    # otherwise, return our move
    else:
        return map(ld2rc, best_state.name.split('-'))

###################### Your code between these two comment lines ####################################
        
def main():
    if len(sys.argv) == 2:
        fname = sys.argv[1]
    else:
        fname = raw_input("setup file name?")
    game = Amazons(fname)
    game.play()

if __name__ == "__main__":
    main()