import random



board=[[None,None,None],
       [None,None,None],
       [None,None,None]]



def display_board():
    for row in board:
        print(row)

move=input("X or O:> ")

while True:
    bot_move_row=random.randint(0,2)
    bot_move_column=random.randint(0,2)
    row=int(input("Which row would you like to place:> "))
    column=int(input("Which column:> "))
    
    
    if board[row][column] is None:
        board[row][column]=move.upper()
        if board[bot_move_row][bot_move_column] is None:
            board[bot_move_row][bot_move_column]="O"
    elif board[row][column] is not None:
        print("Spot taken")
    display_board()
    
    choice=input("exit:>")
    if choice =="y":
        break
    else:
        continue

print("Youve exited the game")