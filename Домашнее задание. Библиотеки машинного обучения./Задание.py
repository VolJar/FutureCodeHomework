import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # отношение Об. и Тс. 4:1

model = LinearRegression().fit(X_train, y_train)
y_pred = model.predict(X_test)

plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='#3333ff', label='Обучающие данные', alpha=0.7)
plt.scatter(X_test, y_test, color='#ff0000', label='Тестовые данные', alpha=0.7)
plt.plot(X_test, y_pred, color='#999999', linewidth=3, label='Линия регрессии')
plt.xlabel('Признак')
plt.ylabel('Целевая переменная')
plt.title('Линейная регрессия')
plt.legend()
plt.show()
