
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


#a): Die Reichweite W erreicht ihr Maximum bei einem Winkel alpha = 45 Grad.

g = 9.81

v0_values = np.linspace(0, 100)
alpha_deg_values = np.linspace(0, 90)

[v0_grid, alpha_deg_grid] = np.meshgrid(v0_values, alpha_deg_values)
alpha_rad_grid = np.deg2rad(alpha_deg_grid)

W = (v0_grid**2) * np.sin(2 * alpha_rad_grid) / g


fig = plt.figure(0)
cont = plt.contour(v0_grid, alpha_deg_grid, W, cmap=cm.coolwarm)
fig.colorbar(cont, shrink=0.5, aspect=5)
plt.title('Wurfweite W(v0, α) – Höhenlinien')
plt.xlabel('v0 [m/s]')
plt.ylabel('α [deg]')
plt.show()


fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(v0_grid, alpha_deg_grid, W, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('Wurfweite W(v0, α) – Oberfläche')
ax.set_xlabel('v0 [m/s]')
ax.set_ylabel('α [deg]')
ax.set_zlabel('W [m]')
plt.show()


fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(v0_grid, alpha_deg_grid, W, rstride=5, cstride=5)
plt.title('Wurfweite W(v0, α) – Gitter')
ax.set_xlabel('v0 [m/s]')
ax.set_ylabel('α [deg]')
ax.set_zlabel('W [m]')
plt.show()



R = 8.31


V_values = np.linspace(1e-6, 0.2)
T_values = np.linspace(0, 1e4)

[V_grid, T_grid] = np.meshgrid(V_values, T_values)
p = R * T_grid / V_grid

fig = plt.figure(3)
cont = plt.contour(V_grid, T_grid, p, cmap=cm.coolwarm)
fig.colorbar(cont, shrink=0.5, aspect=5)
plt.title('p(V, T) = R T / V – Höhenlinien')
plt.xlabel('V [m^3]')
plt.ylabel('T [K]')
plt.show()


fig = plt.figure(4)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(V_grid, T_grid, p, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('p(V, T) = R T / V – Oberfläche')
ax.set_xlabel('V [m^3]')
ax.set_ylabel('T [K]')
ax.set_zlabel('p [N/m^2]')
plt.show()

fig = plt.figure(5)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(V_grid, T_grid, p, rstride=5, cstride=5)
plt.title('p(V, T) = R T / V – Gitter')
ax.set_xlabel('V [m^3]')
ax.set_ylabel('T [K]')
ax.set_zlabel('p [N/m^2]')
plt.show()


# 2)
p_values = np.linspace(1e4, 1e5)
T_values = np.linspace(0, 1e4)

[p_grid, T_grid] = np.meshgrid(p_values, T_values)
V = R * T_grid / p_grid


fig = plt.figure(6)
cont = plt.contour(p_grid, T_grid, V, cmap=cm.coolwarm)
fig.colorbar(cont, shrink=0.5, aspect=5)
plt.title('V(p, T) = R T / p – Höhenlinien')
plt.xlabel('p [N/m^2]')
plt.ylabel('T [K]')
plt.show()


fig = plt.figure(7)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(p_grid, T_grid, V, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('V(p, T) = R T / p – Oberfläche')
ax.set_xlabel('p [N/m^2]')
ax.set_ylabel('T [K]')
ax.set_zlabel('V [m^3]')
plt.show()


fig = plt.figure(8)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(p_grid, T_grid, V, rstride=5, cstride=5)
plt.title('V(p, T) = R T / p – Gitter')
ax.set_xlabel('p [N/m^2]')
ax.set_ylabel('T [K]')
ax.set_zlabel('V [m^3]')
plt.show()


# 3)
p_values = np.linspace(1e4, 1e6)
V_values = np.linspace(0, 10)

[p_grid, V_grid] = np.meshgrid(p_values, V_values)
T = (p_grid * V_grid) / R


fig = plt.figure(9)
cont = plt.contour(p_grid, V_grid, T, cmap=cm.coolwarm)
fig.colorbar(cont, shrink=0.5, aspect=5)
plt.title('T(p, V) = p V / R – Höhenlinien')
plt.xlabel('p [N/m^2]')
plt.ylabel('V [m^3]')
plt.show()

fig = plt.figure(10)
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(p_grid, V_grid, T, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.title('T(p, V) = p V / R – Oberfläche')
ax.set_xlabel('p [N/m^2]')
ax.set_ylabel('V [m^3]')
ax.set_zlabel('T [K]')
plt.show()


fig = plt.figure(11)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(p_grid, V_grid, T, rstride=5, cstride=5)
plt.title('T(p, V) = p V / R – Gitter')
ax.set_xlabel('p [N/m^2]')
ax.set_ylabel('V [m^3]')
ax.set_zlabel('T [K]')
plt.show()