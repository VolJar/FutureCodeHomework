import numpy as np

X = np.array([[1, 145], [2, 163], [3, 240], [3, 350], [4, 421], [4, 397], [5, 620]])
Y = np.array([80, 170, 100, 220, 200, 270, 500])
A = np.dot(X.T, Y)
B = np.dot(X.T, X)
w = A / B
print(w)
