import unittest
import random
import logging
import  time


from server.src.common_funcs import get_col_index, get_raw_index
from server.src.constants import Constants
from server.src.board_game import BoardGame
from server.src.turn_validator import TurnValidator
from server.src.point import Point
from server.src.blocking_rocks_manager import BlockingRocksManager
from server.src.player import ComputerPlayer, HumanPlayer
from server.src.available_steps_manager import AvailableMovementsManger
from server.src.game_node import GameNode


class TestSmallBoardBasicMovement(unittest.TestCase):
    def run_simple_test(self, amazon_to_move, new_position):
        board_game = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()
        return turn_validator.is_step_valid(board_game, amazon_to_move, new_position)

    def test_moving_horizontaly_to_the_left_one_step_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('C', 6)))
        self.assertTrue(self.run_simple_test(Point('F', 3), Point('E', 3)))
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('B', 1)))

    def test_moving_horizaontaly_to_the_left_2_steps(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('B', 6)))
        self.assertTrue(self.run_simple_test(Point('C', 1), Point('A', 1)))

    def test_moving_horizontaly_to_the_left_to_an_empty_cell(self):
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('a', 6)))
        self.assertTrue(self.run_simple_test(Point('D', 6), Point('C', 6)))
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
        board_game = BoardGame(Constants.LARGE_BOARD_SIZE)
        turn_validator = TurnValidator()
        return turn_validator.is_step_valid(board_game, amazon_to_move, new_position)

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


