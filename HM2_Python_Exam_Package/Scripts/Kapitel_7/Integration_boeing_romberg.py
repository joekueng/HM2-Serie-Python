import numpy as np


def trapezoidal_rule(function_to_integrate, lower_bound, upper_bound, number_of_intervals):
    interval_width = (upper_bound - lower_bound) / number_of_intervals

    total_sum = 0.5 * function_to_integrate(lower_bound)
    total_sum += 0.5 * function_to_integrate(upper_bound)

    for interval_index in range(1, number_of_intervals):
        current_value = lower_bound + interval_index * interval_width
        total_sum += function_to_integrate(current_value)

    return interval_width * total_sum


def romberg_extrapolation(function_to_integrate, lower_bound, upper_bound, romberg_levels):
    romberg_table = np.zeros((romberg_levels, romberg_levels))

    for row_index in range(romberg_levels):
        number_of_intervals = 2 ** row_index
        romberg_table[row_index, 0] = trapezoidal_rule(
            function_to_integrate,
            lower_bound,
            upper_bound,
            number_of_intervals
        )

    for column_index in range(1, romberg_levels):
        for row_index in range(column_index, romberg_levels):
            factor = 4 ** column_index
            romberg_table[row_index, column_index] = (
                factor * romberg_table[row_index, column_index - 1]
                - romberg_table[row_index - 1, column_index - 1]
            ) / (factor - 1)

    return romberg_table


airplane_mass = 97000
initial_velocity = 100
romberg_levels = 6


def time_integrand(velocity):
    return airplane_mass / (5 * velocity ** 2 + 570000)


def distance_integrand(velocity):
    return airplane_mass * velocity / (5 * velocity ** 2 + 570000)


time_romberg_table = romberg_extrapolation(
    time_integrand,
    0,
    initial_velocity,
    romberg_levels
)

distance_romberg_table = romberg_extrapolation(
    distance_integrand,
    0,
    initial_velocity,
    romberg_levels
)

stopping_time = time_romberg_table[-1, -1]
braking_distance = distance_romberg_table[-1, -1]

print("Romberg Tabelle fur t_E:")
print(time_romberg_table)
print()

print("Romberg Tabelle  x_E:")
print(distance_romberg_table)
print()

print(f"Bremszeit t_E = {stopping_time:.6f} s")
print(f"Bremsweg x_E = {braking_distance:.6f} m")