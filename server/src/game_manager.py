import logging

class GameManager:
    def __init__(self, black_player, white_player, turn_validator, board_game, blocking_manager):
        self.black_player = black_player
        self.white_player = white_player
        self.turn_validator = turn_validator
        self.board_game = board_game
        self.blocking_manager = blocking_manager

    def run_single_turn(self, player):
        # validate this is the correct amazona
        amazon_to_move = player.get_amazon_to_move()  # must have input validation!
        if (player.color == "BLACK"):
            is_amazon_valid = self.board_game.is_black_amazon(
                amazon_to_move.y, amazon_to_move.x)
        elif (player.color == "WHITE"):
            is_amazon_valid = self.board_game.is_white_amazon(
                amazon_to_move.y, amazon_to_move.x)
        else:
            raise RuntimeError("Un-recognized player playes")
        while (not is_amazon_valid):
            amazon_to_move = player.get_amazon_to_move()  # must have input validation!
            if (player.color == "BLACK"):
                is_amazon_valid = self.board_game.is_black_amazon(
                    amazon_to_move.y, amazon_to_move.x)
            elif (player.color == "WHITE"):
                is_amazon_valid = self.board_game.is_white_amazon(
                    amazon_to_move.y, amazon_to_move.x)
            else:
                raise RuntimeError("Un-recognized player playes")

        current_player_move = player.make_move()
        is_move_valid = self.turn_validator.is_step_valid(
            amazon_to_move, current_player_move)
        while (not is_move_valid):
            current_player_move = player.make_move()
            is_move_valid = self.turn_validator.is_step_valid(
                amazon_to_move, current_player_move)
        self.board_game.update_move(
            amazon_to_move, current_player_move, player.color)
        current_player_shoot = player.shoot_blocking_rock()
        is_shooting_valid = self.turn_validator.is_shoot_valid(
            current_player_move, current_player_shoot)
        while (not is_shooting_valid):
            current_player_shoot = player.shoot_blocking_rock()
            is_shooting_valid = self.turn_validator.is_shoot_valid(
                current_player_move, current_player_shoot)
        if (self.board_game.shoot_blocking_rock(current_player_shoot)):
            self.blocking_manager.get_rock()
        else:
            logging.error("<run_single_turn()> Error. we decieded we can shoot blocking rock, but update failed")

    def is_there_reason_to_play(self, player):
        if (self.blocking_manager.are_blocks_available() and
                self.turn_validator.is_there_are_available_mooves_for_player(player.get_color())):
            return True
        return False

    def run_round(self):
        # if there are rocks , self.blocking_manager.get_rock() need to check it after every turn shoul
        if self.is_there_reason_to_play(self.white_player):
            self.run_single_turn(self.white_player)
            logging.info("<run_round()> " + self.white_player.get_name() + " made successfull move!")
            if self.is_there_reason_to_play(self.black_player):
                self.run_single_turn(self.black_player)
                logging.info("<run_round()> " + self.black_player.get_name() + " made successfull move!")
                return True
        logging.warn("<run_round()> No more options available, stopping the game")
        return False

    def run_game(self):
        # first step, initialize queens on the board
        is_game_still_run = self.run_round()
        while (is_game_still_run):
            is_game_still_run = self.run_round()
        logging.info("<run_game()> game is over, according to board's state, need to define the winner")
        number_of_possible_moves_for_white = self.board_game.get_white_available_mooves()
        number_of_possible_moves_for_black = self.board_game.get_black_available_mooves()
        if (number_of_possible_moves_for_white > number_of_possible_moves_for_black):
            logging.info("<run_game()> White has won! Congrats")
        elif (number_of_possible_moves_for_black > number_of_possible_moves_for_white):
            logging.info("<run_game()> Black has won! Congrats")
        else:
            logging.error("<run_game()> There is a tie.. it means it's a bug since there ")





# class Game:
#     """
#     Object to encapsulate the WHOLE game we are playing
#     """
#     def __init__(self, board):
#         self.initial_state = None
#         self.current_state = None
#         self.game_tree = None
#         self.game_board = board.config
#         self.board = board


