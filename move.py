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
        """ Checks the move for validity """

        piece, (x, y) = tile

        if self.castles: return True # Implementation missing
        if (x, y) == (self.x, self.y): return False
        if self.hint.hintRow and self.hint.hintRow != y: return False
        if self.hint.hintCol and self.hint.hintCol != x: return False
        
        if piece.pieceType == PieceType.K:
            return abs(self.x - x) <= 1 and abs(self.y - y) <= 1
        if piece.pieceType == PieceType.Q:
            return (x == self.x or
                y == self.y or
                x + y == self.x + self.y or
                x - y == self.x - self.y)
        if piece.pieceType == PieceType.B:
            return (x + y == self.x + self.y or
                x - y == self.x - self.y)
        if piece.pieceType == PieceType.N:
            return ((abs(self.x - x) == 2 and abs(self.y - y) == 1) or
                (abs(self.x - x) == 1 and abs(self.y - y) == 2))
        if piece.pieceType == PieceType.R:
            return (x == self.x or
                y == self.y)
        if piece.pieceType == PieceType.P:
            sign = -1
            pawnRow = 7
            if piece.player == Player.BLACK:
                sign = +1
                pawnRow = 2
            if self.captured: return self.y - y == sign and abs(self.x - x) == 1
            if y == pawnRow: return sign * (self.y - y) <= 2 and self.x == x
            return self.y - y == sign and self.x == x
        return False

    def execute(self, chessBoard):
        """ Executes the current move on the given board """

        pawnRow = 2
        kingRow = 1
        if self.piece.player == Player.WHITE:
            pawnRow = 7
            kingRow = 8

        if (self.castles):
            if self.piece.pieceType == PieceType.K:
                chessBoard.board[7][kingRow] = chessBoard.board[5][kingRow]
                chessBoard.board[6][kingRow] = chessBoard.board[8][kingRow]
                chessBoard.board[5][kingRow] = None
                chessBoard.board[8][kingRow] = None
                return
            if self.piece.pieceType == PieceType.Q:
                chessBoard.board[3][kingRow] = chessBoard.board[5][kingRow]
                chessBoard.board[4][kingRow] = chessBoard.board[1][kingRow]
                chessBoard.board[1][kingRow] = None
                chessBoard.board[5][kingRow] = None
                return

        found = False
        for tile in [x for x in chessBoard if x[0] and x[0].player == self.piece.player and x[0].pieceType == self.piece.pieceType]:
            if self.isValid(chessBoard, tile):
                chessBoard.board[self.x][self.y] = chessBoard.board[tile[1][0]][tile[1][1]]
                chessBoard.board[tile[1][0]][tile[1][1]] = None
                found = True
                break
        if not found:
            print(self.piece, self.x, self.y, self.hint, self.castles)

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
