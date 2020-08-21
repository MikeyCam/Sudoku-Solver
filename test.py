import numpy as np
import pandas as pd 
import random



indicies = []
for x in range(0,9):
    for y in range(0,9):
        index = [x, y]
        indicies.append(index)


x = random.sample(indicies, 81)






# random = np.random.randint(low = 1, high = 9, dtype = "int")


# for i in random.sample(range(0, 80), 80):
#     print(i)