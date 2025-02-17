import math
# Initialize the board
board = [
 ['_', '_', '_'],
 ['_', '_', '_'],
 ['_', '_', '_']
]
# Display the board
def print_board():
 for row in board:
 print(" ".join(row))
 print()
# Check if there are empty cells
def is_moves_left():
 for row in board:
 if '_' in row:
 return True
 return False
# Evaluate the board
def evaluate():
 # Check rows and columns
 for i in range(3):
 if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '_':
 return 10 if board[i][0] == 'X' else -10
 if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '_':
 return 10 if board[0][i] == 'X' else -10
 # Check diagonals
 if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
 return 10 if board[0][0] == 'X' else -10
 if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
 return 10 if board[0][2] == 'X' else -10
 return 0
# Minimax function
def minimax(depth, is_max):
 score = evaluate()
 # Terminal state
 if score == 10 or score == -10:
 return score
 if not is_moves_left():
 return 0
 if is_max:
 best = -math.inf
 for i in range(3):
 for j in range(3):
 if board[i][j] == '_':
 board[i][j] = 'X'
 best = max(best, minimax(depth + 1, False))
 board[i][j] = '_'
 return best
 else:
 best = math.inf
 for i in range(3):
 for j in range(3):
 if board[i][j] == '_':
 board[i][j] = 'O'
 best = min(best, minimax(depth + 1, True))
 board[i][j] = '_'
 return best
# Find the best move for AI
def find_best_move():
 best_val = -math.inf
 best_move = (-1, -1)
 for i in range(3):
 for j in range(3):
 if board[i][j] == '_':
 board[i][j] = 'X'
 move_val = minimax(0, False)
 board[i][j] = '_'
 if move_val > best_val:
 best_val = move_val
 best_move = (i, j)
 return best_move
# Main game loop
def main():
 print("Tic Tac Toe Game")
 print("You are O, AI is X")
 print_board()
 while True:
 # Human move
 user_row, user_col = map(int, input("Enter your move (row and column): ").split())
 if board[user_row][user_col] != '_':
 print("Invalid move! Try again.")
 continue
 board[user_row][user_col] = 'O'
 print_board()
 if evaluate() == -10:
 print("You win!")
 break
 if not is_moves_left():
 print("It's a draw!")
 break
 # AI move