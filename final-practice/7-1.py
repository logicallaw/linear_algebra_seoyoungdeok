import numpy as np

A = np.array([[1,1,4,1,2],
              [0,1,2,1,1],
              [0,0,0,1,2],
              [1,-1,0,0,2],
              [2,1,6,0,1]])

print(np.linalg.matrix_rank(A))