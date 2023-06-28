board = [0,1],[2,3]
move = -1
def field():
    print("+ - + - +")
    print("|",board[0][0],"|", board[0][1],"|")
    print("+ - + - +")
    print("|",board[1][0],"|", board[1][1],"|")
    print("+ - + - +")
    

field()
move = int(input("Replace a number "))
if move == 0:
    board[0][0]="X"
elif move == 1:
    board[0][1]="X"
elif move == 2:
    board[1][0]="X"
else:
    board[1][1]="X"

field()
print(board[:])
#

#theList = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(board)):
    if move in board[i]:
        print("[{0}][{1}]".format(i, board[i].index(move))) #[1][1]
