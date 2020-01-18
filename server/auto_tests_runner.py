from constants import LARGE_BOARD_SIZE, SMALL_BOARD_SIZE, CellState, COLUMNS_ARRAY, NUMBER_OF_ROCKS_IN_SMALL_BOARD, NUMBER_OF_ROCKS_IN_LARGE_BOARD
from board_game import BoardGame
from turn_validator import TurnValidator
from point import Point
from blocking_rocks_manager import BlockingRocksManager
from player import ComputerPlayer, HumanPlayer
from game_manager import GameManager

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
        raise RuntimeError("Error With case 23")
    test_case24 = run_simple_test(static_start_pos, Point('B', 6), True, SMALL_BOARD_SIZE)
    number_of_passed_tests += 1
    if (not test_case24):
        raise RuntimeError("Error With case 24")
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

    static_start_pos = Point('D', 10)

    test_case62 = run_simple_test(static_start_pos, Point('d', 11), False, LARGE_BOARD_SIZE)
    if (not test_case62):
        raise RuntimeError("Error With case 62")
    number_of_passed_tests += 1
    test_case63 = run_simple_test(static_start_pos, Point('@', 10), False, LARGE_BOARD_SIZE)
    if (not test_case63):
        raise RuntimeError("Error With case 63")
    number_of_passed_tests += 1
    test_case64 = run_simple_test(static_start_pos, Point('A', 10), True, LARGE_BOARD_SIZE)
    if (not test_case64):
        raise RuntimeError("Error With case 64")
    number_of_passed_tests += 1
    test_case65 = run_simple_test(static_start_pos, Point('A', 7), False, LARGE_BOARD_SIZE)
    if (not test_case65):
        raise RuntimeError("Error With case 65")
    number_of_passed_tests += 1
    test_case66 = run_simple_test(static_start_pos, Point('D', 9), True, LARGE_BOARD_SIZE)
    if (not test_case66):
        raise RuntimeError("Error With case 66")
    number_of_passed_tests += 1
    test_case67 = run_simple_test(static_start_pos, Point('B', 9), False, LARGE_BOARD_SIZE)
    if (not test_case67):
        raise RuntimeError("Error With case 67")
    number_of_passed_tests += 1
    test_case68 = run_simple_test(static_start_pos, Point('D', 8), True, LARGE_BOARD_SIZE)
    if (not test_case68):
        raise RuntimeError("Error With case 68")
    number_of_passed_tests += 1
    test_case69 = run_simple_test(static_start_pos, Point('D', 1), False, LARGE_BOARD_SIZE)
    if (not test_case69):
        raise RuntimeError("Error With case 69")
    number_of_passed_tests += 1
    test_case70 = run_simple_test(static_start_pos, Point('D', -1), False, LARGE_BOARD_SIZE)
    if (not test_case70):
        raise RuntimeError("Error With case 70")
    number_of_passed_tests += 1
    test_case71 = run_simple_test(static_start_pos, Point('D', 2), True, LARGE_BOARD_SIZE)
    if (not test_case71):
        raise RuntimeError("Error With case 71")
    number_of_passed_tests += 1
    test_case72 = run_simple_test(static_start_pos, Point('J', 4), False, LARGE_BOARD_SIZE)
    if (not test_case72):
        raise RuntimeError("Error With case 72")
    number_of_passed_tests += 1
    test_case73 = run_simple_test(static_start_pos, Point('I', 5), True, LARGE_BOARD_SIZE)
    if (not test_case73):
        raise RuntimeError("Error With case 73")
    number_of_passed_tests += 1
    test_case74 = run_simple_test(static_start_pos, Point('H', 10), False, LARGE_BOARD_SIZE)
    if (not test_case74):
        raise RuntimeError("Error With case 74")
    number_of_passed_tests += 1
    test_case75 = run_simple_test(static_start_pos, Point('K', 10), False, LARGE_BOARD_SIZE)
    if (not test_case75):
        raise RuntimeError("Error With case 75")
    number_of_passed_tests += 1
    test_case76 = run_simple_test(static_start_pos, Point('E', 10), True, LARGE_BOARD_SIZE)
    if (not test_case76):
        raise RuntimeError("Error With case 76")
    number_of_passed_tests += 1

    static_start_pos = Point('G', 1)

    test_case77 = run_simple_test(static_start_pos, Point('G', -1), False, LARGE_BOARD_SIZE)
    if (not test_case77):
        raise RuntimeError("Error With case 77")
    number_of_passed_tests += 1
    test_case78 = run_simple_test(static_start_pos, Point('K', 1), False, LARGE_BOARD_SIZE)
    if (not test_case78):
        raise RuntimeError("Error With case 78")
    number_of_passed_tests += 1
    test_case79 = run_simple_test(static_start_pos, Point('I', 2), False, LARGE_BOARD_SIZE)
    if (not test_case79):
        raise RuntimeError("Error With case 79")
    number_of_passed_tests += 1
    test_case80 = run_simple_test(static_start_pos, Point('J', 4), False, LARGE_BOARD_SIZE)
    if (not test_case80):
        raise RuntimeError("Error With case 80")
    number_of_passed_tests += 1
    test_case81 = run_simple_test(static_start_pos, Point('I', 3), True, LARGE_BOARD_SIZE)
    if (not test_case81):
        raise RuntimeError("Error With case 81")
    number_of_passed_tests += 1
    test_case82 = run_simple_test(static_start_pos, Point('H', 3), False, LARGE_BOARD_SIZE)
    if (not test_case82):
        raise RuntimeError("Error With case 82")
    number_of_passed_tests += 1
    test_case83 = run_simple_test(static_start_pos, Point('G', 9), True, LARGE_BOARD_SIZE)
    if (not test_case83):
        raise RuntimeError("Error With case 83")
    number_of_passed_tests += 1
    test_case84 = run_simple_test(static_start_pos, Point('G', 10), False, LARGE_BOARD_SIZE)
    if (not test_case84):
        raise RuntimeError("Error With case 84")
    number_of_passed_tests += 1
    test_case85 = run_simple_test(static_start_pos, Point('G', 11), False, LARGE_BOARD_SIZE)
    if (not test_case85):
        raise RuntimeError("Error With case 85")
    number_of_passed_tests += 1
    test_case86 = run_simple_test(static_start_pos, Point('B', 6), True, LARGE_BOARD_SIZE)
    if (not test_case86):
        raise RuntimeError("Error With case 86")
    number_of_passed_tests += 1
    test_case87 = run_simple_test(static_start_pos, Point('B', 7), False, LARGE_BOARD_SIZE)
    if (not test_case87):
        raise RuntimeError("Error With case 87")
    number_of_passed_tests += 1
    test_case88 = run_simple_test(static_start_pos, Point('E', 1), True, LARGE_BOARD_SIZE)
    if (not test_case88):
        raise RuntimeError("Error With case 88")
    number_of_passed_tests += 1
    test_case89 = run_simple_test(static_start_pos, Point('D', 1), False, LARGE_BOARD_SIZE)
    if (not test_case89):
        raise RuntimeError("Error With case 89")
    number_of_passed_tests += 1
    test_case90 = run_simple_test(static_start_pos, Point('C', 1), False, LARGE_BOARD_SIZE)
    if (not test_case90):
        raise RuntimeError("Error With case 90")
    number_of_passed_tests += 1
    test_case91 = run_simple_test(static_start_pos, Point('@', 1), False, LARGE_BOARD_SIZE)
    if (not test_case91):
        raise RuntimeError("Error With case 91")
    number_of_passed_tests += 1

    print "<turn_validation_job()> Total number of passed tests: " + str(number_of_passed_tests)

