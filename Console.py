import connect_four
import pygame
import fifteen_puzzle
import tic_tac_toe
import board_class as board
import sys


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


pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Gaming Console")
gamepad = pygame.image.load('gamepad.png')
back = pygame.image.load('background.jpg')
pygame.display.set_icon(gamepad)
running = True
button_c4_main = button((255, 255, 255), 225, 15, 250, 100, 'Connect 4')
button_c4_1 = button((0, 255, 0), 475, 129, 100, 100, '2-P')
button_c4_2 = button((0, 255, 0), 125, 129, 100, 100, '1-P')
button_fp_main = button((255, 255, 255), 225, 243, 250, 100, '15 puzzle')
button_fp_1 = button((0, 255, 0), 125, 357, 100, 100, 'Easy')
button_fp_2 = button((0, 255, 0), 475, 357, 100, 100, 'Hard')
button_ttt_main = button((255, 255, 255), 225, 471, 250, 100, 'TicTacToe')
button_ttt_1 = button((0, 255, 0), 475, 585, 100, 100, '2-P')
button_ttt_2 = button((0, 255, 0), 125, 585, 100, 100, '1-P')
while running:
    screen.fill((255, 255, 255))
    screen.blit(back, (0, 0))
    button_c4_main.draw(screen, (0, 0, 0))
    button_fp_1.draw(screen, (0, 0, 0))
    button_fp_main.draw(screen, (0, 0, 0))
    button_fp_2.draw(screen, (0, 0, 0))
    button_c4_1.draw(screen, (0, 0, 0))
    button_c4_2.draw(screen, (0, 0, 0))
    button_ttt_main.draw(screen, (0, 0, 0))
    button_ttt_1.draw(screen, (0, 0, 0))
    button_ttt_2.draw(screen, (0, 0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            if button_c4_1.isOver(pos):
                button_c4_1.color = (255, 0, 0)
            else:
                button_c4_1.color = (0, 255, 0)
            if button_c4_2.isOver(pos):
                button_c4_2.color = (255, 0, 0)
            else:
                button_c4_2.color = (0, 255, 0)
            if button_fp_1.isOver(pos):
                button_fp_1.color = (255, 0, 0)
            else:
                button_fp_1.color = (0, 255, 0)
            if button_fp_2.isOver(pos):
                button_fp_2.color = (255, 0, 0)
            else:
                button_fp_2.color = (0, 255, 0)
            if button_ttt_1.isOver(pos):
                button_ttt_1.color = (255, 0, 0)
            else:
                button_ttt_1.color = (0, 255, 0)
            if button_ttt_2.isOver(pos):
                button_ttt_2.color = (255, 0, 0)
            else:
                button_ttt_2.color = (0, 255, 0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_c4_1.isOver(pos):
                connect_four.start_connect_four(0)
            elif button_c4_2.isOver(pos):
                connect_four.start_connect_four(1)
            elif button_fp_1.isOver(pos):
                fifteen_puzzle.play_fifteen_puzzle(3)
            elif button_fp_2.isOver(pos):
                fifteen_puzzle.play_fifteen_puzzle(4)
            elif button_ttt_1.isOver(pos):
                PLAYER_MSG = {board.TIE: "There is a tie!",
                              board.PLAYER1: "Player 1 has won!",
                              board.PLAYER2: "Player 2 has won!"}
                tic_tac_toe.play_tic_tac_toe(3, 3, PLAYER_MSG, 0)
            elif button_ttt_2.isOver(pos):
                PLAYER_MSG = {board.TIE: "There is a tie!",
                              board.PLAYER1: "Player 1 has won!",
                              board.PLAYER2: "Player 2 has won!"}
                tic_tac_toe.play_tic_tac_toe(3, 3, PLAYER_MSG, 1)
