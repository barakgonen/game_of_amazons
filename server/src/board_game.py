from constants import Constants, CellState
from common_funcs import get_col_index, get_raw_index
from point import Point
import logging

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
        logging.info("<BoardGame::BoardGame()> Placing amazons in the board. Board size is: " + str(size))
        try:
            if (self.size == Constants.LARGE_BOARD_SIZE):
                self.board[get_raw_index(7, self.size)][get_col_index('A', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(10, self.size)][get_col_index('D', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(10, self.size)][get_col_index('G', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(7, self.size)][get_col_index('J', self.size)].state = CellState.BLACK_AMAZON
                self.board[get_raw_index(4, self.size)][get_col_index('A', self.size)].state = CellState.WHITE_AMAZON
                self.board[get_raw_index(1, self.size)][get_col_index('D', self.size)].state = CellState.WHITE_AMAZON
                self.board[get_raw_index(1, self.size)][get_col_index('G', self.size)].state = CellState.WHITE_AMAZON
                self.board[get_raw_index(4, self.size)][get_col_index('J', self.size)].state = CellState.WHITE_AMAZON
  
            elif(self.size == Constants.SMALL_BOARD_SIZE):
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
        logging.debug("<get_size()> Returning size of the board. size is: " + str(self.size))
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
            logging.debug("<update_move()> move updated successfully!")
        else:
            logging.error("<update_move()> something went wrong dude")
        
    # this is the final function called, after validations
    def shoot_blocking_rock(self, rock_target_pos):
        if (self.board[get_raw_index(rock_target_pos.y, self.size)][get_col_index(rock_target_pos.x, self.size)].state == CellState.EMPTY):
            self.board[get_raw_index(rock_target_pos.y, self.size)][get_col_index(rock_target_pos.x, self.size)].state = CellState.BLOCKED
            logging.debug("<shoot_blocking_rock()>, shooting is valid")
            return True
        else:
            logging.error("<shoot_blocking_rock()> Error, you tried to shoot to non-empty cell")
            return False
    
    def get_players_positions(self, player_color):
        cell_state = CellState.WHITE_AMAZON if player_color == "WHITE" else CellState.BLACK_AMAZON
        players_pos = []
        # iterate as you get input A,1 or 1,A...
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                if cell_state == CellState.BLACK_AMAZON:
                    if self.is_black_amazon(i, Constants.COLUMNS_ARRAY[j]):
                        players_pos.append(Point(Constants.COLUMNS_ARRAY[j], i))
                elif cell_state == CellState.WHITE_AMAZON:    
                    if self.is_white_amazon(i, Constants.COLUMNS_ARRAY[j]):
                        players_pos.append(Point(Constants.COLUMNS_ARRAY[j], i))
                else:
                    raise IndexError("BARAK YOU GOT A BUG!")
        return players_pos



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
# class Board:
#     def __init__(self, size, wqs, bqs):
#         self.time_limit = None
#         self.bWhite = True
#         self.config = [['.' for c in range(size)] for r in range(size)]
#         for (r,c) in wqs:
#             self.config[r][c] = 'Q'
#         for (r,c) in bqs:
#             self.config[r][c] = 'q'
            
#     def print_board(self):
#         size = len(self.config)
#         print ("     Black")
#         tmp = "  "+" ".join(map(lambda x: chr(x+ord('a')),range(size)))
#         print (tmp)
#         for r in range(size-1, -1, -1):
#             print r, " ".join(self.config[r]), r
#         print (tmp)
#         print ("     White\n")

#     def valid_path(self, src, dst):
#         (srcr, srcc) = src
#         (dstr, dstc) = dst        

#         srcstr = rc2ld(src)
#         dststr = rc2ld(dst)

#         symbol = self.config[srcr][srcc]
#         if (self.bWhite and symbol != 'Q') or (not self.bWhite and symbol != 'q'):
#             print "invalid move: cannot find queen at src:",srcstr
#             return False

#         h = dstr-srcr
#         w = dstc-srcc
#         if h and w and abs(h/float(w)) != 1: 
#             print("invalid move: not a straight line")
#             return False
#         if not h and not w:
#             print("invalid move: same start-end")
#             return False

#         if not h:
#             op = (0, int(w/abs(w)))
#         elif not w:
#             op = (int(h/abs(h)),0)
#         else:
#             op = (int(h/abs(h)),int(w/abs(w)))

#         (r,c) = (srcr,srcc)
#         while (r,c) != (dstr, dstc):
#             (r,c) = (r+op[0], c+op[1])
#             if (self.config[r][c] != '.'):
#                 print "invalid move: the path is not cleared between",srcstr,dststr
#                 return False
#         return True

#     def move_queen(self, src, dst):
#         self.config[dst[0]][dst[1]] = self.config[src[0]][src[1]]
#         self.config[src[0]][src[1]] = '.'

#     def shoot_arrow(self, dst):
#         self.config[dst[0]][dst[1]] = 'x'

#     def end_turn(self):
#         # count up each side's territories
#         (w,b) = self.count_areas()
#         # if none of the queens of either side can move, the player who just
#         # played wins, since that player claimed the last free space.
#         if b == w and b == 0:
#             if self.bWhite: w = 1
#             else: b = 1
#         # switch player
#         self.bWhite = not self.bWhite
#         return (w,b)

#     # adapted from standard floodfill method to count each player's territories
#     # - if a walled-off area with queens from one side belongs to that side
#     # - a walled-off area with queens from both side is neutral
#     # - a walled-off area w/ no queens is deadspace
#     def count_areas(self):
#         # replace all blanks with Q/q/n/-
#         def fill_area(replace):
#             count = 0
#             for r in range(size):
#                 for c in range(size):
#                     if status[r][c] == '.':
#                         count+=1
#                         status[r][c] = replace
#             return count
        
#         # find all blank cells connected to the seed blank at (seedr, seedc) 
#         def proc_area(seedr,seedc):
#             symbols = {} # keeps track of types of symbols encountered in this region
#             connected = [(seedr,seedc)] # a stack for df traversal on the grid
#             while connected:
#                 (r, c) = connected.pop()
#                 status[r][c] = '.'
#                 for ops in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]:
#                     (nr, nc) = (r+ops[0], c+ops[1])
#                     if nr < 0 or nr >= size or nc < 0 or nc >= size:
#                         continue
#                     # if it's a new blank, need to process it; also add to seen
#                     if self.config[nr][nc] == '.' and status[nr][nc] == '?':
#                         status[nr][nc] = '.'
#                         connected.append((nr,nc))
#                     # if it's a queen or an arrow; just mark as seen
#                     elif self.config[nr][nc] != '.': 
#                         status[nr][nc] = 'x'
#                         symbols[self.config[nr][nc]] = 1

#             if 'Q' in symbols and not 'q' in symbols: # area belongs to white
#                 return (fill_area('Q'), 0, 0)
#             elif 'q' in symbols and not 'Q' in symbols: #area belongs to black
#                 return (0, fill_area('q'),0)
#             elif 'q' in symbols and 'Q' in symbols: # area is neutral
#                 return (0, 0, fill_area('n'))
#             else: # deadspace -- still have to fill but don't return its area value
#                 fill_area('-')
#                 return (0,0,0)

#         size = len(self.config)
#         # data structure for keeping track of seen locations
#         status = [['?' for i in range(size)] for j in range(size)]
#         wtot = btot = ntot = 0
#         for r in range(size):
#             for c in range(size):            
#                 # if it's an empty space and we haven't seen it before, process it
#                 if self.config[r][c] == '.' and status[r][c] == '?':
#                     (w,b,n) = proc_area(r,c)
#                     wtot += w
#                     btot += b
#                     ntot += n
#                 # if it's anything else, but we haven't seen it before, just mark it as seen and move on
#                 elif status[r][c] == '?':
#                     status[r][c] = 'x'
                    
#         if ntot == 0: # no neutral space left -- should end game
#             if wtot > btot:
#                 return (wtot-btot, 0)
#             else: return (0, btot-wtot)
#         else: return (wtot+ntot, btot+ntot)

# # utility functions:
# # ld2rc -- takes a string of the form, letter-digit (e.g., "a3")
# # and returns a tuple in (row, column): (3,0)
# # rc2ld -- takes a tuple of the form (row, column) -- e.g., (3,0)
# # and returns a string of the form, letter-digit (e.g., "a3")

# def ld2rc(raw_loc):
#     return (int(raw_loc[1]), ord(raw_loc[0])-ord('a'))
# def rc2ld(tup_loc):
#     return chr(tup_loc[1]+ord('a'))+str(tup_loc[0])

# # get next move from a human player
# # The possible return values are the same as an automatic player:
# # Usually, the next move should be returned. It must be specified in the following format:
# # [(queen-start-row, queen-start-col), (queen-end-row,queen-end-col), (arrow-end-row, arrow-end-col)]
# # To resign from the game, return False

# def human(board):

#     board.print_board()

#     if board.bWhite:
#         print("You're playing White (Q)")
#     else:
#         print("You're playing Black (q)")

#     print("Options:")
#     print('* To move, type "<loc-from> <loc-to>" (e.g., "a3-d3")')
#     print('* To resign, type "<return>"')
#     while True: # loop to get valid queen move from human
#         while True: # loop to check for valid input syntax first
#             raw_move = raw_input("Input please: ").split()
#             if not raw_move: # human resigned
#                 return False
#             # if they typed "a3-d3"
#             elif re.match("^[a-j][0-9]\-[a-j][0-9]$",raw_move[0]):
#                 break
#             else: print str(raw_move),"is not a valid input format"
#         (src, dst) = map(ld2rc, raw_move[0].split('-'))
#         if board.valid_path(src, dst):
#             board.move_queen(src, dst)
#             break 

#     board.print_board()
#     print("Options:")
#     print('* To shoot, type "<loc-to>" (e.g., "h3")')
#     print('* To resign, type "<return>"')
#     while True: # loop to get valid move from human
#         while True: # loop to check for valid syntax first
#             raw_move = raw_input("Input please: ").split()
#             if not raw_move:
#                 return False
#             if re.match("^[a-j][0-9]$",raw_move[0]):
#                 break
#             else: print raw_move,"is not a valid input"
#         adst = ld2rc(raw_move[0])
#         if board.valid_path(dst,adst):
#             return (src,dst,adst)
