""" Utility functions """

import sys
import pygame
from color import *
from player import *

def quitGame():
    """ Terminates the game """

    sys.exit(0)

def makeMoves(gameStr):
    """ Creates a list of PGN notation moves from a single string
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
    return [[img.subsurface((i * wd, j * ht, wd, ht)).copy() for j in range(ver)] for i in range(hor)]

def getPlayerColor(player):
    """ Returns the color the corresponds to that player """

    return Color.black if player == Player.BLACK else Color.white

def getSprite(piece, sprites):
    """ Select sprite from sprites corresponding to piece """

    return sprites[piece.pieceType][piece.player]

def centerRect(src, dest):
    """ Centers src rect in dest rect """

    x = (dest.width - src.width) / 2 + dest.x
    y = (dest.height - src.height) / 2 + dest.y
    return pygame.Rect((x, y, src.width, src.height))

def isUppercase(let):
    """ Check if let is an uppercase letter """

    return 'A' <= let and let <= 'Z'

def isLowercase(let):
    """ Check if let is a lowercase letter """

    return 'a' <= let and let <= 'z'

def isNumberChar(let):
    """ Check if let is a numerical character """

    return '0' <= let and let <= '9'

def colFromFile(file):
    """ Convert file char to column """

    return ord(file) - ord('a') + 1

def rowFromRank(rank):
    """ Convert rank number to row """

    return ord('9') - ord(rank)

def clicked(prevKeys, keys, key):
    """ Checks if key was pressed during the last update """

    return keys[key] and (not prevKeys[key])

def released(prevKeys, keys, key):
    """ Checks if key was released during the last update """

    return (not keys[key]) and prevKeys[key]