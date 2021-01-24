import test_class as test
import fifteen_puzzle
import numpy as np


def run_suite():
    """Run informal tests on code."""
    suite = test.TestSuite()

    # testing the init() find_empty() methods
    size = 5
    game1 = fifteen_puzzle.FifteenPuzzle(size)
    print("Zero's position", game1.find_empty())
    print(game1)

    # testing the count_inversions() method
    list1 = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    suite.run_test(game1.count_inversions(list1), 1, "Test #1.1")
    list2 = [1, 8, 2, 4, 3, 7, 6, 5]
    suite.run_test(game1.count_inversions(list2), 10, "Test #1.2")
    list3 = [13, 2, 10, 3, 1, 12, 8, 4, 5, 9, 6, 15, 14, 11, 7]
    suite.run_test(game1.count_inversions(list3), 41, "Test #1.3")
    list4 = [6, 13, 7, 10, 8, 9, 11, 15, 2, 12, 5, 14, 3, 1, 4]
    suite.run_test(game1.count_inversions(list4), 62, "Test #1.4")
    list5 = [3, 9, 11, 15, 14, 11, 4, 6, 13, 10, 12, 2, 7, 8, 5]
    suite.run_test(game1.count_inversions(list5), 61, "Test #1.5")
    suite.run_test(game1.count_inversions(list(range(10))), 0, "Test #1.6")

    # testing the first_inversion() and count_inversions() methods
    list6 = list(range(0, 9))
    print(list6)
    print(game1.first_inversion(list6))
    print(list6)
    suite.run_test(game1.first_inversion(list1), (0, 1), "Test #2.1")
    suite.run_test(game1.first_inversion(list2), (1, 2), "Test #2.2")
    suite.run_test(game1.first_inversion(list4), (1, 2), "Test #2.3")
    list4[1], list4[2] = list4[2], list4[1]
    suite.run_test(game1.count_inversions(list4), 61, "Test #1.7")
    suite.run_test(game1.first_inversion(list5), (3, 4), "Test #2.4")
    list5[3], list5[4] = list5[4], list5[3]
    suite.run_test(game1.count_inversions(list5), 60, "Test #1.8")

    # testing the change_board() and move_cmd_line() methods
    test_board1 = [[4, 16, 12, 21, 6],
                   [11, 13, 17, 22, 24],
                   [23, 20, 0, 1, 8],
                   [18, 15, 5, 14, 10],
                   [2, 7, 19, 9, 3]]
    game1.change_board(np.array(test_board1))
    suite.run_test(game1.find_empty(), (2, 2), "Test #3.1")
    print(game1)
    game1.move_cmd_line("u")
    suite.run_test(game1.find_empty(), (1, 2), "Test #3.2")
    suite.run_test(game1.get_cell_content((2, 2)), 17, "Test #3.3")
    game1.move_cmd_line("l")
    suite.run_test(game1.find_empty(), (1, 1), "Test #3.4")
    suite.run_test(game1.get_cell_content((1, 2)), 13, "Test #3.5")
    game1.move_cmd_line("d")
    suite.run_test(game1.find_empty(), (2, 1), "Test #3.6")
    suite.run_test(game1.get_cell_content((1, 1)), 20, "Test #3.7")
    game1.move_cmd_line("r")
    suite.run_test(game1.find_empty(), (2, 2), "Test #3.8")
    suite.run_test(game1.get_cell_content((2, 1)), 17, "Test #3.9")

    # testing the boundaries with move_cmd_line() method
    test_board2 = [[4, 16, 12, 21, 6],
                   [11, 13, 17, 22, 24],
                   [23, 20, 3, 1, 8],
                   [18, 15, 5, 14, 10],
                   [2, 7, 19, 9, 0]]
    game1.change_board(np.array(test_board2))
    game1.move_cmd_line("d")
    suite.run_test(game1.find_empty(), (4, 4), "Test #3.10")
    game1.move_cmd_line("r")
    suite.run_test(game1.find_empty(), (4, 4), "Test #3.11")

    # testing the is_over() method
    suite.run_test(game1.is_over(), False, "Test #4.1")
    game1.change_board(np.array(test_board1))
    suite.run_test(game1.is_over(), False, "Test #4.2")
    game1.change_board(np.array(range(0, 16)).reshape((4, 4)))
    suite.run_test(game1.is_over(), False, "Test #4.3")

    test_board3 = [[1, 2],
                   [3, 0]]
    game1.change_board(np.array(test_board3))
    suite.run_test(game1.is_over(), True, "Test #4.4")

    test_board4 = [[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 0]]
    game1.change_board(np.array(test_board4))
    suite.run_test(game1.is_over(), True, "Test #4.5")

    test_board5 = [[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 0]]
    game1.change_board(np.array(test_board5))
    suite.run_test(game1.is_over(), True, "Test #4.6")

    test_board6 = [[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 0]]
    game1.change_board(np.array(test_board6))
    suite.run_test(game1.is_over(), True, "Test #4.7")

    test_board7 = [[1, 2, 3, 4, 5, 6],
                   [7, 8, 9, 10, 11, 12],
                   [13, 14, 15, 16, 17, 18],
                   [19, 20, 21, 22, 23, 24],
                   [25, 26, 27, 28, 29, 30],
                   [31, 32, 33, 34, 35, 0]]
    game1.change_board(np.array(test_board7))
    suite.run_test(game1.is_over(), True, "Test #4.8")

    test_board8 = [[1, 2, 3, 4, 5, 6, 7],
                   [8, 9, 10, 11, 12, 13, 14],
                   [15, 16, 17, 18, 19, 20, 21],
                   [22, 23, 24, 25, 26, 27, 28],
                   [29, 30, 31, 32, 33, 34, 35],
                   [36, 37, 38, 39, 40, 41, 42],
                   [43, 44, 45, 46, 47, 48, 0]]
    game1.change_board(np.array(test_board8))
    suite.run_test(game1.is_over(), True, "Test #4.9")

    # testing the move_gui() method
    game1.change_board(np.array(test_board1))
    print(game1)
    game1.move_gui((4, 4))
    print(game1)
    game1.move_gui((1, 3))
    print(game1)
    game1.move_gui((3, 3))
    print(game1)
    game1.move_gui((2, 3))
    print(game1)
    game1.move_gui((2, 3))
    print(game1)
    game1.move_gui((1, 2))
    print(game1)
    game1.move_gui((2, 4))
    print(game1)
    game1.move_gui((3, 4))
    print(game1)

    # reporting the results of the test
    suite.report_results()
