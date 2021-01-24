import test_class as test
import board_class as board
import numpy as np


def run_suite():
    """Run informal tests on code."""
    suite = test.TestSuite()

    # testing the __init__(), __str__() and change_board() methods
    game1 = board.Board(6, 7)
    print(game1)

    # testing the change_board() method
    test_board1 = np.array([[0, 0, 1, 0],
                            [0, 0, 0, 0],
                            [1, 0, 0, -1],
                            [0, 0, 0, 0],
                            [0, -1, 0, 0]])

    game1.change_board(test_board1)
    print(game1)
    print(game1._height, "x", game1._width)

    # testing the is_empty() method
    suite.run_test(game1.is_empty((0, 0)), True, "Test #1.1")
    suite.run_test(game1.is_empty((4, 1)), False, "Test #1.2")
    suite.run_test(game1.is_empty((2, 3)), False, "Test #1.3")
    suite.run_test(game1.is_empty((2, 1)), True, "Test #1.4")

    # testing the set_full() and get_cell_content() methods
    game1.set_full((4, 0), board.PLAYER1)
    suite.run_test(game1.get_cell_content((4, 0)), board.PLAYER1, "Test #2.1")
    game1.set_full((4, 2), board.PLAYER1)
    suite.run_test(game1.get_cell_content((4, 2)), board.PLAYER1, "Test #2.2")
    game1.set_full((0, 0), board.PLAYER2)
    suite.run_test(game1.get_cell_content((0, 0)), board.PLAYER2, "Test #2.3")

    # testing the clear_board() method
    game1.clear_board()
    print(game1)

    # reporting the results of the test
    suite.report_results()
