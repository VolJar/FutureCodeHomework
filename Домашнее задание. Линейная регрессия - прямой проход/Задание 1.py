x = [1, 3, 7]
y = [2, 6, 14]
w = [0, 0]
lr = 0.01
epochs = 1007
for j in range(epochs):
    for i in range(len(x) - 1):
        Y = w[0] + w[1] * x[i]
        w[1] = w[1] + 2 * lr * x[i] * (y[i] - Y)
        w[0] = w[0] + 2 * lr * (y[i] - Y)
print(round(w[1]), round(w[0]))
