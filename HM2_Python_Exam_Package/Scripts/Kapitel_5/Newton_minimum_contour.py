import numpy as np
import matplotlib.pyplot as plt


def f(vector):
    x, y = vector
    return np.array([
        4 * x**3 - 4 * x * y + 20 * x - 8.4,
        -2 * x**2 + 2 * y,
    ], dtype=float)


def jacobian(vector):
    x, y = vector
    return np.array([
        [12 * x**2 - 4 * y + 20, -4 * x],
        [-4 * x, 2],
    ], dtype=float)


def objective(vector):
    x, y = vector
    return x**4 - 2 * x**2 * y + 10 * x**2 - 8.4 * x + y**2 + 5.764


def newton_system(f_function, jacobian_function, start_vector, tolerance=1e-8, max_iterations=50):
    current_vector = np.array(start_vector, dtype=float)

    for iteration in range(1, max_iterations + 1):
        function_value = f_function(current_vector)
        newton_step = np.linalg.solve(jacobian_function(current_vector), -function_value)
        current_vector = current_vector + newton_step
        error = np.linalg.norm(f_function(current_vector), ord=np.inf)

        print(
            f"iteration {iteration:2d}: "
            f"x = {current_vector}, step_norm = {np.linalg.norm(newton_step):.3e}, "
            f"error_inf = {error:.3e}"
        )

        if error < tolerance:
            return current_vector, iteration

    raise RuntimeError("Newton method did not converge")


def plot_zero_contours(x_min=0.0, x_max=1.0, y_min=0.0, y_max=1.0):
    x_values = np.linspace(x_min, x_max, 400)
    y_values = np.linspace(y_min, y_max, 400)
    x_grid, y_grid = np.meshgrid(x_values, y_values)

    f1_values = 4 * x_grid**3 - 4 * x_grid * y_grid + 20 * x_grid - 8.4
    f2_values = -2 * x_grid**2 + 2 * y_grid

    plt.figure()
    plt.contour(x_grid, y_grid, f1_values, levels=[0], colors="tab:red")
    plt.contour(x_grid, y_grid, f2_values, levels=[0], colors="tab:blue")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.title("f1 = 0 and f2 = 0")


if __name__ == "__main__":
    # Adapt this start vector from the contour plot or from the exam statement.
    start_vector = np.array([0.2, 0.8])

    plot_zero_contours()
    solution, iterations = newton_system(f, jacobian, start_vector)

    print("\nRESULT")
    print("solution =", solution)
    print("iterations =", iterations)
    print("f(solution) =", f(solution))
    print("objective(solution) =", objective(solution))

    plt.plot(solution[0], solution[1], "ok", label="Newton solution")
    plt.legend()
    plt.show()
