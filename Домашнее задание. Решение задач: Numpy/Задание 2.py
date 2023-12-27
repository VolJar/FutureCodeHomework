import numpy as np

c = 0
rep = 1000
for count in range(rep):
    arr = np.random.randint(1, 10, size=100)
    if len(arr[arr > 7]) == 20:
        c += 1
print(f"{(100 * c) / rep}%")
