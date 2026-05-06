import numpy as np
import matplotlib.pyplot as plt


def summed_trapezoidal_cumulative(function_values, time_values):

    integral_values = np.zeros_like(time_values)

    for index in range(1, len(time_values)):
        step_width = time_values[index] - time_values[index - 1]
        integral_values[index] = integral_values[index - 1] + (
            step_width * 0.5 * (function_values[index - 1] + function_values[index])
        )

    return integral_values



relative_exhaust_velocity = 2600.0
initial_mass = 300000.0
final_mass = 80000.0
burn_time = 190.0
gravitational_acceleration = 9.81


mass_flow = (initial_mass - final_mass) / burn_time


number_of_steps = 10000
time_values = np.linspace(0.0, burn_time, number_of_steps + 1)


def acceleration(time):
    return (
        relative_exhaust_velocity
        * mass_flow
        / (initial_mass - mass_flow * time)
        - gravitational_acceleration
    )



acceleration_values = acceleration(time_values)

velocity_numerical = summed_trapezoidal_cumulative(
    acceleration_values,
    time_values
)

height_numerical = summed_trapezoidal_cumulative(
    velocity_numerical,
    time_values
)


velocity_analytical = (
    relative_exhaust_velocity
    * np.log(initial_mass / (initial_mass - mass_flow * time_values))
    - gravitational_acceleration * time_values
)

height_analytical = (
    -relative_exhaust_velocity
    * (initial_mass - mass_flow * time_values)
    / mass_flow
    * np.log(initial_mass / (initial_mass - mass_flow * time_values))
    + relative_exhaust_velocity * time_values
    - 0.5 * gravitational_acceleration * time_values ** 2
)


final_acceleration = acceleration_values[-1]
final_velocity_numerical = velocity_numerical[-1]
final_height_numerical = height_numerical[-1]
final_velocity_analytical = velocity_analytical[-1]
final_height_analytical = height_analytical[-1]
final_acceleration_in_g = final_acceleration / gravitational_acceleration

print(f"Massenstrom mu = {mass_flow:.6f} kg/s")
print()
print("Numerische Lösung mit summierter Trapez-Regel:")
print(f"v(t_E) = {final_velocity_numerical:.6f} m/s")
print(f"h(t_E) = {final_height_numerical:.6f} m")
print()
print("Analytische Lösung:")
print(f"v(t_E) = {final_velocity_analytical:.6f} m/s")
print(f"h(t_E) = {final_height_analytical:.6f} m")
print()
print("Beschleunigung Brennphase:")
print(f"a(t_E) = {final_acceleration:.6f} m/s^2")
print(f"a(t_E) / g = {final_acceleration_in_g:.6f}")

# Plot a(t)
plt.figure()
plt.plot(time_values, acceleration_values)
plt.xlabel("t [s]")
plt.ylabel("a(t) [m/s^2]")
plt.title("Beschleunigung a(t)")
plt.grid(True)
plt.savefig("Kuengioe_S10_Aufg2_Beschleunigung.png", dpi=300, bbox_inches="tight")

plt.figure()
plt.plot(time_values, velocity_numerical, label="numerisch")
plt.plot(time_values, velocity_analytical, "--", label="analytisch")
plt.xlabel("t [s]")
plt.ylabel("v(t) [m/s]")
plt.title("Geschwindigkeit v(t)")
plt.legend()
plt.grid(True)
plt.savefig("Kuengioe_S10_Aufg2_Geschwindigkeit.png", dpi=300, bbox_inches="tight")

plt.figure()
plt.plot(time_values, height_numerical, label="numerisch")
plt.plot(time_values, height_analytical, "--", label="analytisch")
plt.xlabel("t [s]")
plt.ylabel("h(t) [m]")
plt.title("Höhe h(t)")
plt.legend()
plt.grid(True)
plt.savefig("Kuengioe_S10_Aufg2_Höhe.png", dpi=300, bbox_inches="tight")

plt.show()
