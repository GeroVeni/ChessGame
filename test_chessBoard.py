""" Unit test for chessBoard file """

from player import *
from pieceType import *
from chessPiece import *
from chessBoard import *

def test_chessBoard_constructor():
    """ Tests the chess board constructor """
    
    chessBoard = ChessBoard()
    assert(chessBoard.board[1][1].player == Player.WHITE and
        chessBoard.board[1][1].pieceType == PieceType.R)
    assert(chessBoard.board[8][8].player == Player.BLACK and
        chessBoard.board[8][8].pieceType == PieceType.R)
    assert(chessBoard.board[2][6].player == Player.WHITE and
        chessBoard.board[2][2].pieceType == PieceType.P)
    assert(chessBoard.board[7][3].player == Player.BLACK and
        chessBoard.board[7][3].pieceType == PieceType.P)
    assert(chessBoard.board[1][4].player == Player.WHITE and
        chessBoard.board[1][4].pieceType == PieceType.Q)
    assert(chessBoard.board[8][5].player == Player.BLACK and
        chessBoard.board[8][5].pieceType == PieceType.K)
    assert(chessBoard.board[5][5] == None)

def test_chessBoard_iteration():
    """ Tests the python-style loop """

    chessBoard = ChessBoard()
    assert(len([x for x in chessBoard]) == 64)
    for piece in chessBoard:
        if piece != None:
            assert(chessBoard.board[piece[1][0]][piece[1][1]] == piece[0])
