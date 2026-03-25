import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

from Kuengjoe_S05_Aufg2 import Kuengjoe_S05_Aufg2


def main():
    time_values_years = np.array(
        [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
        dtype=float,
    )

    population_values_millions = np.array(
        [75.995, 91.972, 105.711, 123.203, 131.669, 150.697, 179.323, 203.212, 226.505, 249.633, 281.422, 308.745],
        dtype=float,
    )

    dense_evaluation_time_values = np.linspace(
        time_values_years[0],
        time_values_years[-1],
        1000,
    )

    # a) Eigene natürliche kubische Spline aus Aufgabe 2
    spline_values_custom_implementation = Kuengjoe_S05_Aufg2(
        time_values_years,
        population_values_millions,
        dense_evaluation_time_values,
        plot_result=False,
    )

    # b) SciPy CubicSpline mit natürlichen Randbedingungen
    scipy_natural_cubic_spline = CubicSpline(
        time_values_years,
        population_values_millions,
        bc_type="natural",
    )
    spline_values_scipy = scipy_natural_cubic_spline(dense_evaluation_time_values)

    # c) Polynom 11. Grades mit verschobener Zeitachse
    shifted_time_values_years = time_values_years - 1900.0
    shifted_dense_evaluation_time_values = dense_evaluation_time_values - 1900.0

    polynomial_degree = 11
    polynomial_coefficients = np.polyfit(
        shifted_time_values_years,
        population_values_millions,
        polynomial_degree,
    )
    polynomial_values_degree_eleven = np.polyval(
        polynomial_coefficients,
        shifted_dense_evaluation_time_values,
    )

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(
        dense_evaluation_time_values,
        spline_values_custom_implementation,
        label="Aufgabe 2: eigene natürliche kubische Spline",
    )
    plt.plot(
        dense_evaluation_time_values,
        spline_values_scipy,
        "--",
        label="SciPy CubicSpline (natural)",
    )
    plt.plot(
        dense_evaluation_time_values,
        polynomial_values_degree_eleven,
        ":",
        label="Polynom 11. Grades",
    )
    plt.plot(
        time_values_years,
        population_values_millions,
        "o",
        label="Messdaten",
    )

    plt.xlabel("Jahr")
    plt.ylabel("Bevölkerung (in Mio.)")
    plt.title("Vergleich der Interpolationen")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    custom_values_at_nodes = Kuengjoe_S05_Aufg2(
        time_values_years,
        population_values_millions,
        time_values_years,
        plot_result=False,
    )
    scipy_values_at_nodes = scipy_natural_cubic_spline(time_values_years)
    polynomial_values_at_nodes = np.polyval(
        polynomial_coefficients,
        shifted_time_values_years,
    )

    print("Original data:")
    print(population_values_millions)
    print()

    print("Custom spline at nodes:")
    print(custom_values_at_nodes)
    print()

    print("SciPy spline at nodes:")
    print(scipy_values_at_nodes)
    print()

    print("Degree-11 polynomial at nodes:")
    print(polynomial_values_at_nodes)


if __name__ == "__main__":
    main()