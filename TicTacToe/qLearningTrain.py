import numpy as np
from tictactoe import Board
import random
import math
import pickle
from MiniMax import *

board = Board(dimensions=(3, 3))
gamma = 0.9
alpha = 0.3
epsilon = 0.9
q_table = {}
POSITIONS = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

def giveReward(board):
    if board.result() is not None:
        if board.result() == 1:
            return 10
        elif board.result() == 2:
            return -10
        elif board.result() == 0:
            return 1
    else:
        return 0

def getBoardHash(board):
    test = []
    for position in POSITIONS:
        test.append(str(board.get_mark_at_position(position)))
    return test

def addKeyQTable(board):
    defQ = 1
    stateKey = (str(getBoardHash(board)), board.turn)
    if q_table.get(stateKey) is None:
        moves = board.possible_moves()
        q_table[stateKey] = {tuple(move): defQ for move in moves}
    return stateKey

def stochasticMinMax(q, minmax):
    minmaxQ = minmax(list(q.values()))
    if list(q.values()).count(minmax)>1:
        bestMove = [move for move in list(q.keys()) if q[move] == minmaxQ]
        move = bestMove[np.random.choice(len(bestMove))]
    else:
        move = minmax(q, key=q.get)
    return move

def getMoveQ(board):
    if np.random.uniform() < epsilon:
        action = randomPlayer(board)
        return action
    else:
        state_key = addKeyQTable(board)
        q_value = q_table[state_key]
        if board.turn == 1:
            return stochasticMinMax(q_value, max)
        elif board.turn == 2:
            return stochasticMinMax(q_value, min)

def qLearn(board, move):
    stateKey = addKeyQTable(board)
    copyBoard = board.copy()
    copyBoard.push(move)
    reward = giveReward(copyBoard)
    nextStateKey = addKeyQTable(copyBoard)
    
    if copyBoard.result() is not None:
        expected = reward
    else:
        nextQ = q_table[nextStateKey]
        if copyBoard.turn == 1:
            expected = reward + (gamma * min(nextQ.values()))
        elif copyBoard.turn == 2:
            expected = reward + (gamma * max(nextQ.values()))
        delta = alpha * (expected - q_table[stateKey][move])
        q_table[stateKey][move] += delta
        
def play(board, episodes):
    for i in range(episodes):
        if i % 10000 == 0:
            print("Rounds {}".format(i))
        if i >= ((0.4)*i):
            epsilon = 0.5
        elif i >= ((0.5)*i):
            epsilon = 0.3
        elif i >= ((0.6)*i):
            epsilon = 0.2
        elif i >= ((0.7)*i):
            epsilon = 0.1
        copyBoard = board.copy()
        while copyBoard.result() is None:
            if copyBoard.turn == 1:
                move1 = getMoveQ(copyBoard)
                qLearn(copyBoard, move1)
                copyBoard.push(move1)
            elif copyBoard.turn == 2:
                move2 = getMoveQ(copyBoard)
                # move2 = defaultPlayer(copyBoard, copyBoard.turn)
                qLearn(copyBoard, move2)
                qLearn(copyBoard, tuple(move2))
                copyBoard.push(move2)