import random
counter=0


board=[[None,None,None],
       [None,None,None],
       [None,None,None]]

bot_move_row=0
bot_move_column=0
def display_board():
    for row in board:
        print(row)

print("WELCOME TO TIKTOK TOE, \033[31m you're PLAYER 1 and represent an  X\033[0m")

while True:
    
    row=int(input("Which row would you like to place:> "))
    column=int(input("Which column:> "))
    
    #players movement
    if board[row][column] is None:
        board[row][column]=move.upper()
        
    elif board[row][column] is not None:
        print("Spot taken")
    #bot movement
    while board[bot_move_row][bot_move_column] is not None:# if the spot is filled well keep finding new bot coordinates
        bot_move_row=random.randint(0,2)
        bot_move_column=random.randint(0,2)
        
    board[bot_move_row][bot_move_column]="O"
    display_board()
    
    choice=input("exit:>")
    if choice =="y":
        break
    else:
        continue

print("Youve exited the game")