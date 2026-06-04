import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


# Suchbegriffe:
# Spline Randbedingungen, kubische Spline, natural, natuerlich, natürlich,
# not-a-knot, clamped, periodic, periodisch, SciPy CubicSpline,
# s(t), s'(t), s''(t), Geschwindigkeit, Beschleunigung.


# INPUT: Knoten und Randbedingung anpassen.
t_nodes = np.array([0.0, 0.5, 2.0, 3.0], dtype=float)
y_nodes = np.array([1.0, 2.0, 2.5, 0.0], dtype=float)
query_points = np.array([1.0], dtype=float)

# Optionen:
# "natural"
# "not-a-knot"
# "periodic"  -> erster und letzter y-Wert muessen gleich sein
# ((1, left_slope), (1, right_slope)) fuer clamped slope conditions
boundary_condition = "not-a-knot"


def build_spline(t_nodes, y_nodes, boundary_condition):
    return CubicSpline(t_nodes, y_nodes, bc_type=boundary_condition)


def print_values(spline, points):
    points = np.atleast_1d(points)
    print("query points =", points)
    print("s(t)   =", spline(points, 0))
    print("s'(t)  =", spline(points, 1))
    print("s''(t) =", spline(points, 2))


if __name__ == "__main__":
    spline = build_spline(t_nodes, y_nodes, boundary_condition)

    print("CubicSpline boundary condition:", boundary_condition)
    print("coefficient matrix shape =", spline.c.shape)
    print("Intervals use scipy form:")
    print("s_i(t) = c[0,i]*(t-t_i)^3 + c[1,i]*(t-t_i)^2 + c[2,i]*(t-t_i) + c[3,i]")
    print("coefficients c =")
    print(spline.c)
    print()
    print_values(spline, query_points)

    t_plot = np.linspace(t_nodes[0], t_nodes[-1], 400)
    plt.figure()
    plt.plot(t_plot, spline(t_plot), label="s(t)")
    plt.plot(t_plot, spline(t_plot, 1), "--", label="s'(t)")
    plt.plot(t_nodes, y_nodes, "o", label="nodes")
    plt.grid(True)
    plt.legend()
    plt.title(f"CubicSpline bc_type={boundary_condition}")
    plt.show()
