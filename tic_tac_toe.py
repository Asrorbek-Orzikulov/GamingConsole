"""Command-line implementation of Tic-Tac-Toe."""

from argparse import ArgumentParser
from re import findall, ASCII
import pygame
import math

import board_class as board
import test_class as test

PLAYER_MSG = {board.TIE: "There is a tie!",
              board.PLAYER1: "Player 1 has won!",
              board.PLAYER2: "Player 2 has won!"}


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True

        return False


class TicTacToe(board.Board):
    """Implementation of the Tic-Tac-Toe board."""

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

    def cont(self):
        return self._cells

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
        assert (length_win > 2) and (player in [board.PLAYER1, board.PLAYER2])

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
            return board.TIE

        return board.GOING

    def is_going(self):
        """
        Check whether the game is still going.

        Returns
        -------
        bool
            True if the game hasn't ended. False otherwise.

        """
        return self._num_filled != self._height * self._width


def opposite_player(player):
    """
    Return the opponent of the current `player`.

    Parameters
    ----------
    player : int
        Player who did the last move.

    Returns
    -------
    int
        -1 if the input is 1. 1 if the input is -1.

    """
    return player * -1


def ch(l):
    if l == 1:
        return 'X'
    elif l == -1:
        return 'O'
    else:
        return ' '


def draw(screen, game):
    m = game.cont()
    (x, y) = m.shape
    for i in range(x):
        for j in range(y):
            button1 = button((212, 175, 55), 200 + i * 100, 200 + j * 100, 100, 100, ch(m[j][i]))
            button1.draw(screen, (0, 0, 0))


def log(c):
    for i in range(len(c)):
        for j in range(len(c)):
            if c[i][j] == 0:
                return i, j


def play_tic_tac_toe(size, length_win, result_dict, a):
    """
    Play one round of Tic-Tac-Toe.

    Parameters
    ----------
    size : int
        Size of the Tic-Tac-Toe board.
    length_win : int
        The number of consecutive elements needed to win.
    result_dict : dict
        Dictionary mapping results to messages.

    Returns
    -------
    None.

    """
    game = TicTacToe(size, size)
    current_player = board.PLAYER1
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Tic-Tac-Toe")
    back = pygame.image.load('back-2.jpg')
    gamepad = pygame.image.load('gamepad.png')
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    screen.fill((255, 255, 255))
    screen.blit(back, (0, 0))
    if a == 0:
        while game.is_going():
            pygame.display.update()
            for event in pygame.event.get():
                draw(screen, game)
                pygame.display.update()
                if event.type == pygame.QUIT:
                    running = False
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx = event.pos[0]
                    posy = event.pos[1]
                    chosen_col = int(math.floor((posx - 200) / 100))
                    chosen_row = int(math.floor((posy - 200) / 100))
                    choice = (chosen_row, chosen_col)
                    choice = str(choice)
                    dimensions = findall(r"\d+", choice, flags=ASCII)
                    row = int(dimensions[0])
                    col = int(dimensions[1])
                    if all((0 <= row < size, 0 <= col < size,
                            choice == "(" + str(row) + ", " + str(col) + ")")):
                        chosen_pos = (row, col)
                        if game.is_empty(chosen_pos):
                            game.set_full(chosen_pos, current_player)
                            result = game.is_over(chosen_pos, current_player, length_win)
                            if result != board.GOING:
                                break
                            current_player = opposite_player(current_player)
                            continue
                    print("Choose a valid position.")
    elif a == 1:
        while game.is_going():
            pygame.display.update()
            for event in pygame.event.get():
                draw(screen, game)
                pygame.display.update()
                if event.type == pygame.QUIT:
                    running = False
                    return
                if current_player == board.PLAYER1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        posx = event.pos[0]
                        posy = event.pos[1]
                        chosen_col = int(math.floor((posx - 200) / 100))
                        chosen_row = int(math.floor((posy - 200) / 100))
                        choice = (chosen_row, chosen_col)
                        choice = str(choice)
                        dimensions = findall(r"\d+", choice, flags=ASCII)
                        row = int(dimensions[0])
                        col = int(dimensions[1])
                        if all((0 <= row < size, 0 <= col < size,
                                choice == "(" + str(row) + ", " + str(col) + ")")):
                            chosen_pos = (row, col)
                            if game.is_empty(chosen_pos):
                                game.set_full(chosen_pos, current_player)
                                result = game.is_over(chosen_pos, current_player, length_win)
                                if result != board.GOING:
                                    break
                                current_player = opposite_player(current_player)
                                continue
                        print("Choose a valid position.")
                else:
                    chosen_row, chosen_col = log(game.cont())
                    choice = (chosen_row, chosen_col)
                    choice = str(choice)
                    dimensions = findall(r"\d+", choice, flags=ASCII)
                    row = int(dimensions[0])
                    col = int(dimensions[1])
                    if all((0 <= row < size, 0 <= col < size,
                            choice == "(" + str(row) + ", " + str(col) + ")")):
                        chosen_pos = (row, col)
                        if game.is_empty(chosen_pos):
                            game.set_full(chosen_pos, current_player)
                            result = game.is_over(chosen_pos, current_player, length_win)
                            if result != board.GOING:
                                break
                            current_player = opposite_player(current_player)
                            continue
                    print("Choose a valid position.")
    draw(screen, game)
    pygame.display.update()
    print(result_dict[result])
    if result == board.PLAYER1:
        label = myfont.render("Player X wins!!", 5, (0, 0, 0))
        screen.blit(label, (250, 100))
    elif result == board.PLAYER2:
        label = myfont.render("Player O wins!!", 5, (0, 0, 0))
        screen.blit(label, (250, 100))
    else:
        label = myfont.render("It is a tie!!", 5, (0, 0, 0))
        screen.blit(label, (250, 100))
    draw(screen, game)
    pygame.display.update()
    pygame.time.wait(3000)


if __name__ == '__main__':
    parser = ArgumentParser(description="Game configurations")
    parser.add_argument(
        "-s", "--size_of_board", type=int, default=3, choices=range(3, 20),
        help="Size of the board. By default 3 if you want a 3x3 board.")
    parser.add_argument(
        "-l", "--length_of_win", type=int, default=3, choices=range(3, 20),
        help="How many consecutive elements determine a win? By default 3.")
    args = parser.parse_args()

    # setting the game parameters
    SIZE = args.size_of_board
    LENGTH_WIN = args.length_of_win
    if LENGTH_WIN > SIZE:
        parser.error('-l cannot be greater than -s.')
    play_tic_tac_toe(SIZE, LENGTH_WIN, PLAYER_MSG)
