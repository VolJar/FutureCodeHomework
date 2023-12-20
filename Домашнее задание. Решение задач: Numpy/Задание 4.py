import numpy as np

a = np.tile(np.arange(1, 11), (10, 1))
print(a.sum(axis=0))