def blocking_cell_validation_job():
    print "<blocking_cell_validation_job()> Verifier for movement in blocked cells area"
    number_of_passed_tests = 0
    static_start_pos = Point('C', 1)
    # blocked positions
    blocking_lst = [Point('B', 3), Point('B', 2), Point('B', 1), Point('C', 1), 
                    Point('D', 1), Point('D', 2), Point('D', 3), Point('C', 3)]
    test_board = get_blocked_board(static_start_pos, Point('C', 2), SMALL_BOARD_SIZE, "WHITE", blocking_lst)

    #rest of the board, for extra verification
    additional_blocking_lst = [Point('A', 1), Point('A', 2), Point('A', 3), Point('A', 4), Point('A', 5), Point('A', 6),  
                               Point('B', 4), Point('B', 5), Point('B', 6),
                               Point('C', 4), Point('C', 5), Point('C', 6),
                               Point('D', 4), Point('D', 5), Point('D', 6),
                               Point('E', 1), Point('e', 2), Point('E', 3), Point('e', 4), Point('E', 5), Point('E', 6),
                               Point('F', 1), Point('F', 2), Point('F', 3), Point('F', 4), Point('F', 5), Point('F', 6)]
    # Appending lists for test
    blocking_lst.extend(additional_blocking_lst)

    # after getting board prepared, need to run the tests on it
    is_test_fine = run_loop_of_simple_movement_tests(Point('C', 2), blocking_lst, False, test_board)
    if (not is_test_fine):
        raise RuntimeError("Error With case 1")
    number_of_passed_tests += 1

    static_start_pos = Point('C', 1)
    # blocked positions
    blocking_lst = [Point('B', 3), Point('B', 2), Point('B', 1), Point('C', 1), 
                    Point('D', 1), Point('D', 2), Point('D', 3), Point('C', 3)]
    test_board = get_blocked_board(static_start_pos, Point('C', 2), SMALL_BOARD_SIZE, "WHITE", blocking_lst)

    #rest of the board, for extra verification
    additional_blocking_lst = [Point('A', 1), Point('A', 2), Point('A', 3), Point('A', 4), Point('A', 5), Point('A', 6),  
                               Point('B', 4), Point('B', 5), Point('B', 6),
                               Point('C', 4), Point('C', 5), Point('C', 6),
                               Point('D', 4), Point('D', 5), Point('D', 6),
                               Point('E', 1), Point('e', 2), Point('E', 3), Point('e', 4), Point('E', 5), Point('E', 6),
                               Point('F', 1), Point('F', 2), Point('F', 3), Point('F', 4), Point('F', 5), Point('F', 6)]
    # Appending lists for test
    blocking_lst.extend(additional_blocking_lst)

    # after getting board prepared, need to run the tests on it
    is_test_fine = run_loop_of_simple_movement_tests(Point('C', 2), blocking_lst, False, test_board)
    if (not is_test_fine):
        raise RuntimeError("Error With case 1")
    number_of_passed_tests += 1

    # new test case
    # testing turn starting with white amazon at 'D'/6
    static_start_pos = Point('d', 6)
    
    # moving the amazon verticly to 'D'/3
    new_position = Point('D', 3)

    # When the amazon will arive 'C'/3 it will shoot blocking rock to 'B'/3
    blocking_lst = [Point('B', 3)]

    #rest of the board, for extra verification
    test_board = get_blocked_board(static_start_pos, new_position, SMALL_BOARD_SIZE, "WHITE", blocking_lst)
    test_board.print_board()

    # i'd like to test invalid_movement mechanisem, that why i take 2 possible celss and tests that in the next move, the amazon couldn't reach them
    unavailable_cells = [Point('A', 3)]
    # Appending lists for test, amazon could not pass above blocked cell & the cells i mentioned above
    blocking_lst.extend(unavailable_cells)

    # after getting board prepared, need to run the tests on it
    is_test_fine = run_loop_of_simple_movement_tests(new_position, blocking_lst, False, test_board)
    if (not is_test_fine):
        raise RuntimeError("Error With case 2")

    # adding unavailable targets as well
    additional_unavailable_targets = [Point('A', 1), Point('A', 2), Point('A', 3), Point('A', 4), Point('A', 5),
                                      Point('B', 2), Point('B', 3), Point('B', 4), Point('B', 6),
                                      Point('C', 1), Point('C', 5), Point('C', 6),
                                      Point('D', 3),
                                      Point('E', 1), Point('E', 2), Point('e', 5), Point('E', 6),
                                      Point('F', 6), Point('F', 4), Point('F', 3), Point('F', 2)]
    available_moves = [Point('A', 6),
                       Point('B', 1), Point('B', 5), 
                       Point('C', 4), Point('C', 3), Point('C', 2), 
                       Point('D', 1), Point('D', 2), Point('D', 4), Point('D', 5), Point('D', 6), 
                       Point('E', 3), Point('E', 4), 
                       Point('F', 1), Point('F', 5)]
    is_additional_unavailable_moves_are_unavailable = run_loop_of_simple_movement_tests(new_position, additional_unavailable_targets, False, test_board)
    if (not is_additional_unavailable_moves_are_unavailable):
        raise RuntimeError("Error with case 3")
    number_of_passed_tests += 1
    is_additional_available_moves_are_available = run_loop_of_simple_movement_tests(new_position, available_moves, True, test_board)
    if (not is_additional_available_moves_are_available):
        raise RuntimeError("Error with case 4")
    number_of_passed_tests += 1
