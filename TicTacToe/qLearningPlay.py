import pickle
import numpy as np

from tictactoe import Board
import random
import math
from MiniMax import *
from qLearningTrain import getMoveQ

qFile = open("qTables/q_table_final.pkl", "rb")

q_table = pickle.load(qFile)
epsilon = 0.4
POSITIONS = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

def playQLearning(board, games, opponent):
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
                    print("Opponent Q-Agent Turn. Selected Move: ", getMoveQ(board))
                    board.push(getMoveQ(board))
                elif opponent == 4:
                    print("Opponent Minimax-Agent Turn.")
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