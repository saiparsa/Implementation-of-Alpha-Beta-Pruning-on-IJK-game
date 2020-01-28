#!/usr/local/bin/python3

"""
This is where you should write your AI code!

Authors: Sai Prasad Parsa(saiparsa), Sanath Edupuganti(saedup) , Akhil Nagulavancha(aknagu)

Based on skeleton code by Abhilash Kuhikar, October 2019
"""

from logic_IJK import Game_IJK
import math
import copy

global directions
directions=['U','D','L','R']

def getchildren (grid,player,game ):
    game1=copy.deepcopy(game)
    children=[]
    for i in range(0,4):
        
        children.append([(game.makeMove(directions[i])).getGame(),directions[i],player])
    #print(children)
    return children
def Mininax_AlphaBeta(grid, depth , isMaximizingPlayer, alpha , beta, game):
    best_move=' '
    if depth==0:
        #print(score(grid,isMaximizingPlayer),best_move)
        return score(grid,isMaximizingPlayer),best_move
    
    if isMaximizingPlayer :
        best= -math.inf
        #print (getchildren(grid,isMaximizingPlayer,game))
        #print(' ')
        for child in getchildren(grid,isMaximizingPlayer,game):
            
            val = Mininax_AlphaBeta( child[0], depth-1, False, alpha, beta ,game)
            if (val[0]>best):
                best= (val[0])
                best_move=child[1]
            
            
            if beta<=best:
                break
            alpha = max( alpha, best)
        return best,best_move
    
    
    else :
        best1 = math.inf
        for child in getchildren(grid,isMaximizingPlayer,game):
            val = Mininax_AlphaBeta( child[0], depth-1, True, alpha, beta,game)
            if (val[0]<best1):
                best1= float(val[0])
                best_move = child[1]
            
            if best1<=alpha:
                break
            beta =min( beta, best1)
            
        return best1,best_move

def gridtransform(board):
    
    grid=[]
    dirc={'a':2,'b':4,'c':8,'d':16, 'e' :32, 'f':64 , 'g':64, 'h':128, 'i':256,
          'j':512,'k':1024,'A':2,'B':4,'C':8,'D':16, 'E' :32, 'F':64 , 'G':64, 
          'H':128, 'I':256,'J':512,'K':1024}
    for i in range(6):
        for j in range(6):
            if board[i][j]==' ':
                board[i][j]=0
            grid.append(board[i][j])
    for ele in range(0,len(grid)):
        for key in dirc.keys():
            if key==grid[ele]:
                grid[ele]=(dirc[key])
    return grid

def score(grid,Max):
    
    grid=gridtransform(grid)
    maxValue = -1
    zeros = 0
    
    for i in range(36):
        maxValue = max(maxValue, grid[i])
        if grid[i] == 0:
            zeros += 1
    
    if maxValue == grid[0] or maxValue == grid[5] or maxValue == grid[30] or maxValue == grid[35]:
        add=20
    else:
        add=-20
        
    scorelist = [2**35, 2**34, 2**33, 2**32, 2**31, 2**30,
                 2**24, 2**25, 2**26, 2**27, 2**28, 2**29,
                 2**23, 2**22, 2**21, 2**20, 2**19, 2**18,
                 2**12, 2**13, 2**14, 2**15, 2**16, 2**17,
                 2**11, 2**10, 2**9,  2**8,  2**7,  2**6,
                 2**0, 2**1, 2**2, 2**3, 2**4, 2**5]
    scores = 0
    for i in range(36):
        scores += grid[i] ** scorelist[i]
    return zeros**(36-zeros)+add*2000+scores*1000+maxValue*maxvalue
    
    
def next_move(game: Game_IJK)-> None:

    '''board: list of list of strings -> current state of the game
       current_player: int -> player who will make the next move either ('+') or -'-')
       deterministic: bool -> either True or False, indicating whether the game is deterministic or not
    '''

    board = game.getGame()
    player = game.getCurrentPlayer()
    deterministic = game.getDeterministic()
    
    if player=='+':
        Ismax=True
    else:
        Ismax=False
    depth=5
    if(deterministic == True):
        score, move = Mininax_AlphaBeta(board, depth , Ismax, -math.inf , math.inf,game)
        #print('MOVE', move, score)
        
        return move
    


    
    
            
        
        
