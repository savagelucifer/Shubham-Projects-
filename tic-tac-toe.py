# Tic-Tac-Toe Game

board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw():
    return " " not in board


def play_game():
    current_player = "X"

    while True:
        print_board()

        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Invalid position! Choose a number from 1 to 9.")
                continue

            if board[move] != " ":
                print("That spot is already taken!")
                continue

            board[move] = current_player

            if check_winner(current_player):
                print_board()
                print(f"🎉 Player {current_player} wins!")
                break

            if is_draw():
                print_board()
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    play_game()


