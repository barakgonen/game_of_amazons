from constants import LARGE_BOARD_SIZE, SMALL_BOARD_SIZE, CellState, COLUMNS_ARRAY, NUMBER_OF_ROCKS_IN_SMALL_BOARD, NUMBER_OF_ROCKS_IN_LARGE_BOARD
from board_game import BoardGame
from turn_validator import TurnValidator
from point import Point
from blocking_rocks_manager import BlockingRocksManager
from player import ComputerPlayer, HumanPlayer
from game_manager import GameManager
import unittest

def run_simple_test(amazon_to_move, new_position, expected_result, board_size):
    board_game = BoardGame(board_size)
    turn_validator = TurnValidator(board_game)
    return expected_result == turn_validator.is_step_valid(amazon_to_move, new_position)

def get_blocked_board(amazon_to_move, new_position, board_size, amazon_color, blocked_cells):
    board_game = BoardGame(board_size)
    board_game.update_move(amazon_to_move, new_position, amazon_color)
    for target in blocked_cells:
        board_game.shoot_blocking_rock(target)
    return board_game

def get_initialized_board(board_size, blocked_cells):
    board_game = BoardGame(board_size)
    for target in blocked_cells:
        board_game.shoot_blocking_rock(target)
    return board_game

def run_simple_test_with_prepared_board(amazon_to_move, new_position, expected_result, board):
    turn_validator = TurnValidator(board)
    return expected_result == turn_validator.is_step_valid(amazon_to_move, new_position)

def run_loop_of_simple_movement_tests(amazon_to_move, position_lst, expected_result, board):
    result = True
    for pos in position_lst:
        if result == expected_result:
            result = run_simple_test_with_prepared_board(amazon_to_move, pos, expected_result, board)
        else:
            break
    return result

def set_full_blocked_board(board):
    for i in range(1, board.get_size() + 1):
        for j in range(1, board.get_size() + 1):
            if board.is_free_cell(i, COLUMNS_ARRAY[j]):
                board.shoot_blocking_rock(Point(COLUMNS_ARRAY[j], i))

def set_board_blocked_by_list(board, blocking_lst):
    for point in blocking_lst:
        board.shoot_blocking_rock(point)

