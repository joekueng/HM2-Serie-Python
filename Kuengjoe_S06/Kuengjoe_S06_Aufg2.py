import numpy as np
import matplotlib.pyplot as plt


def compute_error_functional(measured_values, fitted_values):
    # Sum of squared errors
    residual_values = measured_values - fitted_values
    return np.sum(residual_values ** 2)


def main():
    data = np.array(
        [
            [33.00, 53.00, 3.32, 3.42, 29.00],
            [31.00, 36.00, 3.10, 3.26, 24.00],
            [33.00, 51.00, 3.18, 3.18, 26.00],
            [37.00, 51.00, 3.39, 3.08, 22.00],
            [36.00, 54.00, 3.20, 3.41, 27.00],
            [35.00, 35.00, 3.03, 3.03, 21.00],
            [59.00, 56.00, 4.78, 4.57, 33.00],
            [60.00, 60.00, 4.72, 4.72, 34.00],
            [59.00, 60.00, 4.60, 4.41, 32.00],
            [60.00, 60.00, 4.53, 4.53, 34.00],
            [34.00, 35.00, 2.90, 2.95, 20.00],
            [60.00, 59.00, 4.40, 4.36, 36.00],
            [60.00, 62.00, 4.31, 4.42, 34.00],
            [60.00, 36.00, 4.27, 3.94, 23.00],
            [62.00, 38.00, 4.41, 3.49, 24.00],
            [62.00, 61.00, 4.39, 4.39, 32.00],
            [90.00, 64.00, 7.32, 6.70, 40.00],
            [90.00, 60.00, 7.32, 7.20, 46.00],
            [92.00, 92.00, 7.45, 7.45, 55.00],
            [91.00, 92.00, 7.27, 7.26, 52.00],
            [61.00, 62.00, 3.91, 4.08, 29.00],
            [59.00, 42.00, 3.75, 3.45, 22.00],
            [88.00, 65.00, 6.48, 5.80, 31.00],
            [91.00, 89.00, 6.70, 6.60, 45.00],
            [63.00, 62.00, 4.30, 4.30, 37.00],
            [60.00, 61.00, 4.02, 4.10, 37.00],
            [60.00, 62.00, 4.02, 3.89, 33.00],
            [59.00, 62.00, 3.98, 4.02, 27.00],
            [59.00, 62.00, 4.39, 4.53, 34.00],
            [37.00, 35.00, 2.75, 2.64, 19.00],
            [35.00, 35.00, 2.59, 2.59, 16.00],
            [37.00, 37.00, 2.73, 2.59, 22.00],
        ],
        dtype=float,
    )

    tank_temperature_values = data[:, 0]
    gasoline_temperature_values = data[:, 1]
    tank_pressure_values = data[:, 2]
    gasoline_pressure_values = data[:, 3]
    measured_mass_values = data[:, 4]

    design_matrix = np.column_stack(
        (
            tank_temperature_values,
            gasoline_temperature_values,
            tank_pressure_values,
            gasoline_pressure_values,
            np.ones(len(data)),
        )
    )

    normal_equation_matrix = design_matrix.T @ design_matrix
    normal_equation_right_hand_side = design_matrix.T @ measured_mass_values
    lambda_coefficients = np.linalg.solve(
        normal_equation_matrix,
        normal_equation_right_hand_side,
    )

    fitted_mass_values = design_matrix @ lambda_coefficients

    error_value = compute_error_functional(
        measured_mass_values,
        fitted_mass_values,
    )

    print("Coefficients:")
    print(f"lambda1 = {lambda_coefficients[0]:.12f}")
    print(f"lambda2 = {lambda_coefficients[1]:.12f}")
    print(f"lambda3 = {lambda_coefficients[2]:.12f}")
    print(f"lambda4 = {lambda_coefficients[3]:.12f}")
    print(f"lambda5 = {lambda_coefficients[4]:.12f}")
    print()

    print("Model:")
    print(
        "m_CH = "
        f"{lambda_coefficients[0]:.12f} * T_tank + "
        f"{lambda_coefficients[1]:.12f} * T_benzin + "
        f"{lambda_coefficients[2]:.12f} * p_tank + "
        f"{lambda_coefficients[3]:.12f} * p_benzin + "
        f"{lambda_coefficients[4]:.12f}"
    )
    print()

    print(f"Error functional = {error_value:.12f}")

    experiment_indices = np.arange(1, len(data) + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(
        experiment_indices,
        measured_mass_values,
        "o",
        label="Measured values",
    )
    plt.plot(
        experiment_indices,
        fitted_mass_values,
        "-",
        label="Linear fit",
    )
    plt.xlabel("Experiment number")
    plt.ylabel("m_CH [g]")
    plt.title("Linear least squares fit for m_CH")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()