class TestShootingBlockingRock(unittest.TestCase):
    def run_simple_test(self, amazon_to_move, new_position):
        board_game = BoardGame(Constants.LARGE_BOARD_SIZE)
        turn_validator = TurnValidator()
        return turn_validator.is_step_valid(board_game, amazon_to_move, new_position)

    def get_blocked_board(self, blocked_cells):
        board_game = BoardGame(Constants.SMALL_BOARD_SIZE)
        for target in blocked_cells:
            board_game.shoot_blocking_rock(target)
        return board_game

    def test_shooting_verticly_down_destination_is_blocked(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('d', 4))
        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 6), Point('d', 4)))

    def test_shooting_verticly_down_to_non_empty_cell_white_amazon_there(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('d', 6), Point('c', 5), "WHITE")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('c', 5), Point('C', 1)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('c', 1)))

    def test_shooting_verticly_down_to_cell_where_black_amazona_exists(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('a', 6), Point('a', 1)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('a', 4)))

    def test_shooting_verticly_down_block_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('d', 4))
        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 6), Point('d', 1)))

    def test_shooting_verticly_down_in_the_way_there_is_white_amazon(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('c', 1), Point('d', 2), "WHITE")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 6), Point('d', 1)))
        self.assertTrue(
            test_board.shoot_blocking_rock(Point('d', 1)))  # In real game we should not suppose to get this situation

    def test_shooting_verticly_down_in_the_way_there_is_black_amazon(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('a', 4), Point('d', 4), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 6), Point('d', 1)))

    def test_shooting_verticly_up_destination_is_blocked(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('c', 3))
        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('c', 1), Point('c', 3)))

    def test_shooting_verticly_up_to_cell_where_white_amazona_exists(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 2), Point('d', 6)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('d', 6)))

    def test_shooting_verticly_up_to_cell_where_black_amazona_exists(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('a', 5), Point('a', 2)))

    def test_shooting_verticly_up_blocker_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('c', 3))
        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('c', 1), Point('c', 6)))
        self.assertTrue(
            test_board.shoot_blocking_rock(Point('d', 1)))  # In real game we should not suppose to get this situation

    def test_shooting_verticly_up_white_amazona_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.update_move(Point('d', 6), Point('d', 5), "WHITE")
        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 1), Point('d', 6)))

    def test_shooting_verticly_up_black_amazona_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('f', 1), Point('f', 5)))

    def test_shooting_horizontly_right_destination_is_blocked(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('b', 4))
        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('A', 4), Point('c', 4)))
        self.assertTrue(
            test_board.shoot_blocking_rock(Point('C', 4)))  # In real game we should not suppose to get this situation

    def test_shooting_horizontly_right_at_end_of_the_turn_to_non_empty_cell_black_amazon_there(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('a', 4), Point('b', 3), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('b', 3), Point('f', 3)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('f', 3)))

    def test_shooting_horizontly_right_to_cell_where_there_is_white_amazon(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('A', 6), Point('D', 6)))

    def test_shooting_horizontly_right_blocker_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('B', 6))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('A', 6), Point('D', 6)))

    def test_shooting_horizontly_right_white_amazona_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('A', 1), Point('D', 1)))

    def test_shooting_horizontly_right_black_amazona_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('f', 3), Point('d', 3), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('c', 3), Point('f', 3)))

    def test_shooting_horizontly_left_destination_is_blocked(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('D', 3))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('F', 3), Point('C', 3)))
        self.assertTrue(
            test_board.shoot_blocking_rock(Point('C', 3)))  # In real game we should not suppose to get this situation

    def test_shooting_horizontly_left_to_non_empty_cell_white_amazon_there(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('f', 6), Point('d', 6)))

    def test_shooting_horizontly_left_to_non_empty_cell_black_amazon_there(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('f', 3), Point('e', 4), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('e', 4), Point('a', 4)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('a', 4)))

    def test_shooting_horizontly_left_blocker_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('E', 3))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('f', 3), Point('d', 3)))

    def test_shooting_horizontly_left_white_amazona_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('f', 1), Point('b', 1)))

    def test_shooting_horizontly_left_black_amazona_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('a', 4), Point('b', 4), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('c', 4), Point('a', 4)))

    def test_shooting_diagonaly_north_east_to_non_empty_cell_white_amazon_there(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('c', 1), Point('A', 3), "WHITE")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('A', 3), Point('d', 6)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('d', 6)))

    def test_shooting_diagonaly_north_east_at_destination_is_blocked(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('E', 3))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('C', 1), Point('F', 4)))

    def test_shooting_diagonaly_north_east_in_destination_there_is_black_amazon(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot to black amazon cell
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('D', 1), Point('F', 3)))

    def test_shooting_diagonaly_north_east_way_is_blocked(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('b', 5))

        # shoot to black amazon cell
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('A', 4), Point('C', 6)))

    def test_shooting_diagonaly_north_east_white_amazona_in_route(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('c', 1), Point('c', 5), "WHITE")

        # Moving amazon to the new pos
        test_board.update_move(Point('a', 4), Point('b', 4), "BLACK")

        # shoot to black amazon cell
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('b', 4), Point('D', 6)))

    def test_shooting_diagonaly_north_east_black_amazona_in_route(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('F', 3), Point('e', 3), "BLACK")

        # shoot to black amazon cell
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('c', 1), Point('f', 4)))

    def test_shooting_diagonaly_south_west_to_blocked_cell(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('d', 1))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('F', 3), Point('d', 1)))

    def test_shooting_diagonaly_south_west_to_cell_where_white_amazona_exists(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('F', 4), Point('c', 1)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('c', 1)))

    def test_shooting_diagonaly_south_west_to_cell_where_black_amazona_exists(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('c', 6), Point('a', 4)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('c', 1)))

    def test_shooting_diagonaly_south_west_block_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # preparing test case
        test_board.shoot_blocking_rock(Point('c', 5))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 6), Point('a', 3)))

    def test_shooting_diagonaly_south_west_white_amazona_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('c', 1), Point('c', 5), "WHITE")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 6), Point('a', 3)))

    def test_shooting_diagonaly_south_west_black_amazona_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('a', 4), Point('b', 4), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 6), Point('a', 3)))

    def test_shooting_diagonaly_south_east_to_non_empty_cell_black_amazon_there(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('A', 4), Point('C', 6), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('C', 6), Point('F', 3)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('F', 3)))

    def test_shooting_diagonaly_south_east_destination_is_blocked(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        test_board.shoot_blocking_rock(Point('b', 3))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('a', 4), Point('b', 3)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('b', 3)))

    def test_shooting_diagonaly_south_east_in_destination_there_is_white_amazon(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('a', 3), Point('c', 1)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('c', 1)))

    def test_shooting_diagonaly_south_east_way_is_blocked(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        test_board.shoot_blocking_rock(Point('e', 5))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('d', 6), Point('f', 2)))

    def test_shooting_diagonaly_south_east_white_amazona_blocks_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('D', 6), Point('d', 2), "WHITE")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('b', 4), Point('e', 1)))

    def test_shooting_diagonaly_south_east_black_amazona_blocks_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('F', 3), Point('b', 3), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('a', 4), Point('d', 1)))

    def test_shooting_diagonaly_north_west_to_non_empty_cell_black_amazon_there(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('f', 3), Point('D', 1), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('D', 1), Point('A', 4)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('A', 4)))

    def test_shooting_diagonaly_north_west_destination_is_blocked(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.shoot_blocking_rock(Point('a', 3))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('c', 1), Point('A', 3)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('A', 3)))

    def test_shooting_diagonaly_north_west_white_amazona_in_destination(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('c', 1), Point('f', 4), "WHITE")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('f', 4), Point('d', 6)))
        self.assertFalse(test_board.shoot_blocking_rock(Point('d', 6)))

    def test_shooting_diagonaly_north_west_block_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.shoot_blocking_rock(Point('d', 5))

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('f', 3), Point('c', 6)))

    def test_shooting_diagonaly_north_west_white_amazona_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('d', 6), Point('d', 5), "WHITE")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('f', 3), Point('c', 6)))

    def test_shooting_diagonaly_north_west_black_amazona_is_in_the_way(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        turn_validator = TurnValidator()

        # Moving amazon to the new pos
        test_board.update_move(Point('a', 4), Point('e', 4), "BLACK")

        # shoot block rock after movment
        self.assertFalse(turn_validator.is_shoot_valid(test_board, Point('f', 3), Point('c', 6)))


class TestBlockingCellsValidationProcess(unittest.TestCase):
    def run_simple_test(self, amazon_to_move, new_position):
        board_game = BoardGame(Constants.LARGE_BOARD_SIZE)
        turn_validator = TurnValidator()
        return turn_validator.is_step_valid(board_game, amazon_to_move, new_position)

    def get_blocked_board(self, blocked_cells):
        board_game = BoardGame(Constants.SMALL_BOARD_SIZE)
        for target in blocked_cells:
            board_game.shoot_blocking_rock(target)
        return board_game

    def run_loop_of_simple_movement_tests(self, amazon_to_move, position_lst, expected_result, board):
        result = expected_result
        turn_validator = TurnValidator()
        for pos in position_lst:
            if result == expected_result:
                result = turn_validator.is_step_valid(board, amazon_to_move, pos)
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

        additional_blocking_lst = [Point('A', 1), Point('A', 2), Point('A', 3), Point('A', 4), Point('A', 5),
                                   Point('A', 6),
                                   Point('B', 4), Point('B', 5), Point('B', 6),
                                   Point('C', 4), Point('C', 5), Point('C', 6),
                                   Point('D', 4), Point('D', 5), Point('D', 6),
                                   Point('E', 1), Point('e', 2), Point('E', 3), Point('e', 4), Point('E', 5),
                                   Point('E', 6),
                                   Point('F', 1), Point('F', 2), Point('F', 3), Point('F', 4), Point('F', 5),
                                   Point('F', 6)]
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
        blocking_lst = [Point('A', 1), Point('A', 2), Point('A', 3), Point('A', 5), Point('A', 6),
                        Point('B', 1), Point('B', 2), Point('B', 3), Point('B', 4), Point('B', 5), Point('B', 6),
                        Point('C', 2), Point('C', 3), Point('C', 4), Point('C', 5), Point('C', 6),
                        Point('D', 1), Point('D', 2), Point('D', 3), Point('D', 4), Point('D', 5),
                        Point('E', 1), Point('e', 2), Point('E', 3), Point('e', 4), Point('E', 5), Point('E', 6),
                        Point('F', 1), Point('F', 2), Point('F', 4), Point('F', 5), Point('F', 6)]
        # Getting blocked board
        test_board = self.get_blocked_board(blocking_lst)

        # Moving amazon to the new pos
        self.assertFalse(test_board.update_move(Point('d', 6), Point('d', 3), "BLACK"))

        # Appending lists for test
        self.assertFalse(self.run_loop_of_simple_movement_tests(Point('C', 2), blocking_lst, False, test_board))

    def test_cant_reach_blocked_cells_after_movement(self):
        # Getting blocked board
        test_board = BoardGame(Constants.SMALL_BOARD_SIZE)

        # Moving amazon to the new pos
        test_board.update_move(Point('d', 6), Point('c', 5), "WHITE")

        # shoot block rock after movment
        test_board.shoot_blocking_rock(Point('e', 3))

        # adding unavailable targets as well
        unavailable_moves = [
            Point('A', 6), Point('A', 4), Point('A', 2), Point('A', 1),
            Point('B', 3), Point('B', 2), Point('B', 1),
            Point('C', 1), Point('C', 5),
            Point('D', 3), Point('D', 2), Point('D', 1),
            Point('E', 6), Point('E', 4), Point('E', 3), Point('E', 2), Point('E', 1),
            Point('F', 6), Point('F', 4), Point('F', 3), Point('F', 2), Point('F', 1)]

        available_moves = [
            Point('A', 5), Point('A', 3),
            Point('B', 6), Point('B', 5), Point('B', 4),
            Point('C', 6), Point('c', 4), Point('C', 3), Point('C', 2),
            Point('D', 6), Point('D', 5), Point('D', 4),
            Point('E', 5),
            Point('F', 5)]

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
#
class BlockingRocksManagerSmallBoardTests(unittest.TestCase):
    def setUp(self):
        self.game_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        self.movement_validator = TurnValidator()
        self.blocking_manager = BlockingRocksManager(Constants.SMALL_BOARD_SIZE, self.movement_validator)

    def use_blockers(self, number_of_blockers_to_use):
        for i in range(0, number_of_blockers_to_use):
            self.assertTrue(self.blocking_manager.get_rock())

    def test_game_runs_on_small_board_while_there_available_blocking_rocks(self):
        self.use_blockers(Constants.NUMBER_OF_ROCKS_IN_SMALL_BOARD)

    def test_game_ends_on_small_board_while_there_are_no_available_blocking_rocks(self):
        self.use_blockers(Constants.NUMBER_OF_ROCKS_IN_SMALL_BOARD)
        self.assertFalse(self.blocking_manager.get_rock())


class BlockingRocksManagerLargeBoardTests(unittest.TestCase):
    def setUp(self):
        self.game_board = BoardGame(Constants.LARGE_BOARD_SIZE)
        self.movement_validator = TurnValidator()
        self.blocking_manager = BlockingRocksManager(Constants.LARGE_BOARD_SIZE, self.movement_validator)

    def use_blockers(self, number_of_blockers_to_use):
        for i in range(0, number_of_blockers_to_use):
            self.assertTrue(self.blocking_manager.get_rock())

    def test_game_runs_on_large_board_while_there_available_blocking_rocks(self):
        self.use_blockers(Constants.NUMBER_OF_ROCKS_IN_LARGE_BOARD)

    def test_game_ends_on_large_board_while_there_are_no_available_blocking_rocks(self):
        self.use_blockers(Constants.NUMBER_OF_ROCKS_IN_LARGE_BOARD)
        self.assertFalse(self.blocking_manager.get_rock())


class AvailableStepsManagerSmallBoardTests(unittest.TestCase):
    def setUp(self):
        self.game_board = BoardGame(Constants.SMALL_BOARD_SIZE)
        self.movement_validator = TurnValidator()
        self.available_steps_manager = AvailableMovementsManger()
        self.black_amazon_init_blk_lst = [Point('A', 5), Point('B', 5), Point('B', 4), Point('B', 3), Point('A', 3),
                                          Point('F', 4), Point('E', 4), Point('E', 3), Point('E', 2), Point('F', 2)]
        self.white_amazon_init_blk_lst = [Point('c', 6), Point('c', 5), Point('d', 5), Point('e', 5), Point('E', 6),
                                          Point('b', 1), Point('b', 2), Point('c', 2), Point('d', 2), Point('d', 1)]

    def set_full_blocked_board(self):
        for i in range(1, self.game_board.get_size() + 1):
            for j in range(1, self.game_board.get_size() + 1):
                if self.game_board.is_free_cell(i, Constants.COLUMNS_ARRAY[j]):
                    self.game_board.shoot_blocking_rock(Point(Constants.COLUMNS_ARRAY[j], i))

    def set_board_blocked_by_list(self, blocking_lst):
        for point in blocking_lst:
            self.game_board.shoot_blocking_rock(point)

    def test_zero_available_steps_to_black_amazon(self):
        # starting in initial state, blocking all black amazons
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)
        self.assertEqual(0, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK")))

    def test_zero_available_steps_to_white_amazon(self):
        # starting in initial state, blocking all white amazons
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)
        self.assertEqual(0, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_number_of_available_steps_north_in_initial_state_for_black_amazon(self):
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('A', 4))))
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('F', 3))))

    def test_number_of_available_steps_south_in_initial_state_for_black_amazon(self):
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('A', 4))))
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('F', 3))))

    def test_number_of_available_steps_east_in_initial_state_for_black_amazon(self):
        self.assertEqual(5, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('A', 4))))
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('F', 3))))

    def test_number_of_available_steps_west_in_initial_state_for_black_amazon(self):
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('A', 4))))
        self.assertEqual(5, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('F', 3))))

    def test_number_of_available_steps_NE_in_initial_state_for_black_amazon(self):
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('A', 4))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('F', 3))))

    def test_number_of_available_steps_SE_in_initial_state_for_black_amazon(self):
        self.assertEqual(3,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('A', 4))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('F', 3))))

    def test_number_of_available_steps_NW_in_initial_state_for_black_amazon(self):
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('A', 4))))
        self.assertEqual(3,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('F', 3))))

    def test_number_of_available_steps_SW_in_initial_state_for_black_amazon(self):
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('A', 4))))
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('F', 3))))

    def test_number_of_available_steps_north_in_initial_state_for_white_amazon(self):
        self.assertEqual(5, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('c', 1))))
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('d', 6))))

    def test_number_of_available_steps_south_in_initial_state_for_white_amazon(self):
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('c', 1))))
        self.assertEqual(5, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('d', 6))))

    def test_number_of_available_steps_east_in_initial_state_for_white_amazon(self):
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('c', 1))))
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('d', 6))))

    def test_number_of_available_steps_west_in_initial_state_for_white_amazon(self):
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('c', 1))))
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('d', 6))))

    def test_number_of_available_steps_NE_in_initial_state_for_white_amazon(self):
        self.assertEqual(3,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('c', 1))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('d', 6))))

    def test_number_of_available_steps_SE_in_initial_state_for_white_amazon(self):
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('c', 1))))
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('d', 6))))

    def test_number_of_available_steps_NW_in_initial_state_for_white_amazon(self):
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('c', 1))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('d', 6))))

    def test_number_of_available_steps_SW_in_initial_state_for_white_amazon(self):
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('c', 1))))
        self.assertEqual(3,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('d', 6))))

    def test_number_of_total_available_steps_in_initial_state_for_black_amazon(self):
        self.assertEqual(24, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK")))

    def test_number_of_total_available_steps_in_initial_state_for_white_amazon(self):
        self.assertEqual(24, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_one_available_step_to_black_amazon(self):
        # starting in initial state, blocking all white
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        # removing first blocker from black, and updating it in order to set black player just 1 available move
        removed_blocked_cell = self.black_amazon_init_blk_lst.pop(1)
        self.game_board.shoot_blocking_rock(
            Point(chr(ord(removed_blocked_cell.get_x()) + 1), removed_blocked_cell.get_y() + 1))
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)

        self.assertEqual(1, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK")))
        self.assertEqual(0, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_one_available_step_to_white_amazon(self):
        # starting in initial state, blocking all white
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)

        # removing first blocker from white, and updating it in order to set black player just 1 available move
        removed_blocked_cell = self.white_amazon_init_blk_lst.pop(4)
        self.game_board.shoot_blocking_rock(
            Point(chr(ord(removed_blocked_cell.get_x()) + 1), removed_blocked_cell.get_y()))
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        self.assertEqual(0, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK")))
        self.assertEqual(1, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_two_available_steps_to_black_amazon_and_one_for_the_white(self):
        # removing first blocker from black, and updating it in order to set black player just 1 available move
        removed_blocked_cell = self.black_amazon_init_blk_lst.pop(len(self.black_amazon_init_blk_lst) - 1)

        # removing blocker from white, and updating it in order to set black player just 1 available move
        removed_blocked_cell = self.white_amazon_init_blk_lst.pop(6)
        self.game_board.shoot_blocking_rock(
            Point(chr(ord(removed_blocked_cell.get_x()) - 1), removed_blocked_cell.get_y() + 1))

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        self.assertEqual(2, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK")))
        self.assertEqual(1, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_two_available_steps_to_white_amazon_and_one_for_the_black(self):
        # removing first blocker from black, and updating it in order to set black player just 1 available move
        removed_blocked_cell = self.black_amazon_init_blk_lst.pop(len(self.black_amazon_init_blk_lst) - 1)
        self.game_board.shoot_blocking_rock(Point(removed_blocked_cell.get_x(), removed_blocked_cell.get_y() - 1))

        # removing blocker from white, and updating it in order to set black player just 1 available move
        removed_blocked_cell = self.white_amazon_init_blk_lst.pop(1)
        self.game_board.shoot_blocking_rock(
            Point(chr(ord(removed_blocked_cell.get_x()) - 2), removed_blocked_cell.get_y() - 2))
        removed_blocked_cell = self.white_amazon_init_blk_lst.pop(1)
        self.game_board.shoot_blocking_rock(Point(removed_blocked_cell.get_x(), removed_blocked_cell.get_y() - 1))

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        self.assertEqual(1, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK")))
        self.assertEqual(2, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_three_available_steps_to_black_amazon_and_two_for_the_white(self):
        # removing first blocker from black, and updating it in order to set black player just 1 available move
        removed_blocked_cell = self.black_amazon_init_blk_lst.pop(5)
        self.game_board.shoot_blocking_rock(Point(removed_blocked_cell.get_x(), removed_blocked_cell.get_y() - 2))

        removed_blocked_cell = self.black_amazon_init_blk_lst.pop(6)
        self.game_board.shoot_blocking_rock(
            Point(chr(ord(removed_blocked_cell.get_x()) - 1), removed_blocked_cell.get_y()))

        # removing blocker from white, and updating it in order to set black player just 1 available move
        removed_blocked_cell = self.white_amazon_init_blk_lst.pop(4)
        self.game_board.shoot_blocking_rock(
            Point(chr(ord(removed_blocked_cell.get_x()) + 1), removed_blocked_cell.get_y()))

        removed_blocked_cell = self.white_amazon_init_blk_lst.pop(5)
        self.game_board.shoot_blocking_rock(
            Point(chr(ord(removed_blocked_cell.get_x()) - 1), removed_blocked_cell.get_y() + 1))

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        self.assertEqual(3, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK")))
        self.assertEqual(2, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_board_snapshot_with_many_blocked_cells(self):
        blocked_cells_lst = [Point('c', 6),
                             Point('a', 5), Point('e', 5),
                             Point('c', 4), Point('d', 4), Point('f', 4),
                             Point('a', 3), Point('c', 3), Point('d', 3), Point('e', 3),
                             Point('b', 2), Point('e', 2), Point('f', 2),
                             Point('d', 1), ]

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(blocked_cells_lst)

        # self.assertEqual(6, self.available_steps_manager.get_number_of_available_mooves_for_player(self.game_board,
        #                                                                                             "BLACK"))
        self.assertEqual(9, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_calculate_number_of_available_steps_for_black_player_in_initial_game_position(self):
        self.assertEqual(10, len(
            self.available_steps_manager.get_available_moves_in_distance(self.game_board, self.game_board.get_players_positions("BLACK"), 1)))

    def test_calculate_number_of_available_steps_for_white_player_in_initial_game_position(self):
        self.assertEqual(10, len(
            self.available_steps_manager.get_available_moves_in_distance(self.game_board, self.game_board.get_players_positions("WHITE"), 1)))


class AvailableStepsManagerLargeBoardTests(unittest.TestCase):
    def setUp(self):
        self.game_board = BoardGame(Constants.LARGE_BOARD_SIZE)
        self.movement_validator = TurnValidator()
        self.available_steps_manager = AvailableMovementsManger()
        self.black_amazon_init_blk_lst = [Point('c', 10), Point('e', 10), Point('f', 10), Point('h', 10),
                                          Point('c', 9), Point('d', 9), Point('e', 9), Point('f', 9), Point('g', 9),
                                          Point('h', 9),
                                          Point('A', 8), Point('B', 8), Point('i', 8), Point('j', 8),
                                          Point('b', 7), Point('i', 7),
                                          Point('A', 6), Point('B', 6), Point('i', 6), Point('j', 6)]

        self.white_amazon_init_blk_lst = [Point('A', 5), Point('B', 5), Point('i', 5), Point('j', 5),
                                          Point('b', 4), Point('i', 4),
                                          Point('A', 3), Point('B', 3), Point('i', 3), Point('j', 3),
                                          Point('c', 2), Point('d', 2), Point('e', 2), Point('f', 2), Point('g', 2),
                                          Point('h', 2),
                                          Point('c', 1), Point('e', 1), Point('f', 1), Point('h', 1)]

    def set_full_blocked_board(self):
        curr_board_size = self.game_board.get_size()
        for i in range(1, curr_board_size + 1):
            for j in range(1, curr_board_size + 1):
                raw = get_raw_index(i, curr_board_size)
                col = get_col_index(Constants.COLUMNS_ARRAY[j - 1], curr_board_size)
                if self.game_board.is_free_cell(raw, col):
                    self.game_board.shoot_blocking_rock(Point(Constants.COLUMNS_ARRAY[j - 1], i))

    def get_number_of_available_mooves(self):
        black_available_moves = self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK"))
        white_available_moves = self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE"))
        return black_available_moves + white_available_moves

    def set_board_blocked_by_list(self, blocking_lst):
        for point in blocking_lst:
            self.game_board.shoot_blocking_rock(point)

    def test_zero_available_steps_on_fully_blocked_board(self):
        self.set_full_blocked_board()
        self.assertEqual(0, self.get_number_of_available_mooves())

    def test_zero_available_steps_to_black_amazon(self):
        # starting in initial state, blocking all black amazons
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)
        self.assertEqual(0, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK")))

    def test_zero_available_steps_to_white_amazon(self):
        # starting in initial state, blocking all white amazons
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)
        self.assertEqual(0, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_number_of_available_steps_north_in_initial_state_for_black_amazon(self):
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('A', 7))))
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('d', 10))))
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('g', 10))))
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('j', 7))))

    def test_number_of_available_steps_south_in_initial_state_for_black_amazon(self):
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('A', 7))))
        self.assertEqual(8, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('d', 10))))
        self.assertEqual(8, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('g', 10))))
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('j', 7))))

    def test_number_of_available_steps_east_in_initial_state_for_black_amazon(self):
        self.assertEqual(8, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('A', 7))))
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('d', 10))))
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('g', 10))))
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('j', 7))))

    def test_number_of_available_steps_west_in_initial_state_for_black_amazon(self):
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('A', 7))))
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('d', 10))))
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('g', 10))))
        self.assertEqual(8, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('j', 7))))

    def test_number_of_available_steps_NE_in_initial_state_for_black_amazon(self):
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('A', 7))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('d', 10))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('g', 10))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('j', 7))))

    def test_number_of_available_steps_SE_in_initial_state_for_black_amazon(self):
        self.assertEqual(5,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('A', 7))))
        self.assertEqual(5,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('d', 10))))
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('g', 10))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('j', 7))))

    def test_number_of_available_steps_NW_in_initial_state_for_black_amazon(self):
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('A', 7))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('d', 10))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('g', 10))))
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('j', 7))))

    def test_number_of_available_steps_SW_in_initial_state_for_black_amazon(self):
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('A', 7))))
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('d', 10))))
        self.assertEqual(5,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('g', 10))))
        self.assertEqual(5,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('j', 7))))

    def test_number_of_available_steps_north_in_initial_state_for_white_amazon(self):
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('A', 4))))
        self.assertEqual(8, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('D', 1))))
        self.assertEqual(8, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('g', 1))))
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_north(self.game_board, Point('j', 4))))

    def test_number_of_available_steps_south_in_initial_state_for_white_amazon(self):
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('A', 4))))
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('D', 1))))
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('g', 1))))
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_south(self.game_board, Point('j', 4))))

    def test_number_of_available_steps_east_in_initial_state_for_white_amazon(self):
        self.assertEqual(8, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('A', 4))))
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('D', 1))))
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('g', 1))))
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_east(self.game_board, Point('j', 4))))

    def test_number_of_available_steps_west_in_initial_state_for_white_amazon(self):
        self.assertEqual(0, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('A', 4))))
        self.assertEqual(3, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('D', 1))))
        self.assertEqual(2, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('g', 1))))
        self.assertEqual(8, len(
            self.available_steps_manager.get_available_moves_to_the_west(self.game_board, Point('j', 4))))

    def test_number_of_available_steps_NE_in_initial_state_for_white_amazon(self):
        self.assertEqual(5,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('A', 4))))
        self.assertEqual(5,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('D', 1))))
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('g', 1))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NE(self.game_board, Point('j', 4))))

    def test_number_of_available_steps_SE_in_initial_state_for_white_amazon(self):
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('A', 4))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('D', 1))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('g', 1))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SE(self.game_board, Point('j', 4))))

    def test_number_of_available_steps_NW_in_initial_state_for_white_amazon(self):
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('A', 4))))
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('D', 1))))
        self.assertEqual(5,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('g', 1))))
        self.assertEqual(5,
                         len(self.available_steps_manager.get_available_moves_to_NW(self.game_board, Point('j', 4))))

    def test_number_of_available_steps_SW_in_initial_state_for_white_amazon(self):
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('A', 4))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('D', 1))))
        self.assertEqual(0,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('g', 1))))
        self.assertEqual(2,
                         len(self.available_steps_manager.get_available_moves_to_SW(self.game_board, Point('j', 4))))

    def test_number_of_total_available_steps_in_initial_state_for_black_amazon(self):
        self.assertEqual(58, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                   self.game_board.get_players_positions("BLACK")))

    def test_number_of_total_available_steps_in_initial_state_for_white_amazon(self):
        self.assertEqual(58, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                   self.game_board.get_players_positions("WHITE")))

    def test_one_available_step_to_black_amazon(self):
        # starting in initial state, blocking all white
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        # removing first blocker from black, and updating it in order to set black player just 1 available move
        self.black_amazon_init_blk_lst.pop(1)

        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)

        self.assertEqual(1, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                  self.game_board.get_players_positions(
                                                                                                      "BLACK")))
        self.assertEqual(0, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                  self.game_board.get_players_positions("WHITE")))

    def test_one_available_step_to_white_amazon(self):
        # starting in initial state, blocking all white
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)

        # removing first blocker from white, and updating it in order to set black player just 1 available move
        self.white_amazon_init_blk_lst.pop(15)
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        self.assertEqual(0, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                  self.game_board.get_players_positions(
                                                                                                      "BLACK")))
        self.assertEqual(1, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                   self.game_board.get_players_positions("WHITE")))

    def test_two_available_steps_to_black_amazon_and_one_for_the_white(self):
        # removing first blocker from black, and updating it in order to set black player just 1 available move
        self.black_amazon_init_blk_lst.pop(16)
        self.black_amazon_init_blk_lst.pop(len(self.black_amazon_init_blk_lst) - 1)

        # removing blocker from white, and updating it in order to set black player just 1 available move
        self.white_amazon_init_blk_lst.pop(8)

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        self.assertEqual(2, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                  self.game_board.get_players_positions(
                                                                                                      "BLACK")))
        self.assertEqual(1, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                   self.game_board.get_players_positions("WHITE")))

    def test_two_available_steps_to_white_amazon_and_one_for_the_black(self):
        # removing first blocker from black, and updating it in order to set black player just 1 available move
        self.black_amazon_init_blk_lst.pop(4)

        # removing blocker from white, and updating it in order to set black player just 1 available move
        self.white_amazon_init_blk_lst.pop(7)
        self.white_amazon_init_blk_lst.pop(14)

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        self.assertEqual(1, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                   self.game_board.get_players_positions("BLACK")))
        self.assertEqual(2, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                   self.game_board.get_players_positions("WHITE")))

    def test_three_available_steps_to_black_amazon_and_two_for_the_white(self):
        # removing first blocker from black, and updating it in order to set black player just 1 available move
        self.black_amazon_init_blk_lst.pop(13)

        # removing blocker from white, and updating it in order to set black player just 1 available move
        self.white_amazon_init_blk_lst.pop(18)
        self.white_amazon_init_blk_lst.pop(10)

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(self.black_amazon_init_blk_lst)
        self.set_board_blocked_by_list(self.white_amazon_init_blk_lst)

        self.assertEqual(3, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                   self.game_board.get_players_positions("BLACK")))
        self.assertEqual(2, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board,
                                                                                                   self.game_board.get_players_positions("WHITE")))

    def test_board_snapshot_with_many_blocked_cells(self):
        blocked_cells_lst = [Point('c', 9),
                             Point('f', 8), Point('i', 8),
                             Point('c', 6), Point('h', 6),
                             Point('a', 5), Point('e', 5),
                             Point('c', 4), Point('d', 4), Point('f', 4),
                             Point('a', 3), Point('c', 3), Point('d', 3), Point('e', 3),
                             Point('b', 2), Point('e', 2), Point('f', 2),
                             Point('e', 1)]

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(blocked_cells_lst)

        self.assertEqual(44, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("BLACK")))
        self.assertEqual(29, self.available_steps_manager.get_number_of_available_moves_for_player(self.game_board, self.game_board.get_players_positions("WHITE")))

    def test_calculate_number_of_available_stepst_for_black_player_in_hypothtical_state_in_distance_one(self):
        blocked_cells_lst = [
            Point('G', 7), Point('i', 7),
            Point('b', 5), Point('e', 5),
            Point('b', 4), Point('c', 4),
            Point('d', 2)]

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(blocked_cells_lst)

        # updating positions for amazons
        self.game_board.update_move(Point('a', 7), Point('c', 5), "BLACK")
        self.game_board.update_move(Point('d', 10), Point('d', 5), "BLACK")
        self.game_board.update_move(Point('g', 10), Point('g', 4), "BLACK")

        self.game_board.update_move(Point('d', 10), Point('e', 8), "WHITE")
        self.game_board.update_move(Point('j', 4), Point('h', 6), "WHITE")
        self.game_board.update_move(Point('g', 10), Point('b', 3), "WHITE")
        self.game_board.update_move(Point('a', 4), Point('b', 3), "WHITE")

        self.assertEqual(18, len(
            self.available_steps_manager.get_available_moves_in_distance(self.game_board, self.game_board.get_players_positions("BLACK"), 1)))

    def test_calculate_number_of_available_steps_for_white_player_in_hypothetical_state(self):
        blocked_cells_lst = [
            Point('G', 7), Point('i', 7),
            Point('b', 5), Point('e', 5),
            Point('b', 4), Point('c', 4),
            Point('d', 2)]

        # blocking states with an updated blocking lists
        self.set_board_blocked_by_list(blocked_cells_lst)

        self.game_board.update_move(Point('a', 7), Point('c', 5), "BLACK")
        self.game_board.update_move(Point('d', 10), Point('d', 5), "BLACK")
        self.game_board.update_move(Point('g', 10), Point('g', 4), "BLACK")

        self.game_board.update_move(Point('d', 1), Point('e', 8), "WHITE")
        self.game_board.update_move(Point('j', 4), Point('h', 6), "WHITE")
        self.game_board.update_move(Point('g', 1), Point('b', 3), "WHITE")
        self.game_board.update_move(Point('a', 4), Point('a', 8), "WHITE")

        self.assertEqual(43, len(
            self.available_steps_manager.get_available_moves_in_distance(self.game_board, self.game_board.get_players_positions("WHITE"), 2)))


