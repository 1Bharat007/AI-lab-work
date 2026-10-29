# LAB 02D: Hill Climbing

def f(x):
    return -(x - 5) ** 2 + 25

x = 0
step = 0.1

while True:
    current = f(x)

    left = x - step
    right = x + step

    if f(left) > current:
        x = left
    elif f(right) > current:
        x = right
    else:
        break

print("Best x:", round(x, 2))
print("Maximum value:", round(f(x), 2))