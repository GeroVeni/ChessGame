""" Utility functions """

import sys
from color import *
from player import *

def quitGame():
    """ Terminates the game """

    sys.exit(0)

def makeMoves(gameStr):
    """ Creates a list on PGN notation moves 
    gameStr: the full string read from a pgn file """

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
    return moves

def splitImage(img, hor, ver):
    """ Splits the images into 'hor' columns and 'ver' rows
    img: the surface to be split
    hor: the column count
    ver: the row count"""

    wd = img.get_width() / hor
    ht = img.get_height() / ver
    return [[img.subsurface((i * wd, j * ht, wd, ht)) for j in range(ver)] for i in range(hor)]

def getPlayerColor(player):
    """ Returns the color the corresponds to that player """

    return Color.black if player == Player.BLACK else Color.white
