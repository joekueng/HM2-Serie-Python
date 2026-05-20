import numpy as np
import matplotlib.pyplot as plt


def Kuengjoe_S11_Aufg1(function_right_hand_side, xmin, xmax, ymin, ymax, hx, hy, show_plot=True):
    x_values = np.arange(xmin, xmax + hx / 2, hx)
    y_values = np.arange(ymin, ymax + hy / 2, hy)

    x_grid, y_grid = np.meshgrid(x_values, y_values)

    y_direction_components = function_right_hand_side(x_grid, y_grid)
    x_direction_components = np.ones_like(y_direction_components)

    plt.quiver(
        x_grid,
        y_grid,
        x_direction_components,
        y_direction_components,
        angles="xy"
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Richtungsfeld mit numerischen Lösungen")
    plt.grid(True)

    if show_plot:
        plt.show()


def Kuengjoe_S11_Aufg3(function_right_hand_side, a, b, n, y0):
    x_values = np.linspace(a, b, n + 1)
    step_size = (b - a) / n

    y_euler = np.zeros(n + 1)
    y_mittelpunkt = np.zeros(n + 1)
    y_modeuler = np.zeros(n + 1)

    y_euler[0] = y0
    y_mittelpunkt[0] = y0
    y_modeuler[0] = y0

    for step_index in range(n):
        current_x_value = x_values[step_index]
        next_x_value = x_values[step_index + 1]

        # Euler-Verfahren
        current_euler_y_value = y_euler[step_index]
        euler_slope = function_right_hand_side(current_x_value, current_euler_y_value)
        y_euler[step_index + 1] = current_euler_y_value + step_size * euler_slope

        # Mittelpunkt-Verfahren
        current_mittelpunkt_y_value = y_mittelpunkt[step_index]
        first_mittelpunkt_slope = function_right_hand_side(
            current_x_value,
            current_mittelpunkt_y_value
        )

        midpoint_x_value = current_x_value + step_size / 2
        midpoint_y_value = current_mittelpunkt_y_value + step_size / 2 * first_mittelpunkt_slope

        midpoint_slope = function_right_hand_side(
            midpoint_x_value,
            midpoint_y_value
        )

        y_mittelpunkt[step_index + 1] = current_mittelpunkt_y_value + step_size * midpoint_slope

        # Modifiziertes Euler-Verfahren / Heun-Verfahren
        current_modeuler_y_value = y_modeuler[step_index]
        first_modeuler_slope = function_right_hand_side(
            current_x_value,
            current_modeuler_y_value
        )

        predicted_modeuler_y_value = current_modeuler_y_value + step_size * first_modeuler_slope

        second_modeuler_slope = function_right_hand_side(
            next_x_value,
            predicted_modeuler_y_value
        )

        y_modeuler[step_index + 1] = current_modeuler_y_value + step_size / 2 * (
            first_modeuler_slope + second_modeuler_slope
        )

    # Richtungsfeld und Lösungen zeichnen
    minimum_y_value = min(
        np.min(y_euler),
        np.min(y_mittelpunkt),
        np.min(y_modeuler)
    ) - 0.5

    maximum_y_value = max(
        np.max(y_euler),
        np.max(y_mittelpunkt),
        np.max(y_modeuler)
    ) + 0.5

    plt.figure(figsize=(8, 6))

    Kuengjoe_S11_Aufg1(
        function_right_hand_side,
        xmin=a,
        xmax=b,
        ymin=minimum_y_value,
        ymax=maximum_y_value,
        hx=(b - a) / 20,
        hy=(maximum_y_value - minimum_y_value) / 20,
        show_plot=False
    )

    plt.plot(x_values, y_euler, marker="o", label="Euler")
    plt.plot(x_values, y_mittelpunkt, marker="o", label="Mittelpunkt")
    plt.plot(x_values, y_modeuler, marker="o", label="Modifizierter Euler")

    plt.legend()
    plt.show()

    return x_values, y_euler, y_mittelpunkt, y_modeuler


def differential_equation_from_aufgabe2(x, y):
    return x**2 / y


x_values, y_euler, y_mittelpunkt, y_modeuler = Kuengjoe_S11_Aufg3(
    differential_equation_from_aufgabe2,
    a=0,
    b=1.4,
    n=2,
    y0=2
)

print("x =", x_values)
print("Euler =", y_euler)
print("Mittelpunkt =", y_mittelpunkt)
print("Modifizierter Euler =", y_modeuler)