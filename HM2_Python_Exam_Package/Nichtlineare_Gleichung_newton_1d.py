import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


# Suchbegriffe:
# Newton 1D, Newton-Verfahren eindimensional, Nullstelle, Tangentenverfahren,
# f(x)=0, Ableitung, derivative, Konvergenz, Fehler.


x_symbol = sp.symbols("x")

# INPUT: Funktion, Startwert und Toleranz anpassen.
function_expr = x_symbol**3 - x_symbol - 1
start_value = 1.0
tolerance = 1e-10
maximum_iterations = 50


derivative_expr = sp.diff(function_expr, x_symbol)
function = sp.lambdify(x_symbol, function_expr, modules="numpy")
derivative = sp.lambdify(x_symbol, derivative_expr, modules="numpy")


def newton_1d(function, derivative, start_value, tolerance=1e-10, maximum_iterations=50):
    current_value = float(start_value)

    for iteration in range(1, maximum_iterations + 1):
        function_value = float(function(current_value))
        derivative_value = float(derivative(current_value))

        if derivative_value == 0:
            raise ZeroDivisionError(f"Derivative is zero at iteration {iteration}")

        step = -function_value / derivative_value
        current_value = current_value + step
        error = abs(function(current_value))

        print(
            f"iteration {iteration:2d}: "
            f"x = {current_value:.12f}, step = {step:.3e}, |f(x)| = {error:.3e}"
        )

        if error < tolerance:
            return current_value, iteration, error

    raise RuntimeError("Newton 1D did not converge")


if __name__ == "__main__":
    solution, iterations, final_error = newton_1d(
        function,
        derivative,
        start_value,
        tolerance,
        maximum_iterations,
    )

    print("\nRESULT")
    print("f(x) =", function_expr)
    print("f'(x) =", derivative_expr)
    print("solution =", solution)
    print("iterations =", iterations)
    print("|f(solution)| =", final_error)

    x_plot = np.linspace(solution - 2, solution + 2, 400)
    plt.figure()
    plt.plot(x_plot, function(x_plot), label="f(x)")
    plt.axhline(0.0, color="black", linewidth=0.8)
    plt.plot(solution, function(solution), "o", label="Newton solution")
    plt.grid(True)
    plt.legend()
    plt.show()
