import numpy as np
import matplotlib.pyplot as plt


def Kuengjoe_S12_Aufg1(f, a, b, n, y0):
    step_size = (b - a) / n

    x_values = np.linspace(a, b, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0

    for step_index in range(n):
        k1 = f(x_values[step_index], y_values[step_index])
        k2 = f(x_values[step_index] + step_size / 2, y_values[step_index] + step_size * k1 / 2)
        k3 = f(x_values[step_index] + step_size / 2, y_values[step_index] + step_size * k2 / 2)
        k4 = f(x_values[step_index] + step_size, y_values[step_index] + step_size * k3)

        y_values[step_index + 1] = y_values[step_index] + step_size / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return x_values, y_values


def Kuengjoe_S12_neues_RK_Verfahren(f, a, b, n, y0):
    step_size = (b - a) / n

    x_values = np.linspace(a, b, n + 1)
    y_values = np.zeros(n + 1)
    y_values[0] = y0

    for step_index in range(n):
        k1 = f(x_values[step_index], y_values[step_index])
        k2 = f(x_values[step_index] + 0.5 * step_size, y_values[step_index] + 0.5 * step_size * k1)
        k3 = f(x_values[step_index] + 0.75 * step_size, y_values[step_index] + 0.75 * step_size * k1)
        k4 = f(x_values[step_index] + 0.75 * step_size, y_values[step_index] + 0.75 * step_size * k3)

        y_values[step_index + 1] = y_values[step_index] + step_size * (
            0.1 * k1 + 0.2 * k2 + 0.3 * k3 + 0.4 * k4
        )

    return x_values, y_values


def differential_equation(t, y):
    return 1 - y / t


def exact_solution(t):
    return t / 2 + 9 / (2 * t)


if __name__ == "__main__":
    a = 1
    b = 6
    step_size = 0.01
    n = int((b - a) / step_size)
    y0 = 5

    t_values, classical_rk_solution = Kuengjoe_S12_Aufg1(differential_equation, a, b, n, y0)
    _, new_rk_solution = Kuengjoe_S12_neues_RK_Verfahren(differential_equation, a, b, n, y0)
    exact_values = exact_solution(t_values)

    classical_error = np.abs(exact_values - classical_rk_solution)
    new_error = np.abs(exact_values - new_rk_solution)

    classical_error_for_plot = np.maximum(classical_error, 1e-16)
    new_error_for_plot = np.maximum(new_error, 1e-16)

    print("Maximaler Fehler klassisches RK4:", np.max(classical_error))
    print("Maximaler Fehler neues RK-Verfahren:", np.max(new_error))
    print()

    print("The new method works in principle, but is significantly less accurate than the classic RK4.")
    print("The error remains small at h = 0.01, but the method is not as good as the classical Runge-Kutta method.")

    plt.figure()
    plt.plot(t_values, classical_rk_solution, label="klassisches RK4")
    plt.plot(t_values, new_rk_solution, label="neues RK-Verfahren")
    plt.plot(t_values, exact_values, "--", label="exakte Lösung")
    plt.xlabel("t")
    plt.ylabel("y(t)")
    plt.title("Aufgabe 2a und 2d")
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.semilogy(t_values, classical_error_for_plot, label="Fehler klassisches RK4")
    plt.semilogy(t_values, new_error_for_plot, label="Fehler neues RK-Verfahren")
    plt.xlabel("t")
    plt.ylabel("absoluter Fehler")
    plt.title("Halblogarithmischer Plot des absoluten Fehlers")
    plt.grid(True)
    plt.legend()

    plt.show()