def turns_possible_job():
    # Test cases
    # 0 turns possible with full board
    current_board = BoardGame(LARGE_BOARD_SIZE)
    set_full_blocked_board(current_board)
    turn_validator = TurnValidator(current_board)
    is_game_over = not(turn_validator.is_there_are_available_mooves_for_player(CellState.WHITE_AMAZON) and turn_validator.is_there_are_available_mooves_for_player(CellState.BLACK_AMAZON))

    if (not is_game_over):
        raise RuntimeError("Error with case 44")
    
    # 0 turns possible with small board
    current_board = BoardGame(SMALL_BOARD_SIZE)
    set_full_blocked_board(current_board)
    turn_validator = TurnValidator(current_board)
    is_game_over = not(turn_validator.is_there_are_available_mooves_for_player(CellState.WHITE_AMAZON) and turn_validator.is_there_are_available_mooves_for_player(CellState.BLACK_AMAZON))

    if (not is_game_over):
        raise RuntimeError("Error with case 44")

    # more than 0 possible whithout rocks
    current_board = BoardGame(SMALL_BOARD_SIZE)
    blocking_manager = BlockingRocksManager(current_board.get_size())
    for i in range(0, NUMBER_OF_ROCKS_IN_SMALL_BOARD + 1):
        blocking_manager.get_rock()
    if (blocking_manager.are_blocks_available()):
        raise RuntimeError("Error with case 45")

    current_board = BoardGame(LARGE_BOARD_SIZE)
    blocking_manager = BlockingRocksManager(current_board.get_size())
    for i in range(0, NUMBER_OF_ROCKS_IN_LARGE_BOARD + 1):
        blocking_manager.get_rock()
    if (blocking_manager.are_blocks_available()):
        raise RuntimeError("Error with case 45")

    # new case. using game manager to see that it knows to decide wethere game can run: available mooves or rocks
    board_game = BoardGame(SMALL_BOARD_SIZE)
    blocking_rocks_manager = BlockingRocksManager(board_game.get_size())
    set_full_blocked_board(board_game)
    p1 = HumanPlayer("BARAK", CellState.WHITE_AMAZON)
    p2 = ComputerPlayer("ALGORITHM", CellState.BLACK_AMAZON)
    turn_validator = TurnValidator(board_game)
    game_manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
    # in case there are no available mooves
    if (game_manager.is_there_reason_to_play(p1.get_color()) or game_manager.is_there_reason_to_play(p2.get_color())):
        raise RuntimeError("Error with test case 46")
    
    for i in range(0, NUMBER_OF_ROCKS_IN_SMALL_BOARD + 1):
        blocking_rocks_manager.get_rock()
    # in case there are no rocks and no available mooves
    if (game_manager.is_there_reason_to_play(p1.get_color()) or game_manager.is_there_reason_to_play(p2.get_color())):
        raise RuntimeError("Error with test case 47")

    # small board tests
    # 0 turns possible for black - available only 1 cell horizontaly
    board_game = BoardGame(SMALL_BOARD_SIZE)
    turn_validator = TurnValidator(board_game)
    blocking_lst = [Point('A', 6), Point('A', 5), Point('A', 3), Point('A', 2), Point('A', 1),
                    Point('B', 6), Point('B', 5), Point('B', 4), Point('B', 3), Point('B', 2), Point('B', 1),
                    Point('C', 6), Point('C', 5), Point('C', 3), Point('C', 2), 
                    Point('D', 5), Point('D', 4), Point('D', 3), Point('D', 2), Point('D', 1),
                    Point('E', 6), Point('e', 5), Point('E', 4), Point('E', 3), Point('E', 2), Point('E', 1),
                    Point('F', 6), Point('F', 5), Point('F', 4), Point('F', 2), Point('F', 1)]

    set_board_blocked_by_list(board_game, blocking_lst)
    p1 = HumanPlayer("BARAK", CellState.WHITE_AMAZON)
    p2 = ComputerPlayer("ALGORITHM", CellState.BLACK_AMAZON)
    turn_validator = TurnValidator(board_game)
    blocking_rocks_manager = BlockingRocksManager(board_game.get_size())
    game_manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
    # in case there are no available mooves
    if (game_manager.is_there_reason_to_play(p1.get_color()) or game_manager.is_there_reason_to_play(p2.get_color())):
        raise RuntimeError("Error with test case 48")

    # 0 turns possible for white - available only 1 cell verticaly but in a distance, means its blocked
    board_game = BoardGame(SMALL_BOARD_SIZE)
    turn_validator = TurnValidator(board_game)
    blocking_lst = [Point('A', 5), Point('A', 3), Point('A', 2), Point('A', 1),
                    Point('B', 6), Point('B', 5), Point('B', 4), Point('B', 3), Point('B', 2), Point('B', 1),
                    Point('C', 6), Point('C', 5), Point('C', 3), Point('C', 2), 
                    Point('D', 5), Point('D', 4), Point('D', 3), Point('D', 2), Point('D', 1),
                    Point('E', 6), Point('e', 5), Point('E', 4), Point('E', 3), Point('E', 2), Point('E', 1),
                    Point('F', 6), Point('F', 5), Point('F', 4), Point('F', 2), Point('F', 1)]

    set_board_blocked_by_list(board_game, blocking_lst)
    p1 = HumanPlayer("BARAK", CellState.WHITE_AMAZON)
    p2 = ComputerPlayer("ALGORITHM", CellState.BLACK_AMAZON)
    turn_validator = TurnValidator(board_game)
    blocking_rocks_manager = BlockingRocksManager(board_game.get_size())
    game_manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
    # in case there are no available mooves
    if (game_manager.is_there_reason_to_play(p1.get_color()) or game_manager.is_there_reason_to_play(p2.get_color())):
        raise RuntimeError("Error with test case 48")
    # 0 turns possible for black - available only 1 cell diagonaly but in a distance, means its blocked
     
    # 1 turn possible for black horizontly
    board_game = BoardGame(SMALL_BOARD_SIZE)
    turn_validator = TurnValidator(board_game)
    blocking_lst = [Point('A', 6), Point('A', 5), Point('A', 3), Point('A', 2), Point('A', 1),
                    Point('B', 6), Point('B', 5), Point('B', 3), Point('B', 2), Point('B', 1),
                    Point('C', 6), Point('C', 5), Point('C', 4), Point('C', 3), Point('C', 2), 
                    Point('D', 5), Point('D', 4), Point('D', 3), Point('D', 2), Point('D', 1),
                    Point('E', 6), Point('e', 5), Point('E', 4), Point('E', 3), Point('E', 2), Point('E', 1),
                    Point('F', 6), Point('F', 5), Point('F', 4), Point('F', 2), Point('F', 1)]

    set_board_blocked_by_list(board_game, blocking_lst)
    p1 = HumanPlayer("BARAK", CellState.WHITE_AMAZON)
    p2 = ComputerPlayer("ALGORITHM", CellState.BLACK_AMAZON)
    turn_validator = TurnValidator(board_game)
    blocking_rocks_manager = BlockingRocksManager(board_game.get_size())
    game_manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
    # in case there are no available mooves
    if (game_manager.is_there_reason_to_play(p1.get_color()) or not game_manager.is_there_reason_to_play(p2.get_color())):
        raise RuntimeError("Error with test case 47")
    
    # 1 turn possible for white verticly (up)
    board_game = BoardGame(SMALL_BOARD_SIZE)
    turn_validator = TurnValidator(board_game)
    blocking_lst = [Point('A', 6), Point('A', 5), Point('A', 3), Point('A', 2), Point('A', 1),
                    Point('B', 6), Point('B', 5), Point('B', 3), Point('B', 4), Point('B', 2), Point('B', 1),
                    Point('C', 6), Point('C', 5), Point('C', 4), Point('C', 3),
                    Point('D', 5), Point('D', 4), Point('D', 3), Point('D', 2), Point('D', 1),
                    Point('E', 6), Point('e', 5), Point('E', 4), Point('E', 3), Point('E', 2), Point('E', 1),
                    Point('F', 6), Point('F', 5), Point('F', 4), Point('F', 2), Point('F', 1)]

    set_board_blocked_by_list(board_game, blocking_lst)
    p1 = HumanPlayer("BARAK", CellState.WHITE_AMAZON)
    p2 = ComputerPlayer("ALGORITHM", CellState.BLACK_AMAZON)
    turn_validator = TurnValidator(board_game)
    blocking_rocks_manager = BlockingRocksManager(board_game.get_size())
    game_manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
    # in case there are no available mooves
    if (not game_manager.is_there_reason_to_play(p1.get_color()) or game_manager.is_there_reason_to_play(p2.get_color())):
        raise RuntimeError("Error with test case 48")

    # 2 turns possible for black
    board_game = BoardGame(SMALL_BOARD_SIZE)
    turn_validator = TurnValidator(board_game)
    blocking_lst = [Point('A', 6), Point('A', 5), Point('A', 3), Point('A', 2), Point('A', 1),
                    Point('B', 6), Point('B', 5), Point('B', 3), Point('B', 2),
                    Point('C', 6), Point('C', 5), Point('C', 4), Point('C', 3), Point('C', 2),
                    Point('D', 5), Point('D', 4), Point('D', 3), Point('D', 2),
                    Point('E', 6), Point('e', 5), Point('E', 4), Point('E', 3), Point('E', 2), Point('E', 1),
                    Point('F', 6), Point('F', 5), Point('F', 2), Point('F', 1)]

    set_board_blocked_by_list(board_game, blocking_lst)
    p1 = HumanPlayer("BARAK", CellState.WHITE_AMAZON)
    p2 = ComputerPlayer("ALGORITHM", CellState.BLACK_AMAZON)
    turn_validator = TurnValidator(board_game)
    blocking_rocks_manager = BlockingRocksManager(board_game.get_size())
    game_manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
    # in case there are no available mooves
    if (game_manager.is_there_reason_to_play(p1.get_color()) and (not game_manager.is_there_reason_to_play(p2.get_color()))):
        raise RuntimeError("Error with test case 49")

    # 2 turns possible for white
    board_game = BoardGame(SMALL_BOARD_SIZE)
    turn_validator = TurnValidator(board_game)
    blocking_lst = [Point('A', 6), Point('A', 5), Point('A', 3), Point('A', 2), Point('A', 1),
                    Point('B', 6), Point('B', 5), Point('B', 4), Point('B', 3), Point('B', 2),
                    Point('C', 6), Point('C', 5), Point('C', 4), Point('C', 3), Point('C', 2),
                    Point('D', 5), Point('D', 4), Point('D', 3), Point('D', 2),
                    Point('E', 6), Point('e', 5), Point('E', 4), Point('E', 3), Point('E', 2), Point('E', 1),
                    Point('F', 6), Point('F', 5), Point('F', 4), Point('F', 2), Point('F', 1)]

    set_board_blocked_by_list(board_game, blocking_lst)
    p1 = HumanPlayer("BARAK", CellState.WHITE_AMAZON)
    p2 = ComputerPlayer("ALGORITHM", CellState.BLACK_AMAZON)
    turn_validator = TurnValidator(board_game)
    blocking_rocks_manager = BlockingRocksManager(board_game.get_size())
    game_manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)

    # in case there are no available mooves
    if (not game_manager.is_there_reason_to_play(p1.get_color()) and game_manager.is_there_reason_to_play(p2.get_color())):
        raise RuntimeError("Error with test case 49")

    # 10 turns possible for black
    board_game = BoardGame(SMALL_BOARD_SIZE)
    turn_validator = TurnValidator(board_game)
    blocking_lst = [Point('A', 6), Point('A', 5), Point('A', 3), Point('A', 2), Point('A', 1),
                    Point('B', 6)               , Point('B', 3), Point('B', 2), Point('B', 1),
                                   Point('C', 5), Point('C', 3), Point('C', 2),
                                                  Point('D', 3), Point('D', 2), Point('D', 1),
                    Point('E', 6), Point('e', 5),                Point('E', 2), Point('E', 1),
                    Point('F', 6), Point('F', 5),                               Point('F', 1)]

    set_board_blocked_by_list(board_game, blocking_lst)
    p1 = HumanPlayer("BARAK", CellState.WHITE_AMAZON)
    p2 = ComputerPlayer("ALGORITHM", CellState.BLACK_AMAZON)
    turn_validator = TurnValidator(board_game)
    blocking_rocks_manager = BlockingRocksManager(board_game.get_size())
    game_manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
    # in case there are no available mooves
    if (game_manager.is_there_reason_to_play(p1.get_color()) and (not game_manager.is_there_reason_to_play(p2.get_color()))):
        raise RuntimeError("Error with test case 50")

    # large board tests TBD do i need it?
    # 1 turn possible for black
    # 1 turn possible for white
    # 2 turns possible for black
    # 2 turns possible for white
    # 10 turns possible for black
    # 10 turns possible for white

    return True

