from random import randint


board = []
for n in range(5):
    board.append(["O"] * 5)


# Display board in the terminal
def display_board(board):
    for row in board:
        print(" ".join(row))


# User defines where they put their ships
def player_ship(board):
    valid_row = False
    valid_col = False
    print("\nEnter your ships co-ordinates..")
    while valid_row == False:
        try:
            player_ship_row = int(
                input("Enter your ship's row: "))
            if (player_ship_row not in range(1, len(board) + 1)):
                print("Invalid. Enter a number from 1 - 5").format(len(board) + 1)
            else:
                valid_row = True
        except ValueError:
            print("Not an valid number, please try again")
    while valid_col == False:
        try:
            player_ship_col = int(
                input("Enter your ship's column: "))
            if (player_ship_col not in range(1, len(board) +1)):
                 print("Invalid. Enter a number from 1 - 5").format(len(board) + 1)
            else:
                valid_col = True
        except ValueError:
            print("Not an valid number, please try again")    


# Main function to run the game
def main():
    display_board(board)
    player_ship(board)


main()

