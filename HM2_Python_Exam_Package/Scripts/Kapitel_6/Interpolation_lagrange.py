import numpy as np

def lagrange_int(x, y, x_int):
    s = 0

    for i in range(len(x)):
        L = 1
        for j in range(len(x)):
            if i != j:
                L = L * (x_int - x[j]) / (x[i] - x[j])
        s = s + y[i] * L

    return s


x = [0, 2500, 5000, 10000]
y = [1013, 747, 540, 226]
x_int = 3750

y_int = lagrange_int(x, y, x_int)

print("y_int =", y_int)