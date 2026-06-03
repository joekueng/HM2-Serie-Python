import numpy as np
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Parametri del tempo e step
t_start = 0.0
t_end = 190.0
step_size = 1.0

# Condizioni iniziali (array numpy). 
# Se è un'equazione singola, metti un array di 1 elemento, es: np.array([0.0])
# Se è un sistema, metti tutti i valori iniziali, es: np.array([0.0, 0.0])
state_start = np.array([0.0, 0.0], dtype=float)

# Definisci qui la tua equazione differenziale y' = f(t, y)
# Nota: state è un array numpy contenente [y1, y2, ...]
def rhs_function(time, state):
    # Esempio: Oscillatore armonico o altro
    # height, velocity = state
    # return np.array([velocity, -9.81])
    
    # Esempio originale (Razzo):
    y1, y2 = state # y1 = h, y2 = v
    relative_exhaust_velocity = 2600.0
    initial_mass = 300000.0
    final_mass = 80000.0
    burn_time = 190.0
    mass_flow = (initial_mass - final_mass) / burn_time
    mass = initial_mass - mass_flow * time
    acceleration = relative_exhaust_velocity * mass_flow / mass - 9.81
    
    return np.array([y2, acceleration], dtype=float)

# Nomi delle variabili di stato per i plot
state_names = ["h (Altezza)", "v (Velocità)"]


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

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


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    
    # Esecuzione Eulero Modificato
    t_euler, state_euler = modified_euler(
        rhs_function, t_start, t_end, step_size, state_start
    )
    
    # Esecuzione Runge-Kutta 4
    t_rk4, state_rk4 = rk4(
        rhs_function, t_start, t_end, step_size, state_start
    )

    print("="*40)
    print("RISULTATI INTEGRAZIONE ODE")
    print("="*40)
    print(f"Valori finali a t = {t_rk4[-1]}:")
    
    for i in range(len(state_start)):
        print(f"\\n--- Variabile di stato {i}: {state_names[i] if i < len(state_names) else f'y{i}'} ---")
        print(f"Modified Euler : {state_euler[-1, i]}")
        print(f"Runge-Kutta 4  : {state_rk4[-1, i]}")
        print(f"Differenza     : {abs(state_rk4[-1, i] - state_euler[-1, i])}")

    # Plotting
    for i in range(len(state_start)):
        plt.figure()
        plt.plot(t_euler, state_euler[:, i], "--", label=f"Modified Euler")
        plt.plot(t_rk4, state_rk4[:, i], ":", label=f"RK4")
        plt.xlabel("t")
        plt.ylabel(state_names[i] if i < len(state_names) else f"y_{i}")
        plt.title(f"Integrazione {state_names[i] if i < len(state_names) else f'y_{i}'}")
        plt.grid(True)
        plt.legend()
        
    plt.show()
