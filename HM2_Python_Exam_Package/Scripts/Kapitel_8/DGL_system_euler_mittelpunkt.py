import numpy as np
import matplotlib.pyplot as plt


def right_hand_side(t, z):
    # Example from FS25 Teil 1:
    # 0.1 I''' + 2 I'' + I' + 10 I = 0
    # z[0] = I, z[1] = I', z[2] = I''
    return np.array([
        z[1],
        z[2],
        -100 * z[0] - 10 * z[1] - 20 * z[2],
    ], dtype=float)


def euler(f, t_start, t_end, step_size, z_start):
    t_values = np.arange(t_start, t_end + step_size / 2, step_size)
    z_values = np.zeros((len(t_values), len(z_start)), dtype=float)
    z_values[0] = z_start

    for i in range(len(t_values) - 1):
        z_values[i + 1] = z_values[i] + step_size * f(t_values[i], z_values[i])

    return t_values, z_values


def midpoint(f, t_start, t_end, step_size, z_start):
    t_values = np.arange(t_start, t_end + step_size / 2, step_size)
    z_values = np.zeros((len(t_values), len(z_start)), dtype=float)
    z_values[0] = z_start

    for i in range(len(t_values) - 1):
        k1 = f(t_values[i], z_values[i])
        midpoint_state = z_values[i] + step_size / 2 * k1
        k_mid = f(t_values[i] + step_size / 2, midpoint_state)
        z_values[i + 1] = z_values[i] + step_size * k_mid

    return t_values, z_values


if __name__ == "__main__":
    t_start = 0.0
    t_end = 0.1
    step_size = 0.02
    z_start = np.array([1.0, 0.0, 0.0])

    t_euler, z_euler = euler(right_hand_side, t_start, t_end, step_size, z_start)
    t_midpoint, z_midpoint = midpoint(right_hand_side, t_start, t_end, step_size, z_start)

    print("Euler values:")
    for t_value, z_value in zip(t_euler, z_euler):
        print(f"t = {t_value:.4f}, z = {z_value}")

    print("\nMidpoint values:")
    for t_value, z_value in zip(t_midpoint, z_midpoint):
        print(f"t = {t_value:.4f}, z = {z_value}")

    plt.figure()
    plt.plot(t_euler, z_euler[:, 0], "o-", label="Euler z0")
    plt.plot(t_midpoint, z_midpoint[:, 0], "s-", label="Midpoint z0")
    plt.xlabel("t")
    plt.ylabel("z[0]")
    plt.grid(True)
    plt.legend()
    plt.show()
