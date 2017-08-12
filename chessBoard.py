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
        if player == Player.WHITE:
            kingRow = 8
            pawnRow = 7
        for i in range(1, 9): self.board[i][pawnRow] =  ChessPiece(player, PieceType.P)
        for i in [1, 8]: self.board[i][kingRow] =       ChessPiece(player, PieceType.R)
        for i in [2, 7]: self.board[i][kingRow] =       ChessPiece(player, PieceType.N)
        for i in [3, 6]: self.board[i][kingRow] =       ChessPiece(player, PieceType.B)
        self.board[4][kingRow] =                        ChessPiece(player, PieceType.Q)
        self.board[5][kingRow] =                        ChessPiece(player, PieceType.K)
