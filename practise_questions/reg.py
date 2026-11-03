
X = [2, 4, 6, 8]
y = [10, 20, 30, 40]

w = 0.0
b = 0.0

lr = 0.01
epochs = 1000
m = len(X)

for epoch in range(epochs):

    dw = 0
    db = 0

    for i in range(m):

        prediction = w * X[i] + b
        error = prediction - y[i]

        dw += error * X[i]
        db += error

    w -= lr * (2 / m) * dw
    b -= lr * (2 / m) * db

print("Weight:", w)
print("Bias:", b)

x = 5
prediction = w * x + b

print("Predicted value:", prediction)