def winner_selector_job():
    # once the game is over: no more rocks OR no more possible moves for player, need to decide who is the winner
    # by counting number of possible moves
    # set board, set positions, make move and calculate 
    # Test cases need to verify in each board that the game is over (no more possible turns or no more rocks)
    # Black should win
    # white should win
    # need to pay attention there are no doubling, think about case you can go 3 right. it means you have 3 options: 1 right, 2 right, 3 right NOT ONLY 1

    # running test case according to wikipedia
    board_game = BoardGame(LARGE_BOARD_SIZE)
    turn_validator = TurnValidator(board_game)
    blocking_lst = [Point('A', 10),                Point('A', 8),                                                             Point('A', 3), Point('A', 2),
                                    Point('B', 9), Point('B', 8),                               Point('B', 5), Point('B', 4), Point('B', 3), Point('B', 2), 
                                    Point('C', 9),                Point('C', 7), Point('C', 6), Point('C', 5), Point('C', 4),                               Point('C', 1),
                                    Point('D', 9), Point('D', 8), Point('D', 7),                Point('D', 5),                Point('D', 3), Point('D', 2),
                    Point('E', 10),                Point('E', 8), Point('E', 7), Point('E', 6),                               Point('E', 3),                Point('E', 1),
                                    Point('F', 9), Point('F', 8),                Point('F', 6), Point('F', 5), Point('F', 4), Point('F', 3), Point('F', 2), Point('F', 1),
                                                   Point('G', 8),                Point('G', 6),                Point('G', 4), Point('G', 3), Point('G', 2), 
                    Point('H', 10),                Point('H', 8),                Point('H', 6), Point('H', 5),                Point('H', 3), 
                                    Point('I', 9), Point('I', 8), Point('I', 7), Point('I', 6), 
                                                   Point('J', 8),                Point('J', 6),                                                             Point('J', 1)]
    # need to move white from D/1 to D/7
    board_game.update_move(Point('D', 1), Point('D', 7), "WHITE")
    # need to move black from J/7 to D/1
    board_game.update_move(Point('J', 7), Point('D', 1), "BLACK")
    # need to move white from J/6 to J/7
    board_game.update_move(Point('J', 4), Point('J', 7), "WHITE")
    # need to move black from A/7 to D/4
    board_game.update_move(Point('A', 7), Point('D', 4), "BLACK")
    # need to move white from G/1 to G/2
    board_game.update_move(Point('G', 1), Point('G', 2), "WHITE")
    # need to move black from G/10 to G/1
    board_game.update_move(Point('G', 10), Point('G', 1), "BLACK")
    # need to move white from G/2to E/2
    board_game.update_move(Point('G', 2), Point('E', 2), "WHITE")
    # need to move black from D/4 to E/5
    board_game.update_move(Point('D', 4), Point('E', 5), "BLACK")
    # need to move white from A/4 to A/6
    board_game.update_move(Point('A', 4), Point('A', 6), "WHITE")
    # need to move white from A/6 to C/8
    board_game.update_move(Point('A', 6), Point('C', 8), "WHITE")
    # need to move white from D/7 to F/7
    board_game.update_move(Point('D', 7), Point('F', 7), "WHITE")

    set_board_blocked_by_list(board_game, blocking_lst)
    p1 = HumanPlayer("BARAK", CellState.WHITE_AMAZON)
    p2 = ComputerPlayer("ALGORITHM", CellState.BLACK_AMAZON)
    turn_validator = TurnValidator(board_game)
    blocking_rocks_manager = BlockingRocksManager(board_game.get_size())
    game_manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
    # in case there are no available mooves
    if (game_manager.is_there_reason_to_play(p1.get_color()) and (not game_manager.is_there_reason_to_play(p2.get_color()))):
        raise RuntimeError("Error with test case 50")

    expected_possible_moves_for_white = board_game.get_white_available_mooves()
    expected_possible_moves_for_black = board_game.get_black_available_mooves()
    if (not expected_possible_moves_for_white == 8):
        raise RuntimeError("Error with test case 51")

    if (not expected_possible_moves_for_black == 31):
        raise RuntimeError("Error with test case 52")
    
    
    
    return True



    # blocking_lst = [Point('A', 10), Point('A', 9), Point('A', 8), Point('A', 7), Point('A', 6), Point('A', 5), Point('A', 3), Point('A', 2), Point('A', 1),
    #                 Point('B', 10), Point('B', 9), Point('B', 8), Point('B', 7), Point('B', 6), Point('B', 5), Point('B', 3), Point('B', 2), Point('B', 1),
    #                 Point('C', 10), Point('C', 9), Point('C', 8), Point('C', 7), Point('C', 6), Point('C', 5), Point('C', 3), Point('C', 2), Point('C', 1),
    #                 Point('D', 10), Point('D', 9), Point('D', 8), Point('D', 7), Point('D', 6), Point('D', 5), Point('D', 3), Point('D', 2), Point('D', 1),
    #                 Point('E', 10), Point('E', 9), Point('E', 8), Point('E', 7), Point('E', 6), Point('E', 5), Point('E', 3), Point('E', 2), Point('E', 1),
    #                 Point('F', 10), Point('F', 9), Point('F', 8), Point('F', 7), Point('F', 6), Point('F', 5), Point('F', 3), Point('F', 2), Point('F', 1),
    #                 Point('G', 10), Point('G', 9), Point('G', 8), Point('G', 7), Point('G', 6), Point('G', 5), Point('G', 3), Point('G', 2), Point('G', 1),
    #                 Point('H', 10), Point('H', 9), Point('H', 8), Point('H', 7), Point('H', 6), Point('H', 5), Point('H', 3), Point('H', 2), Point('H', 1),
    #                 Point('I', 10), Point('I', 9), Point('I', 8), Point('I', 7), Point('I', 6), Point('I', 5), Point('I', 3), Point('I', 2), Point('I', 1),
    #                 Point('J', 10), Point('J', 9), Point('J', 8), Point('J', 7), Point('J', 6), Point('J', 5), Point('J', 4), Point('J', 3), Point('J', 2), Point('J', 1)]

