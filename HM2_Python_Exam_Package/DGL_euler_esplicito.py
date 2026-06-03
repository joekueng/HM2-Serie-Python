import numpy as np
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Parametri del tempo e step
t_start = 0.0
t_end = 2.0
step_size = 0.1

# Condizioni iniziali (array numpy). 
# Es per sistema: np.array([1.0, 0.0])
# Es per eq singola: np.array([1.0])
state_start = np.array([1.0], dtype=float)

# Definisci qui la tua equazione differenziale y' = f(t, y)
def rhs_function(time, state):
    # state è un array. Esempio per eq singola:
    y = state[0]
    return np.array([time * y])

# Nomi delle variabili di stato per i plot
state_names = ["y"]

# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

def euler_explicit(f, t_start, t_end, step_size, state_start):
    t_values = np.arange(t_start, t_end + step_size / 2, step_size)
    state_values = np.zeros((len(t_values), len(state_start)), dtype=float)
    state_values[0] = state_start

    for index in range(len(t_values) - 1):
        t = t_values[index]
        y = state_values[index]
        state_values[index + 1] = y + step_size * f(t, y)

    return t_values, state_values


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    t_euler, state_euler = euler_explicit(
        rhs_function, t_start, t_end, step_size, state_start
    )

    print("="*40)
    print("RISULTATI EULERO ESPLICITO")
    print("="*40)
    print(f"Valore finale a t = {t_euler[-1]}:")
    for i in range(len(state_start)):
        print(f"  {state_names[i] if i < len(state_names) else f'y{i}'} = {state_euler[-1, i]}")

    for i in range(len(state_start)):
        plt.figure()
        plt.plot(t_euler, state_euler[:, i], "o-", label="Euler Explicit")
        plt.xlabel("t")
        plt.ylabel(state_names[i] if i < len(state_names) else f"y_{i}")
        plt.title(f"Integrazione {state_names[i] if i < len(state_names) else f'y_{i}'}")
        plt.grid(True)
        plt.legend()
        
    plt.show()
