import os

board = [['_','_','_'],
         ['_','_','_'],
         ['_','_','_']]

symbols = ['X', 'O']
turn = 0
p1_name = 'Player 1'
p2_name = 'Player 2'

def welcome_screen():
  logo = '''
 ____  __  ___    ____  __    ___    ____  __  ____ 
(_  _)(  )/ __)  (_  _)/ _\  / __)  (_  _)/  \(  __)
  )(   )(( (__     )( /    \( (__     )( (  O )) _) 
 (__) (__)\___)   (__)\_/\_/ \___)   (__) \__/(____)
  '''
  print(logo)

#checks number of X and O in board and holds a counter value, when 3 values are found then stop game and run game over screen 
#Check Diagonals
#if board[0][0]+ board[1][1]+board[2][2]=='XXX':
      #print("Player 1 wins!")
      #quit()




def check_win_screen(game_board):
  # Horizontal Checks 
  for j in game_board:
    #Horizontal checks in row 0
    if game_board[0][0]+ game_board[0][1]+game_board[0][2]=='XXX':
      print_board(game_board)
      print(f"{p1_name} wins!")
      quit()
    if game_board[0][0]+game_board[0][1]+game_board[0][2]=="OOO":
      print_board(game_board)
      print(f"{p2_name} wins!")
      quit()
    #Horizontal Checks in row 1 
    if game_board[1][0]+game_board[1][1]+game_board[1][2]=="XXX":
      print_board(game_board)
      print(f"{p1_name} wins!")
      quit()
    if game_board[1][0]+game_board[1][1]+game_board[1][2]=="OOO":
      print_board(game_board)
      print(f"{p2_name} wins!")
      quit()
    #Horizontal Checks in row 2
    if game_board[2][0]+game_board[2][1]+game_board[2][2]=="XXX":
      print_board(game_board)
      print(f"{p1_name} wins!")
      quit()
    if game_board[2][0]+game_board[2][1]+game_board[2][2]=="OOO":
      print_board(game_board)
      print(f"{p2_name} wins!")
      quit()
    #Vertical Checks in column 0 
    if game_board[0][0]+game_board[1][0]+game_board[2][0]=="XXX":
      print_board(game_board)
      print(f"{p1_name} wins!")
      quit() 
    if game_board[0][0]+ game_board[1][0] + game_board[2][0]=="OOO":
      print_board(game_board)
      print(f"{p2_name} wins!")
      quit() 
    #Vertical checks in column 1
    if game_board[0][1]+game_board[1][1]+game_board[2][1]=="XXX":
      print_board(game_board)
      print(f"{p1_name} wins!")
      quit() 
    if game_board[0][1]+game_board[1][1]+game_board[2][1]=="OOO":
      print_board(game_board)
      print(f"{p2_name} wins!")
      quit() 
    #Vertical Checks for Column 2 
    if game_board[0][2]+game_board[1][2]+game_board[2][2]=="XXX":
      print_board(game_board)
      print(f"{p1_name} wins!")
      quit()
    if game_board[0][2]+game_board[1][2]+game_board[2][2]=="OOO":
      print_board(game_board)
      print(f"{p2_name} wins!")
      quit() 
    #Diagonal Checks from Right to left 
    if game_board[0][2]+game_board[1][1]+game_board[2][0]=="XXX":
      print_board(game_board)
      print(f"{p1_name} wins!")
      quit()
    if game_board[0][2]+game_board[1][1]+game_board[2][0]=="OOO":
      print_board(game_board)
      print(f"{p2_name} wins!")
      quit() 
    # Diagonal Checks for Left to Right 
    if game_board[0][0]+game_board[1][1]+game_board[2][2]=="XXX":
      print_board(game_board)
      print(f"{p1_name} wins!")
      quit() 
    if game_board[0][0]+game_board[1][1]+game_board[2][2]=="OOO":
      print_board(game_board)
      print("Player 2 wins!")
      quit()  


       
  


# Prints the board
def print_board(game_board):
  ro = -1
  print("  0 1 2")
  for row in game_board:
    ro += 1
    print(ro, end=" ")
    for col in row:
      # Now prints the coords of each position of the board, per request of Bryan's and Markus's request #
      print(col, end=" ")
    print()

# Inserts a move at a given row & column
def make_move(row, col, symbol, game_board):
  if (game_board[row][col] == "_"):
    game_board[row][col] = symbol
    
    # Clear the console from previous turn
    clearConsole()

    # Next turn
    change_turn()
  
  else:
    # Clear the console from previous turn
    #clearConsole()
    
    print("already chosen!")


# Returns true when the game is over 
# Note: Currently only detects draws, not wins or losses
def is_game_over(game_board):
  if is_game_draw(game_board) is True:
    return True 
  return False

def is_game_draw(game_board):
  for row in game_board:
   for item in row:
     if item == '_' :
       return False 
  return True

# Alternates the turn between 0 and 1
def change_turn():
  global turn
  turn = (turn + 1) % 2
  if turn==0:
    print("\033[1;34;40m \n")
  else:
    print("\033[1;32;40m \n")
  

def player_in():
  while True:
    try:
      row_choice = int(input('Which row would you like to choose? '))
      col_choice = int(input('Which column would you like to choose? '))
      return row_choice, col_choice
    except:
      print("Not a valid option, please try again.")

def clearConsole():
  command = 'clear'
  if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
    command = 'cls'
  os.system(command)

def show_name():
  if turn == 0:
    print(f"Player 1: {p1_name}")
  else:
    print(f"Player 2: {p2_name}")

welcome_screen()

p1_name = input('Player 1, what is your name? ')
p2_name = input('Player 2, what is your name? ')

while not is_game_over(board):
  
  # Print the board and whose turn it is
  print_board(board)
  show_name()

  if turn==0:
    print("\033[1;34;40m \n")
  else:
    print("\033[1;32;40m \n")
  
  # Get the user input
  row_choice, col_choice = player_in()

  if (row_choice > 2 or row_choice < 0 or col_choice > 2 or col_choice < 0):
    print(f"({row_choice}, {col_choice}) is not on the grid. Please use row and column numbers from 0 to 2.")
    continue

  print("\033[1;34;40m \n")


  # Put their move on the board
  make_move(row_choice, col_choice, symbols[turn], board)

  
  # Clear_Console and Change_Turns have been moved within the make_move function to fix Ivan's issue #

  
  # Check for Win
  check_win_screen(board)

print_board(board)

if is_game_draw(board) is True:
    print("There are no space left in the board for you to fill.")


