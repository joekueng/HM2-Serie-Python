import numpy as np
import matplotlib.pyplot as plt


def differential_equation(x, y):
    return x**2 / y


def exact_solution(x):
    return np.sqrt(2 * x**3 / 3 + 4)


def euler_method(f, a, b, h, y0):
    n = int((b - a) / h)
    x_values = np.linspace(a, b, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0

    for step_index in range(n):
        y_values[step_index + 1] = y_values[step_index] + h * f(x_values[step_index], y_values[step_index])

    return x_values, y_values


def midpoint_method(f, a, b, h, y0):
    n = int((b - a) / h)
    x_values = np.linspace(a, b, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0

    for step_index in range(n):
        k1 = f(x_values[step_index], y_values[step_index])
        k2 = f(x_values[step_index] + h / 2, y_values[step_index] + h * k1 / 2)

        y_values[step_index + 1] = y_values[step_index] + h * k2

    return x_values, y_values


def modified_euler_method(f, a, b, h, y0):
    n = int((b - a) / h)
    x_values = np.linspace(a, b, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0

    for step_index in range(n):
        k1 = f(x_values[step_index], y_values[step_index])
        k2 = f(x_values[step_index] + h, y_values[step_index] + h * k1)

        y_values[step_index + 1] = y_values[step_index] + h / 2 * (k1 + k2)

    return x_values, y_values


def classical_runge_kutta_method(f, a, b, h, y0):
    n = int((b - a) / h)
    x_values = np.linspace(a, b, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0

    for step_index in range(n):
        k1 = f(x_values[step_index], y_values[step_index])
        k2 = f(x_values[step_index] + h / 2, y_values[step_index] + h * k1 / 2)
        k3 = f(x_values[step_index] + h / 2, y_values[step_index] + h * k2 / 2)
        k4 = f(x_values[step_index] + h, y_values[step_index] + h * k3)

        y_values[step_index + 1] = y_values[step_index] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return x_values, y_values


if __name__ == "__main__":
    a = 0
    b = 10
    h = 0.1
    y0 = 2

    x_values, euler_solution = euler_method(differential_equation, a, b, h, y0)
    _, midpoint_solution = midpoint_method(differential_equation, a, b, h, y0)
    _, modified_euler_solution = modified_euler_method(differential_equation, a, b, h, y0)
    _, rk4_solution = classical_runge_kutta_method(differential_equation, a, b, h, y0)

    exact_values = exact_solution(x_values)

    euler_error = np.abs(exact_values - euler_solution)
    midpoint_error = np.abs(exact_values - midpoint_solution)
    modified_euler_error = np.abs(exact_values - modified_euler_solution)
    rk4_error = np.abs(exact_values - rk4_solution)

    euler_error_for_plot = np.maximum(euler_error, 1e-16)
    midpoint_error_for_plot = np.maximum(midpoint_error, 1e-16)
    modified_euler_error_for_plot = np.maximum(modified_euler_error, 1e-16)
    rk4_error_for_plot = np.maximum(rk4_error, 1e-16)

    print("Maximaler globaler Fehler:")
    print("Euler:", np.max(euler_error))
    print("Mittelpunkt:", np.max(midpoint_error))
    print("Modifizierter Euler:", np.max(modified_euler_error))
    print("Klassisches RK4:", np.max(rk4_error))

    plt.figure()
    plt.plot(x_values, exact_values, label="exakte Lösung")
    plt.plot(x_values, euler_solution, label="Euler")
    plt.plot(x_values, midpoint_solution, label="Mittelpunkt")
    plt.plot(x_values, modified_euler_solution, label="modifizierter Euler")
    plt.plot(x_values, rk4_solution, label="klassisches RK4")
    plt.xlabel("x")
    plt.ylabel("y(x)")
    plt.title("Aufgabe 3a: Numerische Lösungen")
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.semilogy(x_values, euler_error_for_plot, label="Fehler Euler")
    plt.semilogy(x_values, midpoint_error_for_plot, label="Fehler Mittelpunkt")
    plt.semilogy(x_values, modified_euler_error_for_plot, label="Fehler modifizierter Euler")
    plt.semilogy(x_values, rk4_error_for_plot, label="Fehler klassisches RK4")
    plt.xlabel("x")
    plt.ylabel("globaler Fehler |y(x_i) - y_i|")
    plt.title("Aufgabe 3a: Globaler Fehler mit logarithmischer y-Achse")
    plt.grid(True)
    plt.legend()

    plt.show()
