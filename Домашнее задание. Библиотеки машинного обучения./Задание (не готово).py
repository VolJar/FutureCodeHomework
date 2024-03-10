from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # один признак
y = 4 + 3 * X + np.random.randn(100, 1)  # целевая переменная с небольшим шумом
X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=0.2, random_state=42) # где random_state
# идентичен сиду
Lr = LinearRegression().fit(X_train, Y_train)
plt.scatter(X_train, Y_train, color="b", label="Данные обучения")
plt.scatter(X_test, Y_test, color="r", label="Данные теста")
