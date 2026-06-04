import numpy as np
import matplotlib.pyplot as plt


# Template esame: ordine globale, riduzione dello step e stabilita
# per y' = lambda*y. Cambia rhs/exact per il compito concreto.


lambda_value = -1.0
x_start = 0.0
x_end = 1.0
y_start = 1.0
step_sizes = np.array([0.5, 0.25, 0.125, 0.0625], dtype=float)
stability_step_sizes = np.array([0.5, 1.0, 2.1], dtype=float)


def rhs(x, y):
    return lambda_value * y


def exact_solution(x):
    return y_start * np.exp(lambda_value * (x - x_start))


def euler(f, x0, y0, x1, h):
    x_values = np.arange(x0, x1 + h / 2, h)
    y_values = np.zeros(len(x_values), dtype=float)
    y_values[0] = y0

    for i in range(len(x_values) - 1):
        y_values[i + 1] = y_values[i] + h * f(x_values[i], y_values[i])

    return x_values, y_values


def midpoint(f, x0, y0, x1, h):
    x_values = np.arange(x0, x1 + h / 2, h)
    y_values = np.zeros(len(x_values), dtype=float)
    y_values[0] = y0

    for i in range(len(x_values) - 1):
        k1 = f(x_values[i], y_values[i])
        k_mid = f(x_values[i] + h / 2, y_values[i] + h / 2 * k1)
        y_values[i + 1] = y_values[i] + h * k_mid

    return x_values, y_values


def modified_euler(f, x0, y0, x1, h):
    x_values = np.arange(x0, x1 + h / 2, h)
    y_values = np.zeros(len(x_values), dtype=float)
    y_values[0] = y0

    for i in range(len(x_values) - 1):
        k1 = f(x_values[i], y_values[i])
        predictor = y_values[i] + h * k1
        k2 = f(x_values[i] + h, predictor)
        y_values[i + 1] = y_values[i] + h / 2 * (k1 + k2)

    return x_values, y_values


def rk4(f, x0, y0, x1, h):
    x_values = np.arange(x0, x1 + h / 2, h)
    y_values = np.zeros(len(x_values), dtype=float)
    y_values[0] = y0

    for i in range(len(x_values) - 1):
        x = x_values[i]
        y = y_values[i]
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        y_values[i + 1] = y + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return x_values, y_values


def explicit_euler_stable(lambda_value, h):
    # For test equation y'=lambda*y: stable if |1 + h*lambda| <= 1.
    return abs(1 + h * lambda_value) <= 1


def estimated_order(errors, hs):
    errors = np.asarray(errors, dtype=float)
    hs = np.asarray(hs, dtype=float)
    mask = errors > 0
    return np.polyfit(np.log(hs[mask]), np.log(errors[mask]), 1)[0]


def predicted_error_after_halving(error, order):
    return error / 2**order


methods = [
    ("Euler", euler, 1),
    ("Mittelpunkt", midpoint, 2),
    ("Modified Euler", modified_euler, 2),
    ("RK4", rk4, 4),
]


if __name__ == "__main__":
    exact_end = exact_solution(x_end)

    print("Stability check for y' = lambda*y")
    print(f"lambda = {lambda_value}")
    print("Explicit Euler is stable for 0 < h < 2/abs(lambda) when lambda < 0.")
    print(f"limit h < {2 / abs(lambda_value):.6f}\n")

    for h in stability_step_sizes:
        print(f"h = {h:.6f}, Euler stable = {explicit_euler_stable(lambda_value, h)}")

    print("\nFinal errors and estimated global order")
    plt.figure()

    for name, method, theoretical_order in methods:
        errors = []
        for h in step_sizes:
            x_values, y_values = method(rhs, x_start, y_start, x_end, h)
            error = abs(y_values[-1] - exact_end)
            errors.append(error)

        order = estimated_order(errors[1:], step_sizes[1:])
        print(f"\n{name}")
        print(f"theoretical order = {theoretical_order}")
        print(f"estimated order   = {order:.3f}")
        print(f"last error        = {errors[-1]:.6e}")
        print(
            "if h is halved: expected next error approx",
            f"{predicted_error_after_halving(errors[-1], theoretical_order):.6e}",
        )

        plt.loglog(step_sizes, errors, "o-", label=name)

    plt.xlabel("h")
    plt.ylabel("global error at x_end")
    plt.grid(True, which="both")
    plt.legend()
    plt.show()
