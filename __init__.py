""" Main file """

import pygame
from color import Color
from utils import *
from chessBoard import *
from render import *


# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BOARD_SIZE = 500


# Initialize window
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
chessBoard = ChessBoard()

# Load resources
file = open('resources/PGN/dummy.pgn', 'r')
moves = makeMoves(file.read())
img = pygame.image.load('resources/images/pieces.png').convert_alpha()
sprites = splitImage(img, 6, 2)
chessBoardRenderer = ChessBoardRenderer(pygame.Rect((150, 50, BOARD_SIZE, BOARD_SIZE)), screen, sprites)

# Color.setChessBlack((51, 34, 0))
# Color.setChessWhite((153, 77, 0))

# Core functions
def processEvents():
    """ Handles the event queue """

    for event in pygame.event.get():
        if event.type == pygame.QUIT: quitGame()

def render(screen): # TO BE MOVED TO render.py
    """ Renders the canvas and the sprites """

    screen.fill(Color.background)
    chessBoardRenderer.render(chessBoard)
    pygame.display.update()

def update(delta = None):
    """ Updates game state """

    if pygame.key.get_pressed()[pygame.K_ESCAPE]: quitGame()

if __name__ == '__main__':
    # Main loop
    while 1:
        processEvents()
        update()
        render(screen)