class TestSmallBoardBasicMovement(unittest.TestCase):
    def run_simple_test(self, amazon_to_move, new_position):
        board_game = BoardGame(SMALL_BOARD_SIZE)
        turn_validator = TurnValidator(board_game)
        return turn_validator.is_step_valid(amazon_to_move, new_position)

    def test_moving_horizontaly_to_the_left_one_step_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('C', 6)))
        self.assertTrue(self.run_simple_test(Point('F', 3), Point('E', 3)))
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('B', 1)))

    def test_moving_horizaontaly_to_the_left_2_steps(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('B', 6)))
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('A', 1)))
        
    def test_moving_horizontaly_to_the_left_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('a', 6)))
        self.assertTrue(self.run_simple_test(Point('F', 3), Point('C', 3)))

    def test_moving_horizaontaly_to_the_left_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('F', 3), Point('@', 3)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('@', 1)))

    def test_moving_horizontaly_to_the_right_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('E', 6)))
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('D', 1)))
    
    def test_moving_horizaontaly_to_the_right_2_steps(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('F', 6)))
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('E', 1)))     

    def test_moving_horizaontaly_to_the_right_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('G', 6)))
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('h', 6)))
        self.assertFalse(self.run_simple_test(Point('F', 3), Point('G', 3)))
        self.assertFalse(self.run_simple_test(Point('F', 3), Point('G', 3)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('G', 1)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('K', 1)))
    
    def test_moving_verticly_up_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('D', 7)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('C', 11)))

    def test_moving_verticly_down_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('D', 5)))
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('D', 4)))
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('D', 3)))
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('D', 2)))
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('D', 1)))
        self.assertTrue(self.run_simple_test(Point('F', 3), Point('F', 2)))
        self.assertTrue(self.run_simple_test(Point('F', 3), Point('F', 1)))

    def test_moving_verticly_down_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('D', -1)))
        self.assertFalse(self.run_simple_test(Point('f', 3), Point('F', -1)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('C', -1)))

    def test_moving_verticly_up_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('C', 2)))
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('C', 3)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('C', 7)))
    
    def test_moving_verticly_up_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('C', 7)))
        self.assertFalse(self.run_simple_test(Point('A', 4), Point('A', 17)))
    
    def test_moving_diagonaly_up_right_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('E', 7)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('G', 5)))

    def test_moving_diagonaly_down_right_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('A', 4), Point('E', -1)))
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('H', 2)))
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('H', 5)))
        self.assertFalse(self.run_simple_test(Point('F', 3), Point('G', 2)))
        self.assertFalse(self.run_simple_test(Point('F', 3), Point('H', 2)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('D', -1)))
    
    def test_moving_diagonaly_up_right_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('F', 3), Point('C', 6)))
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('D', 2)))

    def test_moving_diagonaly_up_right_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('F', 3), Point('G', 4)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('E', 2)))
    
    def test_moving_diagonaly_up_left_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('F', 3), Point('E', 4)))
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('B', 2)))
    
    def test_moving_diagonaly_up_left_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('B', 3)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('B', 5)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('@', 4)))
        self.assertFalse(self.run_simple_test(Point('C', 1), Point('A', 2)))
    
    def test_moving_diagonaly_down_right_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('E', 5)))
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('F', 4)))

    def test_moving_diagonaly_down_right_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('E', 3)))
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('E', 4)))
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('F', 5)))
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('F', 3)))

    def test_moving_diagonaly_down_left_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('c', 5)))
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('b', 4)))
        self.assertTrue(self.run_simple_test(Point('F', 3), Point('D', 1)))

    def test_moving_diagonaly_down_left_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('A', 4)))
        self.assertFalse(self.run_simple_test(Point('D', 6), Point('B', 5)))
        self.assertFalse(self.run_simple_test(Point('F', 3), Point('E', 1)))
        self.assertFalse(self.run_simple_test(Point('F', 3), Point('D', 2))) 

