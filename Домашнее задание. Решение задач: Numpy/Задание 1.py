import numpy as np

arr = np.random.randint(1, 10, size=100)
print(f'{(100 * len(arr[arr > 7])) / len(arr)}%')
