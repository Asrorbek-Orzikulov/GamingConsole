"""Command-line implementation of Connect Four."""

import board_class as board
import pygame
import sys
import math
import numpy
import random

SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


class ConnectFour(board.Board):
    """Implementation of the Connect Four board."""

    def choose_col(self, col):
        """
        Return the position of the bottom element of a `given` col.

        Parameters
        ----------
        col : int
            The column a player wants to place his color in.

        Returns
        -------
        tuple
            The position in (row, col) form if the chosen column has
            empty cells. Otherwise, (-1, -1) is returned.

        """
        assert 0 <= col <= self._width

        for row in range(self._height - 1, -1, -1):
            if self._cells[row, col] == board.EMPTY:
                return (row, col)

        return (-1, -1)


def draw_board(board,screen):
    w=board.get_width()
    h = board.get_height()
    for c in range(w):
        for r in range(h):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(w):
        for r in range(h):
            height = (h+1)*SQUARESIZE
            cells=board.get_cells()
            if numpy.flip(cells,0)[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif numpy.flip(cells,0)[r][c] == -1:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


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


def start_connect_four(a):
    """
    Play one round of Connect Four.

    Returns
    -------
    None.

    """
    game = ConnectFour(6, 7)
    current_player = board.PLAYER1
    pygame.init()
    w=game.get_width()
    h=game.get_height()
    width = (w) * SQUARESIZE
    height = (h + 1) * SQUARESIZE
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Connect 4")
    icon=pygame.image.load('circle.png')
    pygame.display.set_icon(icon)
    pygame.event.get()
    draw_board(game,screen)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 75)
    if a == 0:
        while game.is_going():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = min(max(event.pos[0], RADIUS), width - RADIUS)
                    if current_player == board.PLAYER1:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                    else:
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    draw_board(game,screen)
                    posx = event.pos[0]
                    chosen_col = int(math.floor(posx / SQUARESIZE))
                    chosen_pos = game.choose_col(int(chosen_col))
                    if chosen_pos == (-1, -1):
                        continue

                    game.set_full(chosen_pos, current_player)
                    result = game.is_over(chosen_pos, current_player, 4)
                    current_player = opposite_player(current_player)
                    draw_board(game,screen)
                    if current_player == board.PLAYER1:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                    else:
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
                    pygame.display.update()

                    if result == board.TIE:
                        message = "There is a tie!"
                        print(message)
                        label = myfont.render("It is a TIE!!!", 1, RED)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        draw_board(game, screen)
                        pygame.time.wait(3000)
                        break
                    elif result == board.PLAYER1:
                        message = "Player 1 has won!"
                        print(message)
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        draw_board(game, screen)
                        pygame.time.wait(3000)
                        break
                    elif result == board.PLAYER2:
                        message = "Player 2 has won!"
                        print(message)
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        draw_board(game, screen)
                        pygame.time.wait(3000)
                        break
                    else:
                        continue

    elif a == 1:
        while game.is_going():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return
                if current_player == board.PLAYER1:
                    if event.type == pygame.MOUSEMOTION:
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                        posx = min(max(event.pos[0], RADIUS), width - RADIUS)
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                    pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                        draw_board(game, screen)
                        posx = event.pos[0]
                        chosen_col = int(math.floor(posx / SQUARESIZE))
                        chosen_pos = game.choose_col(int(chosen_col))
                        if chosen_pos == (-1, -1):
                            continue

                        game.set_full(chosen_pos, current_player)
                        result = game.is_over(chosen_pos, current_player, 4)
                        current_player = opposite_player(current_player)
                        draw_board(game, screen)
                        pygame.display.update()

                        if result == board.TIE:
                            message = "There is a tie!"
                            print(message)
                            label = myfont.render("It is a TIE!!!", 1, RED)
                            screen.blit(label, (40, 10))
                            pygame.display.update()
                            draw_board(game, screen)
                            pygame.time.wait(3000)
                            break
                        elif result == board.PLAYER1:
                            message = "Player 1 has won!"
                            print(message)
                            label = myfont.render("Player 1 wins!!", 1, RED)
                            screen.blit(label, (40, 10))
                            pygame.display.update()
                            draw_board(game, screen)
                            pygame.time.wait(3000)
                            break
                        elif result == board.PLAYER2:
                            message = "Player 2 has won!"
                            print(message)
                            label = myfont.render("Player 2 wins!!", 1, YELLOW)
                            screen.blit(label, (40, 10))
                            pygame.display.update()
                            draw_board(game, screen)
                            pygame.time.wait(3000)
                            break
                        else:
                            continue
                else:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    draw_board(game, screen)
                    chosen_col = random.randint(0, 6)
                    chosen_pos = game.choose_col(int(chosen_col))
                    if chosen_pos == (-1, -1):
                        continue
                    game.set_full(chosen_pos, current_player)
                    result = game.is_over(chosen_pos, current_player, 4)
                    current_player = opposite_player(current_player)
                    draw_board(game, screen)
                    if current_player == board.PLAYER1:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                    else:
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
                    pygame.display.update()

                    if result == board.TIE:
                        message = "There is a tie!"
                        print(message)
                        label = myfont.render("It is a TIE!!!", 1, RED)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        draw_board(game, screen)
                        pygame.time.wait(3000)
                        break
                    elif result == board.PLAYER1:
                        message = "Player 1 has won!"
                        print(message)
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        draw_board(game, screen)
                        pygame.time.wait(3000)
                        break
                    elif result == board.PLAYER2:
                        message = "Player 2 has won!"
                        print(message)
                        label = myfont.render("Player 2 wins!!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        pygame.display.update()
                        draw_board(game, screen)
                        pygame.time.wait(3000)
                        break
                    else:
                        continue


if __name__ == "__main__":
    start_connect_four(0)
    pygame.quit()
    sys.exit()
