import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(16, 2, 1000)
plt.hist(data, color='red', alpha=0.5, edgecolor='black', bins=20)
plt.title(f'В среднем {int(np.mean(data))} с')
plt.suptitle('Результаты забега школьников на 100 метров', fontweight='bold')
plt.xlabel('Время участников (t, с)')
plt.ylabel('Количество (ч)')
plt.show()
