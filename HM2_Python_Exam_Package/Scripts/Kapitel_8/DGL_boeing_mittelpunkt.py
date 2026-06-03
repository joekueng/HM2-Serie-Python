import numpy as np
import matplotlib.pyplot as plt


def calculate_right_hand_side(time_value, state_vector):
    position = state_vector[0]
    velocity = state_vector[1]

    position_derivative = velocity
    velocity_derivative = (-5 * velocity**2 - 0.1 * position - 570000) / 97000

    return np.array([position_derivative, velocity_derivative])


def solve_with_midpoint_method(right_hand_side_function, start_time, end_time, step_size, initial_state):
    time_values = np.arange(start_time, end_time + step_size, step_size)

    state_values = np.zeros((len(time_values), len(initial_state)))
    state_values[0] = initial_state

    for time_index in range(len(time_values) - 1):
        current_time = time_values[time_index]
        current_state = state_values[time_index]

        first_slope = right_hand_side_function(current_time, current_state)

        midpoint_time = current_time + step_size / 2
        midpoint_state = current_state + step_size / 2 * first_slope

        midpoint_slope = right_hand_side_function(midpoint_time, midpoint_state)

        state_values[time_index + 1] = current_state + step_size * midpoint_slope

    return time_values, state_values


def calculate_zero_crossing(time_values, position_values, velocity_values):
    for time_index in range(len(velocity_values) - 1):
        current_velocity = velocity_values[time_index]
        next_velocity = velocity_values[time_index + 1]

        if current_velocity >= 0 and next_velocity <= 0:
            current_time = time_values[time_index]
            next_time = time_values[time_index + 1]

            current_position = position_values[time_index]
            next_position = position_values[time_index + 1]

            interpolation_factor = current_velocity / (current_velocity - next_velocity)

            stopping_time = current_time + interpolation_factor * (next_time - current_time)
            stopping_position = current_position + interpolation_factor * (next_position - current_position)

            return stopping_time, stopping_position

    return None, None





airplane_mass = 97000
start_time = 0
end_time = 20
step_size = 0.1

initial_position = 0
initial_velocity = 100
initial_state = np.array([initial_position, initial_velocity])

time_values, state_values = solve_with_midpoint_method(
    calculate_right_hand_side,
    start_time,
    end_time,
    step_size,
    initial_state
)

position_values = state_values[:, 0]
velocity_values = state_values[:, 1]

stopping_time, stopping_position = calculate_zero_crossing(
    time_values,
    position_values,
    velocity_values
)

plt.figure(figsize=(10, 5))
plt.plot(time_values, position_values, label="x(t) Position [m]")
plt.plot(time_values, velocity_values, label="v(t) Geschwindigkeit [m/s]")
plt.axhline(0, linestyle="--")
plt.xlabel("Zeit t [s]")
plt.ylabel("x(t) und v(t)")
plt.title("Landende Boeing 737-200: Mittelpunktverfahren")
plt.legend()
plt.grid(True)
plt.show()

print(f"Stillstand nach ca. {stopping_time:.1f} s")
print(f"Bremsweg ca. {stopping_position:.1f} m")

