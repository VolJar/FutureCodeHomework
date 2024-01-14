import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x * np.arccos(x)


X = np.linspace(-10, 10, 10000)
Y = f(X)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('xarccosx')
plt.grid()
plt.plot(X, Y, color='green', dashes=[8, 4], alpha=0.5, label='Вот такая моя функция')
plt.legend()
plt.show()
