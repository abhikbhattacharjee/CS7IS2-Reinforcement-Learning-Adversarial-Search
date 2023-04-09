# CS7IS2-Reinforcement-Learning-Adversarial-Search
CS7IS2 Assignment 2 - AI Solver for the Games - Tic Tac Toe and Connect4. Algorithms Explored - Q Learning (Reinforcement Learning) and MiniMax (With and Without Alpha-Beta Pruning)

The code is divided into two parts - One each for TicTacToe and Connect4 respectively.

## TicTacToe
The code for TicTacToe provides three functionalities:
1. Training the Q-Agent for a custom number of episodes
2. Running the Minimax Agent (with and without Alpha-Beta Pruning) against the Smart Default opponent. The Minimax agent can be customised to play the first turn or the second turn based on user input from the menu
3. Running the Q-Agent against the Random Default or Minimax Agent

Sample TicTacToe Board
```
 O | O | O 
-----------
 X | X |   
-----------
 O | X | X 
 ```

To run the main script for TicTacToe, run the following commands:
```
cd TicTacToe
python3 main.py
```

After running the above commands, the user would be presented with the following screen
```
Choice:
 1. Train Q-Agent
 2. Play Minimax vs Default
 3. Play Q-Agent vs Default or Minimax

Enter Choice: 
```
Based on the input from the user, the further prompts would be provided on the Command Line. As per the requirements and the option selected by the user, the respective scripts would be triggered and the resultant output would be provided on the command line itself.

## Connect4
The main script of Connect4 lets us define the size of the board in which we want to run the Q-Learning and the Minimax algorithms. For Minimax algorithm, the code can be run against board of any size greater than or equal to 4x4. But in order to run the Q-Agent for a custom board size, the agent needs to be trained first. Currently, the Q-Agent for the following sizes are available to use:
1. 4x4 Connect4 Board
2. 4x5 Connect4 Board
3. 5x5 Connect4 Board
4. 6x7 Connect4 Board

The code for Connect4 provides three functionalities:
1. Training the Q-Agent for a custom board size and custom number of episodes
2. Running the Minimax Agent (with Alpha-Beta Pruning) against the Smart Default opponent. The Minimax agent can be customised to play the first turn or the second turn based on user input from the menu
3. Running the Q-Agent against the Random Default or Minimax Agent

Sample Connect4 Board
```
   |   |   |   |   |   
-----------------------
   |   | O |   |   |   
-----------------------
   |   | O |   | O |   
-----------------------
 X |   | O | X | X |   
-----------------------
 O |   | O | X | X | X 
-----------------------
 O | X | X | O | O | X 
-----------------------
 O | O | X | O | X | X 
 ```

To run the main script for Connect4, run the following commands:
```
cd Connect4
python3 main.py
```

After running the above commands, the user would be presented with the following screen
```
Please enter board size:
Rows: 4
Columns: 5
Choice:
 1. Train Q-Agent
 2. Play Minimax vs Default
 3. Play Q-Agent vs Default or Minimax

Enter Choice: 
```
Based on the input from the user, the further prompts would be provided on the Command Line. As per the requirements and the option selected by the user, the respective scripts would be triggered and the resultant output would be provided on the command line itself.
