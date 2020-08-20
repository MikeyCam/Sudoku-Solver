import numpy as np

board = np.array(  [[0, 2, 3, 1, 5, 0, 9, 0, 0],
                    [0, 0, 5, 0, 6, 0, 0, 0, 1],
                    [0, 6, 4, 2, 0, 9, 5, 8, 3],
                    [5, 4, 1, 0, 8, 0, 3, 0, 2],
                    [0, 0, 9, 0, 0, 0, 7, 0, 4],
                    [0, 0, 0, 0, 4, 2, 1, 0, 8],
                    [3, 9, 0, 4, 0, 6, 8, 0, 5],
                    [0, 0, 8, 7, 2, 0, 6, 3, 0],
                    [0, 5, 0, 3, 0, 0, 0, 0, 0]])

board = np.array(board)

def possible(row, col, n):  
    row_array = board[row] # Use row number to return the row array
    column_array = board[:, col] # Use column number to return the column array
    # Find the block array based off the corner values in the above two lines of code
    block_array = board[int((row // 3) * 3):
                            int((row // 3) * 3) + 3, 
                       int((col // 3) * 3):
                            int((col // 3) * 3) + 3]
    block_array = block_array.flatten() # Flatten 3x3 array so it is the same size as the other arrays 
    all_numbers_array = np.stack([row_array, column_array, block_array]) # Stack arrays on top of each other
    unique_numbers_array = np.unique(all_numbers_array) # Return unique numbers only
    available_boolean = n not in unique_numbers_array # check whether a given number is in the unique numbers array       
    return available_boolean

def solve():
    for row in range(0, 9):
        for col in range(0,9):
            if(board[row,col] == 0):
                for n in range(1, 10):
                    if(possible(row, col, n) == True):
                        board[row,col] = n
                        # print(board)
                        if (board != 0).all():
                            raise StopIteration
                        solve()
                        board[row,col] = 0
                return

def solver():
  try:
      solve()
  except StopIteration:
      board
  return board

print(solver())