#end testcase

# new test case
    # testing turn starting with white amazon at 'C'/1
    static_start_pos = Point('C', 1)
    
    # moving the amazon verticly to 'C'/3
    new_position = Point('C', 3)

    # When the amazon will arive 'C'/3 it will shoot blocking rock to 'C'/4
    blocking_lst = [Point('C', 4)]

    #rest of the board, for extra verification
    test_board = get_blocked_board(static_start_pos, new_position, SMALL_BOARD_SIZE, "WHITE", blocking_lst)
    test_board.print_board()

    # i'd like to test invalid_movement mechanisem, that why i take 2 possible celss and tests that in the next move, the amazon couldn't reach them
    unavailable_cells = [Point('C', 5), Point('C', 6)]
    # Appending lists for test, amazon could not pass above blocked cell & the cells i mentioned above
    blocking_lst.extend(unavailable_cells)

    # after getting board prepared, need to run the tests on it
    is_test_fine = run_loop_of_simple_movement_tests(new_position, blocking_lst, False, test_board)
    if (not is_test_fine):
        raise RuntimeError("Error With case 2")

    # adding unavailable targets as well
    additional_unavailable_targets = [Point('A', 2), Point('A', 4), Point('A', 6),  
                                      Point('B', 1), Point('B', 5), Point('B', 6),
                                      Point('C', 3), Point('C', 4), Point('C', 5), Point('C', 6),
                                      Point('D', 1), Point('D', 5), Point('D', 6),
                                      Point('E', 2), Point('e', 4), Point('E', 6),
                                      Point('F', 1), Point('F', 2), Point('F', 3), Point('F', 4), Point('F', 5)]
    available_moves = [Point('A', 5), Point('A', 3), Point('A', 1),
                       Point('B', 4), Point('B', 3), Point('B', 2), 
                       Point('C', 2), Point('C', 1), 
                       Point('D', 4), Point('D', 3), Point('D', 2), 
                       Point('e', 1), Point('E', 3), Point('E', 5), 
                       Point('F', 6)]
    is_additional_unavailable_moves_are_unavailable = run_loop_of_simple_movement_tests(new_position, additional_unavailable_targets, False, test_board)
    if (not is_additional_unavailable_moves_are_unavailable):
        raise RuntimeError("Error with case 3")
    number_of_passed_tests += 1
    is_additional_available_moves_are_available = run_loop_of_simple_movement_tests(new_position, available_moves, True, test_board)
    if (not is_additional_available_moves_are_available):
        raise RuntimeError("Error with case 4")
    number_of_passed_tests += 1
