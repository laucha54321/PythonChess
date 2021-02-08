#Setup
import pygame
import math
import ChessEngine
from pygame.locals import *
pygame.init()
resolution = 800
squareSize = resolution/8
Tablero = []
Images = {}
run = True
whiteTurns = True
piece = [
    ["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["--","--","--","--","--","--","--","--"],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"],
]
posiciones=[
    ["a8","b8","c8","d8","e8","f8","g8","h8"],
    ["a7","b7","c7","d7","e7","f7","g7","h7"],
    ["a6","b6","c6","d6","e6","f6","g6","h6"],
    ["a5","b5","c5","d5","e5","f5","g5","h5"],
    ["a4","b4","c4","d4","e4","f4","g4","h4"],
    ["a3","b3","c3","d3","e3","f3","g3","h3"],
    ["a2","b2","c2","d2","e2","f2","g2","h2"],
    ["a1","b1","c1","d1","e1","f1","g1","h1"]
]
referencetofunction = {
    "br":ChessEngine.rookMove,"bn":ChessEngine.horseMove,"bb":ChessEngine.bishopMove,
    "bq":ChessEngine.queenMove,"bk":ChessEngine.kingMove,"bp":ChessEngine.blackpawnMove,
    "wp":ChessEngine.whitepawnMove,"wr":ChessEngine.rookMove,"wn":ChessEngine.horseMove,
    "wb":ChessEngine.bishopMove,"wk":ChessEngine.kingMove,"wq":ChessEngine.queenMove 
    }
win = pygame.display.set_mode((resolution,resolution))
pygame.display.set_caption ("Chess")
    
def loadImages():
    pieces =["br","bn","bb","bk","bq","bp","wr","wn","wb","wk","wq","wp"]
    for pieces in pieces:
        Images[pieces] = pygame.transform.scale(pygame.image.load("ChessPieces/" + pieces +".png"),(int(squareSize),int(squareSize)))

def drawpieces(x,y):
    if piece[int(y)][int(x)] != "--":
        win.blit(Images[piece[int(y)][int(x)]],(x*squareSize,y*squareSize))


def drawboard():
    x = 0
    y = 0
    white = True
    while y < resolution:
        lista = []
        while x < resolution:
            if white == True:
                pygame.draw.rect(win,(255,255,245),(x,y,squareSize,squareSize))
                white = False
                lista.append(True)
                drawpieces(x/squareSize,y/squareSize);
            else:
                pygame.draw.rect(win,(120,255,0),(x,y,squareSize,squareSize))
                white = True
                lista.append(False)
                drawpieces(x/squareSize,y/squareSize);
            pygame.display.update()
            x = x + squareSize
        Tablero.append(lista)
        if white == True:
            white = False
        else: 
            white = True
        x = 0
        y = y + squareSize
    pygame.display.update()
    #print(Tablero)

def quepiezaes(x,y):
    print(piece[x][y])

loadImages()
drawboard()


while run:

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            mouseX,mouseY = pygame.mouse.get_pos()
            posicionCrudaX =int(math.trunc(mouseY/squareSize))
            posicionCrudaY =int(math.trunc(mouseX/squareSize))
            posicion = posiciones[posicionCrudaX][posicionCrudaY]
            print(posicion)
            posiblemoves=[]
            if (piece[posicionCrudaX][posicionCrudaY] != "--"):
                posiblemoves = ChessEngine.kingMove(posicionCrudaX,posicionCrudaY)
                print(posiblemoves)
                piecetomove = piece[posicionCrudaX][posicionCrudaY]
                posicionCrudaYAnterior = posicionCrudaY
                posicionCrudaXAnterior = posicionCrudaX
                quepiezaes(posicionCrudaX,posicionCrudaY)
            if piece[posicionCrudaX][posicionCrudaY] == "--":
                piece[posicionCrudaX][posicionCrudaY] = piecetomove
                piecetomove = "--"
                piece[posicionCrudaXAnterior][posicionCrudaYAnterior] = "--"
                #print(piece)
            drawboard()
        

            


        if event.type == pygame.QUIT:
            run = False
