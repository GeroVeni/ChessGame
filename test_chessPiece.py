""" Unit test for chessPiece file """

from pieceType import *
from player import *
from chessPiece import *

def test_chessPiece_constructor():
    """ Tests the chess piece constructor """

    piece = ChessPiece(Player.WHITE, PieceType.K)
    assert(piece.player == Player.WHITE)
    assert(piece.pieceType == PieceType.KING)
