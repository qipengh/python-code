

import sys
import pygame
import time
import copy

from pygame.locals import *

FPS = 10
WINDOWWIDTH = 1000
WINDOWHEIGHT = 750
SPACESIZE = 35
BOARDWIDTH = 19
BOARDHEIGHT = 19
WHITE_TILE = 'WHITE_TILE'
BLACK_TILE = 'BLACK_TILE'
EMPTY_SPACE = 'EMPTY_SPACE'
ANIMATIONSPEED = 25

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * SPACESIZE))/2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * SPACESIZE))/2)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 155, 0)
BRIGHTBLUE = (0, 50, 255)

TEXTBGCOLOR1 = BRIGHTBLUE
TEXTBGCOLOR2 = GREEN
GRIDLINECOLOR = BLACK
TEXTCOLOR = WHITE


def main():
    global MAINCLOCK, DISPLAYSURF, FONT, BIGFONT, BGIMAGE

    pygame.init()
    MAINCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Gomoku')
    FONT = pygame.font.Font('freesansbold.ttf', 16)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 32)

    boardImage = pygame.image.load('wuziqiboard.png')
    boardImage = pygame.transform.smoothscale(boardImage, (BOARDWIDTH * SPACESIZE, BOARDHEIGHT * SPACESIZE))
    boardImageRect = boardImage.get_rect()
    boardImageRect.topleft = (XMARGIN, YMARGIN)
    BGIMAGE = pygame.image.load('wuziqibackground.png')
    BGIMAGE = pygame.transform.smoothscale(BGIMAGE, (WINDOWWIDTH, WINDOWHEIGHT))
    BGIMAGE.blit(boardImage, boardImageRect)

    # Run the main game
    # print 'start'
    while True:
        if runGame() == False:
            break


def runGame():
    winner = 'tie'
    mainBorad = getNewBoard()
    # resetBoard(mainBorad)
    turn = 'playerA'
    drawBoard(mainBorad)
    # playerATile, playerBTile = enterPlayerTile()
    newGameSurf = FONT.render('New Game', True, TEXTCOLOR, TEXTBGCOLOR2)
    newGameRect = newGameSurf.get_rect()
    newGameRect.topright = (WINDOWWIDTH - 8, 10)

    while True:
        if turn == 'playerA':
            playerTile = BLACK_TILE
        if turn == 'playerB':
            playerTile = WHITE_TILE

        if getValidMoves(mainBorad) == []:
            break
        movexy = None
        while movexy is None:

            checkForQuit()
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    if newGameRect.collidepoint((mousex, mousey)):
                        return True
                    movexy = getSpaceClick(mousex, mousey)
                    print(movexy)
                    if movexy is not None and not isValidMove(mainBorad, movexy[0], movexy[1]):
                        movexy = None

            drawBoard(mainBorad)
            # drawInfo()
            DISPLAYSURF.blit(newGameSurf, newGameRect)

            MAINCLOCK.tick(FPS)
            pygame.display.update()

        makeMove(mainBorad, playerTile, movexy[0], movexy[1])
        drawBoard(mainBorad)
        if hasWon(turn, mainBorad):
            if turn == 'playerA':
                winner = turn
            else:
                winner = 'playerB'
            break
        if getValidMoves(mainBorad) != []:
            if turn == 'playerA':
                turn = 'playerB'
            else:
                turn = 'playerA'

    if winner == 'tie':
        text = 'The game was a tie!'
    elif winner == 'playerA':
        text = 'BLACK win!'
    else:
        text = 'WHITE win!'

    textSurf = FONT.render(text, True, TEXTCOLOR, TEXTBGCOLOR1)
    textRect = textSurf.get_rect()
    textRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(textSurf, textRect)

    # Display the "Play again?" text with Yes and No buttons.
    text2Surf = BIGFONT.render('Play again?', True, TEXTCOLOR, TEXTBGCOLOR1)
    text2Rect = text2Surf.get_rect()
    text2Rect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 50)

    # Make "Yes" button.
    yesSurf = BIGFONT.render('Yes', True, TEXTCOLOR, TEXTBGCOLOR1)
    yesRect = yesSurf.get_rect()
    yesRect.center = (int(WINDOWWIDTH / 2) - 60, int(WINDOWHEIGHT / 2) + 90)

    # Make "No" button.
    noSurf = BIGFONT.render('No', True, TEXTCOLOR, TEXTBGCOLOR1)
    noRect = noSurf.get_rect()
    noRect.center = (int(WINDOWWIDTH / 2) + 60, int(WINDOWHEIGHT / 2) + 90)

    while True:
        # Process events until the user clicks on Yes or No.
        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                if yesRect.collidepoint((mousex, mousey)):
                    return True
                elif noRect.collidepoint((mousex, mousey)):
                    return False
        DISPLAYSURF.blit(textSurf, textRect)
        DISPLAYSURF.blit(text2Surf, text2Rect)
        DISPLAYSURF.blit(yesSurf, yesRect)
        DISPLAYSURF.blit(noSurf, noRect)
        pygame.display.update()
        MAINCLOCK.tick(FPS)




