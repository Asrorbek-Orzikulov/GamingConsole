"""Board class for the Gaming Console."""

import numpy as np
import test_class as test

EMPTY = 0
PLAYER1 = 1
PLAYER2 = -1
TIE = 2
GOING = 3


class Board:
    """Implementation of 2D board of cells."""

    _opposites = {(1, 0): (-1, 0),
                  (1, 1): (-1, -1),
                  (0, 1): (0, -1),
                  (-1, 1): (1, -1)}

    def __init__(self, height, width, test_board=None):
        """
        Take in `height` and `width` of the board and initialize
        an empty board of the given size. The board is indexed by
        rows (left to right) and by columns (top to bottom).

        If `test_board` is not None, this input board will be used
        as the game board.

        Parameters
        ----------
        height : int
            The number of rows.
        width : int
            The number of columns.
        test_board : numpy.array, optional
            This argument is to be used for testing purposes only.
            The default is None.

        Returns
        -------
        None.

        """
        if test_board is None:
            self._height = height
            self._width = width
            self._cells = np.zeros((self._height, self._width), dtype=int)
            self._num_filled = 0
        else:
            self.change_board(test_board)

    def __str__(self):
        """
        Return the multi-line string represenation of the board.

        Returns
        -------
        str_board : str
            String represenation of the board.

        """
        str_board = ""
        for row in self._cells:
            row_str = "["
            for col in row:
                if col == -1:
                    row_str += " " + str(col)
                else:
                    row_str += "  " + str(col)

            str_board += row_str + "]"
            str_board += "\n"
        return str_board

    def change_board(self, test_board):
        """
        Change the game board with the new board.

        The method is used for testing purposes only.

        Parameters
        ----------
        test_board : numpy.array
            New board that will replace the current game board.

        Returns
        -------
        None.

        """
        self._cells = test_board
        self._height = self._cells.shape[0]
        self._width = self._cells.shape[1]
        self._num_filled = 0
        for row in range(self._height):
            for col in range(self._width):
                if self._cells[row, col] != EMPTY:
                    self._num_filled += 1

    def is_empty(self, pos):
        """
        Show whether a given cell is empty.

        Parameters
        ----------
        pos : tuple
            Position of the cell in (row, col) form.

        Returns
        -------
        bool
            True if the given cell is EMPTY. False otherwise.

        """
        return self._cells[pos[0], pos[1]] == EMPTY

    def is_going(self):
        """
        Check whether the game is still going.

        Returns
        -------
        bool
            True if the game hasn't ended. False otherwise.

        """
        return self._num_filled != self._height * self._width

    def sum_along_direction(self, start_pos, direction, length_win):
        """
        Compute the sum of `length_win` cells along the given `direction`.

        Parameters
        ----------
        start_pos : tuple
            The cell from which we start and compute the sum along
            the given direction.
        direction : tuple
            Direction in the (row, col) form whose components show
            changes in row position and column position, respectively.
        length_win : int
            The number of consecutive elements needed to win.

        Returns
        -------
        int
            0 if any cell to be summed goes beyond the borders. Otherwise,
            the computed sum is returned.

        """
        current_row, current_col = start_pos
        row_change, col_change = direction
        last_cell_row = (length_win - 1) * row_change + current_row
        last_cell_col = (length_win - 1) * col_change + current_col
        if not all([0 <= current_row <= self._height - 1,
                    0 <= current_col <= self._width - 1,
                    0 <= last_cell_row <= self._height - 1,
                    0 <= last_cell_col <= self._width - 1]):
            return 0

        cells = [(current_row + step * row_change,
                  current_col + step * col_change)
                 for step in range(length_win)]
        sum_cells = sum(self._cells[cell[0], cell[1]] for cell in cells)
        return sum_cells

    def is_over(self, pos, player, length_win):
        """
        Check if the game is over after the move of the `player`.

        Parameters
        ----------
        pos : tuple
            Position of the last move in (row, col) form.
        player : int
            The player doing the move.
        length_win : int
            The number of consecutive elements needed to win.

        Returns
        -------
        int
            1 for PLAYER1, -1 for PLAYER2, 2 for TIE, 3 if the game is GOING.

        """
        assert (length_win > 2) and (player in [PLAYER1, PLAYER2])

        for direction in self._opposites:
            for step in range(length_win):
                current_row = pos[0] + step * direction[0]
                current_col = pos[1] + step * direction[1]
                current_pos = (current_row, current_col)
                sum_cells = self.sum_along_direction(
                    current_pos, self._opposites[direction], length_win)
                if sum_cells == player * length_win:
                    self._num_filled = self._height * self._width
                    return player

        if self._num_filled == self._height * self._width:
            return TIE

        return GOING

    def set_full(self, pos, player):
        """
        Fill the given cell with the player's mark.

        Parameters
        ----------
        pos : tuple
            Position to be filled in (row, col) form.
        player : int
            The player doing the move.

        Returns
        -------
        None.

        """
        self._cells[pos[0], pos[1]] = player
        self._num_filled += 1

    def clear_board(self):
        """
        Clear the board and make all cells EMPTY.

        Returns
        -------
        None.

        """
        self._cells = np.zeros((self._height, self._width), dtype=int)
        self._num_filled = 0

    def get_board_size(self):
        """
        Return the dimesion of the board.

        Returns
        -------
        tuple
            Dimension of the board in (height, width) form.

        """
        return (self._height, self._width)
    def get_width(self):
        return self._width
    def get_height(self):
        return self._height
    def get_cells(self):
        return self._cells
    def get_cell_content(self, pos):
        """
        Return the content of the given cell.

        Parameters
        ----------
        pos : tuple
            Position of the cell in (row, col) form.

        Returns
        -------
        int
            0 for EMPTY; 1 for PLAYER1; -1 for PLAYER2

        """
        return self._cells[pos[0], pos[1]]

    def get_cell_content(self):
        """
        Return the content of the given cell.

        Parameters
        ----------
        pos : tuple
            Position of the cell in (row, col) form.

        Returns
        -------
        int
            0 for EMPTY; 1 for PLAYER1; -1 for PLAYER2

        """
        return self._cells
