""" Main file """

import pygame
import sys


# Contstants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


# Utility functions
def quitGame():
    """ Terminates the game """

    sys.exit(0)

def makeMoves(gameStr):
    """ Creates a list on PGN notation moves """

    moves = []
    move = ''
    adding = 'none'
    for i in gameStr:
        if adding == 'none':
            if i == '.': adding = 'white'
        elif adding == 'white':
            if i == ' ' or i == '\n':
                adding = 'black'
                moves.append(move)
                move = ''
            else: move = move + i
        elif adding == 'black':
            if i == ' ' or i == '\n':
                adding = 'none'
                moves.append(move)
                move = ''
            else: move = move + i
    if (adding != 'none'): moves.append(move)
    log = open("gamestr.log", 'w')
    for m in moves: log.write(m + '\n')
    return moves

def splitImage(img, hor, ver):
    """ Splits the images into 'hor' columns and 'ver' rows """

    wd = img.get_width() / hor
    ht = img.get_height() / ver
    return [[img.subsurface((i * wd, j * ht, wd, ht)) for j in range(ver)] for i in range(hor)]

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
