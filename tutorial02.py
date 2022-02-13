import itertools

def win(current_game):
    
    def all_same(l,how):
        if l.count(l[0]) == len(l) and l[0] != 0:
            print(f"Player {l[0]} is the winner {how}")
            return True
        else:
            return False
    
    #HORIZONTAL
    for row in game: #checks for horizontal winner
        print(row)
        if all_same(row,"horizontally!(-)"):
            return True
 
     #DIAGONAL 
    diags = []
    for col,row in enumerate(reversed(range(len(game)))):#This checks for backward diagonal
        diags.append(game[row][col])
    if all_same(diags,"diagonally!(/)"):
        return True

    diags  = []#this checks for forward diagonal
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags, "diagonally(\\)"):
        return True

    #VERTICAL
    
    for col in range(len(game)):#this checks for vertical winner
        check = []
        for row in game:
            check.append(row[col])
               
        if all_same(check, "vertically!(|)"):
            return True
    return False
                
        
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupado! Choose Another!")
            return game_map, False
        if not just_display:#This code ensures that the assignment parameters do not affect a just display syntax
            game_map[row][column]  = player
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        for count,row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as e:
        print("ERROR!,Input only numbers between 0-2 as row/column", e)
        return game_map, False
    except Exception as e:
        print("ERROR!,Something went very wrong", e)
        return game_map, False
play = True
players = [1,2]
while play:
    game_size  = int(input("What size of game do you want?:"))
    game=[[0 for i in range(game_size)]for i in range(game_size)]#List manipulation for the array
    
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won:
        current_player  = next(player_choice)
        print(f"Current Player : {current_player}")
        played =  False
        while not played:
            column_choice = int(input("What column do you want to play (0,1,2): "))
            row_choice = int(input("What row do you want to play (0,1,2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        
        if win(game):
            game_won = True
            again = input("Would you like to play again? (Y/N)")
            if again.lower() == 'y':
                print('RESTARTING ....................................................')
            elif again.lower() == 'n' :
                print('BYEEEEEE........................................................')
                play = False
            else:
                print("Not a Valid answer, Goodbye")
                print('BYEEEEEE........................................................')
                play = False
            





    
        
            



    
    
    
