import numpy as np
import matplotlib.pyplot as plt


# Serie 1, Aufgabe 2b:
# w(x,t) = sin(x + c*t)
# v(x,t) = sin(x + c*t) + cos(2*x + 2*c*t)
# Plot both functions in 3D with plot_wireframe, for c = 1.


c = 1.0
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 80)
t_values = np.linspace(0, 4 * np.pi, 80)
x_grid, t_grid = np.meshgrid(x_values, t_values)


def w_function(x, t, c=1.0):
    return np.sin(x + c * t)


def v_function(x, t, c=1.0):
    return np.sin(x + c * t) + np.cos(2 * x + 2 * c * t)


def plot_wireframe(z_values, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_wireframe(x_grid, t_grid, z_values, rstride=4, cstride=4)
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("t")
    ax.set_zlabel("amplitude")


if __name__ == "__main__":
    w_values = w_function(x_grid, t_grid, c)
    v_values = v_function(x_grid, t_grid, c)

    plot_wireframe(w_values, "w(x,t) = sin(x + c*t), c=1")
    plot_wireframe(v_values, "v(x,t) = sin(x + c*t) + cos(2*x + 2*c*t), c=1")
    plt.show()
