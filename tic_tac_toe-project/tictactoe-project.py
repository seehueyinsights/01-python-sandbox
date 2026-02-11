"""
Tic-Tac-Toe
Current Version: 2.0 (Feb 2026)
-------------------------------
Refactored version with functions and input validation.
-------------------------------
A simple 2-player terminal game.
Author: see.huey.insights
"""


# global win conditions
win_list_h =[(0,1,2),(3,4,5),(6,7,8)]
win_list_v =[(0,3,6),(1,4,7),(2,5,8)]
win_list_x =[(0,4,8),(2,4,6)]

# function to check for integer between 1 to 9
def input_check(str):
    # Check player input
    try:
        val=int(str)
        return val>0 and val<10
    except ValueError:
        try:  
            val=float(str)
            return False
        except ValueError:
            return False
            
# function to check for winner (or draw)
def check_win(play_temp, play_grid):
    # build the results list
    output_list_h = []
    output_list_v = []
    output_list_x = []

    # create horizontal output 
    for i in range(0,3):
        for item in win_list_h[i]:
            output_list_h.append(play_temp[item])

    # create vertical output 
    for i in range(0,3):
        for item in win_list_v[i]:
            output_list_v.append(play_temp[item])

    # create diagonal output 
    for i in range(0,2):
        for item in win_list_x[i]:
            output_list_x.append(play_temp[item])

    # check for winners
    
    # check vertical and horizontal
    for i in range(0,7,3):
        # horizontal check
        if output_list_h[i:i+3].count("X") == 3: return "X wins"
        if output_list_h[i:i+3].count("O") == 3: return "O wins"
        
        # vertical check
        if output_list_v[i:i+3].count("X") == 3: return "X wins"
        if output_list_v[i:i+3].count("O") == 3: return "O wins"

    # diagonal check
    for i in range(0, 4, 3):
        if output_list_x[i:i+3].count("X") == 3: return "X wins"
        if output_list_x[i:i+3].count("O") == 3: return "O wins"

    # check draw
    if sum(play_grid) == 0:
        return "Draw"
        
    return None # Game continues

# function to announce results
def play_result(result):
    if result == "X wins":
        print("\n" + "!" * 20 + " GAME OVER " + "!" * 20 + "\n")
        print("Player 2 [X] Wins!")
        print()
    elif result == "O wins":
        print("\n" + "!" * 20 + " GAME OVER " + "!" * 20 + "\n")
        print("Player 1 [O] Wins!")
        print()
    elif result == "Draw":
        print("\n" + "!" * 20 + " Drawn Game No Winner " + "!" * 20 + "\n")
        print()


# setup and display the grid

grid_list = [['1','2','3'],
             ['4','5','6'],
             ['7','8','9']]
for item in grid_list:
    print(item)
print("This is the input grid")

print()

play_mat = {'top_in':[' ',' ',' '], 'middle_in':[' ',' ',' '], 'bottom_in':[' ',' ',' ']}
for inputs in play_mat:
    print(play_mat[inputs])
print("This is the play mat")


# Start the play by getting Player 1 input

play_grid=[1,2,3,4,5,6,7,8,9]
play_temp=[" "," "," "," "," "," "," "," "," "," "]

player=0
play_val=0
print("Player 1 [O] will start first -->")
for i in range(1,10):
    player=i
    va=0
    if player%2==0:   #odd for player 1, even for player 2
        print('Player 2 [X] input a grid position# --> ')
    else: 
        print("Player 1 [O] input a grid position# --> ")
    while input_check(va)==False:     
        print("Valid grid position# are 1 to 9")
        va=input()
        if int(va) not in play_grid: 
            print("Position already taken")
            va = 0
    
    play_val=int(va)-1 #convert into integer for slicing into play_list
    if player%2==0:   #odd for player 1, even for player 2
        play_temp[play_val]='X'
    else: 
        play_temp[play_val]='O'
    
    play_grid[play_val]=play_grid[play_val]-int(va)
                        # map player choice into grid

    # Show the play grid
    print("\n" + "# " * 10 + " UPDATED GRID " + "# " * 10 + "\n")
    print(*play_temp[0:3], sep = " | ")
    print(*play_temp[3:6], sep = " | ")
    print(*play_temp[6:9], sep = " | ")
    print("\n" + "# " * 27 + "\n")
    
    # check current game status for win condition
    game_status = check_win(play_temp, play_grid)

    # announce the results
    if game_status is not None:
        play_result(game_status)
        break 

    # Show the available moves grid
    print("\n" + "=" * 20 + " AVAILABLE MOVES " + "=" * 20 + "\n")
    print("These are the remaining play positions")
    print(*play_grid[0:3], sep = " | ")
    print(*play_grid[3:6], sep = " | ")
    print(*play_grid[6:], sep = " | ")
    print("\n" + "=" * 57 + "\n")
    print()

