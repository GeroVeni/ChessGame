""" Contains tools for move parsing, validating and executing """

from pieceType import *
from player import *
from utils import *
from chessPiece import *

class Hint:
    """ Class describing extra inforamtion in extracted from abbreviated algebraic chess notation """

    ROW = 0
    COL = COLUMN = 1

    def __init__(self, hintCol, hintRow):
        self.hintCol = hintCol
        self.hintRow = hintRow

class PieceMove:
    """ Class containing information about a move """

    def __init__(self, piece, x = None, y = None, hint = None, captured = False, promotedTo = None, castles = None):
        self.piece = piece
        self.x = x
        self.y = y
        self.hint = hint
        self.captured = captured
        self.promotedTo = promotedTo
        self.castles = castles

    def isValid(self, chessBoard, tile):
        return True

    def execute(self, chessBoard):
        pawnRow = 2
        kingRow = 1
        if self.piece.player == Player.WHITE:
            pawnRow = 7
            kingRow = 8

        if (self.castles):
            if self.pieceType == PieceType.K:
                chessBoard.board[kingRow][7] = chessBoard.board[kingRow][5]
                chessBoard.board[kingRow][6] = chessBoard.board[kingRow][8]
                chessBoard.board[kingRow][5] = None
                chessBoard.board[kingRow][8] = None
                return
            if self.pieceType == PieceType.Q:
                chessBoard.board[kingRow][3] = chessBoard.board[kingRow][5]
                chessBoard.board[kingRow][4] = chessBoard.board[kingRow][1]
                chessBoard.board[kingRow][1] = None
                chessBoard.board[kingRow][5] = None
                return

        for tile in [x for x in chessBoard if x[0].player == self.piece.player and x[0].pieceType == self.piece.pieceType]:
            if self.isValid(chessBoard, tile):
                chessBoard.board[x][y] = chessBoard.board[tile[1][0]][tile[1][1]]
                chessBoard.board[tile[1][0]][tile[1][1]] = None

def moveParser(player, moveStr):
    """ Converts PGN notation to PieceMove object """

    start = 0
    pieceType = PieceType.P

    if isUppercase(moveStr[start]):
        if moveStr[start] == 'O':
            castlesPiece = PieceType.K if len(moveStr) == 3 else PieceType.Q
            return PieceMove(ChessPiece(player, castlesPiece), castles = True)
        else:
            pieceType = convertCharToPieceType(moveStr[start])
            start += 1

    hintChar = hintRow = hintCol = None
    captured = False

    if moveStr[start] == 'x':
        captured = True
        start += 1
    elif moveStr[start + 1] == 'x':
        captured = True
        hintChar = moveStr[start]
        start += 2
    elif isLowercase(moveStr[start + 1]):
        hintChar = moveStr[start]
        start += 1
    c = colFromFile(moveStr[start])
    r = rowFromRank(moveStr[start + 1])
    start += 2

    if hintChar:
        if isNumberChar(hintChar):
            hintRow = rowFromRank(hintChar)
        else:
            hintCol = colFromFile(hintChar)

    return PieceMove(ChessPiece(player, pieceType), c, r, Hint(hintCol, hintRow), captured)
