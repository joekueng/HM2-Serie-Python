import numpy as np
import matplotlib.pyplot as plt

x = np.array([1981, 1984, 1989, 1993, 1997, 2000, 2001, 2003, 2004, 2010], dtype=float)
y = np.array([0.5, 8.2, 15, 22.9, 36.6, 51, 56.3, 61.8, 65, 76.7], dtype=float)

x_plot = np.arange(1975, 2020.1, 0.1)

p1 = np.polyfit(x, y, len(x) - 1)
y_plot1 = np.polyval(p1, x_plot)

plt.figure()
plt.plot(x_plot, y_plot1)
plt.plot(x, y, "o")
plt.xlim(1975, 2020)
plt.ylim(-100, 250)
plt.title("Aufgabe 3a")
plt.grid()

# Das Polynom geht praktisch durch alle Datenpunkte.



x_mean = np.mean(x)
x_shift = x - x_mean
x_plot_shift = x_plot - x_mean

p2 = np.polyfit(x_shift, y, len(x_shift) - 1)
y_plot2 = np.polyval(p2, x_plot_shift)

plt.figure()
plt.plot(x_plot, y_plot2)
plt.plot(x, y, "o")
plt.xlim(1975, 2020)
plt.ylim(-100, 250)
plt.title("Aufgabe 3b")
plt.grid()

# Mit verschobenen x-Werten ist die numerische Stabilität besser.



y_2020_a = np.polyval(p1, 2020)
y_2020_b = np.polyval(p2, 2020 - x_mean)

print("Schätzwert 2020 aus a):", y_2020_a)
print("Schätzwert 2020 aus b):", y_2020_b)

# Der Schätzwert für 2020 ist unsicher, weil er außerhalb des Datenintervalls liegt.



def lagrange_int(x, y, x_int):
    y_int = np.zeros(len(x_int))

    for k in range(len(x_int)):
        s = 0
        for i in range(len(x)):
            L = 1
            for j in range(len(x)):
                if i != j:
                    L = L * (x_int[k] - x[j]) / (x[i] - x[j])
            s = s + y[i] * L
        y_int[k] = s

    return y_int

y_lagrange = lagrange_int(x, y, x_plot)

plt.figure()
plt.plot(x_plot, y_lagrange, label="Lagrange")
plt.plot(x_plot, y_plot2, label="polyfit b)")
plt.plot(x, y, "o")
plt.xlim(1975, 2020)
plt.ylim(-100, 250)
plt.title("Aufgabe 3d")
plt.grid()
plt.legend()

# Beide Kurven sind fast gleich. Kleine Unterschiede kommen von numerischen Fehlern.

plt.show()