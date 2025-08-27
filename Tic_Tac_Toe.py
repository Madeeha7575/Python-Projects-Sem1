board = [" " for _ in range(9)] # 3x3 grid

def print_board():
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print(f"--|---|--")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print(f"--|---|--")
    print(f"{board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(player):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],[0, 4, 8], [2, 4, 6] ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False
def is_draw():
    return " " not in board
def make_move(position,player):
    if board[position] == " ":
        board[position]= player
        return True
    else:
        print("The spot is already taken!")
        return False
    
def play_game():
    current_player = "X"
    print("Welcome to TIC TAC TOE Game!")
    print("Player 1 : X | Player 2 : O")
    print("Choose positions below from 1-9:")
    print("1 | 2 | 3 |\n--|---|--\n4 | 5 | 6 |\n--|---|--\n7 | 8 | 9 |")
    
    while True:
        try:
            move = int(input(f"Player {current_player} Enter your move1-9:"))-1
            if move <0 or move>8:
                print("Invalid position.Enter between 1-9.")
                continue
            if make_move(move,current_player):
                print_board()
                if check_winner(current_player):
                    print(f"Player {current_player} has won!")
                    break
                elif is_draw():
                    print("It's a draw.")
                    break
                current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input.Enter a number from 1-9.")
play_game()