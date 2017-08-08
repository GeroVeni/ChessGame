""" Utility functions and class about game board """

from player import *
from pieceType import *
from chessPiece import *

class ChessBoard:
    """ Chess board class """

    def __init__(self):
        self.makeBoard()

    def __iter__(self):
        return iter([(self.board[i][j], (i, j)) for i in range(1, 9) for j in range(1, 9)])

    def makeBoard(self):
        """ Defines and initiallizes game board """

        self.board = [[None for i in range(9)] for j in range(9)]
        self.playerSetup(Player.WHITE)
        self.playerSetup(Player.BLACK)

    def playerSetup(self, player):
        """ Creates pieces for a player """

        kingRow = 1
        pawnRow = 2
        if player == Player.BLACK:
            kingRow = 8
            pawnRow = 7
        for i in range(1, 9): self.board[pawnRow][i] =  ChessPiece(player, PieceType.P)
        for i in [1, 8]: self.board[kingRow][i] =       ChessPiece(player, PieceType.R)
        for i in [2, 7]: self.board[kingRow][i] =       ChessPiece(player, PieceType.N)
        for i in [3, 6]: self.board[kingRow][i] =       ChessPiece(player, PieceType.B)
        self.board[kingRow][4] =                        ChessPiece(player, PieceType.Q)
        self.board[kingRow][5] =                        ChessPiece(player, PieceType.K)
