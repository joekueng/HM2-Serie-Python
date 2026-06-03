import numpy as np
import matplotlib.pyplot as plt


def _compute_natural_cubic_spline_coefficients(interpolation_nodes_x, interpolation_values_y):
    interpolation_nodes_x = np.asarray(interpolation_nodes_x, dtype=float).reshape(-1)
    interpolation_values_y = np.asarray(interpolation_values_y, dtype=float).reshape(-1)

    if interpolation_nodes_x.size != interpolation_values_y.size:
        raise ValueError("x e y must be same length.")

    if interpolation_nodes_x.size < 2:
        raise ValueError("at least 2 nodes are required.")

    if np.any(np.diff(interpolation_nodes_x) <= 0):
        raise ValueError("x values must be strictly increasing.")

    interval_widths = np.diff(interpolation_nodes_x)
    number_of_intervals = interpolation_nodes_x.size - 1

    system_matrix = np.zeros((number_of_intervals + 1, number_of_intervals + 1), dtype=float)
    right_hand_side = np.zeros(number_of_intervals + 1, dtype=float)

    system_matrix[0, 0] = 1.0
    system_matrix[-1, -1] = 1.0

    for internal_node_index in range(1, number_of_intervals):
        left_interval_width = interval_widths[internal_node_index - 1]
        right_interval_width = interval_widths[internal_node_index]

        system_matrix[internal_node_index, internal_node_index - 1] = left_interval_width
        system_matrix[internal_node_index, internal_node_index] = 2.0 * (left_interval_width + right_interval_width)
        system_matrix[internal_node_index, internal_node_index + 1] = right_interval_width

        right_hand_side[internal_node_index] = 6.0 * (
            (interpolation_values_y[internal_node_index + 1] - interpolation_values_y[internal_node_index]) / right_interval_width
            - (interpolation_values_y[internal_node_index] - interpolation_values_y[internal_node_index - 1]) / left_interval_width
        )

    second_derivative_values = np.linalg.solve(system_matrix, right_hand_side)

    coefficient_a_values = interpolation_values_y[:-1].copy()
    coefficient_b_values = np.zeros(number_of_intervals, dtype=float)
    coefficient_c_values = second_derivative_values[:-1] / 2.0
    coefficient_d_values = np.zeros(number_of_intervals, dtype=float)

    for interval_index in range(number_of_intervals):
        current_interval_width = interval_widths[interval_index]

        coefficient_b_values[interval_index] = (
            (interpolation_values_y[interval_index + 1] - interpolation_values_y[interval_index]) / current_interval_width
            - (current_interval_width / 6.0) * (
                2.0 * second_derivative_values[interval_index] + second_derivative_values[interval_index + 1]
            )
        )

        coefficient_d_values[interval_index] = (
            (second_derivative_values[interval_index + 1] - second_derivative_values[interval_index])
            / (6.0 * current_interval_width)
        )

    return coefficient_a_values, coefficient_b_values, coefficient_c_values, coefficient_d_values


def Kuengjoe_S05_Aufg2(x, y, xx, plot_result=True):
    interpolation_nodes_x = np.asarray(x, dtype=float).reshape(-1)
    interpolation_values_y = np.asarray(y, dtype=float).reshape(-1)
    evaluation_points_xx = np.asarray(xx, dtype=float).reshape(-1)

    if np.any(evaluation_points_xx < interpolation_nodes_x[0]) or np.any(evaluation_points_xx > interpolation_nodes_x[-1]):
        raise ValueError("Tutti i valori di xx devono stare nell'intervallo [x0, xn].")

    (
        coefficient_a_values,
        coefficient_b_values,
        coefficient_c_values,
        coefficient_d_values,
    ) = _compute_natural_cubic_spline_coefficients(interpolation_nodes_x, interpolation_values_y)

    number_of_intervals = interpolation_nodes_x.size - 1

    interval_indices_for_evaluation = np.searchsorted(interpolation_nodes_x, evaluation_points_xx, side="right") - 1
    interval_indices_for_evaluation = np.clip(interval_indices_for_evaluation, 0, number_of_intervals - 1)

    yy = np.zeros_like(evaluation_points_xx, dtype=float)

    for evaluation_point_index, interval_index in enumerate(interval_indices_for_evaluation):
        local_x_distance = evaluation_points_xx[evaluation_point_index] - interpolation_nodes_x[interval_index]

        yy[evaluation_point_index] = (
            coefficient_a_values[interval_index]
            + coefficient_b_values[interval_index] * local_x_distance
            + coefficient_c_values[interval_index] * local_x_distance ** 2
            + coefficient_d_values[interval_index] * local_x_distance ** 3
        )

    if plot_result:
        plt.figure(figsize=(8, 5))
        plt.plot(evaluation_points_xx, yy, label="Natürliche kubische Spline")
        plt.plot(interpolation_nodes_x, interpolation_values_y, "o", label="Stützpunkte")
        plt.xlabel("x")
        plt.ylabel("S(x)")
        plt.title("Natürliche kubische Spline")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    return yy


if __name__ == "__main__":
    x_test_values = np.array([4, 6, 8, 10], dtype=float)
    y_test_values = np.array([6, 3, 9, 0], dtype=float)
    xx_test_values = np.linspace(4, 10, 400)

    yy_test_values = Kuengjoe_S05_Aufg2(x_test_values, y_test_values, xx_test_values, plot_result=True)

    print("value of yy_test_values:")
    print(Kuengjoe_S05_Aufg2(x_test_values, y_test_values, x_test_values, plot_result=False))