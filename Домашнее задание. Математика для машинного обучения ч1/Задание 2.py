import numpy as np

A_a = np.array([[1, 2], [4, 5], [7, 8]])
B = np.array([[1, 1, 0], [0, 1, 1], [1, 0, 1]])
A_b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(B @ A_a)
print(A_b @ B)
print(B @ A_b)
