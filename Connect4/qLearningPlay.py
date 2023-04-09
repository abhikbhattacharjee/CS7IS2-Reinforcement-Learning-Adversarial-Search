import pickle
import numpy as np
from connectClass import Connect4
from tictactoe import Board
import random
import math
from MiniMax import *
from qLearningTrain import *

epsilon = 0

def playQLearning(board, games, opponent):
    
    if (board.dimensions) == (6, 7):
        POSITIONS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)]
        qFile = open("qTables/q_table_c4_6x7.pkl", "rb")
        q_table = pickle.load(qFile)
    elif (board.dimensions) == (4, 4):
        POSITIONS = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
        qFile = open("qTables/q_table_c4_4x4.pkl", "rb")
        q_table = pickle.load(qFile)
    elif (board.dimensions) == (4,5):
        POSITIONS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
        qFile = open("qTables/q_table_c4_4x5.pkl", "rb")
        q_table = pickle.load(qFile)
    elif (board.dimensions) == (5,5):
        POSITIONS = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
        qFile = open("qTables/q_table_c4_5x5.pkl", "rb")
        q_table = pickle.load(qFile)
    
    copyBoard = board.copy()
    for i in range(games):
        board = copyBoard.copy()
        while board.result() is None:
            if board.turn == 1:
                print("Q-Agent Turn. Selected Move: ", getMoveQ(board))
                board.push(getMoveQ(board))
                print(board)
            elif board.turn == 2:
                if opponent == 1:
                    print("Default Agent Turn. Selected Move: ", defaultPlayer(board, board.turn))
                    board.push(defaultPlayer(board, board.turn))
                elif opponent == 2:
                    print("Random Agent Turn. Selected Move: ", randomPlayer(board))
                    board.push(randomPlayer(board))
                elif opponent == 3:
                    print("Opponent Minimax-Agent Turn")
                    playMinimax(board, False, 'AlphaBeta')
                print(board)
            print("**"*10)
        if board.result() is not None:
            if board.result() == 1:
                print("Q AGENT WINS!!")
                print("**"*10)
            elif board.result() == 2:
                print(f"DEFAULT AGENT WINS!!")
                print("**"*10)
            else:
                print("DRAW!!")
                print("**"*10)