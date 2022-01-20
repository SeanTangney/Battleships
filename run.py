"""
DOcsting
"""
import random
import shutil

SCREEN_WIDTH = shutil.get_terminal_size().columns

board = []
for n in range(5):
    board.append([" 0"] * 5)


def display_board(board):
    """
    Display board in the terminal
    """

    for row in board:
        print((" ").join(row))


def player_ship(board):
    """
    User defines where they put their ships
    """
    valid_row = False
    valid_col = False
    print("Enter your ships co-ordinates..")
    while not valid_row:
        try:
            player_ship_row = int(input("Enter your ship's row: "))
            if player_ship_row not in range(1, len(board) + 1):
                print("Invalid. Enter a number from 1 - 5")
            else:
                valid_row = True
        except ValueError:
            print("Not an valid number, please try again")
    while not valid_col:
        try:
            player_ship_col = int(input("Enter your ship's column: "))
            if player_ship_col not in range(1, len(board) + 1):
                print("Invalid. Enter a number from 1 - 5")
            else:
                board[player_ship_row - 1][player_ship_col - 1] = "*"
                valid_col = True
        except ValueError:
            print("Not an valid number, please try again")

    return board


def random_row(board):
    """
    find random row
    """
    return random.randint(0, len(board) - 1)


def random_col(board):
    """
    find random column
    """
    return random.randint(0, len(board) - 1)


def comp_ship(board):
    """
    randomize the comp ships
    """
    valid_comp_location = False
    while not valid_comp_location:
        comp_ship_row = random_row(board)
        comp_ship_col = random_col(board)
        if board[comp_ship_row][comp_ship_col] != "#":
            valid_comp_location = True
    return comp_ship_row, comp_ship_col


def main():
    """
    Main function to run the game
    """
    display_board(board)
    player_ship(board)


main()
