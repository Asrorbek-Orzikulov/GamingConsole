"""Command-line implementation of Fifteen puzzle."""

from argparse import ArgumentParser
import numpy as np
import pygame

from board_class import Board, EMPTY
import test_class as test


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
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


class FifteenPuzzle(Board):
    """Implementation of the Fifteen Puzzle board."""

    _directions = {"u": (-1, 0),
                   "d": (1, 0),
                   "l": (0, -1),
                   "r": (0, 1)}

    def __init__(self, size, test_board=None):
        """
        Take in `size` and initialize a square board of that size.

        The board is indexed by rows (left to right) and by columns
        (top to bottom). If `test_board` is not None, this input
        board will be used as the game board.

        Parameters
        ----------
        size : int
            The number of row and columns in the board.
        test_board : numpy.array, optional
            This argument is to be used for testing purposes only.
            The default is None.

        Returns
        -------
        None.

        """
        if test_board is None:
            self._height = size
            self._width = size
            self.generate_board(size)
        else:
            self.change_board(test_board)
            self._zero = self.find_empty()

    def __str__(self):
        """
        Return the multi-line string represenation of the board.

        Returns
        -------
        str_board : str
            String represenation of the board.

        """
        return str(self._cells)

    def generate_board(self, size):
        """
        Generate a solvable board of given `size`.

        Parameters
        ----------
        size : int
            The number of row and columns in the board.

        Returns
        -------
        numpy.array
            A solvable board.

        """
        rand_list = list(range(1, size ** 2))
        np.random.shuffle(rand_list)
        inversions = self.count_inversions(rand_list)

        # board creation depending on size and the inversions count
        if (size % 2 == 1) and (inversions % 2 == 0):
            row_0 = np.random.choice(size)
        elif (size % 2 == 1) and (inversions % 2 == 1):
            first, second = self.first_inversion(rand_list)
            rand_list[first], rand_list[second] = rand_list[second], rand_list[first]
            row_0 = np.random.choice(size)
        elif inversions % 2 == 1:
            row_0 = np.random.choice(range(0, size, 2))
        else:
            row_0 = np.random.choice(range(1, size, 2))

        col_0 = np.random.choice(size)
        index_0 = row_0 * size + col_0
        self._zero = (row_0, col_0)
        rand_list = rand_list[:index_0] + [EMPTY] + rand_list[index_0:]
        self._cells = np.array(rand_list).reshape((size, size), order="C")

    def find_empty(self):
        """
        Find the position of the empty cell.

        Returns
        -------
        tuple

        """
        for row in range(self._height):
            for col in range(self._width):
                if self._cells[row, col] == EMPTY:
                    return row, col

        return (-1, 1)

    def count_inversions(self, input_list):
        """
        Count the number of inversions in a list.

        Parameters
        ----------
        input_list : list
            List for which we count the number of inverted elements.

        Returns
        -------
        int

        """
        count = 0
        for i in range(len(input_list)):
            j = i + 1
            while j < len(input_list):
                if input_list[i] > input_list[j]:
                    count += 1
                j += 1

        return count

    def first_inversion(self, input_list):
        """
        Find the first consecutive inversion.

        Parameters
        ----------
        input_list : list
            List in which we want to find the first consecutive inversion.
            If the list does not contain any inversions, it is randomly
            shuffled and the method is called recursively.

        Returns
        -------
        tuple
            Tuple of the form (`idx`, `idx` + 1) showing the positions
            of two inverted elements.

        """
        for i in range(len(input_list) - 1):
            if input_list[i] > input_list[i + 1]:
                return (i, i + 1)

        np.random.shuffle(input_list)
        return self.first_inversion(input_list)

    def is_over(self):
        """
        Check if the game is over.

        Returns
        -------
        bool
            True if the game is over.

        """
        row_0, col_0 = self._zero
        self._cells[row_0, col_0] = self._height * self._width
        for row in range(self._height):
            for col in range(self._width):
                if self._cells[row, col] != self._height * row + col + 1:
                    self._cells[row_0, col_0] = EMPTY
                    return False

        self._cells[row_0, col_0] = EMPTY
        return True

    def move_cmd_line(self, dir_str):
        """
        Move EMPTY along the given direction.

        Parameters
        ----------
        dir_str : str
            Shows where EMPTY should be moved.

        Returns
        -------
        None.

        """
        row_0, col_0 = self._zero
        row_move, col_move = self._directions[dir_str]
        new_row = row_0 + row_move
        new_col = col_0 + col_move
        if (0 <= new_row < self._height) and (0 <= new_col < self._width):
            changed_num = self._cells[new_row, new_col]
            self._cells[row_0, col_0] = changed_num
            self._cells[new_row, new_col] = EMPTY
            self._zero = (new_row, new_col)
        else:
            print("Cannot move to this cell")

    def move_gui(self, pos):
        """
        Move the chosen tile to the empty position.

        Parameters
        ----------
        pos : tuple
            Tile which we want to move to the empty position.

        Returns
        -------
        None.

        """
        row_0, col_0 = self._zero
        difference = abs(pos[0] - row_0) + abs(pos[1] - col_0)
        if difference == 1:
            changed_num = self.get_cell_content(pos)
            self._cells[row_0, col_0] = changed_num
            self._cells[pos[0], pos[1]] = EMPTY
            self._zero = pos

    def cont(self):
        return self._cells


link = "https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/"


def draw(screen, game):
    m = game.cont()
    (x, y) = m.shape
    for i in range(x):
        for j in range(y):
            button1 = button((212, 175, 55), 200 + i * 100, 200 + j * 100, 100, 100, str(m[j][i]))
            button1.draw(screen, (0, 0, 0))


def play_fifteen_puzzle(size):
    """
    Play one round of Fifteen Puzzle.

    Parameters
    ----------
    size : int
        Size of the Fifteen Puzzle board.

    Returns
    -------
    None.

    """
    game = FifteenPuzzle(size)
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("15 puzzle")
    back = pygame.image.load('back-2.jpg')
    gamepad = pygame.image.load('gamepad.png')
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    screen.fill((255, 255, 255))
    screen.blit(back, (0, 0))
    while not game.is_over():
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move = 'r'
                    game.move_cmd_line(move)
                if event.key == pygame.K_LEFT:
                    move = 'l'
                    game.move_cmd_line(move)
                if event.key == pygame.K_UP:
                    move = 'u'
                    game.move_cmd_line(move)
                if event.key == pygame.K_DOWN:
                    move = 'd'
                    game.move_cmd_line(move)
            draw(screen, game)
            pygame.display.update()

    label = myfont.render("You win!!", 1, (0, 0, 0))
    screen.blit(label, (250, 100))
    draw(screen, game)
    pygame.display.update()
    pygame.time.wait(3000)



if __name__ == '__main__':
    parser = ArgumentParser(description="Game configurations")
    parser.add_argument(
        "-s", "--size_of_board", type=int, default=4, choices=range(2, 20),
        help="Size of the board. By default 4 if you want a Fifteen Puzzle.")
    args = parser.parse_args()

    # setting the game parameters
    SIZE = args.size_of_board
    # play_fifteen_puzzle(5)