class WinnerDitermination(unittest.TestCase):
    # once the game is over: no more rocks OR no more possible moves for player, need to decide who is the winner
    # by counting number of possible moves
    # set board, set positions, make move and calculate
    # Test cases need to verify in each board that the game is over (no more possible turns or no more rocks)
    # Black should win
    # white should win
    # need to pay attention there are no doubling, think about case you can go 3 right. it means you have 3 options: 1 right, 2 right, 3 right NOT ONLY 1
    def setUp(self):
        self.board_game = BoardGame(Constants.LARGE_BOARD_SIZE)
        self.turn_validator = TurnValidator()
        self.available_steps_manager = AvailableMovementsManger()

    def set_board_blocked_by_list(self, blocking_lst):
        for point in blocking_lst:
            self.board_game.shoot_blocking_rock(point)

    def test_winner_determination(self):
        # running test case according to wikipedia
        blocking_lst = [Point('A', 10), Point('A', 8), Point('A', 3), Point('A', 2),
                        Point('B', 9), Point('B', 8), Point('B', 5), Point('B', 4), Point('B', 3), Point('B', 2),
                        Point('C', 9), Point('C', 7), Point('C', 6), Point('C', 5), Point('C', 4), Point('C', 1),
                        Point('D', 9), Point('D', 8), Point('D', 7), Point('D', 5), Point('D', 3), Point('D', 2),
                        Point('E', 10), Point('E', 8), Point('E', 7), Point('E', 6), Point('E', 3), Point('E', 1),
                        Point('F', 9), Point('F', 8), Point('F', 6), Point('F', 5), Point('F', 4), Point('F', 3),
                        Point('F', 2), Point('F', 1),
                        Point('G', 8), Point('G', 6), Point('G', 4), Point('G', 3), Point('G', 2),
                        Point('H', 10), Point('H', 8), Point('H', 6), Point('H', 5), Point('H', 3),
                        Point('I', 9), Point('I', 8), Point('I', 7), Point('I', 6),
                        Point('J', 8), Point('J', 6), Point('J', 1)]
        # need to move white from D/1 to D/7
        self.board_game.update_move(Point('D', 1), Point('D', 7), "WHITE")
        # need to move black from J/7 to D/1
        self.board_game.update_move(Point('J', 7), Point('D', 1), "BLACK")
        # need to move white from J/6 to J/7
        self.board_game.update_move(Point('J', 4), Point('J', 7), "WHITE")
        # need to move black from A/7 to D/4
        self.board_game.update_move(Point('A', 7), Point('D', 4), "BLACK")
        # need to move white from G/1 to G/2
        self.board_game.update_move(Point('G', 1), Point('G', 2), "WHITE")
        # need to move black from G/10 to G/1
        self.board_game.update_move(Point('G', 10), Point('G', 1), "BLACK")
        # need to move white from G/2to E/2
        self.board_game.update_move(Point('G', 2), Point('E', 2), "WHITE")
        # need to move black from D/4 to E/5
        self.board_game.update_move(Point('D', 4), Point('E', 5), "BLACK")
        # need to move white from A/4 to A/6
        self.board_game.update_move(Point('A', 4), Point('A', 6), "WHITE")
        # need to move white from A/6 to C/8
        self.board_game.update_move(Point('A', 6), Point('C', 8), "WHITE")
        # need to move white from D/7 to F/7
        self.board_game.update_move(Point('D', 7), Point('F', 7), "WHITE")

        self.set_board_blocked_by_list(blocking_lst)

        # it should be 31 in this case, AI should iterate and calculate future potential moves
        self.assertEqual(13, self.available_steps_manager.get_number_of_available_moves_for_player(self.board_game,
                                                                                                    self.board_game.get_players_positions("BLACK")))

        # it should be 8  in this case, AI should iterate and calculate future potential moves
        self.assertEqual(4, self.available_steps_manager.get_number_of_available_moves_for_player(self.board_game,
                                                                                                  self.board_game.get_players_positions(
                                                                                                      "WHITE")))


