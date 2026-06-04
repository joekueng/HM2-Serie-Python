import numpy as np


# Vereinfachtes Newton-Verfahren:
# Die Jacobi-Matrix wird nur am Startpunkt berechnet und bleibt danach fix.


def function_values(vector):
    x1, x2, x3 = vector
    return np.array([
        x1 + x2**2 - x3**2 - 13,
        np.log(x2 / 4) + np.exp(0.5 * x3 - 1) - 1,
        (x2 - 3)**2 - x3**3 + 7,
    ], dtype=float)


def jacobian_matrix(vector):
    x1, x2, x3 = vector
    return np.array([
        [1.0, 2 * x2, -2 * x3],
        [0.0, 1 / x2, 0.5 * np.exp(0.5 * x3 - 1)],
        [0.0, 2 * (x2 - 3), -3 * x3**2],
    ], dtype=float)


def simplified_newton(start_vector, tolerance=1e-8, maximum_iterations=50):
    current_vector = np.array(start_vector, dtype=float)
    fixed_jacobian = jacobian_matrix(current_vector)

    for iteration in range(maximum_iterations + 1):
        current_values = function_values(current_vector)
        current_norm = np.linalg.norm(current_values, ord=np.inf)

        print(
            f"{iteration:2d}: x = {current_vector}, "
            f"||f(x)||_inf = {current_norm:.3e}"
        )

        if current_norm < tolerance:
            return current_vector, iteration, current_norm

        newton_step = np.linalg.solve(fixed_jacobian, -current_values)
        current_vector = current_vector + newton_step

    final_norm = np.linalg.norm(function_values(current_vector), ord=np.inf)
    return current_vector, maximum_iterations, final_norm


if __name__ == "__main__":
    start_vector = np.array([1.5, 3.0, 2.5], dtype=float)
    solution, iterations, norm = simplified_newton(start_vector)

    print("\nResult")
    print("solution =", solution)
    print("iterations =", iterations)
    print("final norm =", norm)