class TestLargeBoardBasicMovement(unittest.TestCase):
    def run_simple_test(self, amazon_to_move, new_position):
        board_game = BoardGame(LARGE_BOARD_SIZE)
        turn_validator = TurnValidator(board_game)
        return turn_validator.is_step_valid(amazon_to_move, new_position)

    def test_moving_horizontaly_to_the_left_one_step_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('J', 7), Point('I', 7)))
        self.assertTrue(self.run_simple_test(Point('G', 10), Point('F', 10)))

    def test_moving_horizaontaly_to_the_left_2_steps(self):
        self.assertTrue(self.run_simple_test(Point('G', 1), Point('E', 1)))
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('C', 10)))
        
    def test_moving_horizontaly_to_the_left_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('A', 10)))
        self.assertTrue(self.run_simple_test(Point('G', 1), Point('F', 1)))
    
    def test_moving_horizontaly_to_the_left_to_non_empty_cell(self):
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('D', 1)))
        self.assertFalse(self.run_simple_test(Point('G', 10), Point('D', 10)))

    def test_moving_horizaontaly_to_the_left_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 10), Point('@', 10)))
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('@', 1)))

    def test_moving_horizontaly_to_the_right_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('E', 10)))
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('F', 10)))
    
    def test_moving_horizaontaly_to_the_right_2_steps(self):
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('F', 10)))
        self.assertTrue(self.run_simple_test(Point('A', 4), Point('C', 4)))

    def test_moving_horizaontaly_to_the_right_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 10), Point('K', 10)))
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('K', 1)))

    def test_moving_verticly_up_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('A', 4), Point('A', 112212)))
        self.assertFalse(self.run_simple_test(Point('G', 10), Point('A', 112)))
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('G', 10)))
        self.assertFalse(self.run_simple_test(Point('D', 1), Point('D', 10)))

    def test_moving_verticly_up_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('G', 1), Point('G', 2)))
        self.assertTrue(self.run_simple_test(Point('G', 1), Point('G', 9)))

    def test_moving_verticly_down_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('D', 2)))
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('D', 8)))
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('D', 9)))

    def test_moving_verticly_down_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 10), Point('D', -1)))
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('G', -1)))

    def test_moving_verticly_down_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 10), Point('D', 1)))
        self.assertFalse(self.run_simple_test(Point('G', 10), Point('G', 1)))
    
    def test_moving_verticly_up_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 10), Point('d', 11)))
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('G', 11)))
    
    def test_moving_diagonaly_up_right_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('J', 7), Point('K', 8)))
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('L', 8)))

    def test_moving_diagonaly_down_right_to_non_existing_cell(self):
        self.assertFalse(self.run_simple_test(Point('A', 7), Point('I', -2)))
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('H', -1)))

    def test_moving_diagonaly_up_right_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('d', 1), Point('h', 5)))
        self.assertTrue(self.run_simple_test(Point('G', 1), Point('I', 3)))

    def test_moving_diagonaly_up_right_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('I', 2)))
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('H', 3)))

    def test_moving_diagonaly_up_left_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('G', 1), Point('B', 6)))
        self.assertTrue(self.run_simple_test(Point('D', 1), Point('B', 3)))

    def test_moving_diagonaly_up_left_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('G', 1), Point('B', 7)))
        self.assertFalse(self.run_simple_test(Point('J', 7), Point('G', 10)))

    def test_moving_diagonaly_down_right_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('I', 5)))
        self.assertTrue(self.run_simple_test(Point('G', 10), Point('I', 8)))

    def test_moving_diagonaly_down_right_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('G', 10), Point('J', 7)))
        self.assertFalse(self.run_simple_test(Point('G', 10), Point('J', 8)))

    def test_moving_diagonaly_down_left_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 10), Point('B', 8)))
        self.assertTrue(self.run_simple_test(Point('J', 7), Point('E', 2)))

    def test_moving_diagonaly_down_left_to_invalid_cell(self):
        self.assertFalse(self.run_simple_test(Point('D', 10), Point('B', 9)))
        self.assertFalse(self.run_simple_test(Point('D', 10), Point('A', 7)))