# def resetBoard(board):
#     for x in xrange(BOARDWIDTH):
#         for y in xrange(BOARDHEIGHT):
#             board[x][y] = EMPTY_SPACE

# def enterPlayerTile():


# def drawInfo():


def getSpaceClick(mousex, mousey):

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if mousex > x * SPACESIZE + XMARGIN:
                if mousex < (x + 1) * SPACESIZE + XMARGIN:
                    if mousey > y * SPACESIZE + YMARGIN:
                        if mousey < (y + 1) * SPACESIZE + YMARGIN:
                            return x,y
    return None


def hasWon(turn, b):
    if turn == 'playerA':
        check = BLACK_TILE
    else:
        check = WHITE_TILE

    for x in range(BOARDWIDTH):

        for y in range(BOARDHEIGHT):
            if b[x][y] == check:
                if x < BOARDHEIGHT - 4 and y < BOARDWIDTH - 4:
                    if b[x][y:y+5] == [check]*5:
                        return True
                    if [b[x][y],b[x+1][y],b[x+2][y],b[x+3][y],b[x+4][y]] == [check]*5:
                        return True
                    if [b[x][y],b[x+1][y+1],b[x+2][y+2],b[x+3][y+3],b[x+4][y+4]] == [check]*5:
                        return True
                if x >= 4 and y < BOARDWIDTH - 4:
                    if [b[x][y],b[x-1][y+1],b[x-2][y+2],b[x-3][y+3],b[x-4][y+4]] == [check]*5:
                        return True


def makeMove(board, tile, xstart, ystart):
    board[xstart][ystart] = tile


def checkForQuit():
    for event in pygame.event.get((QUIT, KEYUP)):
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


def getValidMoves(board):
    validMoves = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            if isValidMove(board, x, y) != False:
                validMoves.append((x, y))

    return validMoves


def isValidMove(board, xstart, ystart):
    if board[xstart][ystart] != EMPTY_SPACE or not isOnBoard(xstart, ystart):
        return False
    return True


def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y >= 0 and y < BOARDHEIGHT



def drawBoard(board):
    DISPLAYSURF.blit(BGIMAGE, BGIMAGE.get_rect())

    for x in range(BOARDWIDTH + 1):
        startx = (x * SPACESIZE) + XMARGIN
        starty = YMARGIN
        endx = (x * SPACESIZE) + XMARGIN
        endy = YMARGIN + (BOARDHEIGHT * SPACESIZE)
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))
    for y in range(BOARDHEIGHT + 1):
        startx = XMARGIN
        starty = (y * SPACESIZE) + YMARGIN
        endx = XMARGIN + (BOARDHEIGHT * SPACESIZE)
        endy = (y * SPACESIZE) + YMARGIN
        pygame.draw.line(DISPLAYSURF, GRIDLINECOLOR, (startx, starty), (endx, endy))

    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            centerx, centery = translateBoardToPixelCoord(x, y)
            if board[x][y] == WHITE_TILE or board[x][y] == BLACK_TILE:
                if board[x][y] == WHITE_TILE:
                    tileColor = WHITE
                else:
                    tileColor = BLACK
                pygame.draw.circle(DISPLAYSURF, tileColor, (centerx, centery), int(SPACESIZE / 2) - 4)


def translateBoardToPixelCoord(x, y):
    return XMARGIN + x * SPACESIZE + int(SPACESIZE / 2), YMARGIN + y * SPACESIZE + int(SPACESIZE / 2)


def getNewBoard():
    board = []
    for i in range(BOARDWIDTH):
        board.append([EMPTY_SPACE] * BOARDHEIGHT)

    return board

if __name__ == '__main__':
    main()
