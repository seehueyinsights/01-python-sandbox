"""
Tic-Tac-Toe Game (ver 1)
----------------
A simple 2-player terminal game.
Author: see.huey.insights
"""

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
            
# check for integer between 1 to 9


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
        if va in play_grid:
            print("Position already taken")
            va=0
    
    play_val=int(va)-1 #convert into integer for slicing into play_list
    if player%2==0:   #odd for player 1, even for player 2
        play_temp[play_val]='X'
    else: 
        play_temp[play_val]='O'
    
    play_grid[play_val]=play_grid[play_val]-int(va)
                        # map player choice into grid
    print("# # #")
    print(*play_temp[0:3], sep = ", ")
    print(*play_temp[3:6], sep = ", ")
    print(*play_temp[6:9], sep = ", ")
    print("# # #")
    print("This are the play positions")
    print(*play_grid[0:3], sep = ", ")
    print(*play_grid[3:6], sep = ", ")
    print(*play_grid[6:], sep = ", ")
    print()
    
    
    # check against the win condition horizontal
win_list_h =[(0,1,2),(3,4,5),(6,7,8)]
win_list_v =[(0,3,6),(1,4,7),(2,5,8)]
win_list_x =[(0,4,8),(2,4,6)]
    
output_list_h=[]
output_list_v=[]
output_list_x=[]
    
for i in range(0,3):
    for item in win_list_h[i]:
            #create horizontal output 
        output_list_h.append(play_temp[item])
   
for i in range(0,3):
    for item in win_list_v[i]:
            #create vertical output 
        output_list_v.append(play_temp[item])
    
for i in range(0,2):
    for item in win_list_x[i]:
            #create cross output 
        output_list_x.append(play_temp[item])
        

# check win condition
a=0
for i in range(0,7,3):
    if output_list_h[i:i+3].count("X")==3 or output_list_v[i:i+3].count("X")==3:
        print("Player 2 [X] Wins!")
        a=1
    else:
        if output_list_h[i:i+3].count("O")==3 or output_list_v[i:i+3].count("O")==3:
            print("Player 1 [O] Wins!")
            a=1

for i in range(0,4,3):
    if output_list_x[i:i+3].count("X")==3: 
        print("Player 2 [X] Wins!")
        a=1
    else:
        if output_list_x[i:i+3].count("O")==3: 
            print("Player 1 [O] Wins!")
            a=1

if a==0:
    print("Drawn Game No Winner!")