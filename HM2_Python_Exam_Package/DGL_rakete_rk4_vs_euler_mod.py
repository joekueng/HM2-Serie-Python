import numpy as np
import matplotlib.pyplot as plt


relative_exhaust_velocity = 2600.0
initial_mass = 300000.0
final_mass = 80000.0
burn_time = 190.0
gravitational_acceleration = 9.81
mass_flow = (initial_mass - final_mass) / burn_time


def rocket_rhs(time, state):
    height, velocity = state
    mass = initial_mass - mass_flow * time
    acceleration = relative_exhaust_velocity * mass_flow / mass - gravitational_acceleration
    return np.array([velocity, acceleration], dtype=float)


def modified_euler(f, t_start, t_end, step_size, state_start):
    t_values = np.arange(t_start, t_end + step_size / 2, step_size)
    state_values = np.zeros((len(t_values), len(state_start)), dtype=float)
    state_values[0] = state_start

    for index in range(len(t_values) - 1):
        t = t_values[index]
        y = state_values[index]
        predictor = y + step_size * f(t, y)
        state_values[index + 1] = y + step_size / 2 * (
            f(t, y) + f(t + step_size, predictor)
        )

    return t_values, state_values


def rk4(f, t_start, t_end, step_size, state_start):
    t_values = np.arange(t_start, t_end + step_size / 2, step_size)
    state_values = np.zeros((len(t_values), len(state_start)), dtype=float)
    state_values[0] = state_start

    for index in range(len(t_values) - 1):
        t = t_values[index]
        y = state_values[index]
        k1 = f(t, y)
        k2 = f(t + step_size / 2, y + step_size * k1 / 2)
        k3 = f(t + step_size / 2, y + step_size * k2 / 2)
        k4 = f(t + step_size, y + step_size * k3)
        state_values[index + 1] = y + step_size / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return t_values, state_values


def exact_velocity(time):
    return (
        relative_exhaust_velocity
        * np.log(initial_mass / (initial_mass - mass_flow * time))
        - gravitational_acceleration * time
    )


def exact_height(time):
    mass = initial_mass - mass_flow * time
    return (
        relative_exhaust_velocity
        / mass_flow
        * (initial_mass - mass + mass * np.log(mass / initial_mass))
        - gravitational_acceleration * time**2 / 2
    )


if __name__ == "__main__":
    step_size = 1.0
    state_start = np.array([0.0, 0.0])

    t_euler, state_euler = modified_euler(
        rocket_rhs,
        0.0,
        burn_time,
        step_size,
        state_start,
    )
    t_rk4, state_rk4 = rk4(
        rocket_rhs,
        0.0,
        burn_time,
        step_size,
        state_start,
    )

    height_exact = exact_height(t_rk4)
    velocity_exact = exact_velocity(t_rk4)

    print("Modified Euler: h(t_E) =", state_euler[-1, 0], "v(t_E) =", state_euler[-1, 1])
    print("RK4:            h(t_E) =", state_rk4[-1, 0], "v(t_E) =", state_rk4[-1, 1])
    print("Exact:          h(t_E) =", height_exact[-1], "v(t_E) =", velocity_exact[-1])
    print("RK4 height error =", abs(state_rk4[-1, 0] - height_exact[-1]))
    print("RK4 velocity error =", abs(state_rk4[-1, 1] - velocity_exact[-1]))

    plt.figure()
    plt.plot(t_rk4, height_exact, label="h exact")
    plt.plot(t_euler, state_euler[:, 0], "--", label="h modified Euler")
    plt.plot(t_rk4, state_rk4[:, 0], ":", label="h RK4")
    plt.xlabel("t [s]")
    plt.ylabel("h [m]")
    plt.grid(True)
    plt.legend()

    plt.figure()
    plt.plot(t_rk4, velocity_exact, label="v exact")
    plt.plot(t_euler, state_euler[:, 1], "--", label="v modified Euler")
    plt.plot(t_rk4, state_rk4[:, 1], ":", label="v RK4")
    plt.xlabel("t [s]")
    plt.ylabel("v [m/s]")
    plt.grid(True)
    plt.legend()
    plt.show()
