import test_class as test
import tic_tac_toe
import board_class as board
import numpy as np

def run_suite():
    """Run informal tests on code."""
    suite = test.TestSuite()

    # testing the sum_along_direction() method
    test_board2 = np.array([[row + col for col in range(5)]
                            for row in range(6)])
    game1 = tic_tac_toe.TicTacToe(6, 5, test_board2)
    print(game1)
    suite.run_test(game1.sum_along_direction((4, 2), (-1, 0), 3), 15, "Test #3.1")
    suite.run_test(game1.sum_along_direction((4, 2), (0, -1), 3), 15, "Test #3.2")
    suite.run_test(game1.sum_along_direction((4, 2), (0, 1), 3), 21, "Test #3.3")
    suite.run_test(game1.sum_along_direction((4, 2), (0, -1), 4), 0, "Test #3.4")
    suite.run_test(game1.sum_along_direction((4, 2), (1, 0), 3), 0, "Test #3.5")
    suite.run_test(game1.sum_along_direction((4, 2), (1, 0), 2), 13, "Test #3.6")
    suite.run_test(game1.sum_along_direction((4, 2), (-1, 1), 3), 18, "Test #3.7")
    suite.run_test(game1.sum_along_direction((4, 2), (-1, 1), 4), 0, "Test #3.8")
    suite.run_test(game1.sum_along_direction((4, 2), (1, -1), 3), 0, "Test #3.9")
    suite.run_test(game1.sum_along_direction((5, 0), (0, 1), 5), 35, "Test #3.10")
    suite.run_test(game1.sum_along_direction((5, 0), (-1, -1), 3), 0, "Test #3.11")
    suite.run_test(game1.sum_along_direction((5, -1), (0, 1), 3), 0, "Test #3.12")
    suite.run_test(game1.sum_along_direction((-1, -1), (1, 1), 3), 0, "Test #3.13")

    # testing the is_over() and is_going() methods
    suite.run_test(game1.is_going(), True, "Test 4.1")
    test_board3 = np.array([[0, 0, 1, 0, -1, 0, 1],
                            [0, 0, 0, 0, -1, 0, 1],
                            [1, 1, 1, -1, -1, 0, -1],
                            [0, 0, 0, 0, 0, -1, 0],
                            [0, -1, 0, 0, -1, 1, -1]])
    game1.change_board(test_board3)
    print(game1)
    suite.run_test(game1.is_over((2, 0), board.PLAYER1, 3), board.PLAYER1, "Test #4.2")
    suite.run_test(game1.is_going(), False, "Test 4.3")
    game1.change_board(test_board3)
    suite.run_test(game1.is_over((2, 1), board.PLAYER1, 3), board.PLAYER1, "Test #4.4")
    game1.change_board(test_board3)
    suite.run_test(game1.is_over((2, 2), board.PLAYER1, 3), board.PLAYER1, "Test #4.5")
    suite.run_test(game1.is_going(), False, "Test 4.6")

    game1.change_board(test_board3)
    suite.run_test(game1.is_over((2, 0), board.PLAYER1, 4), board.GOING, "Test #4.7")
    suite.run_test(game1.is_going(), True, "Test 4.8")

    game1.change_board(test_board3)
    suite.run_test(game1.is_over((0, 4), board.PLAYER2, 3), board.PLAYER2, "Test #4.9")
    game1.change_board(test_board3)
    suite.run_test(game1.is_over((1, 4), board.PLAYER2, 3), board.PLAYER2, "Test #4.10")
    game1.change_board(test_board3)
    suite.run_test(game1.is_over((3, 5), board.PLAYER2, 3), board.PLAYER2, "Test #4.11")
    game1.change_board(test_board3)
    suite.run_test(game1.is_over((4, 6), board.PLAYER2, 3), board.PLAYER2, "Test #4.12")
    suite.run_test(game1.is_going(), False, "Test 4.13")

    game1.change_board(test_board3)
    suite.run_test(game1.is_over((4, 6), board.PLAYER2, 4), board.GOING, "Test #4.14")
    suite.run_test(game1.is_going(), True, "Test 4.15")

    game1.change_board(test_board3)
    suite.run_test(game1.is_over((3, 0), board.PLAYER2, 4), board.GOING, "Test #4.16")
    game1.change_board(test_board3)
    suite.run_test(game1.is_over((-1, -1), board.PLAYER2, 4), board.GOING, "Test #4.17")
    # suite.run()

    test_board4 = np.array([[1, -1, 1, -1, 1, -1, 1],
                            [-1, 1, 1, 1, -1, 1, -1],
                            [1, 1, -1, 1, -1, 1, -1],
                            [1, 1, -1, -1, -1, 1, -1],
                            [1, -1, -1, -1, -1, 1, -1],
                            [1, -1, 1, -1, -1, 1, -1]])
    game1.change_board(test_board4)
    print(game1)
    suite.run_test(game1.is_over((1, 1), board.PLAYER1, 4), board.TIE, "Test #4.18")
    game1.change_board(test_board4)
    suite.run_test(game1.is_over((2, 3), board.PLAYER1, 4), board.TIE, "Test #4.19")
    game1.change_board(test_board4)
    suite.run_test(game1.is_over((2, 2), board.PLAYER2, 4), board.TIE, "Test #4.20")
    suite.run_test(game1.is_going(), False, "Test 4.21")

    # reporting the results of the test
    suite.report_results()
