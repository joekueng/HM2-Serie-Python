import math


def KuengJoe_S8_Aufg3a(x, y):
    total = 0.0
    for i in range(len(x) - 1):
        total += ((y[i] + y[i + 1]) / 2.0) * (x[i + 1] - x[i])
    return total


r_km = [0, 800, 1200, 1400, 2000, 3000, 3400, 3600, 4000, 5000, 5500, 6370]
rho = [13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300]

r_m = [value * 1000.0 for value in r_km]
y = [rho[i] * 4.0 * math.pi * r_m[i] ** 2 for i in range(len(r_m))]

earth_mass = KuengJoe_S8_Aufg3a(r_m, y)

reference_mass = 5.972e24
absolute_error = abs(earth_mass - reference_mass)
relative_error = absolute_error / reference_mass

print("Earth mass:", earth_mass)
print("Reference mass:", reference_mass)
print("Absolute error:", absolute_error)
print("Relative error:", relative_error)