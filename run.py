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
            print("Not an valid number, please try again")  #
    return board  


# find random row
def random_row(board):
    return radint(0, len(board) - 1)


# find random column
def random_col(board):
    return radint(0, len(board) - 1)



# randomize the comp ships 
def comp_ship(board):
    valid_comp_location = False
    while(valid_comp_location == False):
        comp_ship_row = random_row(board)
        comp_ship_col = random_col(board)
        if(board[comp_ship_row][comp_ship_col] != "#"):
            valin_comp_location = True
    return comp_ship_row, comp_ship_col


# Main function to run the game
def main():
    display_board(board)
    player_ship(board)


main()

