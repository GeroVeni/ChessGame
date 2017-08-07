""" Utility functions and class about pieces """

class ChessPiece:
    """ Class that describes a piece """

    def __init__(self, player = None, pieceType = None):
        if (player == None or pieceType == None):
            self.player = self.pieceType = None
        else:
            self.player = player
            self.pieceType = pieceType
