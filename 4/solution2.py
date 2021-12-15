import numpy as np

FILENAME = "input"

def is_winner(board):
    marked = board < 0
    return marked.all(0).any() or marked.all(1).any()

with open(FILENAME) as f:
    contents = f.read().split("\n\n")
    drawn_numbers = contents[0].split(",")
    boards = [np.matrix(board.replace("\n", ";")) for board in contents[1:]]
    for drawn_number in drawn_numbers:
        for board in boards:
            if is_winner(board):
                continue
            for cell in np.nditer(board, op_flags=['readwrite']):
                if cell == int(drawn_number):
                    if cell == 0:
                        cell[...] = cell-1
                    else:
                        cell[...] = cell*-1
            if is_winner(board):
                print(board)
                sum = 0

                for cell in np.nditer(board):
                    sum += cell if cell > 0 else 0

                final_score = sum*int(drawn_number)

                print(final_score)