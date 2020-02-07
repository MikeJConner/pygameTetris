import math
import random
import pygame
import tkinter
import tkinter.font as font
BOARDSIZE = 600
BOARDHEIGHT = 24
BOARDWIDTH = 10

class Cube(object):

    def __init__(self, color):
        pass

    def move(self):
        pass

    def draw(self):
        pass

class Piece(object):

    def __init__(self):
        pass

    def move(self):
        pass

    def draw(self):
        pass

def drawGrid(surface):
    sizeBtwn = BOARDSIZE // BOARDHEIGHT
    x = 0
    y = 0
    dif = (BOARDHEIGHT - BOARDWIDTH) // 2
    start = dif
    end = BOARDHEIGHT - dif
    for l in range(BOARDHEIGHT):
        x += sizeBtwn
        y += sizeBtwn
        pygame.draw.line(surface, (255, 255, 255), (sizeBtwn * dif + sizeBtwn,y), (sizeBtwn + BOARDSIZE - sizeBtwn * dif, y))
        if(l >= start and l <= end):
            pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, BOARDSIZE))
            
def redrawWindow(surface):
    surface.fill((0,0,0))
    drawGrid(surface)
    pygame.display.update()

def generatePiece():
    pieceDict = {
    "I": (("0","0","1","0","0"),
          ("0","0","1","0","0"),
          ("0","0","1","0","0"),
          ("0","0","1","0","0")),
    "O": (("0","0","0","0","0"),
          ("0","1","1","0","0"),
          ("0","1","1","0","0"),
          ("0","0","0","0","0"))
    }

def messageBox():
    pass

def main():
    win = pygame.display.set_mode((BOARDSIZE, BOARDSIZE))
    redrawWindow(win)

main()
