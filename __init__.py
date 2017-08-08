""" Main file """

import pygame
from color import Color
from utils import *


# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


# Core functions
def processEvents():
    """ Handles the event queue """

    for event in pygame.event.get():
        if event.type == pygame.QUIT: quitGame()

def render():
    """ Renders the canvas and the sprites """

    pygame.display.update()

def update():
    """ Updates game state """

    if pygame.key.get_pressed()[pygame.K_ESCAPE]: quitGame()

if __name__ == '__main__':

    # Initialize window
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Load resources
    file = open('resources/PGN/dummy.pgn', 'r')
    moves = makeMoves(file.read())
    img = pygame.image.load('resources/images/pieces.png').convert_alpha()
    piecesImages = splitImage(img, 6, 2)

    # Main loop
    while 1:
        processEvents()
        update()
        render()