#     def player(self, node):
#         # given a state, determine current player
#         # accept a node --> return what player is up
#         if node.bWhite:
#             return 'w'
#         else:
#             return 'b'

#     #                 #
#     #     HELPERS     #
#     #                 #
#     def setGameTree(self, tree):
#         self.game_tree = tree

#     def getQueenLocations(self):
#         # get locations of all the queens
#         # return  a list with locations in tuples, (y,x)
#         # need to know whether you are Q or q though.... how?
#         if self.board.bWhite:
#             matchChar = 'Q'
#         else:
#             matchChar = 'q'

#         queenList = []
#         # get uppercase queens
#         for row in xrange(0, len(self.game_board)):
#             for col in xrange(0, len(self.game_board)):
#                 if self.game_board[row][col] == matchChar:
#                     queenList.append((row, col))
#         return queenList


#     def getValidDiags(self, location, search_depth=1):
#         #--> iterate until no longer in bounds or hit an x, or a queen.. anything but a '.'
#         # create our list
#         diagonalsList = []

#         # store the board size, to make code simpler
#         boardSize = len(self.game_board)-1 # subtracting one because we are checking indices

#         # ground the location so we know where we're starting from
#         row = location[0]
#         col = location[1]

#         #--------------------------
#         #   Bottom Left Diagonal
#         #--------------------------
#         # -1 row, -1 col
#         r = row
#         c = col
#         valid = True
#         while valid:
#             # update the row/col values
#             r -= 1
#             c -= 1

#             # protect against out of bounds
#             if r < 0 or c < 0:
#                 break

#             # pull out the value
#             v = self.game_board[r][c]
#             if not v == '.':
#                 break
#             # otherwise, we have a '.', and the cell is valid
#             else:
#                 diagonalsList.append((r, c))

#         #--------------------------
#         #    Top Right Diagonal
#         #--------------------------
#         # +1 row, +1 col
#         r = row
#         c = col
#         valid = True
#         while valid:
#             # update the row/col values
#             r += 1
#             c += 1

#             # protect against out of bounds
#             if r > boardSize or c > boardSize:
#                 break

#             # pull out the value
#             v = self.game_board[r][c]
#             if not v == '.':
#                 break
#             # otherwise, we have a '.', and the cell is valid
#             else:
#                 diagonalsList.append((r, c))

#         #--------------------------
#         #   Bottom Right Diagonal
#         #--------------------------
#         # -1 row, +1 col
#         r = row
#         c = col
#         valid = True
#         while valid:
#             # update the row/col values
#             r -= 1
#             c += 1
#             # protect against out of bounds
#             if r < 0 or c > boardSize:
#                 break

#             # pull out the value
#             v = self.game_board[r][c]
#             if not v == '.':
#                 break
#             # otherwise, we have a '.', and the cell is valid
#             else:
#                 diagonalsList.append((r, c))

#         #--------------------------
#         #    Top Left Diagonal
#         #--------------------------
#         # +1 row, -1 col
#         r = row
#         c = col
#         valid = True
#         while valid:
#             # update the row/col values
#             r += 1
#             c -= 1
#             # protect against out of bounds
#             if r > boardSize or c < 0:
#                 break

#             # pull out the value
#             v = self.game_board[r][c]
#             if not v == '.':
#                 break
#             # otherwise, we have a '.', and the cell is valid
#             else:
#                 diagonalsList.append((r, c))

#         # return the list, now that we're all done
#         return diagonalsList


#     def getValidVerts(self, location):
#         #--> iterate until no longer in bounds or hit an x, or a queen.. anything but a '.'
#         # create our list
#         vertsList = []

#         # store the board size, to make code simpler
#         boardSize = len(self.game_board)-1 # subtracting one because we are checking indices

#         # ground the location so we know where we're starting from
#         row = location[0]
#         col = location[1]

#         #--------------------------
#         #         Top Rows
#         #--------------------------
#         # row+1, col=same
#         r = row
#         c = col
#         valid = True
#         while valid:
#             # update the row/col values
#             r += 1

#             # protect against out of bounds
#             if r > boardSize:
#                 break

#             # pull out the value
#             v = self.game_board[r][c]
#             if not v == '.':
#                 break
#             # otherwise, we have a '.', and the cell is valid
#             else:
#                 vertsList.append((r, c))