#end testcase

    # testing turn starting with black amazon at 'F'/3
    static_start_pos = Point('F', 3)
    
    # moving the amazon diagonaly to 'D'/5
    new_position = Point('D', 5)

    # When the amazon will arive at 'D'/5 it will shoot blocking rock to 'F'/3
    blocking_lst = [Point('F', 3)]

    #rest of the board, for extra verification
    test_board = get_blocked_board(static_start_pos, new_position, SMALL_BOARD_SIZE, "BLACK", blocking_lst)
    test_board.print_board()

    # i'd like to test invalid_movement mechanisem, that why i take 2 possible celss and tests that in the next move, the amazon couldn't reach them
    unavailable_cells = [Point('F', 3), Point('G', 2)]
    # Appending lists for test, amazon could not pass above blocked cell & the cells i mentioned above
    blocking_lst.extend(unavailable_cells)

    # after getting board prepared, need to run the tests on it
    is_test_fine = run_loop_of_simple_movement_tests(new_position, blocking_lst, False, test_board)
    if (not is_test_fine):
        raise RuntimeError("Error With case 2")

    # adding unavailable targets as well
    additional_unavailable_targets = [Point('A', 6), Point('A', 4), Point('A', 3), Point('A', 1),
                                      Point('B', 6), Point('B', 4), Point('B', 2), Point('B', 1),
                                      Point('C', 1), Point('C', 2), Point('C', 3), 
                                      Point('D', 5), Point('D', 6),
                                      Point('E', 3), Point('e', 2), Point('E', 1),
                                      Point('F', 1), Point('F', 2), Point('F', 3), Point('F', 4), Point('F', 5), Point('F', 6)]
    available_moves = [Point('A', 5), Point('A', 2),
                       Point('B', 5), Point('B', 3),  
                       Point('C', 4), Point('C', 5), Point('C', 6),
                       Point('D', 4), Point('D', 3), Point('D', 2), Point('D', 1),
                       Point('e', 6), Point('E', 5), Point('E', 4)]

    is_additional_unavailable_moves_are_unavailable = run_loop_of_simple_movement_tests(new_position, additional_unavailable_targets, False, test_board)
    if (not is_additional_unavailable_moves_are_unavailable):
        raise RuntimeError("Error with case 3")
    number_of_passed_tests += 1

    is_additional_available_moves_are_available = run_loop_of_simple_movement_tests(new_position, available_moves, True, test_board)
    if (not is_additional_available_moves_are_available):
        raise RuntimeError("Error with case 4")
    number_of_passed_tests += 1


