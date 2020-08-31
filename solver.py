import numpy as np
import pandas as pd
import random


def possible(row, col, n, board):
    row_array = board[row]  # Use row number to return the row array
    # Use column number to return the column array
    column_array = board[:, col]
    # Find the block array based off the corner values in the above two lines of code
    block_array = board[int((row // 3) * 3):
                        int((row // 3) * 3) + 3,
                        int((col // 3) * 3):
                        int((col // 3) * 3) + 3]
    # Flatten 3x3 array so it is the same size as the other arrays
    block_array = block_array.flatten()
    # Stack arrays on top of each other
    all_numbers_array = np.stack([row_array, column_array, block_array])
    unique_numbers_array = np.unique(
        all_numbers_array)  # Return unique numbers only
    # Check whether a given number is in the unique numbers array
    available_boolean = n not in unique_numbers_array
    return available_boolean


def solve(board):
    for row in range(0, 9):
        for col in range(0, 9):
            if(board[row, col] == 0):
                for n in range(1, 10):
                    if(possible(row, col, n, board) == True):
                        board[row, col] = n
                        if (board != 0).all():
                            raise StopIteration
                        solve(board)
                        board[row, col] = 0
                return


def solver(board):
    try:
        solve(board)
    except StopIteration:
        board
    return board


def random_board(total_blanks):

    board =  np.full((9,9), 0)

    # Input random values
    board[0, 0] = np.random.randint(low=1, high=9, dtype="int")
    board[1, 3] = np.random.randint(low=1, high=9, dtype="int")
    board[2, 6] = np.random.randint(low=1, high=9, dtype="int")
    board[3, 1] = np.random.randint(low=1, high=9, dtype="int")
    board[4, 4] = np.random.randint(low=1, high=9, dtype="int")
    board[5, 7] = np.random.randint(low=1, high=9, dtype="int")
    board[6, 2] = np.random.randint(low=1, high=9, dtype="int")
    board[7, 5] = np.random.randint(low=1, high=9, dtype="int")
    board[8, 8] = np.random.randint(low=1, high=9, dtype="int")

    solved_board = solver(board)

    indicies = []
    for x in range(0, 9):
        for y in range(0, 9):
            index = [x, y]
            indicies.append(index)

    randoms_needed = random.sample(indicies, total_blanks)
    for r, c in randoms_needed:
        board[r, c] = 0

    return board
