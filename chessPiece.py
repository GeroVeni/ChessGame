""" Utility functions and class about pieces """

from player import *
from pieceType import *

class ChessPiece:
    """ Class that describes a piece """

    def __init__(self, player = None, pieceType = None):
        if (player == None or pieceType == None):
            self.player = self.pieceType = None
        else:
            self.player = player
            self.pieceType = pieceType

    def __str__(self):
        colorStr = 'Black' if self.player == Player.BLACK else 'White'
        typeStr = convertPieceTypeToString(self.pieceType)
        return "'" + colorStr + " " + typeStr + "'"
