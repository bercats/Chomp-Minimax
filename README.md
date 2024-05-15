# Program Description

This assignment is about the chomp game.  
The game has two modes, Player vs. Player and Player vs. AI.  
The AI mode uses the minimax algorithm to decide the moves of the AI.  
The poisonous chocolate bar is indicated with a `#` symbol on the print statements and as a `-1` in the code. The non-eaten chocolates are indicated with `1` and the eaten chocolates are indicated with `0`.  
Players can choose the size of the chocolate bar and the starting player.  
The game ends when the poisonous chocolate is eaten.

# How to Compile and Run

The program can be compiled and run using the command line terminal with Python 3.12 (or possibly other versions, we tested it on 3.12).

The program may cause errors if any unexpected input is given to the menu, so it is recommended to follow the instructions given by the program.

The program can be run by typing the following command in the terminal:  
`python3 main.py`

# Sample Run

A sample run of the game looks like this:

`Enter number of rows: 2
Enter number of columns: 2
Choose mode (AI/Human): AI
Do you want to start first? (y/n): n
# 1
1 1

AI's turn
AI chooses move: (1, 1)
# 1
1 0

Human's turn
Enter row and column: 0 1
# 0
1 0

AI's turn
AI chooses move: (1, 0)
# 0
0 0

Human's turn
Enter row and column: 0 0
Human has to eat the poisonous piece! AI wins!
AI visited 24 nodes.`
