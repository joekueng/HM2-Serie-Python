import math


def solve_romberg_table(function_to_integrate, interval_start, interval_end, max_level):
    romberg_table = [
        [0.0 for column_index in range(max_level + 1)]
        for row_index in range(max_level + 1)
    ]

    for row_index in range(max_level + 1):
        number_of_subintervals = 2 ** row_index
        step_size = (interval_end - interval_start) / number_of_subintervals

        trapezoidal_sum = 0.5 * (
            function_to_integrate(interval_start) + function_to_integrate(interval_end)
        )

        for interior_point_index in range(1, number_of_subintervals):
            current_x_value = interval_start + interior_point_index * step_size
            trapezoidal_sum += function_to_integrate(current_x_value)

        romberg_table[row_index][0] = step_size * trapezoidal_sum

        for column_index in range(1, row_index + 1):
            extrapolation_factor = 4 ** column_index
            romberg_table[row_index][column_index] = (
                extrapolation_factor * romberg_table[row_index][column_index - 1]
                - romberg_table[row_index - 1][column_index - 1]
            ) / (extrapolation_factor - 1)

    return romberg_table


def Kuengjoe_S9_Aufg3(function_to_integrate, interval_start, interval_end, max_level):
    romberg_table = solve_romberg_table(
        function_to_integrate,
        interval_start,
        interval_end,
        max_level
    )
    return romberg_table[max_level][max_level]


def function_for_aufgabe_2(x_value):
    return math.cos(x_value * x_value)


romberg_table = solve_romberg_table(function_for_aufgabe_2, 0.0, math.pi, 4)

print("Romberg-Tabelle:")
for row_index in range(len(romberg_table)):
    for column_index in range(row_index + 1):
        print(f"T{row_index}{column_index} = {romberg_table[row_index][column_index]:.10f}")
    print()

final_value = Kuengjoe_S9_Aufg3(function_for_aufgabe_2, 0.0, math.pi, 4)
print(f"Letzter Wert T = {final_value:.10f}")