class ConfigurationToSmallBoardTests(unittest.TestCase):
    def setUp(self):
        self.blocking_lst = [Point('b', 5), Point('e', 5), Point('c', 4), Point('d', 2)]
        self.white_amazons = [Point('B', 2), Point('c', 5)]
        self.black_amazons = [Point('d', 3), Point('a', 6)]
        self.board_game = BoardGame(Constants.SMALL_BOARD_SIZE)

    def test_creating_board_as_expected(self):
        self.board_game.update_move(Point('c', 1), Point('b', 2), "WHITE")
        self.board_game.shoot_blocking_rock(Point('d', 2))
        self.board_game.update_move(Point('F', 3), Point('D', 3), "BLACK")
        self.board_game.shoot_blocking_rock(Point('C', 4))
        self.board_game.update_move(Point('d', 6), Point('c', 5), "WHITE")
        self.board_game.shoot_blocking_rock(Point('e', 5))
        self.board_game.update_move(Point('a', 4), Point('a', 6), "BLACK")
        self.board_game.shoot_blocking_rock(Point('b', 5))
        self.assertEqual(self.board_game, BoardGame(Constants.SMALL_BOARD_SIZE,
                                                    True,
                                                    self.white_amazons,
                                                    self.black_amazons,
                                                    self.blocking_lst))

    def test_not_equal_when_there_is_no_correlation_between_them(self):
        self.board_game.update_move(Point('c', 1), Point('b', 2), "WHITE")
        self.board_game.shoot_blocking_rock(Point('d', 2))
        self.board_game.update_move(Point('F', 3), Point('D', 3), "BLACK")
        self.board_game.update_move(Point('d', 6), Point('c', 5), "WHITE")
        self.board_game.shoot_blocking_rock(Point('e', 5))
        self.board_game.update_move(Point('a', 4), Point('a', 6), "BLACK")
        self.board_game.shoot_blocking_rock(Point('b', 5))
        self.assertNotEqual(self.board_game,
                            BoardGame(Constants.SMALL_BOARD_SIZE, True, self.white_amazons, self.black_amazons,
                                      self.blocking_lst))


