import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# Serie 1, Aufgabe 1:
# Compact top-level script for contour, plot_surface and plot_wireframe.


def plot_all(x_grid, y_grid, z_grid, title, x_label, y_label, z_label):
    fig = plt.figure()
    contour = plt.contour(x_grid, y_grid, z_grid, cmap=cm.coolwarm)
    fig.colorbar(contour, shrink=0.5, aspect=5)
    plt.title(title + " - contour")
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    surface = ax.plot_surface(
        x_grid,
        y_grid,
        z_grid,
        cmap=cm.coolwarm,
        linewidth=0,
        antialiased=False,
    )
    fig.colorbar(surface, shrink=0.5, aspect=5)
    ax.set_title(title + " - surface")
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_wireframe(x_grid, y_grid, z_grid, rstride=5, cstride=5)
    ax.set_title(title + " - wireframe")
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)


if __name__ == "__main__":
    g = 9.81
    v0_values = np.linspace(0, 100, 80)
    alpha_deg_values = np.linspace(0, 90, 80)
    v0_grid, alpha_deg_grid = np.meshgrid(v0_values, alpha_deg_values)
    alpha_rad_grid = np.deg2rad(alpha_deg_grid)
    throw_range = v0_grid**2 * np.sin(2 * alpha_rad_grid) / g

    plot_all(
        v0_grid,
        alpha_deg_grid,
        throw_range,
        "Wurfweite W(v0, alpha)",
        "v0 [m/s]",
        "alpha [deg]",
        "W [m]",
    )

    gas_constant = 8.31
    volume_values = np.linspace(1e-6, 0.2, 80)
    temperature_values = np.linspace(0, 1e4, 80)
    volume_grid, temperature_grid = np.meshgrid(volume_values, temperature_values)
    pressure = gas_constant * temperature_grid / volume_grid

    plot_all(
        volume_grid,
        temperature_grid,
        pressure,
        "p(V,T) = R*T/V",
        "V [m^3]",
        "T [K]",
        "p [N/m^2]",
    )

    plt.show()
