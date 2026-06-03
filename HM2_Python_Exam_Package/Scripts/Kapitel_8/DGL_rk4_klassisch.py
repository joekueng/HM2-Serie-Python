import numpy as np
import matplotlib.pyplot as plt


def Kuengjoe_S12_Aufg1(f, a, b, n, y0):
    h = (b - a) / n

    x = np.linspace(a, b, n + 1)
    y = np.zeros(n + 1)
    y[0] = y0

    for i in range(n):
        k1 = f(x[i], y[i])
        k2 = f(x[i] + h / 2, y[i] + h * k1 / 2)
        k3 = f(x[i] + h / 2, y[i] + h * k2 / 2)
        k4 = f(x[i] + h, y[i] + h * k3)

        y[i + 1] = y[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return x, y


if __name__ == "__main__":
    def f(t, y):
        return 1 - y / t

    a = 1
    b = 6
    h = 0.01
    n = int((b - a) / h)
    y0 = 5

    t, y_rk4 = Kuengjoe_S12_Aufg1(f, a, b, n, y0)
    y_exact = t / 2 + 9 / (2 * t)

    plt.plot(t, y_rk4, label="RK4 numerisch")
    plt.plot(t, y_exact, "--", label="exakt")
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title("Aufgabe 1 Test mit Aufgabe 2a")
    plt.grid(True)
    plt.legend()
    plt.show()
