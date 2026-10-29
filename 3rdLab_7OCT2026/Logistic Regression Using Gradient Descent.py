import math

X = [[1, 2], [2, 1], [3, 4], [4, 3]]
y = [0, 0, 1, 1]

w1 = 0.0
w2 = 0.0
b = 0.0

lr = 0.1
epochs = 1000
m = len(X)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

for epoch in range(epochs):
    dw1 = 0
    dw2 = 0
    db = 0

    for i in range(m):
        z = w1 * X[i][0] + w2 * X[i][1] + b
        prediction = sigmoid(z)
        error = prediction - y[i]

        dw1 += error * X[i][0]
        dw2 += error * X[i][1]
        db += error

    w1 -= lr * dw1 / m
    w2 -= lr * dw2 / m
    b -= lr * db / m

for point in X:
    z = w1 * point[0] + w2 * point[1] + b
    prediction = sigmoid(z)
    print(point, "Class:", 1 if prediction >= 0.5 else 0)