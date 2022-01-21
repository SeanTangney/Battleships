"""
Battleship game
"""
import random
import shutil

SCREEN_WIDTH = shutil.get_terminal_size().columns

board = []
SIZE = 5

for n in range(SIZE):
    board.append([" 0"] * SIZE)


def display_board():
    """
    Display board in the terminal
    """
    for row in board:
        print((" ").join(row))


def display_new_board():
    """
    Display updated board with users ships
    """
    for row in board:
        print((" ").join(row))

    if user_ship_count != 4:
        player_ship(board)
    else:
        print("Thats's all of your ships selected")


def player_ship(board):
    """
    User defines where they put their ships
    """
    user_ship_count = 0
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
                board[player_ship_row - 1][player_ship_col - 1] = " *"
                valid_col = True
                user_ship_count += 1
                display_new_board()
        except ValueError:
            print("Not an valid number, please try again")


def random_row():
    """
    find random row
    """
    return random.randint(0, len(board) - 1)


def random_col():
    """
    find random column
    """
    return random.randint(0, len(board) - 1)


def comp_ship():
    """
    randomize the comp ships
    """
    valid_comp_location = False
    while not valid_comp_location:
        comp_ship_row = random_row()
        comp_ship_col = random_col()
        if board[comp_ship_row][comp_ship_col] != "#":
            valid_comp_location = True
    return comp_ship_row, comp_ship_col


def main():
    """
    Main function to run the game
    """
    display_board()
    player_ship(board)


main()
