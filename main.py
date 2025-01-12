import random



board=[[None,None,None],
       [None,None,None],
       [None,None,None]]


print(len(board))
def display_board():
    for row in board:
        print(row)

move=input("X or O:> ")

while True:
    bot_move_row=random.randint(-1,3)
    bot_move_column=random.randint(-1,3)
    row=int(input("Which row would you like to place:> "))
    column=int(input("Which column:> "))
    
    board[row][column]=move.upper()
    board[bot_move_row][bot_move_column]="O"
    display_board()
    
    choice=input("exit:>")
    if choice =="y":
        break
    else:
        continue
    '''if len(board)==9:
        break'''

print("Youve exited the game")