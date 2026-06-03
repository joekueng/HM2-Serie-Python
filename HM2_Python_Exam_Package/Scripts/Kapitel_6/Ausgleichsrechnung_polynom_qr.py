import numpy as np
import matplotlib.pyplot as plt


def evaluate_quadratic_function(x_values, coefficients):
    a_coefficient, b_coefficient, c_coefficient = coefficients
    return a_coefficient * x_values ** 2 + b_coefficient * x_values + c_coefficient


def compute_error_functional(measured_values, fitted_values):
    residual_values = measured_values - fitted_values
    return np.sum(residual_values ** 2)


def main():
    temperature_values = np.array(
        [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        dtype=float,
    )
    density_values = np.array(
        [999.9, 999.7, 998.2, 995.7, 992.2, 988.1, 983.2, 977.8, 971.8, 965.3, 958.4],
        dtype=float,
    )

    design_matrix = np.column_stack(
        (
            temperature_values ** 2,
            temperature_values,
            np.ones_like(temperature_values),
        )
    )
    observation_vector = density_values

    normal_equation_matrix = design_matrix.T @ design_matrix
    normal_equation_right_hand_side = design_matrix.T @ observation_vector
    coefficients_without_qr = np.linalg.solve(
        normal_equation_matrix,
        normal_equation_right_hand_side,
    )

    orthogonal_matrix, upper_triangular_matrix = np.linalg.qr(design_matrix)
    coefficients_with_qr = np.linalg.solve(
        upper_triangular_matrix,
        orthogonal_matrix.T @ observation_vector,
    )

    coefficients_polyfit = np.polyfit(
        temperature_values,
        density_values,
        2,
    )

    condition_number_ata = np.linalg.cond(normal_equation_matrix)
    condition_number_r = np.linalg.cond(upper_triangular_matrix)

    plot_temperature_values = np.linspace(0, 100, 500)

    fitted_curve_without_qr = evaluate_quadratic_function(
        plot_temperature_values,
        coefficients_without_qr,
    )
    fitted_curve_with_qr = evaluate_quadratic_function(
        plot_temperature_values,
        coefficients_with_qr,
    )
    fitted_curve_polyfit = evaluate_quadratic_function(
        plot_temperature_values,
        coefficients_polyfit,
    )

    fitted_data_without_qr = design_matrix @ coefficients_without_qr
    fitted_data_with_qr = design_matrix @ coefficients_with_qr
    fitted_data_polyfit = design_matrix @ coefficients_polyfit

    error_without_qr = compute_error_functional(
        observation_vector,
        fitted_data_without_qr,
    )
    error_with_qr = compute_error_functional(
        observation_vector,
        fitted_data_with_qr,
    )
    error_polyfit = compute_error_functional(
        observation_vector,
        fitted_data_polyfit,
    )

    print("a) Coefficients without QR decomposition:")
    print(
        f"a = {coefficients_without_qr[0]:.12f}, "
        f"b = {coefficients_without_qr[1]:.12f}, "
        f"c = {coefficients_without_qr[2]:.12f}"
    )
    print()

    print("a) Coefficients with QR decomposition:")
    print(
        f"a = {coefficients_with_qr[0]:.12f}, "
        f"b = {coefficients_with_qr[1]:.12f}, "
        f"c = {coefficients_with_qr[2]:.12f}"
    )
    print()

    print("b) Condition numbers:")
    print(f"cond(A^T A) = {condition_number_ata:.12e}")
    print(f"cond(R)     = {condition_number_r:.12e}")
    print()

    print("c) Coefficients with numpy.polyfit():")
    print(
        f"a = {coefficients_polyfit[0]:.12f}, "
        f"b = {coefficients_polyfit[1]:.12f}, "
        f"c = {coefficients_polyfit[2]:.12f}"
    )
    print()

    print("d) Error functionals:")
    print(f"Error without QR   = {error_without_qr:.12f}")
    print(f"Error with QR      = {error_with_qr:.12f}")
    print(f"Error with polyfit = {error_polyfit:.12f}")
    print()

    plt.figure(figsize=(9, 6))
    plt.plot(
        temperature_values,
        density_values,
        "o",
        label="Data points",
    )
    plt.plot(
        plot_temperature_values,
        fitted_curve_without_qr,
        label="Normal equations without QR",
    )
    plt.plot(
        plot_temperature_values,
        fitted_curve_with_qr,
        "--",
        label="Normal equations with QR",
    )
    plt.plot(
        plot_temperature_values,
        fitted_curve_polyfit,
        ":",
        label="numpy.polyfit()",
    )
    plt.xlabel("Temperature T [°C]")
    plt.ylabel("Density ρ [g/l]")
    plt.title("Quadratic least squares fit")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
