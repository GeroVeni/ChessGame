""" Tools relevant to PieceType enum """

class PieceType:
    """ Piece type enum """

    K = KING = 0
    Q = QUEEN = 1
    B = BISHOP = 2
    N = KNIGHT = 3
    R = ROOK = 4
    P = PAWN = 5

def convertCharToPieceType(let):
    if let == 'K': return PieceType.K
    if let == 'Q': return PieceType.Q
    if let == 'B': return PieceType.B
    if let == 'N': return PieceType.N
    if let == 'R': return PieceType.R
    return PieceType.P

def convertPieceTypeToString(pieceType):
    if pieceType == PieceType.K: return 'King'
    if pieceType == PieceType.Q: return 'Queen'
    if pieceType == PieceType.B: return 'Bishop'
    if pieceType == PieceType.N: return 'Knight'
    if pieceType == PieceType.R: return 'Rook'
    if pieceType == PieceType.P: return 'Pawn'
