""" Provides a rendering class for chess board """

import pygame
from color import *
from utils import getSprite, centerRect

class ChessBoardRenderer:
    """ Rendering class for chess board """

    def __init__(self, rect, screen = None, sprites = None):
        self.x = rect.x
        self.y = rect.y
        wd = rect.width
        ht = rect.height
        self.size = wd if wd < ht else ht
        self.screen = screen
        self.sprites = sprites

    def getTileSize(self):
        """ Gets the size of the side of a tile """
        
        return self.size / 8

    def getTile(self, x, y):
        """ Gets a pygame Rect representing tile at (x, y) """

        sz = self.getTileSize()
        tx = (x - 1) * sz + self.x
        ty = (y - 1) * sz + self.y
        return pygame.Rect((tx, ty, sz, sz))

    def loadSprites(sprites):
        """ Loads the pieces sprites """

        self.sprites = sprites

    def loadScreen(screen):
        """ Loads the default screen """

        self.screen = screen

    def makeAxis(self, size = 10):
        top = pygame.Rect(self.x, self.y - size, self.size, size)
        bottom = pygame.Rect(self.x, self.y + self.size, self.size, size)
        left = pygame.Rect(self.x - size, self.y, size, self.size)
        right = pygame.Rect(self.x + self.size, self.y, size, self.size)
        
        return top, bottom, left, right

    def render(self, chessBoard, screen = None):
        """ Renders the chess board on the screen """

        if screen == None:
            screen = self.screen
        if screen == None:
            return

        axisSize = 25
        top, bottom, left, right = self.makeAxis(axisSize)
        font = pygame.font.Font(None, axisSize)
        
        for chInd in range(ord('a'), ord('i')):
            surf = font.render(chr(chInd), False, Color.black)
            i = chInd - ord('a')
            subRects = [pygame.Rect(rect.x + i * self.getTileSize(), rect.y, self.getTileSize(), axisSize) for rect in [top, bottom]]
            for rect in subRects:
                screen.blit(surf, centerRect(surf.get_rect(), rect))

        for ind in range(1, 9):
            surf = font.render(str(9 - ind), False, Color.black)
            i = ind - 1
            subRects = [pygame.Rect(rect.x, rect.y + i * self.getTileSize(), axisSize, self.getTileSize()) for rect in [left, right]]
            for rect in subRects:
                screen.blit(surf, centerRect(surf.get_rect(), rect))

        for piece, (x, y) in chessBoard:
            color = Color.chessWhite if (x + y) % 2 == 0 else Color.chessBlack
            tile = self.getTile(x, y)
            screen.fill(color, tile)
            if self.sprites == None or piece == None:
                continue
            sprite = getSprite(piece, self.sprites)

            screen.blit(sprite, centerRect(sprite.get_rect(), tile))
