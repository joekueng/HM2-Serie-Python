import numpy as np
import matplotlib.pyplot as plt


def Kuengjoe_S11_Aufg1(function_right_hand_side, xmin, xmax, ymin, ymax, hx, hy):
    x_values = np.arange(xmin, xmax + hx / 2, hx)
    y_values = np.arange(ymin, ymax + hy / 2, hy)

    x_grid, y_grid = np.meshgrid(x_values, y_values)

    y_direction_components = function_right_hand_side(x_grid, y_grid)
    x_direction_components = np.ones_like(y_direction_components)

    plt.figure(figsize=(8, 6))
    plt.quiver(
        x_grid,
        y_grid,
        x_direction_components,
        y_direction_components,
        angles="xy"
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Richtungsfeld")
    plt.grid(True)
    plt.show()

def example_function(x, y):
    return x - y

Kuengjoe_S11_Aufg1(
    example_function,
    xmin=-2,
    xmax=2,
    ymin=-2,
    ymax=2,
    hx=0.25,
    hy=0.25
)