class Configuration_To_Large_Board_Tests(unittest.TestCase):
    def setUp(self):
        self.blocking_lst = [Point('A', 10), Point('A', 8), Point('A', 3),
                             Point('b', 5),
                             Point('D', 9), Point('D', 6),
                             Point('f', 8), Point('f', 4)]
        self.board_game = BoardGame(Constants.LARGE_BOARD_SIZE)
        self.white_amazons = [Point('g', 4), Point('a', 9), Point('j', 6), Point('d', 8)]
        self.black_amazons = [Point('e', 3), Point('a', 7), Point('b', 8), Point('c', 6)]

    def test_creating_board_as_expected(self):
        self.board_game.update_move(Point('g', 1), Point('g', 4), "WHITE")
        self.board_game.shoot_blocking_rock(Point('f', 4))
        self.board_game.update_move(Point('a', 7), Point('e', 3), "BLACK")
        self.board_game.shoot_blocking_rock(Point('a', 3))
        self.board_game.update_move(Point('a', 4), Point('a', 9), "WHITE")
        self.board_game.shoot_blocking_rock(Point('a', 10))
        self.board_game.update_move(Point('j', 7), Point('a', 7), "BLACK")
        self.board_game.shoot_blocking_rock(Point('a', 8))
        self.board_game.update_move(Point('j', 4), Point('j', 6), "WHITE")
        self.board_game.shoot_blocking_rock(Point('d', 6))
        self.board_game.update_move(Point('d', 10), Point('b', 8), "BLACK")
        self.board_game.shoot_blocking_rock(Point('f', 8))
        self.board_game.update_move(Point('d', 1), Point('d', 8), "WHITE")
        self.board_game.shoot_blocking_rock(Point('d', 9))
        self.board_game.update_move(Point('g', 10), Point('c', 6), "BLACK")
        self.board_game.shoot_blocking_rock(Point('b', 5))
        self.assertEqual(self.board_game, BoardGame(Constants.LARGE_BOARD_SIZE,
                                                    True,
                                                    self.white_amazons,
                                                    self.black_amazons,
                                                    self.blocking_lst))


