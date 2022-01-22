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
        player_ship(board)
    else:
        print("Thats's all of your ships selected")


def player_ship(board):
    """
    User defines where they put their ships
    """
    global USER_SHIP_COUNT
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
                USER_SHIP_COUNT += 1
                display_new_board()
        except ValueError:
            print("Not an valid number, please try again")


def enemy_ships(enemy_board):
    for ship in range(4):
        ship_row, ship_column = randint(0, 6), randint(0, 6)
        while enemy_board[ship_row][ship_column] == "X":
            ship_row, ship_column = randint(0, 6), randint(0, 6)
            enemy_board[ship_row][ship_column] = "X"
        print("Enemy Board" + enemy_board)


def main():
    """
    Main function to run the game
    """
    display_board()
    player_ship(board)
    print("LETS PLAY!\n" + "\n-=-=-Key-=-=-")
    print("Player Ship Location => *")
    print("Missed Attack => X\nFound Battleships => @\n")
    enemy_ships()


main()
