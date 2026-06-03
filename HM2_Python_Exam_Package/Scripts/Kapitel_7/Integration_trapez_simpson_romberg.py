import numpy as np


def summed_trapezoid_from_function(function, a, b, n):
    x_values = np.linspace(a, b, n + 1)
    y_values = function(x_values)
    h = (b - a) / n
    return h * (0.5 * y_values[0] + np.sum(y_values[1:-1]) + 0.5 * y_values[-1])


def summed_trapezoid_from_table(x_values, y_values):
    return np.trapezoid(y_values, x_values)


def summed_simpson_from_function(function, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson needs an even number of intervals")

    x_values = np.linspace(a, b, n + 1)
    y_values = function(x_values)
    h = (b - a) / n
    return h / 3 * (
        y_values[0]
        + y_values[-1]
        + 4 * np.sum(y_values[1:-1:2])
        + 2 * np.sum(y_values[2:-1:2])
    )


def romberg_from_function(function, a, b, levels):
    table = np.zeros((levels, levels), dtype=float)

    for row in range(levels):
        n = 2**row
        table[row, 0] = summed_trapezoid_from_function(function, a, b, n)

        for column in range(1, row + 1):
            table[row, column] = (
                4**column * table[row, column - 1] - table[row - 1, column - 1]
            ) / (4**column - 1)

    return table


def max_step_trapezoid(error_bound, a, b, max_abs_second_derivative):
    # Error <= (b-a)/12 * h^2 * max |f''|
    return np.sqrt(12 * error_bound / ((b - a) * max_abs_second_derivative))


if __name__ == "__main__":
    # Function example from FS22: integral of 6*x^2 - 2*x from 0 to 4.
    function = lambda x: 6 * x**2 - 2 * x
    a = 0.0
    b = 4.0

    print("summed trapezoid n=4 =", summed_trapezoid_from_function(function, a, b, n=4))
    print("summed simpson n=4 =", summed_simpson_from_function(function, a, b, n=4))
    print("romberg table:")
    print(romberg_from_function(function, a, b, levels=3))

    # Table example: replace with table values from the exam.
    x_table = np.array([0.0, 0.5, 1.0, 1.5, 2.0])
    y_table = np.array([2.0, np.sqrt(15) / 2, np.sqrt(3), np.sqrt(7) / 2, 0.0])
    print("table trapezoid =", summed_trapezoid_from_table(x_table, y_table))
