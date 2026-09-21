# CodeOrbit Tech - Tic-Tac-Toe with Simple AI
# Task 2: Artificial Intelligence Internship

import random

# Display the game board
def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check whether a player has won
def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for combination in winning_combinations:
        if all(board[position] == player for position in combination):
            return True

    return False


# Check whether the board is full
def is_board_full(board):
    return all(position != " " for position in board)


# Simple AI move
def computer_move(board):
    # Try to win
    for position in range(9):
        if board[position] == " ":
            board[position] = "O"
            if check_winner(board, "O"):
                return
            board[position] = " "

    # Try to block the player
    for position in range(9):
        if board[position] == " ":
            board[position] = "X"
            if check_winner(board, "X"):
                board[position] = "O"
                return
            board[position] = " "

    # Choose center if available
    if board[4] == " ":
        board[4] = "O"
        return

    # Choose a random empty position
    empty_positions = [
        position for position in range(9)
        if board[position] == " "
    ]

    if empty_positions:
        position = random.choice(empty_positions)
        board[position] = "O"


# Start the game
def play_game():
    board = [" "] * 9

    print("🎮 Welcome to Tic-Tac-Toe!")
    print("You are X")
    print("Computer is O")

    while True:
        display_board(board)

        # Player move
        try:
            player_move = int(input("Enter your position (1-9): ")) - 1

            if player_move < 0 or player_move > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[player_move] != " ":
                print("That position is already taken.")
                continue

            board[player_move] = "X"

        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check player win
        if check_winner(board, "X"):
            display_board(board)
            print("🎉 You win!")
            break

        # Check draw
        if is_board_full(board):
            display_board(board)
            print("🤝 It's a draw!")
            break

        # Computer move
        print("Computer is thinking...")
        computer_move(board)

        # Check computer win
        if check_winner(board, "O"):
            display_board(board)
            print("🤖 Computer wins!")
            break

        # Check draw
        if is_board_full(board):
            display_board(board)
            print("🤝 It's a draw!")
            break


# Run the game
play_game()