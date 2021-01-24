# Gaming Console

This project has been written in Python 3. Before running the program be sure to install all the libraries included in the requirements.txt file. (Please ensure the version numbers.)

# How to run
First, download the entire repository. Then, run console.py to open the console which contains all the games. 

To Exit out of the Console program use the exit button on the top-right (or top-left) corner of the window.

# Program structure
This gaming console consists of three games: Tic-Tac-Toe, Connect Four and the Fifteen Puzzle. Considering the similarities and differences among games, we decided to structure the project as follows:

• There is a generic board class (board_class.py) that contains methods that are common to all three games. On the board, 0 will denote empty cells, 1 cells chosen by Player #1 and -1 cells chosen by Player #2.

• Tic-Tac-Toe inherits from the board class and implements several other methods that will determine the winner. The most important methods of this class are sum_along_direction and is_over. 

• Connect Four needs all methods used by Tic-Tac-Toe as well as one additional method that translates the column choice of a player into a position of (row, col) form. Therefore, Connect Four inherits from Tic-Tac-Toe.

• Fifteen Puzzle inherits from the board class and implements methods that are unique to it. The most important methods of this class are generate_board and is_over. In this case, 0 denotes the empty space. In this game, the user does not move a particular tile to the empty space (where 0 is), but zero is moved to the desired position. In essence, moving the tile (2, 3) to the empty space to the right of it is the same as moving the empty space to the left. The advantage of the second configuration is that the game can be won faster.
