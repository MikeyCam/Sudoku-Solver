from solver import random_board
Revifrom solver import solver

NUMBER_OF_BLANKS = 20


puzzle = random_board(NUMBER_OF_BLANKS)
print("---------------------------------------")
print("Creating Sudoku Puzzle with {} blanks.".format(str(NUMBER_OF_BLANKS)))
print("---------------------------------------")
print(puzzle)
print("---------------------------------------")

solved_puzzle = solver(puzzle)
print("Solved Sudoku Puzzle.".format(str(NUMBER_OF_BLANKS)))
print("---------------------------------------")
print(solved_puzzle)
print("---------------------------------------")