class TestBlockingCellsValidationProcess(unittest.TestCase):
    def run_simple_test(self, amazon_to_move, new_position):
        board_game = BoardGame(LARGE_BOARD_SIZE)
        turn_validator = TurnValidator(board_game)
        return turn_validator.is_step_valid(amazon_to_move, new_position)

    def get_blocked_board(self, blocked_cells):
        board_game = BoardGame(SMALL_BOARD_SIZE)
        for target in blocked_cells:
            board_game.shoot_blocking_rock(target)
        return board_game

    def run_loop_of_simple_movement_tests(self, amazon_to_move, position_lst, expected_result, board):
        result = expected_result
        for pos in position_lst:
            if result == expected_result:
                    turn_validator = TurnValidator(board)
                    result = turn_validator.is_step_valid(amazon_to_move, pos)
            else:
                break
        return result

    def test_blocked_white_amazon_couldnt_reach_blocked_cells(self):
        blocking_lst = [Point('B', 3), Point('B', 2), Point('B', 1), 
                            Point('D', 1), Point('D', 2), Point('D', 3), Point('C', 3)]
    
        # Getting blocked board
        test_board = self.get_blocked_board(blocking_lst)

        # Moving amazon to the new pos
        test_board.update_move(Point('C', 1), Point('C', 2), "WHITE")

        additional_blocking_lst = [Point('A', 1), Point('A', 2), Point('A', 3), Point('A', 4), Point('A', 5), Point('A', 6),  
                                                                                Point('B', 4), Point('B', 5), Point('B', 6),
                                                                                Point('C', 4), Point('C', 5), Point('C', 6),
                                                                                Point('D', 4), Point('D', 5), Point('D', 6),
                                   Point('E', 1), Point('e', 2), Point('E', 3), Point('e', 4), Point('E', 5), Point('E', 6),
                                   Point('F', 1), Point('F', 2), Point('F', 3), Point('F', 4), Point('F', 5), Point('F', 6)]
        # Appending lists for test
        blocking_lst.extend(additional_blocking_lst)

        self.assertFalse(self.run_loop_of_simple_movement_tests(Point('C', 2), blocking_lst, False, test_board))

    def test_blocked_white_amazon_could_reach_just_to_unblocked_cells(self):
        blocking_lst = [Point('B', 3), Point('B', 2), Point('B', 1), 
                            Point('D', 1), Point('D', 2), Point('D', 3), Point('C', 3)]
    
        # Getting blocked board
        test_board = self.get_blocked_board(blocking_lst)

        # Moving amazon to the new pos
        test_board.update_move(Point('C', 1), Point('C', 2), "WHITE")

        self.assertTrue(self.run_loop_of_simple_movement_tests(Point('C', 2), [Point('C', 1)], True, test_board))   

    def test_blocked_black_amazon_couldnt_reach_blocked_cells(self):
        blocking_lst = [Point('B', 3), Point('B', 2), Point('B', 1), 
                            Point('D', 1), Point('D', 2), Point('D', 3), Point('C', 3)]
    
        # Getting blocked board
        test_board = self.get_blocked_board(blocking_lst)

        # Moving amazon to the new pos
        test_board.update_move(Point('d', 6), Point('d', 3), "BLACK")

        additional_blocking_lst = [Point('A', 1), Point('A', 2), Point('A', 3), Point('A', 4), Point('A', 5), Point('A', 6),  
                                                                                Point('B', 4), Point('B', 5), Point('B', 6),
                                                                                Point('C', 4), Point('C', 5), Point('C', 6),
                                                                                Point('D', 4), Point('D', 5), Point('D', 6),
                                   Point('E', 1), Point('e', 2), Point('E', 3), Point('e', 4), Point('E', 5), Point('E', 6),
                                   Point('F', 1), Point('F', 2), Point('F', 3), Point('F', 4), Point('F', 5), Point('F', 6)]
        # Appending lists for test
        blocking_lst.extend(additional_blocking_lst)
        self.assertFalse(self.run_loop_of_simple_movement_tests(Point('C', 2), blocking_lst, False, test_board))

    def test_cant_reach_blocked_cells_after_movement(self):
        # Getting blocked board
        test_board = BoardGame(SMALL_BOARD_SIZE)

        # Moving amazon to the new pos
        test_board.update_move(Point('d', 6), Point('c', 5), "WHITE")

        # shoot block rock after movment
        test_board.shoot_blocking_rock(Point('e', 3))

        # adding unavailable targets as well
        unavailable_moves =   [
                    Point('A', 6), Point('A', 4), Point('A', 2), Point('A', 1),
                    Point('B', 3), Point('B', 2), Point('B', 1),
                    Point('C', 1), Point('C', 5), 
                    Point('D', 3), Point('D', 2), Point('D', 1),
                    Point('E', 6), Point('E', 4), Point('E', 3), Point('E', 2), Point('E', 1),
                    Point('F', 6), Point('F', 4), Point('F', 3), Point('F', 2), Point('F', 1)]
                    
        available_moves =  [
                    Point('A', 5), Point('A', 3),
                    Point('B', 6), Point('B', 5), Point('B', 4), 
                    Point('C', 6), Point('c', 4), Point('C', 3), Point('C', 2), 
                    Point('D', 6), Point('D', 5), Point('D', 4),
                    Point('E', 5),
                    Point('F', 5)]

        test_board.print_board()

        self.assertFalse(self.run_loop_of_simple_movement_tests(Point('c', 5), unavailable_moves, False, test_board))
        self.assertTrue(self.run_loop_of_simple_movement_tests(Point('c', 5), available_moves, True, test_board))


