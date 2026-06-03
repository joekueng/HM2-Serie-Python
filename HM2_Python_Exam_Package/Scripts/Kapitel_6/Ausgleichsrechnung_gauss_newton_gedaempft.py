import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize

from Daten_gauss_newton import x, y


def model_function(parameter_vector, x_values):
    exponent_values = 10 ** (parameter_vector[2] + parameter_vector[3] * x_values)
    return (parameter_vector[0] + parameter_vector[1] * exponent_values) / (1 + exponent_values)


def residual_vector(parameter_vector):
    return model_function(parameter_vector, x) - y


def jacobian_matrix(parameter_vector):
    exponent_values = 10 ** (parameter_vector[2] + parameter_vector[3] * x)
    denominator_values = 1 + exponent_values
    logarithm_of_ten = np.log(10.0)

    derivative_lambda_0 = 1.0 / denominator_values
    derivative_lambda_1 = exponent_values / denominator_values
    shared_term = ((parameter_vector[1] - parameter_vector[0]) * logarithm_of_ten * exponent_values) / (denominator_values ** 2)
    derivative_lambda_2 = shared_term
    derivative_lambda_3 = x * shared_term

    return np.column_stack((derivative_lambda_0, derivative_lambda_1, derivative_lambda_2, derivative_lambda_3))


def gauss_newton(residual_function, jacobian_function, initial_parameter_vector, tolerance, maximum_iterations):
    current_parameter_vector = np.copy(initial_parameter_vector)

    for _ in range(maximum_iterations):
        orthogonal_matrix, upper_triangular_matrix = np.linalg.qr(jacobian_function(current_parameter_vector))
        step_vector = np.linalg.solve(
            upper_triangular_matrix,
            -orthogonal_matrix.T @ residual_function(current_parameter_vector)
        )
        current_parameter_vector = current_parameter_vector + step_vector

        if np.linalg.norm(step_vector) < tolerance:
            break

    return current_parameter_vector


def gauss_newton_damped(
    residual_function,
    jacobian_function,
    initial_parameter_vector,
    tolerance,
    maximum_iterations,
    maximum_backtracking_steps
):
    current_parameter_vector = np.copy(initial_parameter_vector)

    for _ in range(maximum_iterations):
        orthogonal_matrix, upper_triangular_matrix = np.linalg.qr(jacobian_function(current_parameter_vector))
        step_vector = np.linalg.solve(
            upper_triangular_matrix,
            -orthogonal_matrix.T @ residual_function(current_parameter_vector)
        )

        current_error_value = np.linalg.norm(residual_function(current_parameter_vector)) ** 2
        damping_power = 0

        while damping_power < maximum_backtracking_steps:
            candidate_parameter_vector = current_parameter_vector + step_vector / (2 ** damping_power)
            candidate_error_value = np.linalg.norm(residual_function(candidate_parameter_vector)) ** 2

            if candidate_error_value < current_error_value:
                break

            damping_power += 1

        damped_step_vector = step_vector / (2 ** damping_power)
        current_parameter_vector = current_parameter_vector + damped_step_vector

        if np.linalg.norm(damped_step_vector) < tolerance:
            break

    return current_parameter_vector


def error_function(parameter_vector):
    return np.linalg.norm(residual_vector(parameter_vector)) ** 2


initial_parameter_vector = np.array([100.0, 120.0, 3.0, -1.0], dtype=np.float64)

damped_solution = gauss_newton_damped(
    residual_vector,
    jacobian_matrix,
    initial_parameter_vector,
    1e-5,
    50,
    10
)

print("Damped Gauss-Newton:", damped_solution)

x_plot_values = np.linspace(np.min(x), np.max(x), 400)
plt.plot(x, y, "o", label="data")
plt.plot(x_plot_values, model_function(damped_solution, x_plot_values), label="fit")
plt.legend()
plt.grid(True)
plt.show()

try:
    undamped_solution = gauss_newton(
        residual_vector,
        jacobian_matrix,
        initial_parameter_vector,
        1e-5,
        50
    )
    print("Undamped Gauss-Newton:", undamped_solution)
except np.linalg.LinAlgError as error:
    print("Undamped Gauss-Newton failed:", error)

print("# Kommentar b): Das ungedämpfte Verfahren konvergiert hier nicht stabil.")

fmin_solution = scipy.optimize.fmin(error_function, initial_parameter_vector, disp=False)
print("fmin:", fmin_solution)
