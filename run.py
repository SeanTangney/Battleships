board = []
for n in range(5):
    board.append(["O"] * 5)

"""
Displays the board row by row
"""


def display_board(board):
    for row in board:
        print(" ".join(row))


display_board(board)