# unavailable_moves =   [
#                     Point('A', 6), Point('A', 5), Point('A', 3), Point('A', 2), Point('A', 1),
#                     Point('B', 6), Point('B', 5), Point('B', 3), Point('B', 2), Point('B', 1),
#                     Point('C', 6), Point('C', 5), Point('C', 3), Point('C', 2), Point('C', 1),
#                     Point('D', 6), Point('D', 5), Point('D', 3), Point('D', 2), Point('D', 1),
#                     Point('E', 6), Point('E', 5), Point('E', 3), Point('E', 2), Point('E', 1),
#                     Point('F', 6), Point('F', 5), Point('F', 3), Point('F', 2), Point('F', 1),
#                     Point('G', 6), Point('G', 5), Point('G', 3), Point('G', 2), Point('G', 1)]
class TestShootingBlockerAtTheEndOfTheTurn(unittest.TestCase):
    def run_simple_test(self, amazon_to_move, new_position):
        board_game = BoardGame(LARGE_BOARD_SIZE)
        turn_validator = TurnValidator(board_game)
        return turn_validator.is_step_valid(amazon_to_move, new_position)
    
    def get_blocked_board(self, blocked_cells):
        board_game = BoardGame(SMALL_BOARD_SIZE)
        for target in blocked_cells:
            board_game.shoot_blocking_rock(target)
        return board_game

# # new test case
#     # testing turn starting with white amazon at 'C'/1
#     static_start_pos = Point('C', 1)
    
#     # moving the amazon verticly to 'C'/3
#     new_position = Point('C', 3)

#     # When the amazon will arive 'C'/3 it will shoot blocking rock to 'C'/4
#     blocking_lst = [Point('C', 4)]

#     #rest of the board, for extra verification
#     test_board = get_blocked_board(static_start_pos, new_position, SMALL_BOARD_SIZE, "WHITE", blocking_lst)

#     # i'd like to test invalid_movement mechanisem, that why i take 2 possible celss and tests that in the next move, the amazon couldn't reach them
#     unavailable_cells = [Point('C', 5), Point('C', 6)]
#     # Appending lists for test, amazon could not pass above blocked cell & the cells i mentioned above
#     blocking_lst.extend(unavailable_cells)

#     # after getting board prepared, need to run the tests on it
#     is_test_fine = run_loop_of_simple_movement_tests(new_position, blocking_lst, False, test_board)
#     if (not is_test_fine):
#         raise RuntimeError("Error With case 2")

