"""
Tic-Tac-Toe
Current Version: 3.0 (Feb 2026)
-------------------------------
Updated version with optimised win conditions check and simplified player switch.
-------------------------------
A simple 2-player terminal game.
Author: see.huey.insights
"""


# check player input is within play_grid
def input_check(str):
    try:
        val = int(str)
        return 0 < val < 10
   
    except ValueError:
        return False
            
# define win conditions
def check_win(output_list_h, output_list_v, output_list_x):
    # check win condition against output_list 
    # same logic works for horizontal, vertical, and diagonal 
    for i in range(0, 9, 3):
        if output_list_h[i] == output_list_h[i+1] == output_list_h[i+2] != "": return True
        if output_list_v[i] == output_list_v[i+1] == output_list_v[i+2] != "": return True
        if output_list_x[i] == output_list_x[i+1] == output_list_x[i+2] != "": return True
    return False

# check player win and announces winner
def player_win(current_player):
    print("\n" + "<" * 10 + " GAME OVER " + ">" * 10 + "\n")
    print(f"PLAYER {current_player} [{'O' if current_player == 1 else 'X'}] wins!")



# initialize game variables
play_mat = [" "] * 9  #sets up the play 3x3 game grid
output_list_h = [""] * 9  #sets the translated list for horizontal rows
output_list_v = [""] * 9  #sets the translated list for vertical columns
output_list_x = [""] * 9  #sets the translated list for diagonals
play_grid = list(range(1,10))  #sets up the position reference grid
player = 1  #sets the player turn

# show the play_grid position
print("\n" + "=" * 10 + " THIS IS THE PLAY MAT " + "=" * 10 + "\n")

for i in range(0,9,3):
    print(*play_grid[i:i+3], sep=" | ")

print("\n" + "=" * 42 + "\n")

# play game
print("Player 1 [O] will start first -->")

while True:
    # Get player input
    while True:
        # loops until valid player_grid input
        va = input(f"Player {player} input a grid position# --> ")
       
        # check for valid player_grid input
        if not input_check(va):
            print("Valid grid position# are 1 to 9")
            continue
        
        # check for available player_grid input
        elif int(va) not in play_grid:
            print("Position already taken")
            continue
        
        break
    
    # convert into integer for slicing into play_list
    play_val = int(va) - 1 
    
    # update play_mat with plays
    play_mat[play_val] = "O" if player == 1 else "X"
    
    # update the output lists
     # update horizontal output list
    output_list_h[play_val] = play_mat[play_val]

     # update vertical output list
    v_transpose = (play_val % 3) * 3 + (play_val // 3)
    output_list_v[v_transpose] = play_mat[play_val]

     # update diagonal outout list
    x_pos = [(i * 3) + item.index(play_val) 
             for i, item in enumerate([(0, 4, 8), (2, 4, 6)]) 
             if play_val in item] # loops thru possible diagonals
   
    for p in x_pos:
        output_list_x[p] = play_mat[play_val]
    
    # remove the played position from play_grid
    play_grid.remove(int(va))
    
    # display game board
    print("\n" + "=" * 12 + " UPDATED PLAY MAT " + "=" * 12 + "\n")
  
    for i in range(0,9,3):
        print(*play_mat[i:i+3], sep=" | ")
 
    print("\n" + "=" * 42 + "\n")
    
    # check for win condition
    if check_win(output_list_h, output_list_v, output_list_x):
        player_win(player)
        break
        
    # check for draw condition
    if " " not in play_mat:
        print("\n" + "<" * 10 + " Drawn Game No Winner " + ">" * 10 + "\n")
        break
        
    # switch player
    player = 3 - player  # Alternate between player 1 and player 2
    
    
    
    
    

    