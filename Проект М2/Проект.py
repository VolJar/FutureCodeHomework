import pandas as pd
import matplotlib.pyplot as plt

main_table = pd.read_csv('Housing.csv', sep=',')

bed_cheap = list(set(main_table[main_table["price"] == main_table["price"].min()]["bedrooms"].tolist()))
bed_less_bath = len(main_table[main_table['bedrooms'] <= main_table['bathrooms']])
cheap_with_guest = list(set(main_table[main_table["guestroom"] == "yes"][main_table[main_table["guestroom"] == "yes"]['price'] == main_table[main_table["guestroom"] == "yes"]['price'].min()]['price'].tolist()))
to_from = main_table[(main_table['price'] >= 5000000) | (main_table['price'] < 2000000)]
with_air, nwith_air = main_table[main_table['airconditioning'] == 'yes'], main_table[main_table['airconditioning'] == 'no']

print('№1')

print(f'{", ".join(str(i) for i in bed_cheap)} спальни в самых дешевых домах.')
print(f"{bed_less_bath} домов, в которых количество спален не больше количества ванных.")
print(f'Самый дешёвый дом с гостевой комнатой стоит {", ".join(str(j) for j in cheap_with_guest)}.')
print(f"{round(100 * (to_from[to_from['airconditioning'] == 'yes'].shape[0]) / to_from.shape[0])}% домов от 5000000 или до 2000000 имеют кондиционирование.\n")
input('Нажмите, чтобы перейти к следующему заданию...')

print('№2')

park_color = 'g', 'r', 'b', 'black'
plt.figure(figsize=(12, 6))
plt.title("Распределение домов по цене и площади", fontweight='bold', size=15)
plt.xlabel('Цена (price)')
plt.ylabel('Площадь (area)')
for i in range(4):
    X = main_table[main_table['parking'] == i]['price']
    Y = main_table[main_table['parking'] == i]['area']
    plt.scatter(X, Y, c=park_color[i], s=13, alpha=0.3, label=('0 парковок', '1 парковка', '2 парковки', '3 парковки')[i])
plt.legend()
print('Закройте график, чтобы перейти к следующему заданию...')
plt.show()

print('№3')

fig, axs = plt.subplots(nrows=2, ncols=2)
fig.suptitle('Точечный график присутствий и отсутствий ... в домах', size=15, fontweight='bold')
n2colors = 'red', 'green'
axs[0, 0].grid()
axs[0, 0].set_title('Гостевой комнаты')
axs[0, 1].grid()
axs[0, 1].set_title('Подвала')
axs[1, 0].grid()
axs[1, 0].set_title('Обогрева с помощью горячей воды')
axs[1, 1].grid()
axs[1, 1].set_title('Предбанника')

for i in range(0, 2):
    h = 'yes' if i == 0 else 'no'
    X = main_table[main_table['guestroom'] == h]['price']
    Y = main_table[main_table['guestroom'] == h]['area']
    axs[0, 0].scatter(X, Y, c=n2colors[i], s=13, alpha=0.3, label='Да' if i == 1 else 'Нет')
for i in range(0, 2):
    h = 'yes' if i == 0 else 'no'
    X = main_table[main_table['basement'] == h]['price']
    Y = main_table[main_table['basement'] == h]['area']
    axs[0, 1].scatter(X, Y, c=n2colors[i], s=13, alpha=0.3, label='Да' if i == 1 else 'Нет')
for i in range(0, 2):
    h = 'yes' if i == 0 else 'no'
    X = main_table[main_table['hotwaterheating'] == h]['price']
    Y = main_table[main_table["hotwaterheating"] == h]['area']
    axs[1, 0].scatter(X, Y, c=n2colors[i], s=13, alpha=0.3, label='Да' if i == 1 else 'Нет')
for i in range(0, 2):
    h = 'yes' if i == 0 else 'no'
    X = main_table[main_table['prefarea'] == h]['price']
    Y = main_table[main_table['prefarea'] == h]['area']
    axs[1, 1].scatter(X, Y, c=n2colors[i], s=13, alpha=0.3, label='Да' if i == 1 else 'Нет')
axs[0, 0].legend()
axs[1, 0].legend()
axs[0, 1].legend()
axs[1, 1].legend()
print('Закройте график, чтобы перейти к следующему заданию...')
plt.show()

print('№4')

plt.figure(figsize=(12, 6))
plt.hist(with_air['price'], bins=50, color='green', alpha=0.25, edgecolor='black', label='С кондиционированием')
plt.hist(nwith_air['price'], bins=50, color='red', alpha=0.25, edgecolor='black', label='Без кондиционирования')
plt.title('Распределение цен на дома', fontweight='bold', size=15)
plt.xlabel('Цена (price)')
plt.ylabel('Частота')
plt.legend()
plt.show()
