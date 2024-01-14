import numpy as np
import matplotlib.pyplot as plt

X = np.random.normal(0, 1, 3000)
Y = np.random.normal(3, 4, 3000)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.scatter(X, Y, c='blue', s=3, alpha=0.3, marker='*')
plt.show()
