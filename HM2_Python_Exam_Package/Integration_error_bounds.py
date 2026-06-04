import math

import numpy as np


# Template esame: Rechteckregel, Trapezregel, Simpsonregel,
# errore assoluto e scelta di h/n da una stima di errore.


def function(x):
    return np.sin(x)


a = 0.0
b = np.pi
exact_integral = 2.0
n_intervals = 8

# Bounds su [a, b]. Per sin(x): max |f''| <= 1, max |f''''| <= 1.
max_abs_second_derivative = 1.0
max_abs_fourth_derivative = 1.0
target_error = 1e-4


def midpoint_rectangle_rule(f, a, b, n):
    h = (b - a) / n
    midpoints = a + (np.arange(n) + 0.5) * h
    return h * np.sum(f(midpoints))


def summed_trapezoid_rule(f, a, b, n):
    x_values = np.linspace(a, b, n + 1)
    y_values = f(x_values)
    h = (b - a) / n
    return h * (0.5 * y_values[0] + np.sum(y_values[1:-1]) + 0.5 * y_values[-1])


def summed_simpson_rule(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("Simpson needs an even number of intervals n.")

    x_values = np.linspace(a, b, n + 1)
    y_values = f(x_values)
    h = (b - a) / n
    return h / 3 * (
        y_values[0]
        + y_values[-1]
        + 4 * np.sum(y_values[1:-1:2])
        + 2 * np.sum(y_values[2:-1:2])
    )


def max_step_midpoint_rectangle(error_bound, a, b, max_abs_second_derivative):
    # |I - R_n| <= (b-a)/24 * h^2 * max |f''(x)|
    return math.sqrt(
        24 * error_bound / ((b - a) * max_abs_second_derivative)
    )


def max_step_trapezoid(error_bound, a, b, max_abs_second_derivative):
    # |I - T_n| <= (b-a)/12 * h^2 * max |f''(x)|
    return math.sqrt(
        12 * error_bound / ((b - a) * max_abs_second_derivative)
    )


def max_step_simpson(error_bound, a, b, max_abs_fourth_derivative):
    # |I - S_n| <= (b-a)/180 * h^4 * max |f''''(x)|
    return (
        180 * error_bound / ((b - a) * max_abs_fourth_derivative)
    ) ** 0.25


def required_n_from_hmax(a, b, h_max, force_even=False):
    n = math.ceil((b - a) / h_max)
    if force_even and n % 2 != 0:
        n += 1
    return n


def print_result(name, approximation, exact_value):
    print(f"{name:24s} = {approximation:.12f}")
    print(f"{'abs error':24s} = {abs(approximation - exact_value):.12e}")


if __name__ == "__main__":
    rectangle_value = midpoint_rectangle_rule(function, a, b, n_intervals)
    trapezoid_value = summed_trapezoid_rule(function, a, b, n_intervals)
    simpson_value = summed_simpson_rule(function, a, b, n_intervals)

    print("Numerical integration")
    print(f"interval = [{a}, {b}]")
    print(f"n = {n_intervals}")
    print(f"exact integral = {exact_integral:.12f}\n")

    print_result("midpoint rectangle", rectangle_value, exact_integral)
    print()
    print_result("trapezoid", trapezoid_value, exact_integral)
    print()
    print_result("simpson", simpson_value, exact_integral)

    h_rect = max_step_midpoint_rectangle(
        target_error,
        a,
        b,
        max_abs_second_derivative,
    )
    h_trap = max_step_trapezoid(
        target_error,
        a,
        b,
        max_abs_second_derivative,
    )
    h_simp = max_step_simpson(
        target_error,
        a,
        b,
        max_abs_fourth_derivative,
    )

    print("\nStep size from error bound")
    print(f"target error <= {target_error:g}")
    print(
        "rectangle: h <=",
        h_rect,
        "=> n >=",
        required_n_from_hmax(a, b, h_rect),
    )
    print(
        "trapezoid: h <=",
        h_trap,
        "=> n >=",
        required_n_from_hmax(a, b, h_trap),
    )
    print(
        "simpson:   h <=",
        h_simp,
        "=> n >=",
        required_n_from_hmax(a, b, h_simp, force_even=True),
        "(even)",
    )
