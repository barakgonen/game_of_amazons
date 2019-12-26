from constants import LARGE_BOARD_SIZE, SMALL_BOARD_SIZE
from board_game import BoardGame
from turn_validator import TurnValidator
from point import Point

def turn_validation_job():
    print "<turn_validation_job()> Running small board run from an empty board each time. just verifier for movement logic"
    number_of_passed_tests = 0
    static_start_pos = Point('D', 6)
    test_case1 = run_simple_test(static_start_pos, Point('D', 7), False, SMALL_BOARD_SIZE)
    if (not test_case1):
        raise RuntimeError("Error With case 1")
    number_of_passed_tests += 1

    test_case2 = run_simple_test(static_start_pos, Point('E', 7), False, SMALL_BOARD_SIZE)
    if (not test_case2):
        raise RuntimeError("Error With case 2")
    number_of_passed_tests += 1
    test_case3 = run_simple_test(static_start_pos, Point('E', 6), True, SMALL_BOARD_SIZE)
    if (not test_case3):
        raise RuntimeError("Error With case 3")
    number_of_passed_tests += 1
    test_case4 = run_simple_test(static_start_pos, Point('F', 6), True, SMALL_BOARD_SIZE)
    if (not test_case4):
        raise RuntimeError("Error With case 4")
    number_of_passed_tests += 1
    test_case5 = run_simple_test(static_start_pos, Point('G', 6), False, SMALL_BOARD_SIZE)
    if (not test_case5):
        raise RuntimeError("Error With case 5")
    number_of_passed_tests += 1    
    test_case6 = run_simple_test(static_start_pos, Point('E', 3), False, SMALL_BOARD_SIZE)
    if (not test_case6):
        raise RuntimeError("Error With case 6")
    number_of_passed_tests += 1    
    test_case7 = run_simple_test(static_start_pos, Point('H', 6), False, SMALL_BOARD_SIZE)
    if (not test_case7):
        raise RuntimeError("Error With case 7")
    number_of_passed_tests += 1
    test_case8 = run_simple_test(static_start_pos, Point('H', 5), False, SMALL_BOARD_SIZE)
    if (not test_case8):
        raise RuntimeError("Error With case 8")
    number_of_passed_tests += 1
    test_case9 = run_simple_test(static_start_pos, Point('F', 5), False, SMALL_BOARD_SIZE)
    if (not test_case9):
        raise RuntimeError("Error With case 9")
    number_of_passed_tests += 1    
    test_case10 = run_simple_test(static_start_pos, Point('E', 5), True, SMALL_BOARD_SIZE)
    if (not test_case10):
        raise RuntimeError("Error With case 10")
    number_of_passed_tests += 1    
    test_case11 = run_simple_test(static_start_pos, Point('F', 4), True, SMALL_BOARD_SIZE)
    if (not test_case11):
        raise RuntimeError("Error With case 11")
    number_of_passed_tests += 1    
    test_case12 = run_simple_test(static_start_pos, Point('F', 3), False, SMALL_BOARD_SIZE)
    if (not test_case12):
        raise RuntimeError("Error With case 12")
    number_of_passed_tests += 1    
    test_case13 = run_simple_test(static_start_pos, Point('D', 5), True, SMALL_BOARD_SIZE)
    if (not test_case13):
        raise RuntimeError("Error With case 13")
    number_of_passed_tests += 1    
    test_case14 = run_simple_test(static_start_pos, Point('E', 4), False, SMALL_BOARD_SIZE)
    if (not test_case14):
        raise RuntimeError("Error With case 14")
    number_of_passed_tests += 1    
    test_case15 = run_simple_test(static_start_pos, Point('D', 4), True, SMALL_BOARD_SIZE)
    if (not test_case15):
        raise RuntimeError("Error With case 15")
    number_of_passed_tests += 1    
    test_case16 = run_simple_test(static_start_pos, Point('D', 3), True, SMALL_BOARD_SIZE)
    if (not test_case16):
        raise RuntimeError("Error With case 16")
    number_of_passed_tests += 1    
    test_case17 = run_simple_test(static_start_pos, Point('D', 2), True, SMALL_BOARD_SIZE)
    if (not test_case17):
        raise RuntimeError("Error With case 17")
    number_of_passed_tests += 1    
    test_case18 = run_simple_test(static_start_pos, Point('D', 1), True, SMALL_BOARD_SIZE)
    if (not test_case18):
        raise RuntimeError("Error With case 18")
    number_of_passed_tests += 1    
    test_case19 = run_simple_test(static_start_pos, Point('D', -1), False, SMALL_BOARD_SIZE)
    if (not test_case19):
        raise RuntimeError("Error With case 19")
    number_of_passed_tests += 1    
    test_case20 = run_simple_test(static_start_pos, Point('C', 5), True, SMALL_BOARD_SIZE)
    if (not test_case20):
        raise RuntimeError("Error With case 20")
    number_of_passed_tests += 1
    test_case21 = run_simple_test(static_start_pos, Point('B', 4), True, SMALL_BOARD_SIZE)
    if (not test_case21):
        raise RuntimeError("Error With case 21")
    number_of_passed_tests += 1
    test_case22 = run_simple_test(static_start_pos, Point('A', 4), False, SMALL_BOARD_SIZE)
    if (not test_case22):
        raise RuntimeError("Error With case 22")
    number_of_passed_tests += 1
    test_case23 = run_simple_test(static_start_pos, Point('C', 6), True, SMALL_BOARD_SIZE)
    if (not test_case23):
        raise RuntimeError("Error With case 3")
    test_case24 = run_simple_test(static_start_pos, Point('B', 6), True, SMALL_BOARD_SIZE)
    number_of_passed_tests += 1
    if (not test_case24):
        raise RuntimeError("Error With case 4")
    test_case25 = run_simple_test(static_start_pos, Point('A', 6), True, SMALL_BOARD_SIZE)
    number_of_passed_tests += 1
    if (not test_case25):
        raise RuntimeError("Error With case 25")
    number_of_passed_tests += 1
    test_case26 = run_simple_test(static_start_pos, Point('B', 5), False, SMALL_BOARD_SIZE)
    if (not test_case26):
        raise RuntimeError("Error With case 26")
    number_of_passed_tests += 1

    static_start_pos = Point('F', 3)

    test_case27 = run_simple_test(static_start_pos, Point('G', 3), False, SMALL_BOARD_SIZE)
    if (not test_case27):
        raise RuntimeError("Error With case 27")
    number_of_passed_tests += 1
    test_case28 = run_simple_test(static_start_pos, Point('H', 3), False, SMALL_BOARD_SIZE)
    if (not test_case28):
        raise RuntimeError("Error With case 28")
    number_of_passed_tests += 1
    test_case29 = run_simple_test(static_start_pos, Point('H', 2), False, SMALL_BOARD_SIZE)
    if (not test_case29):
        raise RuntimeError("Error With case 29")
    number_of_passed_tests += 1
    test_case30 = run_simple_test(static_start_pos, Point('G', 2), False, SMALL_BOARD_SIZE)
    if (not test_case30):
        raise RuntimeError("Error With case 30")
    number_of_passed_tests += 1
    test_case31 = run_simple_test(static_start_pos, Point('F', 2), True, SMALL_BOARD_SIZE)
    if (not test_case31):
        raise RuntimeError("Error With case 31")
    number_of_passed_tests += 1
    test_case32 = run_simple_test(static_start_pos, Point('F', 1), True, SMALL_BOARD_SIZE)
    if (not test_case32):
        raise RuntimeError("Error With case 32")
    number_of_passed_tests += 1
    test_case33 = run_simple_test(static_start_pos, Point('D', 1), True, SMALL_BOARD_SIZE)
    if (not test_case33):
        raise RuntimeError("Error With case 33")
    number_of_passed_tests += 1
    test_case34 = run_simple_test(static_start_pos, Point('E', 1), False, SMALL_BOARD_SIZE)
    if (not test_case34):
        raise RuntimeError("Error With case 34")
    number_of_passed_tests += 1
    test_case35 = run_simple_test(static_start_pos, Point('D', 2), False, SMALL_BOARD_SIZE)
    if (not test_case35):
        raise RuntimeError("Error With case 35")
    number_of_passed_tests += 1
    test_case36 = run_simple_test(static_start_pos, Point('E', 3), True, SMALL_BOARD_SIZE)
    if (not test_case36):
        raise RuntimeError("Error With case 36")
    number_of_passed_tests += 1
    test_case37 = run_simple_test(static_start_pos, Point('C', 6), True, SMALL_BOARD_SIZE)
    if (not test_case37):
        raise RuntimeError("Error With case 37")
    number_of_passed_tests += 1
    test_case38 = run_simple_test(static_start_pos, Point('@', 3), False, SMALL_BOARD_SIZE)
    if (not test_case38):
        raise RuntimeError("Error With case 38")
    number_of_passed_tests += 1
    test_case39 = run_simple_test(static_start_pos, Point('C', 3), True, SMALL_BOARD_SIZE)
    if (not test_case39):
        raise RuntimeError("Error With case 39")
    number_of_passed_tests += 1
    test_case40 = run_simple_test(static_start_pos, Point('G', 4), False, SMALL_BOARD_SIZE)
    if (not test_case40):
        raise RuntimeError("Error With case 40")
    number_of_passed_tests += 1
    test_case41 = run_simple_test(static_start_pos, Point('E', 4), True, SMALL_BOARD_SIZE)
    if (not test_case41):
        raise RuntimeError("Error With case 41")
    number_of_passed_tests += 1
    test_case42 = run_simple_test(static_start_pos, Point('F', -1), False, SMALL_BOARD_SIZE)
    if (not test_case42):
        raise RuntimeError("Error With case 42")
    number_of_passed_tests += 1

    static_start_pos = Point('C', 1)

    test_case43 = run_simple_test(static_start_pos, Point('C', -1), False, SMALL_BOARD_SIZE)
    if (not test_case43):
        raise RuntimeError("Error With case 43")
    number_of_passed_tests += 1
    test_case44 = run_simple_test(static_start_pos, Point('D', -1), False, SMALL_BOARD_SIZE)
    if (not test_case44):
        raise RuntimeError("Error With case 44")
    number_of_passed_tests += 1
    test_case45 = run_simple_test(static_start_pos, Point('D', 1), True, SMALL_BOARD_SIZE)
    if (not test_case45):
        raise RuntimeError("Error With case 45")
    number_of_passed_tests += 1
    test_case46 = run_simple_test(static_start_pos, Point('E', 1), True, SMALL_BOARD_SIZE)
    if (not test_case46):
        raise RuntimeError("Error With case 46")
    number_of_passed_tests += 1
    test_case47 = run_simple_test(static_start_pos, Point('G', 1), False, SMALL_BOARD_SIZE)
    if (not test_case47):
        raise RuntimeError("Error With case 47")
    number_of_passed_tests += 1
    test_case48 = run_simple_test(static_start_pos, Point('K', 1), False, SMALL_BOARD_SIZE)
    if (not test_case48):
        raise RuntimeError("Error With case 48")
    number_of_passed_tests += 1
    test_case49 = run_simple_test(static_start_pos, Point('E', 2), False, SMALL_BOARD_SIZE)
    if (not test_case49):
        raise RuntimeError("Error With case 49")
    number_of_passed_tests += 1
    test_case50 = run_simple_test(static_start_pos, Point('D', 2), True, SMALL_BOARD_SIZE)
    if (not test_case50):
        raise RuntimeError("Error With case 50")
    number_of_passed_tests += 1
    test_case51 = run_simple_test(static_start_pos, Point('C', 2), True, SMALL_BOARD_SIZE)
    if (not test_case51):
        raise RuntimeError("Error With case 51")
    number_of_passed_tests += 1
    test_case52 = run_simple_test(static_start_pos, Point('C', 3), True, SMALL_BOARD_SIZE)
    if (not test_case52):
        raise RuntimeError("Error With case 52")
    number_of_passed_tests += 1
    test_case53 = run_simple_test(static_start_pos, Point('C', 7), False, SMALL_BOARD_SIZE)
    if (not test_case53):
        raise RuntimeError("Error With case 53")
    number_of_passed_tests += 1
    test_case54 = run_simple_test(static_start_pos, Point('B', 3), False, SMALL_BOARD_SIZE)
    if (not test_case54):
        raise RuntimeError("Error With case 54")
    number_of_passed_tests += 1
    test_case55 = run_simple_test(static_start_pos, Point('B', 5), False, SMALL_BOARD_SIZE)
    if (not test_case55):
        raise RuntimeError("Error With case 55")
    number_of_passed_tests += 1
    test_case56 = run_simple_test(static_start_pos, Point('B', 2), True, SMALL_BOARD_SIZE)
    if (not test_case56):
        raise RuntimeError("Error With case 56")
    number_of_passed_tests += 1
    test_case57 = run_simple_test(static_start_pos, Point('@', 4), False, SMALL_BOARD_SIZE)
    if (not test_case57):
        raise RuntimeError("Error With case 57")
    number_of_passed_tests += 1
    test_case58 = run_simple_test(static_start_pos, Point('A', 2), False, SMALL_BOARD_SIZE)
    if (not test_case58):
        raise RuntimeError("Error With case 58")
    number_of_passed_tests += 1
    test_case59 = run_simple_test(static_start_pos, Point('B', 1), True, SMALL_BOARD_SIZE)
    if (not test_case59):
        raise RuntimeError("Error With case 59")
    number_of_passed_tests += 1
    test_case60 = run_simple_test(static_start_pos, Point('A', 1), True, SMALL_BOARD_SIZE)
    if (not test_case60):
        raise RuntimeError("Error With case 60")
    number_of_passed_tests += 1
    test_case61 = run_simple_test(static_start_pos, Point('@', 1), False, SMALL_BOARD_SIZE)
    if (not test_case61):
        raise RuntimeError("Error With case 61")
    number_of_passed_tests += 1

    print "Total number of passed tests: " + str(number_of_passed_tests)

# if (board_game.get_size() == LARGE_BOARD_SIZE):
# elif (board_game.get_size() == SMALL_BOARD_SIZE):
#     print "<turn_validation_job()> Small board tests run"
#     # each line represents test case. checking each line returns expected value.. not using pyunit or something..


def run_simple_test(amazon_to_move, new_position, expected_result, board_size):
    board_game = BoardGame(board_size)
    turn_validator = TurnValidator(board_game)
    return expected_result == turn_validator.is_step_valid(amazon_to_move, new_position)
