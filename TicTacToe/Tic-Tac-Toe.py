def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    #print("+", "+", "+", "+", sep="-"*7)
    #print("|", "|", "|", "|", sep=" "*7)
    grid_outer()
    grid_playspace(0)

  
def grid_outer():
    print("+", "+", "+", "+", sep="-"*7)

def grid_inner():
    print("|", "|", "|", "|", sep=" "*7)

def grid_playspace(b):
    for b in range (len(board)):
        grid_inner()
        print("|", board[b][0], "|", board[b][1], "|", board[b][2], "|", sep=" "*3)
        grid_inner()
        grid_outer()


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    int(input("Choose a square to move:"))

def make_list_of_free_fields(board):
        # The function browses the board and builds a list of all the free squares; 
        # the list consists of tuples, while each tuple is a pair of row and column numbers.
    x=None

def victory_for(board, sign):
        # The function analyzes the board's status in order to check if 
        # the player using 'O's or 'X's has won the game
    x=None

def draw_move(board):
        # The function draws the computer's move and updates the board.
    x=None

board = [[1,2,3],[4,5,6],[7,8,9]]
display_board(board)
