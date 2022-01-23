"""
Battleship game
"""
from random import randint
import shutil

SCREEN_WIDTH = shutil.get_terminal_size().columns

board = []
ENEMY_BOARD = []
SIZE = 5
USER_SHIP_COUNT = 0


for n in range(SIZE):
    board.append([" 0"] * SIZE)


for n in range(SIZE):
    ENEMY_BOARD.append([" 0"] * SIZE)


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

    if USER_SHIP_COUNT != 4:
        place_battleships()
    else:
        print("Thats's all of your ships selected")
        print("Please enter attack coordinates. (enemy board is 5x5)")


def place_battleships():
    """
    User defines where they put their ships
    """
    global USER_SHIP_COUNT, board
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
                valid_col = True

        except ValueError:
            print("Not an valid number, please try again")

        board[player_ship_row - 1][player_ship_col - 1] = " *"
        USER_SHIP_COUNT += 1
        display_new_board()


print("LETS PLAY!\n" + "\n-=-=-Key-=-=-")
print("Player Ship Location => *")
print("Missed Attack => X\nFound Battleships => @\n")


def enemy_ships():
    """
    Prints enemy board and adds ships to it
    """
    global ENEMY_BOARD
    ship = 0
    for row_index, row in enumerate(ENEMY_BOARD):
        for col_index, col in enumerate(row):
            if ship != 4:
                if randint(1, 6) // randint(1, 6) == 0:
                    ENEMY_BOARD[row_index][col_index] = " *"
                    ship += 1
                else:
                    ENEMY_BOARD[row_index][col_index] = " 0"
    for row in ENEMY_BOARD:
        print((" ").join(row))


def main():
    """
    Main function to run the game
    """
    # display_board()
    # place_battleships()
    enemy_ships()


main()
