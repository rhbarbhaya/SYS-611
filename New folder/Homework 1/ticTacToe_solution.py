# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe Example

@author: Paul T. Grogan, pgrogan@stevens.edu
"""

# define the game state as a list of lists with 3x3 grid cells
# initialize the cells to a blank space character
state = [
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

# define a function to check if a mark is valid
def is_valid(row, col):
    # check if the row/column is empty
    return state[row][col] == " "

# define a function to mark an 'x' at a row and column
def mark_x(row, col):
    # check if this is a valid move
    if is_valid(row, col):
        # if valid, update the state accordingly
        state[row][col] = "x"

# define a function to mark an 'o' at a row and column
def mark_o(row, col):
    # check if this is a valid move
    if is_valid(row, col):
        # if valid, update the state accordingly
        state[row][col] = "o"

# define a function to print out the grid to the console
def show_grid():
    # iterate over each row in state
    for row in state:
        # print each row entry seperated by a vertical brace (|)
        print "|".join(row)
        # print horizontal braces if row is not the last (index -1)
        if row is not state[-1]:
            print "------"
    # print a blank line at the end
    print ""
    
def get_winner():
  if (state[0][0]==state[0][1]==state[0][2]=="x" or 
      state[1][0]==state[1][1]==state[1][2]=="x" or 
      state[2][0]==state[2][1]==state[2][2]=="x" or 
      state[0][0]==state[1][0]==state[2][0]=="x" or 
      state[0][0]==state[1][0]==state[2][0]=="x" or 
      state[0][1]==state[1][1]==state[2][1]=="x" or 
      state[0][2]==state[1][2]==state[2][2]=="x" or  
      state[0][0]==state[1][1]==state[2][2]=="x" or 
      state[2][0]==state[1][1]==state[0][2]=="x")
    return "x"
  if (state[0][0]==state[0][1]==state[0][2]=="o" or 
      state[1][0]==state[1][1]==state[1][2]=="o" or 
      state[2][0]==state[2][1]==state[2][2]=="o" or 
      state[0][0]==state[1][0]==state[2][0]=="o" or 
      state[0][0]==state[1][0]==state[2][0]=="o" or 
      state[0][1]==state[1][1]==state[2][1]=="o" or 
      state[0][2]==state[1][2]==state[2][2]=="o" or  
      state[0][0]==state[1][1]==state[2][2]=="o" or 
      state[2][0]==state[1][1]==state[0][2]=="o")
    return "o"
  return None

def is_tie():
  if is_winner():
    return False
  if (state[0][0]==" " or state[0][1]==" " or state[0][2]==" " or 
      state[1][0]==" " or state[1][1]==" " or state[1][2]==" " or
      state[2][0]==" " or state[2][1]==" " or state[2][2]==" "):
    return False
  return True

mark_x(1, 1)
show_grid()
mark_o(0, 2)
show_grid()
mark_x(0, 0)
show_grid()
mark_o(2, 2)
show_grid()