# Python Tic-Tac-Toe

This is a terminal-based Tic-Tac-Toe game.

**Versions:**
*   **[v3.0 Optimised (2026)](./tictactoe-project.py):** Current version. Features optimised win-checking function, and a simplified player switch.
*   **[v2.0 Legacy Refactored (2025)](./tictactoe_legacy_2025-project.py):** Legacy version. Features robust input validation, dynamic win-checking functions, and a cleaner interface.
*   **[v1.0 Legacy (2022)](./tictactoe_legacy_2022-project.py):** Original implementation using basic control flow. Kept to demonstrate coding progress and refactoring skills.


## Current Logic

1. **Initialize Game:** Setup play board, position play grid and three logic arrays (Horizontal, Vertical, Diagonal) as lists.
2. **Input Validation:** 
   - Validate integer type (1-9).
   - Ensure position is available in the play grid.
3. **State Update:** 
   - Record and show player's position on play board.
   - Transpose moves into horizontal, vertical and diagonal logic lists.
4. **Win Detection:**
   - Check logic arrays for winning matches.
   - If no winner and board is full, declare Draw.
5. **Switch player:** Switch to next player.


## Legacy Logic

1. **Initialize Grid:** Create a 3x3 mapping (Top, Middle, Bottom).
2. **Player Input:** 
   - Player 1 (O) selects a spot.
   - Player 2 (X) selects a spot.
3. **Update Board:** Insert input into the tracking list.
4. **Game Loop:**
   - Print current grid.
   - Check Win Conditions (Horizontal, Vertical, Diagonal).
   - If a winner is found or board is full, end game.

  
# Legacy Pseudo Code: Tic-Tac-Toe
#
# 1. Print a new Grid
#    - {'top': [1,2,3], 'middle':[4,5,6], 'bottom':[7,8,9]}
#
# 2. Get Player 1 input: ply_1 insert 'O'
#
# 3. Insert ply_1 into play_list
#    - {'top_in':[1,2,3], 'middle_in':[4,5,6], 'bottom_in':[7,8,9]}
#
# 4. Print grid
#
# 5. Get Player 2 input: ply_2 insert 'X'
#
# 6. Print grid
#
# 7. Loop
#
# 8. Check win condition:
#    - hwin: top_in[i:]==same or middle_in[i:]==same or bottom_in[i:]==same
#    - vwin: top_in[i]==middle_in[i]==bottom_in[i]
#    - dwin: [0,0]==[1,1]==[2,2] or top_in[2]==middle_in[1]==bottom_in[0]
#
# 9. Declare a winner