#         #--------------------------
#         #        Bottom Rows
#         #--------------------------
#         # row-1, col=same
#         r = row
#         c = col
#         valid = True
#         while valid:
#             # update the row/col values
#             r -= 1

#             # protect against out of bounds
#             if r < 0:
#                 break

#             # pull out the value
#             v = self.game_board[r][c]
#             if not v == '.':
#                 break
#             # otherwise, we have a '.', and the cell is valid
#             else:
#                 vertsList.append((r, c))

#         # return the verticals we've found
#         return vertsList


#     def getValidHorz(self, location):
#         #--> iterate until no longer in bounds or hit an x, or a queen.. anything but a '.'
#         # create our list
#         horzList = []

#         # store the board size, to make code simpler
#         boardSize = len(self.game_board)-1 # subtracting one because we are checking indices

#         # ground the location so we know where we're starting from
#         row = location[0]
#         col = location[1]

#         #--------------------------
#         #       Right Cols
#         #--------------------------
#         # row=same, col+1
#         r = row
#         c = col
#         valid = True
#         while valid:
#             # update the row/col values
#             c += 1

#             # protect against out of bounds
#             if c > boardSize:
#                 break

#             # pull out the value
#             v = self.game_board[r][c]
#             if not v == '.':
#                 break
#             # otherwise, we have a '.', and the cell is valid
#             else:
#                 horzList.append((r, c))

#         #--------------------------
#         #        Left Cols
#         #--------------------------
#         # row=same, col-1
#         r = row
#         c = col
#         valid = True
#         while valid:
#             # update the row/col values
#             c -= 1

#             # protect against out of bounds
#             if c < 0:
#                 break

#             # pull out the value
#             v = self.game_board[r][c]
#             if not v == '.':
#                 break
#             # otherwise, we have a '.', and the cell is valid
#             else:
#                 horzList.append((r, c))

#         # return the verticals we've found
#         return horzList

#     # Location (x,y) -> [ Locations ]
#     def getValidMoves(self, location_tuple):
#         """
#         General method to get all valid 'moves' from some (y,x) coord
#         :param location_tuple: (y,x)
#         :return: a list of location tuples
#         """
#         # given queen location-->OR<--an arrow location, find all valid moves
#         # for all the elements...
#         diags = self.getValidDiags(location_tuple)
#         verts = self.getValidVerts(location_tuple)
#         horz = self.getValidHorz(location_tuple)

#         # concat them all
#         validMoves = diags + verts + horz

#         # build all queen moves from current step
#         # pass in all queen moves and concat on the possible arrow moves to each
#         # that list is the return value
#         return validMoves

#     # [Queen Locations (y,x)] -> [(Location, [All Locations])
#     def getAllFutureQueenLocations(self, queenLocations):
#         """
#         Take the list of current queen locations, and output a list that contains
#         [ (Queen Location Now, [ All Possible Future Locations in next Move) ]
#         @param list of queen locations
#         :return:  List with the queen location and all possible future locations
#         """
#         # (x,y) -> ( (x,y), [(x,y) .... ])
#         future_locations = []

#         # get all valid moves for each queen
#         for elem in queenLocations:
#             # grab the moves
#             validMoves = self.getValidMoves(elem)
#             # then make a tuple containing (cur_location, [future locations])
#             move_tuple = (elem, validMoves)
#             # and add that tuple to our list
#             future_locations.append(move_tuple)


#         # THINK: later we can map the first location of over the future locations
#         #        then same thing with arrow locations but
#         return future_locations

#     # [Queen Location, [All Locations]] -> [Queen Location, [(All Locations, Arrow Show)])
#     def getArrowLocations(self, queen_and_its_moves):
#         """
#         :param queen_and_its_moves: Take a tuple of form:
#                 ((y,x), [dst])
#         :return: [(dst), (arrow_location) ... ]
#                   Everything in form (y,x) coords
#         """
#         # get all the destinations in future locations
#         dst_and_arrow_list = []
#         #for elem in queen_and_its_moves:
#         dest_list = queen_and_its_moves[1]
#         # take each destination, and find all possible arrow locations
#         for dst in dest_list:
#             arrow_shots_list = self.getValidMoves(dst)
#             endpoints = itertools.repeat(dst, len(arrow_shots_list))
#             dst_and_arrow_tuple = zip(endpoints, arrow_shots_list)
#             dst_and_arrow_list.append(dst_and_arrow_tuple)

