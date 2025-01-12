board=[[None,None,None],
       [None,None,None],
       [None,None,None]]
def display_board():
    for row in board:
        print(row)
while True:
    move=input("X or O:> ")
    row=int(input("Which row would you like to place:> "))
    column=int(input("Which column:> "))
    board[row][column]=move.upper()
    display_board()