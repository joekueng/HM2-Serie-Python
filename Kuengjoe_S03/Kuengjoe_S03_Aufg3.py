import numpy as np


def function_values(x1_value, x2_value, x3_value):
    first_function_value = x1_value + x2_value**2 - x3_value**2 - 13
    second_function_value = np.log(x2_value**4 / 4) + np.exp(0.5 * x3_value - 1) - 1
    third_function_value = (x2_value - 3)**2 - x3_value**3 + 7

    return np.array([
        first_function_value,
        second_function_value,
        third_function_value
    ], dtype=float)


def jacobian_matrix(x1_value, x2_value, x3_value):
    derivative_f1_x1 = 1
    derivative_f1_x2 = 2 * x2_value
    derivative_f1_x3 = -2 * x3_value

    derivative_f2_x1 = 0
    derivative_f2_x2 = 4 / x2_value
    derivative_f2_x3 = 0.5 * np.exp(0.5 * x3_value - 1)

    derivative_f3_x1 = 0
    derivative_f3_x2 = 2 * (x2_value - 3)
    derivative_f3_x3 = -3 * x3_value**2

    return np.array([
        [derivative_f1_x1, derivative_f1_x2, derivative_f1_x3],
        [derivative_f2_x1, derivative_f2_x2, derivative_f2_x3],
        [derivative_f3_x1, derivative_f3_x2, derivative_f3_x3]
    ], dtype=float)


def damped_newton_method(start_vector, tolerance=1e-5, maximum_iterations=100):
    current_vector = np.array(start_vector, dtype=float)

    for iteration_index in range(maximum_iterations):
        current_function_values = function_values(
            current_vector[0],
            current_vector[1],
            current_vector[2]
        )

        current_function_norm = np.linalg.norm(current_function_values, 2)

        if current_function_norm < tolerance:
            return current_vector, iteration_index, current_function_norm

        current_jacobian_matrix = jacobian_matrix(
            current_vector[0],
            current_vector[1],
            current_vector[2]
        )

        newton_step = np.linalg.solve(current_jacobian_matrix, -current_function_values)

        damping_factor = 1.0

        while damping_factor > 1e-8:
            candidate_vector = current_vector + damping_factor * newton_step
            candidate_function_values = function_values(
                candidate_vector[0],
                candidate_vector[1],
                candidate_vector[2]
            )

            if np.linalg.norm(candidate_function_values, 2) < current_function_norm:
                current_vector = candidate_vector
                break

            damping_factor = damping_factor / 2

    final_function_values = function_values(
        current_vector[0],
        current_vector[1],
        current_vector[2]
    )
    final_function_norm = np.linalg.norm(final_function_values, 2)

    return current_vector, maximum_iterations, final_function_norm


start_vector = [1.5, 3.0, 2.5]

solution_vector, number_of_iterations, final_norm = damped_newton_method(start_vector)

print("Start vector =", start_vector)
print("Approximate solution =", solution_vector)
print("Iterations =", number_of_iterations)
print("||f(x^(k))||_2 =", final_norm)