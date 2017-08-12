""" Main file """

import pygame
from color import Color
from utils import *
from chessBoard import *
from render import *
from move import *


# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
DISPLAY_RECT = pygame.Rect((0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
BOARD_SIZE = 500
BOARD_RECT = pygame.Rect((0, 0, BOARD_SIZE, BOARD_SIZE))


# Initialize window and variables
pygame.init()
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
chessBoard = ChessBoard()
prevPressedKeys = {}
pressedKeys = {}

# Load resources
file = open('resources/PGN/dummy.pgn', 'r')
moves = makeMoves(file.read())
movesPos = 0
img = pygame.image.load('resources/images/pieces.png').convert_alpha()
sprites = splitImage(img, 6, 2)
# chessBoardRenderer = ChessBoardRenderer(centerRect(BOARD_RECT, DISPLAY_RECT), screen, sprites)
chessBoardRenderer = ChessBoardRenderer(pygame.Rect(30, 30, 500, 500), screen, sprites)

# Color.setChessBlack((51, 34, 0))
# Color.setChessWhite((153, 77, 0))

# Core functions
def processEvents():
    """ Handles the event queue """

    for event in pygame.event.get():
        if event.type == pygame.QUIT: quitGame()

def render(screen):
    """ Renders the canvas and the sprites """

    screen.fill(Color.background)
    chessBoardRenderer.render(chessBoard)
    pygame.display.update()

def update(delta = None):
    """ Updates game state """

    global prevPressedKeys, pressed_keys, movesPos
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[pygame.K_ESCAPE]: quitGame()
    if clicked(prevPressedKeys, pressed_keys, pygame.K_n):
        if movesPos < len(moves):
            moveParser(movesPos % 2, moves[movesPos]).execute(chessBoard)
            movesPos += 1

    prevPressedKeys = pressed_keys

if __name__ == '__main__':
    # Main loop
    while 1:
        processEvents()
        update()
        render(screen)
