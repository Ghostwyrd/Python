def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    grid_outer()
    grid_playspace(0)
  
def grid_outer():
    print("+", "+", "+", "+", sep="-"*7)

def grid_inner():
    print("|", "|", "|", "|", sep=" "*7)

def grid_playspace(b):
    for b in range(3):
        grid_inner()
        print("|", board[b][0], "|", board[b][1], "|", board[b][2], "|", sep=" "*3)
        grid_inner()
        grid_outer()

board = [[1,2,3], [4,5,6], [7,8,9]]
display_board(board)
