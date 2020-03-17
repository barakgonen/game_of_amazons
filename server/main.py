from server.src.available_steps_manager import AvailableMovementsManger
from server.src.constants import Constants
from server.src.board_game import BoardGame
from server.src.game_manager import GameManager
from server.src.game_node import GameNode
from server.src.turn_validator import TurnValidator
from server.src.player import ComputerPlayer, HumanPlayer
from server.src.blocking_rocks_manager import BlockingRocksManager
import time
import subprocess
import sys


def foo(n):
    for i in range(10000 * n):
        print ("Tick")
        time.sleep(1)

def __get_board_size():
    is_input_valid = False
    while not is_input_valid:
        try:
            board_size = int(input("Enter prefered board size: " + str(Constants.LARGE_BOARD_SIZE) + "^2 or: " + str(
                Constants.SMALL_BOARD_SIZE) + "^2"))
        except Exception:
            print("Your input is invalid.. please try again.")
            continue
        if board_size != Constants.LARGE_BOARD_SIZE and board_size != Constants.SMALL_BOARD_SIZE:
            print("Your input is invalid.. please try again.")
        else:
            is_input_valid = True
            return board_size


def __get_game_mode():
    is_input_valid = False
    while not is_input_valid:
        try:
            game_mode = int(input(""))
        except Exception:
            print("Your input is invalid.. please try again.")
            continue
        if game_mode != Constants.OPONNENT_MODE and game_mode != Constants.ONE_ON_ONE:
            print("Please choose valid game mode, 1 or 2")
        else:
            is_input_valid = True
            return game_mode


def __get_desired_searching_depth(second_time=False):
    if not second_time:
        is_input_valid = False
        while not is_input_valid:
            try:
                depth = int(input("Please, tell me how deep to look at the tree"))
            except Exception:
                print("Your input is invalid.. please try again.")
                continue
            if depth > 4:
                print("depth greater than 4 is not supported by the programmer since it might take long time..")
            else:
                is_input_valid = True
                return depth
    else:
        print("Hi, you allowed to set another searching depth to the second agent, so please choose:")
        return __get_desired_searching_depth()


def __get_number_of_repetting_games(second_time=False):
    if not second_time:
        is_input_valid = False
        while not is_input_valid:
            try:
                repetting_games = int(input("Do you want to make a tournament? how many games you want me to play against myself?"))
            except Exception:
                print("Your input is invalid.. please try again.")
                continue
            else:
                is_input_valid = True
                return repetting_games
    else:
        print("Hi, you allowed to set another searching depth to the second agent, so please choose:")
        return __get_desired_searching_depth()


def __get_running_time_in_sec():
    is_input_valid = False
    while not is_input_valid:
        try:
            time_sec = int(input("Insert number of minutes to think"))
        except Exception:
            print("Your input is invalid.. please try again.")
            continue
        else:
            is_input_valid = True
            return time_sec * 60


def install_deps(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def main():
    install_deps("numpy")
    install_deps("pandas")
    print("=============================================")
    print("Welcome to my version of The Game of Amazons!")
    print("=============================================")
    print("Game developed as final project in course: Introduction to Artificial Intelligence, by Shay Bushinsky, "
          "Haifa University")
    print("Let's start playing! Choose 1 of the following options:")
    print("1 if you would like to play against me XD")
    print("2 if you want me to play against myself")
    playing_mode = int(__get_game_mode())
    board_size = int(__get_board_size())
    searching_depth = int(__get_desired_searching_depth())
    board_game = BoardGame(board_size)
    available_steps_manager = AvailableMovementsManger()
    blocking_rocks_manager = BlockingRocksManager(board_size, available_steps_manager)
    turn_validator = TurnValidator()
    time_in_seconds = int(__get_running_time_in_sec())
    current_game_node = GameNode(board_game, False, available_steps_manager)

    if playing_mode == Constants.OPONNENT_MODE:
        p1 = HumanPlayer("BARAK", "WHITE")
        p2 = ComputerPlayer("ALGORITHM", "BLACK", available_steps_manager, blocking_rocks_manager, searching_depth, turn_validator)
        manager = GameManager(p2, p1, turn_validator, current_game_node, blocking_rocks_manager, available_steps_manager)
        winner = manager.run_game()
    else:
        p1 = ComputerPlayer("ALGO-WHITE", "WHITE", available_steps_manager, blocking_rocks_manager, searching_depth, turn_validator)
        searching_depth = int(__get_desired_searching_depth(True))
        p2 = ComputerPlayer("ALGO-BLACK", "BLACK", available_steps_manager, blocking_rocks_manager, searching_depth, turn_validator)
        is_it_a_compatition = int(__get_number_of_repetting_games())
        winners = dict()
        winners[0] = 0
        winners[1] = 0
        winners[2] = 0
        for i in range(1, is_it_a_compatition+1):
            print("--------------------------------GAME NUMBER: " + str(i) + "Started ----------------------------------")
            manager = GameManager(p2, p1, turn_validator, current_game_node, blocking_rocks_manager, available_steps_manager)
            winner = int(manager.run_game())
            winners[winner] += 1
            print("--------------------------------GAME NUMBER: " + str(i) + "Ended ----------------------------------")
        if winners[1] > winners[2]:
            print("BLACK has won the tournament!, score: " + str(winners[1]) + ":" + str(winners[2]))
        elif winners[2] > winners[1]:
            print("WHITE won the tournament! score: " + str(winners[1]) + ":" + str(winners[2]))
        else:
            print("THERE IS A TIE")


if __name__ == "__main__":
    main()