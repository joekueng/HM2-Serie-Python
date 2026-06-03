import numpy as np
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Parametri del tempo
t_start = 0.0
t_end = 0.1
step_size = 0.02

# Condizioni iniziali (array numpy). 
# Esempio FS25: z = [I, I', I''] => [1.0, 0.0, 0.0]
z_start = np.array([1.0, 0.0, 0.0], dtype=float)

# Definisci qui la tua equazione differenziale vettoriale z' = f(t, z)
def right_hand_side(t, z):
    # Esempio: 0.1 I''' + 2 I'' + I' + 10 I = 0
    # Dove z[0] = I, z[1] = I', z[2] = I''
    # Quindi I''' = -100 I - 10 I' - 20 I''
    
    # z[0]' = z[1]
    # z[1]' = z[2]
    # z[2]' = -100*z[0] - 10*z[1] - 20*z[2]
    return np.array([
        z[1],
        z[2],
        -100 * z[0] - 10 * z[1] - 20 * z[2],
    ], dtype=float)

# Indice della variabile che vuoi plottare (es. 0 per z[0])
plot_index = 0
plot_name = "z[0]"


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

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


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    t_euler, z_euler = euler(right_hand_side, t_start, t_end, step_size, z_start)
    t_midpoint, z_midpoint = midpoint(right_hand_side, t_start, t_end, step_size, z_start)

    print("="*40)
    print("RISULTATI EULERO E PUNTO MEDIO (SISTEMI)")
    print("="*40)

    print("\\nValori Eulero:")
    for t_value, z_value in zip(t_euler, z_euler):
        print(f"t = {t_value:.4f}, z = {z_value}")

    print("\\nValori Punto Medio (Midpoint):")
    for t_value, z_value in zip(t_midpoint, z_midpoint):
        print(f"t = {t_value:.4f}, z = {z_value}")

    plt.figure()
    plt.plot(t_euler, z_euler[:, plot_index], "o-", label=f"Eulero {plot_name}")
    plt.plot(t_midpoint, z_midpoint[:, plot_index], "s-", label=f"Midpoint {plot_name}")
    plt.xlabel("t")
    plt.ylabel(plot_name)
    plt.grid(True)
    plt.title(f"Confronto per la variabile {plot_name}")
    plt.legend()
    plt.show()
