import numpy as np

n= 100
grid = np.random.choice([0, 1, 2, 3], size=(n, n))

print(np.where(grid == 3))