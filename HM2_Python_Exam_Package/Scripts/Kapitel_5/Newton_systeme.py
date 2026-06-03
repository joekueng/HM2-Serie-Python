import numpy as np
import sympy as sp


def function_vector(x_value, y_value):
    first_function_value = (x_value ** 2) / (186 ** 2) - (y_value ** 2) / (300 ** 2 - 186 ** 2) - 1
    second_function_value = ((y_value - 500) ** 2) / (279 ** 2) - ((x_value - 300) ** 2) / (500 ** 2 - 279 ** 2) - 1
    return np.array([first_function_value, second_function_value], dtype=float)


def jacobian_matrix(x_value, y_value):
    jacobian_11 = (2 * x_value) / (186 ** 2)
    jacobian_12 = (-2 * y_value) / (300 ** 2 - 186 ** 2)

    jacobian_21 = (-2 * (x_value - 300)) / (500 ** 2 - 279 ** 2)
    jacobian_22 = (2 * (y_value - 500)) / (279 ** 2)

    return np.array([
        [jacobian_11, jacobian_12],
        [jacobian_21, jacobian_22]
    ], dtype=float)


def newton_method_for_system(start_vector, tolerance=1e-5, maximum_number_of_iterations=100):
    current_vector = np.array(start_vector, dtype=float)

    for iteration_index in range(maximum_number_of_iterations):
        current_function_value = function_vector(current_vector[0], current_vector[1])
        current_function_norm = np.linalg.norm(current_function_value, 2)

        if current_function_norm < tolerance:
            return current_vector, iteration_index, current_function_norm

        current_jacobian_matrix = jacobian_matrix(current_vector[0], current_vector[1])
        newton_step = np.linalg.solve(current_jacobian_matrix, -current_function_value)
        current_vector = current_vector + newton_step

    final_function_value = function_vector(current_vector[0], current_vector[1])
    final_function_norm = np.linalg.norm(final_function_value, 2)
    return current_vector, maximum_number_of_iterations, final_function_norm


def plot_implicit_functions():
    x_symbol, y_symbol = sp.symbols('x y')

    first_function_expression = x_symbol ** 2 / 186 ** 2 - y_symbol ** 2 / (300 ** 2 - 186 ** 2) - 1
    second_function_expression = (y_symbol - 500) ** 2 / 279 ** 2 - (x_symbol - 300) ** 2 / (500 ** 2 - 279 ** 2) - 1

    first_plot = sp.plot_implicit(
        sp.Eq(first_function_expression, 0),
        (x_symbol, -2000, 2000),
        (y_symbol, -2000, 2000),
        show=False
    )

    second_plot = sp.plot_implicit(
        sp.Eq(second_function_expression, 0),
        (x_symbol, -2000, 2000),
        (y_symbol, -2000, 2000),
        show=False
    )

    first_plot.append(second_plot[0])
    first_plot.show()


def main():
    print("Plot of the two hyperbolas is opened...")
    plot_implicit_functions()

    # Hier die 4 Startvektoren aus dem Plot eintragen
    start_vectors = [
        np.array([-1300, 1600]),
        np.array([750, 900]),
        np.array([-200, 70]),
        np.array([250, 220])
    ]

    print("\nNewton-Verfahren für die 4 Startvektoren:\n")

    for solution_index, current_start_vector in enumerate(start_vectors, start=1):
        solution_vector, number_of_iterations, final_norm = newton_method_for_system(current_start_vector)

        print(f"Lösung {solution_index}:")
        print(f"startvektor = {current_start_vector}")
        print(f" Näaherungslösung = ({solution_vector[0]:.10f}, {solution_vector[1]:.10f})")
        print(f" Iterationen = {number_of_iterations}")
        print(f" ||f(x^(k))||_2 = {final_norm:.10e}")
        print()


if __name__ == "__main__":
    main()