X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 0, 0, 1]

w = [0.0, 0.0]
b = 0.0
lr = 0.1

for epoch in range(20):
    for i in range(len(X)):
        z = w[0] * X[i][0] + w[1] * X[i][1] + b
        prediction = 1 if z > 0 else 0
        error = y[i] - prediction

        w[0] += lr * error * X[i][0]
        w[1] += lr * error * X[i][1]
        b += lr * error

for point in X:
    z = w[0] * point[0] + w[1] * point[1] + b
    prediction = 1 if z > 0 else 0
    print(point, "Prediction:", prediction)