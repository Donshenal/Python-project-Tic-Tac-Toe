
def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])
    print("-" * 9)

def user_input(player, board):
    valid_input = False
    while not valid_input:
        input_position = input(f"Player {player}: Enter a position between 1 and 9: ")
        if input_position.isdigit():
            position = int(input_position)
            if 1 <= position <= 9 and board[position - 1] != "X" and board[position - 1] != "O":
                return position
            else:
                print("Invalid move. Try again.")
        else:
            print("Please enter a valid number.")

def check_winner(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]   
    ]
    for combination in win_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

def is_board_full(board):
    return all(cell != " " for cell in board)

def tic_tac_toe():
    board = [i + 1 for i in range(9)]
    players = ["X", "O"]
    player_index = 0

    while True:
        print_board(board)
        player = players[player_index]

        position = user_input(player, board)
        board[position - 1] = player

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break

        if board.count("X") == 5:
            print("It's a draw!")
            break

        player_index = 1 - player_index

if __name__ == "__main__":
    print("Welcome to a new round of Tic-Tac-Toe!")
    tic_tac_toe()
