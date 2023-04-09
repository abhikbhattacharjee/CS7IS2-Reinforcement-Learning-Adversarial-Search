from MiniMax import *
from qLearningTrain import *
from qLearningPlay import *
from tictactoe import Board
import time
import pickle

board = Board(dimensions=(3, 3))

if __name__=='__main__':
    print("Choice:\n 1. Train Q-Agent\n 2. Play Minimax vs Default\n 3. Play Q-Agent vs Default or Minimax\n")
    menu1 = input("Enter Choice: ")
    choice = int(menu1)
    
    if choice == 1:
        menu2 = input("Enter Number to Episodes: ")
        episodes = int(menu2)
        menu3 = input("Enter Pickle File Name to save the Agent: ")
        pkl_name = str(menu3)
        print(f"Training Q-Agent for {episodes} Episodes!\n")
        start = time.time()
        play(board, episodes)
        print('Loop completed')
        pickle.dump(q_table, open(f"qTables/{pkl_name}.pkl", "wb"))
        end = time.time()
        print("Time Elapsed: ", end-start)
    
    if choice == 2:
        menu4 = input("Please select:\n 1. Minimax with AlphaBeta Pruning\n 2. Minimax without AlphaBeta Pruning\n")
        choice2 = int(menu4)
        menu5 = input("Minimax as:\n 1. First Player\n 2. Second Player\n")
        choice3 = int(menu5)
        menu6 = input("Number of Episodes: ")
        choice4 = int(menu6)
        
        if choice2 == 1:
            game(board, choice4, 'AlphaBeta', choice3)
        elif choice2 == 2:
            game(board, choice4, 'Minimax', choice3)
    
    if choice == 3:
        menu7 = input("Choose Opponent:\n 1. Smart Default\n 2. Random Default\n 3. Q-Agent\n 4. Minimax\n")
        choice5 = int(menu7)
        menu8 = input("Number of Episodes: ")
        choice6 = int(menu8)
        playQLearning(board, choice6, choice5)