#         #for elem in dst_and_arrow_list:
#         #    print "DST AND ARROW == " + str(elem)

#         # now, for each dst, all the arrow locations
#         # for elem
#         # index into elem[1], the tuple list of future moves,
#         # and find all future moves from THAT move
#         return dst_and_arrow_list

#     # --> this is like concatting arrow locations with the dest locations
#     # Queen Location (y,x) -> [(src_loc, dst_loc, arrow_loc)]
#     def getAllMovesForQueens(self, future_locations):
#         queens_and_moves = []
#         for elem in future_locations:
#             dst_and_arrows = self.getArrowLocations(elem)
#             queens_and_moves.append((elem[0], dst_and_arrows))

#         # (y,x) -> [ Locations ] ... pull out each location
#         # and for get all arrow locations for each
#         # make a new tuple from the arrow locations.... and concat all those as well
#         return queens_and_moves




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

# class Amazons:
#     def __init__(self, fname):
#         fin = open("C:\\Users\\barak\\Documents\\HaifaUniversity\\AI\\FinalProject\\amazonsconfig.txt", 'r')
#         self.time_limit = int(fin.readline())
#         self.size = int(fin.readline())
#         self.playerW = fin.readline().strip()
#         self.wqs = tuple(map(ld2rc,fin.readline().split()))
#         self.playerB = fin.readline().strip()
#         self.bqs  = tuple(map(ld2rc,fin.readline().split()))
#         self.board = Board(self.size, self.wqs, self.bqs)

#     def update(self, move):
#         try:
#             (src,dst,adst) = move
#         except: return False

#         # try out the move on a temp board        
#         tmp_board = copy.deepcopy(self.board)
#         if tmp_board.valid_path(src,dst):
#             tmp_board.move_queen(src,dst)
#             if tmp_board.valid_path(dst, adst):
#                 # the move is good. make the real board point to it
#                 tmp_board.shoot_arrow(adst)
#                 del self.board
#                 self.board = tmp_board
#                 return True
#         # move failed. 
#         del tmp_board
#         return False

#     def end_turn(self):
#         return self.board.end_turn()

#     def play(self):
#         bPlay = True
#         wscore = bscore = 0
#         while (bPlay):
#             for p in [self.playerW, self.playerB]:
#                 # send player a copy of the current board
#                 tmp_board = copy.deepcopy(self.board)
#                 tstart = time.clock()
#                 tmp_board.time_limit = tstart+self.time_limit
#                 move = eval("%s(tmp_board)"%p)
#                 tstop = time.clock()
#                 del tmp_board

#                 if move:
#                     print p,": move:", [rc2ld(x) for x in move],"time:", tstop-tstart, "seconds"
#                 else: 
#                     print p,"time:", tstop-tstart, "seconds"
#                     # if move == False --> player resigned   
#                     if self.board.bWhite:
#                         (wscore, bscore) = (-1,0)
#                     else: (wscore, bscore) = (0,-1)
#                     bPlay = False
#                     break

#                 # only keep clock for auto players
#                 if p != "human" and (tstop - tstart) > self.time_limit:
#                     print p, ": took too long -- lost a turn"
#                 elif not self.update(move):
#                     print p, ": invalid move", move, " lost a turn"

#                 # at the end of the turn, check whether the game ended
#                 # and update whether white is playing next
#                 (wscore, bscore) = self.end_turn()
#                 if wscore and bscore:
#                     continue
#                 else:
#                     bPlay = False
#                     break
#         # print final board
#         self.board.print_board()
#         if wscore == -1:
#             print self.playerW,"(white) resigned.", self.playerB,"(black) wins"
#         elif bscore == -1:
#             print self.playerB,"(black) resigned.", self.playerW,"(white) wins"
#         elif not wscore:
#             print self.playerB,"(black) wins by a margin of",bscore
#         else: print self.playerW, "(white) wins by a margin of",wscore
                