#     # adding unavailable targets as well
#     additional_unavailable_targets = [Point('A', 2), Point('A', 4), Point('A', 6),  
#                                       Point('B', 1), Point('B', 5), Point('B', 6),
#                                       Point('C', 3), Point('C', 4), Point('C', 5), Point('C', 6),
#                                       Point('D', 1), Point('D', 5), Point('D', 6),
#                                       Point('E', 2), Point('e', 4), Point('E', 6),
#                                       Point('F', 1), Point('F', 2), Point('F', 3), Point('F', 4), Point('F', 5)]
#     available_moves = [Point('A', 5), Point('A', 3), Point('A', 1),
#                        Point('B', 4), Point('B', 3), Point('B', 2), 
#                        Point('C', 2), Point('C', 1), 
#                        Point('D', 4), Point('D', 3), Point('D', 2), 
#                        Point('e', 1), Point('E', 3), Point('E', 5), 
#                        Point('F', 6)]
#     is_additional_unavailable_moves_are_unavailable = run_loop_of_simple_movement_tests(new_position, additional_unavailable_targets, False, test_board)
#     if (not is_additional_unavailable_moves_are_unavailable):
#         raise RuntimeError("Error with case 3")
#     number_of_passed_tests += 1
#     is_additional_available_moves_are_available = run_loop_of_simple_movement_tests(new_position, available_moves, True, test_board)
#     if (not is_additional_available_moves_are_available):
#         raise RuntimeError("Error with case 4")
#     number_of_passed_tests += 1
# #end testcase

#     # testing turn starting with black amazon at 'F'/3
#     static_start_pos = Point('F', 3)
    
#     # moving the amazon diagonaly to 'D'/5
#     new_position = Point('D', 5)

#     # When the amazon will arive at 'D'/5 it will shoot blocking rock to 'F'/3
#     blocking_lst = [Point('F', 3)]

#     #rest of the board, for extra verification
#     test_board = get_blocked_board(static_start_pos, new_position, SMALL_BOARD_SIZE, "BLACK", blocking_lst)

#     # i'd like to test invalid_movement mechanisem, that why i take 2 possible celss and tests that in the next move, the amazon couldn't reach them
#     unavailable_cells = [Point('F', 3), Point('G', 2)]
#     # Appending lists for test, amazon could not pass above blocked cell & the cells i mentioned above
#     blocking_lst.extend(unavailable_cells)

#     # after getting board prepared, need to run the tests on it
#     is_test_fine = run_loop_of_simple_movement_tests(new_position, blocking_lst, False, test_board)
#     if (not is_test_fine):
#         raise RuntimeError("Error With case 2")

#     # adding unavailable targets as well
#     additional_unavailable_targets = [Point('A', 6), Point('A', 4), Point('A', 3), Point('A', 1),
#                                       Point('B', 6), Point('B', 4), Point('B', 2), Point('B', 1),
#                                       Point('C', 1), Point('C', 2), Point('C', 3), 
#                                       Point('D', 5), Point('D', 6),
#                                       Point('E', 3), Point('e', 2), Point('E', 1),
#                                       Point('F', 1), Point('F', 2), Point('F', 3), Point('F', 4), Point('F', 5), Point('F', 6)]
#     available_moves = [Point('A', 5), Point('A', 2),
#                        Point('B', 5), Point('B', 3),  
#                        Point('C', 4), Point('C', 5), Point('C', 6),
#                        Point('D', 4), Point('D', 3), Point('D', 2), Point('D', 1),
#                        Point('e', 6), Point('E', 5), Point('E', 4)]

#     is_additional_unavailable_moves_are_unavailable = run_loop_of_simple_movement_tests(new_position, additional_unavailable_targets, False, test_board)
#     if (not is_additional_unavailable_moves_are_unavailable):
#         raise RuntimeError("Error with case 3")
#     number_of_passed_tests += 1

#     is_additional_available_moves_are_available = run_loop_of_simple_movement_tests(new_position, available_moves, True, test_board)
#     if (not is_additional_available_moves_are_available):
#         raise RuntimeError("Error with case 4")
#     number_of_passed_tests += 1


# # new test case
#     # testing turn starting with black amazon at A/4
#     # Assuming all amazons are on default locations on small board
#     static_start_pos = Point('A', 4)

#     # starting with blocked board, with 6 blockers
#     blockers_pos = [Point('A', 6), Point('A', 2), Point('B', 5), Point('b', 3),
#                     Point('B', 2), Point('D', 5), Point('D', 3)]

#     test_board = get_initialized_board(SMALL_BOARD_SIZE, blockers_pos)

#     valid_movements = [Point('A', 5), Point('A', 3), 
#                        Point('B', 4), 
#                        Point('C', 4), 
#                        Point('D', 4),
#                        Point('E', 4),
#                        Point('F', 4)]
#     invalid_movements = [Point('A', 6), Point('A', 4), Point('A', 2), Point('A', 1),
#                          Point('B', 6), Point('B', 5), Point('B', 3), Point('B', 2), Point('B', 1),
#                          Point('C', 6), Point('C', 5), Point('C', 3), Point('C', 2), Point('C', 1),
#                          Point('D', 6), Point('D', 5), Point('D', 3), Point('D', 2), Point('D', 1),
#                          Point('E', 6), Point('E', 5), Point('E', 3), Point('E', 2), Point('E', 1),
#                          Point('f', 6), Point('fE', 5), Point('f', 3), Point('f', 2), Point('f', 1)]
    
#     # after getting board prepared, need to run the tests on it
#     is_test_fine = run_loop_of_simple_movement_tests(static_start_pos, invalid_movements, False, test_board)
#     if (not is_test_fine):
#         raise RuntimeError("Error With case 2")
#     number_of_passed_tests += 1
#     is_additional_available_moves_are_available = run_loop_of_simple_movement_tests(static_start_pos, valid_movements, True, test_board)
#     if (not is_additional_available_moves_are_available):
#         raise RuntimeError("Error with case 4")
#     number_of_passed_tests += 1
# #end testcase
#     print ("<blocking_cell_validation_job()> Job ended successfully! run: " + str(number_of_passed_tests) + " tests")

if __name__ == '__main__':
    unittest.main()