# new test case
    # testing turn starting with black amazon at A/4
    # Assuming all amazons are on default locations on small board
    static_start_pos = Point('A', 4)

    # starting with blocked board, with 6 blockers
    blockers_pos = [Point('A', 6), Point('A', 2), Point('B', 5), Point('b', 3),
                    Point('B', 2), Point('D', 5), Point('D', 3)]

    test_board = get_initialized_board(SMALL_BOARD_SIZE, blockers_pos)

    valid_movements = [Point('A', 5), Point('A', 3), 
                       Point('B', 4), 
                       Point('C', 4), 
                       Point('D', 4),
                       Point('E', 4),
                       Point('F', 4)]
    invalid_movements = [Point('A', 6), Point('A', 4), Point('A', 2), Point('A', 1),
                         Point('B', 6), Point('B', 5), Point('B', 3), Point('B', 2), Point('B', 1),
                         Point('C', 6), Point('C', 5), Point('C', 3), Point('C', 2), Point('C', 1),
                         Point('D', 6), Point('D', 5), Point('D', 3), Point('D', 2), Point('D', 1),
                         Point('E', 6), Point('E', 5), Point('E', 3), Point('E', 2), Point('E', 1),
                         Point('f', 6), Point('fE', 5), Point('f', 3), Point('f', 2), Point('f', 1)]
    
    # after getting board prepared, need to run the tests on it
    is_test_fine = run_loop_of_simple_movement_tests(static_start_pos, invalid_movements, False, test_board)
    if (not is_test_fine):
        raise RuntimeError("Error With case 2")
    number_of_passed_tests += 1
    is_additional_available_moves_are_available = run_loop_of_simple_movement_tests(static_start_pos, valid_movements, True, test_board)
    if (not is_additional_available_moves_are_available):
        raise RuntimeError("Error with case 4")
    number_of_passed_tests += 1
#end testcase

    print ("<blocking_cell_validation_job()> Job ended successfully! run: " + str(number_of_passed_tests) + " tests")

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

def turns_possible_job():
    # Test cases
    # 0 turns possible with full board
    current_board = BoardGame(LARGE_BOARD_SIZE)
    set_full_blocked_board(current_board)
    turn_validator = TurnValidator(current_board)
    is_game_over = not(turn_validator.is_there_are_available_mooves_for_player(CellState.WHITE_AMAZON) and turn_validator.is_there_are_available_mooves_for_player(CellState.BLACK_AMAZON))

    if (not is_game_over):
        raise RuntimeError("Error with case 44")
    current_board.print_board()
    
    # 0 turns possible with small board
    current_board = BoardGame(SMALL_BOARD_SIZE)
    set_full_blocked_board(current_board)
    turn_validator = TurnValidator(current_board)
    is_game_over = not(turn_validator.is_there_are_available_mooves_for_player(CellState.WHITE_AMAZON) and turn_validator.is_there_are_available_mooves_for_player(CellState.BLACK_AMAZON))

    if (not is_game_over):
        raise RuntimeError("Error with case 44")
    current_board.print_board()

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
    # 1 turn possible for black
    board_game = BoardGame(SMALL_BOARD_SIZE)
    turn_validator = TurnValidator(board_game)
    board_game.print_board()
    
    # 1 turn possible for white
    # 2 turns possible for black
    # 2 turns possible for white
    # 10 turns possible for black
    # 10 turns possible for white


    # large board tests
    # 1 turn possible for black
    # 1 turn possible for white
    # 2 turns possible for black
    # 2 turns possible for white
    # 10 turns possible for black
    # 10 turns possible for white

    # set board, set positions, make move and calculate 
    # set board, set turn for white and notice black couldn't play and stop game
    # set board, set turn for black and notice white couldn't play and stop game
    return True

def winner_selector_job():
    # Test cases need to verify in each board that the game is over (no more possible turns or no more rocks)
    # Black should win
    # white should win
    return True
