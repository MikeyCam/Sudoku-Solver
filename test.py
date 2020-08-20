import numpy as np
import pandas as pd 


board = np.array(  [[0, 2, 3, 1, 5, 0, 9, 0, 0],
                        [0, 0, 5, 0, 6, 0, 0, 0, 1],
                        [0, 6, 4, 2, 0, 9, 5, 8, 3],
                        [5, 4, 1, 0, 8, 0, 3, 0, 2],
                        [0, 0, 9, 0, 0, 0, 7, 0, 4],
                        [0, 0, 0, 0, 4, 2, 1, 0, 8],
                        [3, 9, 0, 4, 0, 6, 8, 0, 5],
                        [0, 0, 8, 7, 2, 0, 6, 3, 0],
                        [0, 5, 0, 3, 0, 0, 0, 0, 0]])

columns = ["Column {}".format(x) for x in range(1,10)]
rows = ["Row {}".format(x) for x in range(1,10)]
board = pd.DataFrame(board, columns=columns, index=rows)

print(board)