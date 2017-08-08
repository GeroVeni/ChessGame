""" Color class and color related functions """

class Color:
    """ Color class """
    
    black =         (  0,   0,   0)
    red =           (255,   0,   0)
    green =         (  0, 255,   0)
    blue =          (  0,   0, 255)
    white =         (255, 255, 255)
    chessWhite =    (200, 200, 200)
    chessBlack =    ( 50,  50,  50)

    def __init__(self, r, g, b):
        if not Color.isComponentValid(r): self.data = None
        elif not Color.isComponentValid(g): self.data = None
        elif not Color.isComponentValid(b): self.data = None
        else: self.data = (r, g, b)

    def __repr__(self):
        return "Color(" + str(r) + ", " + str(g) + ", " + str(b) + ")"

    def __str__(self):
        return self.__repr__()

    def isComponentValid(c):
        """ Checks whether color component values (r,g,b) are in range(0, 255) """
        
        return 0 <= c and c <= 255
