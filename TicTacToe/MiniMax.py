from tictactoe import Board
import random
import math
import time
import sys

minimaxCount = 0
minimaxAlphaBetaCount = 0
        
def randomPlayer(board):
    choice = []
    for moves in board.possible_moves():
        choice.append((moves[0], moves[1]))
    return random.choice(choice)

def winMovePlayer(board, chance):
    for move in board.possible_moves():
        copyBoard = board.copy()
        copyBoard.push(move)
        if copyBoard.result() == chance:
            return move
    return None

def blockMovePlayer(board, chance):
    if chance == 2:
        opponent = 1
    else:
        opponent = 2
    for move in board.possible_moves():
        copyBoard = board.copy()
        copyBoard.set_mark(move.tolist(), opponent)
        if copyBoard.result() == opponent:
            return move
    return None

def defaultPlayer(board, chance):
    winMove = winMovePlayer(board, chance)
    if winMove is not None:
        return winMove
    
    blockMove = blockMovePlayer(board, chance)
    if blockMove is not None:
        return blockMove
    return randomPlayer(board)
    
def minimax(board, isMaxTurn, aiPlayer):
    global minimaxCount
    winStatus = board.result()
    if aiPlayer == 1:
        if winStatus == 0:
            return 0
        elif (winStatus == 2):
            return -10 
        elif (winStatus == 1):
            return 10
    if aiPlayer == 2:
        if winStatus == 0:
            return 0
        elif (winStatus == 2):
            return 10 
        elif (winStatus == 1):
            return -10
    
    bestVal = []
    
    if (len(board.possible_moves() > 0)):
        for moves in board.possible_moves():
            minimaxCount = minimaxCount + 1
            copyBoard = board.copy()
            copyBoard.push(moves)
            bestVal.append(minimax(copyBoard, not isMaxTurn, aiPlayer))
        if isMaxTurn:
            return max(bestVal)
        else:
            return min(bestVal)

def minimaxAlphaBeta(board, isMaxTurn, alpha, beta):
    global minimaxAlphaBetaCount
    winStatus = board.result()
    if winStatus == 0:
        return 0, None
    elif winStatus == 2:
        return -10, None 
    elif winStatus == 1:
        return 10, None
    
    if isMaxTurn:
        bestVal = -math.inf
        choice = None
        for move in board.possible_moves():
            minimaxAlphaBetaCount = minimaxAlphaBetaCount + 1
            copyBoard = board.copy()
            copyBoard.push(move)
            val, moveab = minimaxAlphaBeta(copyBoard, False, alpha, beta)
            if val > bestVal:
                bestVal = val
                choice = move
            alpha = max(alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal, choice
    
    else:
        bestVal = math.inf
        choice = None
        for move in board.possible_moves():
            minimaxAlphaBetaCount = minimaxAlphaBetaCount + 1
            copyBoard = board.copy()
            copyBoard.push(move)
            val, moveab = minimaxAlphaBeta(copyBoard, True, alpha, beta)
            if val < bestVal:
                bestVal = val
                choice = move
            beta = min(beta, bestVal)
            if beta <= alpha:
                break
        return bestVal, choice


def boardBestMove(board, isMaxTurn, aiPlayer):
    bestScore = -math.inf
    bestAction = None
    
    copyBoard = board.copy()
    if (len(copyBoard.possible_moves() > 0)):
        for moves in copyBoard.possible_moves():
            tempCopy = copyBoard.copy()
            copyBoard.push(moves)
            val = minimax(copyBoard, isMaxTurn, aiPlayer)
            copyBoard = tempCopy.copy()
        
            if val > bestScore:
                bestScore = val
                bestAction = moves
    return bestAction

def playMinimax(board, flag, typeAlgo):
    start = time.time()
    global minimaxAlphaBetaCount
    global minimaxCount
    if typeAlgo == 'AlphaBeta':
        if flag == True:
            minimaxAlphaBetaCount = 0
            board.push(minimaxAlphaBeta(board, True, -math.inf, math.inf)[1])
            print("Total States Covered: ", minimaxAlphaBetaCount)
        elif flag == False:
            minimaxAlphaBetaCount = 0
            board.push(minimaxAlphaBeta(board, False, -math.inf, math.inf)[1])
            print("Total States Covered: ", minimaxAlphaBetaCount)
        else:
            "INVALID OPTION!"
    elif typeAlgo == 'Minimax':
        if flag == True:
            minimaxCount = 0
            board.push(boardBestMove(board, False, 1))
            print("Total States Covered: ", minimaxCount)
        elif flag == False:
            minimaxCount = 0
            board.push(boardBestMove(board, False, 2))
            print("Total States Covered: ", minimaxCount)
        else:
            "INVALID OPTION!"
    else:
        "INVALID OPTION!"
    end = time.time()
    print("Elapsed Time: ", end-start)
            
        
def game(board, episodes, typeAlgo, option):
    for i in range(episodes):
        print("**"*20)
        print(f"\nGame {i}\n\n")
        copyBoard = board.copy()
        while copyBoard.result() is None:
            if option == 2:
                if copyBoard.result() is None:
                    copyBoard.push(defaultPlayer(copyBoard, copyBoard.turn))
                    print(copyBoard)
                if copyBoard.result() is None:
                    playMinimax(copyBoard, False, typeAlgo)
                    print(copyBoard)
                print("**"*10)
            if option == 1:
                if copyBoard.result() is None:
                    playMinimax(copyBoard, True, typeAlgo)
                    print(copyBoard)
                if copyBoard.result() is None:
                    copyBoard.push(defaultPlayer(copyBoard, copyBoard.turn))
                    print(copyBoard)
                print("**"*10)
        if copyBoard.result() is not None:
            winner = copyBoard.result()
            if option == 2 and winner == 1:
                print("\nDefault Player wins!!")
            elif option == 2 and winner == 2:
                print(f"\nAI Player {typeAlgo} wins!!")
            elif option == 1 and winner == 1:
                print(f"\nAI Player {typeAlgo} wins!!")
            elif option == 1 and winner == 2:
                print("\nDefault Player wins!!")
            else:
                print("\nDRAW GAME!")