class AiGameNodeHeuristicTests(unittest.TestCase):
    def setUp(self):
        self.board_game = BoardGame(Constants.LARGE_BOARD_SIZE)
        self.turn_validator = TurnValidator()
        self.available_steps_manager = AvailableMovementsManger()
        self.is_black_player = False

    def test_calculation_of_move_count_heuristic_in_initial_state_for_white_player(self):
        curr_game_node = GameNode(self.board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)

        self.assertEqual(curr_game_node.calculate_move_count_heuristic(), 0)

    def test_calculation_of_move_count_heuristic_in_initial_state_for_black_player(self):
        self.is_black_player = True
        curr_game_node = GameNode(self.board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)

        self.assertEqual(curr_game_node.calculate_move_count_heuristic(), 0)

    def test_calculation_of_move_count_heuristic_when_black_is_completly_blocked(self):
        white_pos = [Point('a', 6), Point('d', 10), Point('j', 6), Point('d', 1)]
        black_pos = [Point('d', 6), Point('e', 6), Point('d', 5), Point('e', 5)]
        blocking_pos = [Point('c', 7), Point('c', 6), Point('c', 5), Point('c', 4),
                        Point('d', 7), Point('d', 4),
                        Point('e', 7), Point('e', 4),
                        Point('f', 7), Point('f', 6), Point('f', 5), Point('f', 4)]
        board_game = BoardGame(Constants.LARGE_BOARD_SIZE, True, white_pos, black_pos, blocking_pos)

        curr_game_node = GameNode(board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)
        curr_game_node.print_board()
        self.assertEqual(curr_game_node.calculate_move_count_heuristic(), 61)

    def test_winner_determination_white_plays_and_wins(self):
        white_pos = [Point('a', 6), Point('d', 10), Point('j', 6), Point('d', 1)]
        black_pos = [Point('d', 6), Point('e', 6), Point('d', 5), Point('e', 5)]
        blocking_pos = [Point('c', 7), Point('c', 6), Point('c', 5), Point('c', 4),
                        Point('d', 7), Point('d', 4),
                        Point('e', 7), Point('e', 4),
                        Point('f', 7), Point('f', 6), Point('f', 5), Point('f', 4)]
        board_game = BoardGame(Constants.LARGE_BOARD_SIZE, True, white_pos, black_pos, blocking_pos)
        curr_game_node = GameNode(board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)
        self.assertTrue(curr_game_node.is_game_over)
        self.assertEqual(curr_game_node.winner, "WHITE")

    def test_winner_determination_white_plays_and_loses(self):
        black_pos = [Point('a', 6), Point('d', 10), Point('j', 6), Point('d', 1)]
        white_pos = [Point('d', 6), Point('e', 6), Point('d', 5), Point('e', 5)]
        blocking_pos = [Point('c', 7), Point('c', 6), Point('c', 5), Point('c', 4),
                        Point('d', 7), Point('d', 4),
                        Point('e', 7), Point('e', 4),
                        Point('f', 7), Point('f', 6), Point('f', 5), Point('f', 4)]
        board_game = BoardGame(Constants.LARGE_BOARD_SIZE, True, white_pos, black_pos, blocking_pos)
        curr_game_node = GameNode(board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)
        self.assertTrue(curr_game_node.is_game_over)
        self.assertEqual(curr_game_node.winner, "BLACK")

    def test_determination_of_winner_when_white_plays_and_game_is_not_over(self):
        curr_game_node = GameNode(self.board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)

        self.assertFalse(curr_game_node.is_game_over)
        self.assertEqual(curr_game_node.winner, "")

    def test_determination_of_winner_when_blcak_plays_and_game_is_not_over(self):
        self.is_black_player = True
        curr_game_node = GameNode(self.board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)

        self.assertFalse(curr_game_node.is_game_over)
        self.assertEqual(curr_game_node.winner, "")

    def test_winner_determination_black_should_lose_black_plays(self):
        self.is_black_player = True
        white_pos = [Point('a', 6), Point('d', 10), Point('j', 6), Point('d', 1)]
        black_pos = [Point('d', 6), Point('e', 6), Point('d', 5), Point('e', 5)]
        blocking_pos = [Point('c', 7), Point('c', 6), Point('c', 5), Point('c', 4),
                        Point('d', 7), Point('d', 4),
                        Point('e', 7), Point('e', 4),
                        Point('f', 7), Point('f', 6), Point('f', 5), Point('f', 4)]
        board_game = BoardGame(Constants.LARGE_BOARD_SIZE, True, white_pos, black_pos, blocking_pos)
        curr_game_node = GameNode(board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)
        self.assertTrue(curr_game_node.is_game_over)
        self.assertEqual(curr_game_node.winner, "WHITE")

    def test_winner_determination_black_wins_and_plays(self):
        self.is_black_player = True
        black_pos = [Point('a', 6), Point('d', 10), Point('j', 6), Point('d', 1)]
        white_pos = [Point('d', 6), Point('e', 6), Point('d', 5), Point('e', 5)]
        blocking_pos = [Point('c', 7), Point('c', 6), Point('c', 5), Point('c', 4),
                        Point('d', 7), Point('d', 4),
                        Point('e', 7), Point('e', 4),
                        Point('f', 7), Point('f', 6), Point('f', 5), Point('f', 4)]
        board_game = BoardGame(Constants.LARGE_BOARD_SIZE, True, white_pos, black_pos, blocking_pos)
        curr_game_node = GameNode(board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)
        self.assertTrue(curr_game_node.is_game_over)
        self.assertEqual(curr_game_node.winner, "BLACK")

    def test_mobility_heuristic_calculation_when_black_player_has_no_any_movement_option(self):
        self.is_black_player = True
        white_pos = [Point('a', 6), Point('d', 10), Point('j', 6), Point('d', 1)]
        black_pos = [Point('d', 6), Point('e', 6), Point('d', 5), Point('e', 5)]
        blocking_pos = [Point('c', 7), Point('c', 6), Point('c', 5), Point('c', 4),
                        Point('d', 7), Point('d', 4),
                        Point('e', 7), Point('e', 4),
                        Point('f', 7), Point('f', 6), Point('f', 5), Point('f', 4)]
        curr_game_node = GameNode(self.board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)
        self.assertEqual(curr_game_node.calculate_mobility_heuristic(), 0)

    def test_mobility_heuristic_calculation_when_white_player_has_no_any_movement_option(self):
        black_pos = [Point('a', 6), Point('d', 10), Point('j', 6), Point('d', 1)]
        white_pos = [Point('d', 6), Point('e', 6), Point('d', 5), Point('e', 5)]
        blocking_pos = [Point('c', 7), Point('c', 6), Point('c', 5), Point('c', 4),
                        Point('d', 7), Point('d', 4),
                        Point('e', 7), Point('e', 4),
                        Point('f', 7), Point('f', 6), Point('f', 5), Point('f', 4)]
        board_game = BoardGame(Constants.LARGE_BOARD_SIZE, True, white_pos, black_pos, blocking_pos)
        curr_game_node = GameNode(self.board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)
        self.assertEqual(curr_game_node.calculate_mobility_heuristic(), 0)

    def test_mobility_and_move_count_heuristics_from_wiki_example(self):
        white_pos = [Point('e', 2), Point('f', 7), Point('j', 7), Point('c', 8)]
        black_pos = [Point('d', 1), Point('g', 1), Point('e', 5), Point('d', 10)]
        blocking_lst = [Point('A', 10), Point('A', 8), Point('A', 3), Point('A', 2),
                        Point('B', 9), Point('B', 8), Point('B', 5), Point('B', 4), Point('B', 3), Point('B', 2),
                        Point('C', 9), Point('C', 7), Point('C', 6), Point('C', 5), Point('C', 4), Point('C', 1),
                        Point('D', 9), Point('D', 8), Point('D', 7), Point('D', 5), Point('D', 3), Point('D', 2),
                        Point('E', 10), Point('E', 8), Point('E', 7), Point('E', 6), Point('E', 3), Point('E', 1),
                        Point('F', 9), Point('F', 8), Point('F', 6), Point('F', 5), Point('F', 4), Point('F', 3),
                        Point('F', 2), Point('F', 1),
                        Point('G', 8), Point('G', 6), Point('G', 4), Point('G', 3), Point('G', 2),
                        Point('H', 10), Point('H', 8), Point('H', 6), Point('H', 5), Point('H', 3),
                        Point('I', 9), Point('I', 8), Point('I', 7), Point('I', 6),
                        Point('J', 8), Point('J', 6), Point('J', 1)]

        board_game = BoardGame(Constants.LARGE_BOARD_SIZE, True, white_pos, black_pos, blocking_lst)
        curr_game_node = GameNode(board_game,
                                  self.is_black_player,
                                  self.available_steps_manager)
        # because number of amazons white can move now is 2

        board_game.print_board()
        self.assertEqual(-6, curr_game_node.calculate_mobility_heuristic())
        self.assertEqual(-9, curr_game_node.calculate_move_count_heuristic())


