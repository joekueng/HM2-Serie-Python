import numpy as np
import matplotlib.pyplot as plt


def main():
    data = np.array(
        [
            [1971, 2250.0],
            [1972, 2500.0],
            [1974, 5000.0],
            [1978, 29000.0],
            [1982, 120000.0],
            [1985, 275000.0],
            [1989, 1180000.0],
            [1993, 3100000.0],
            [1997, 7500000.0],
            [1999, 24000000.0],
            [2000, 42000000.0],
            [2002, 220000000.0],
            [2003, 410000000.0],
        ],
        dtype=float,
    )

    year_values = data[:, 0]
    transistor_count_values = data[:, 1]

    shifted_year_values = year_values - 1970.0
    logarithmic_transistor_values = np.log10(transistor_count_values)

    design_matrix = np.column_stack(
        (
            np.ones_like(shifted_year_values),
            shifted_year_values,
        )
    )

    normal_equation_matrix = design_matrix.T @ design_matrix
    normal_equation_right_hand_side = design_matrix.T @ logarithmic_transistor_values
    theta_coefficients = np.linalg.solve(
        normal_equation_matrix,
        normal_equation_right_hand_side,
    )

    theta_1 = theta_coefficients[0]
    theta_2 = theta_coefficients[1]

    fitted_logarithmic_values = design_matrix @ theta_coefficients
    fitted_transistor_count_values = 10 ** fitted_logarithmic_values

    extrapolated_year_value = 2015.0
    extrapolated_logarithmic_value = theta_1 + (extrapolated_year_value - 1970.0) * theta_2
    extrapolated_transistor_count_value = 10 ** extrapolated_logarithmic_value

    yearly_growth_factor = 10 ** theta_2
    doubling_time_years = np.log10(2.0) / theta_2

    print("Fit coefficients:")
    print(f"theta1 = {theta_1:.12f}")
    print(f"theta2 = {theta_2:.12f}")
    print()

    print("Model:")
    print(f"log10(N) = {theta_1:.12f} + (t - 1970) * {theta_2:.12f}")
    print()

    print("Extrapolation for 2015:")
    print(f"N(2015) = {extrapolated_transistor_count_value:.6e}")
    print()

    print("Interpretation:")
    print(f"Yearly growth factor = {yearly_growth_factor:.6f}")
    print(f"Doubling time = {doubling_time_years:.6f} years")
    print()

    if 1.5 <= doubling_time_years <= 2.0:
        print("The result is consistent with Moore's law.")
    else:
        print("The result is not fully consistent with Moore's law.")

    plot_year_values = np.linspace(year_values.min(), extrapolated_year_value, 500)
    plot_shifted_year_values = plot_year_values - 1970.0
    plot_logarithmic_values = theta_1 + plot_shifted_year_values * theta_2
    plot_transistor_count_values = 10 ** plot_logarithmic_values

    plt.figure(figsize=(10, 6))
    plt.semilogy(
        year_values,
        transistor_count_values,
        "o",
        label="Data points",
    )
    plt.semilogy(
        plot_year_values,
        plot_transistor_count_values,
        "-",
        label="Linear fit in log10 scale",
    )
    plt.semilogy(
        extrapolated_year_value,
        extrapolated_transistor_count_value,
        "s",
        label="Extrapolated value for 2015",
    )
    plt.xlabel("Year t")
    plt.ylabel("Number of transistors N")
    plt.title("Processor development and Moore's law")
    plt.grid(True, which="both")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()