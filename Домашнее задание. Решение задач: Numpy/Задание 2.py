import numpy as np

c = 0
for count in range(1000):
    arr = np.random.randint(1, 10, size=100)
    if len(arr[arr > 7]) == 20:
        c += 1
print(f"{c / 10}%")