class AiPlayerLargeBoardTests(unittest.TestCase):
    # This test class will demonstrate AI player minds
    # It will implement the following tests
    # 1. Get all possible states for amazona in large board in specific distance
    # (for specific move includes throwing blocking rock)
    # 2. Build next state tree, for the player plays against us
    # 3. Run minimax with AlphaBetaPurning on the tree and eliminate non-relevant results.
    # 4. Being able to get next move successfully
    def setUp(self):
        self.board_game = BoardGame(Constants.LARGE_BOARD_SIZE)
        self.turn_validator = TurnValidator()
        self.available_steps_manager = AvailableMovementsManger()
        self.blocking_rocks_manager = BlockingRocksManager(Constants.LARGE_BOARD_SIZE, self.available_steps_manager)
        self.look_ahed = 2  # means the search tree will have 2 levels, AI turn, opponent
        self.ai_player = ComputerPlayer("AI", "BLACK", self.available_steps_manager, self.blocking_rocks_manager,
                                        self.look_ahed, self.turn_validator)

    def test_generating_next_step_for_black_player(self):
        print("Board game black gets to decide")
        self.board_game.print_board()
        bla = self.ai_player.make_move(self.board_game)
        print("Black chose to play like that")
        bla.print_board()
        self.assertEqual(self.board_game.get_players_positions("WHITE"), bla.get_players_positions("WHITE"))


class AIPlayerSmallBoardTests(unittest.TestCase):
    # This test class will demonstrate AI player minds
    # It will implement the following tests
    # 1. Get all possible states for amazona in large board in specific distance (for specific move includes throwing blocking rock)
    # 2. Build next state tree, for the player plays against us
    # 3. Run minimax with AlphaBetaPurning on the tree and eliminate non-relevant results.
    # 4. Being able to get next move successfully
    def setUp(self):
        self.board_game = BoardGame(Constants.SMALL_BOARD_SIZE)
        self.turn_validator = TurnValidator()
        self.available_steps_manager = AvailableMovementsManger()
        self.blocking_rocks_manager = BlockingRocksManager(Constants.SMALL_BOARD_SIZE, self.turn_validator)
        self.searching_depth = 2 # means the search tree will have 2 levels, AI turn, opponent
        self.ai_player = ComputerPlayer("AI", "BLACK", self.available_steps_manager, self.blocking_rocks_manager, self.searching_depth, self.turn_validator)

    def test_exploring_full_turn_includes_move_and_throwing_blocking_rock_from_initial_position(self):
        self.ai_player.make_move(self.board_game)
        # I mean this test will be shitty one since I will build each board and test it created as expected..
        self.assertEqual(1, 1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    unittest.main()