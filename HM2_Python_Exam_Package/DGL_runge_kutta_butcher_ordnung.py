import numpy as np
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Parametri del tempo
x_start = 0.0
x_end = 3.0
y_start = 1.0  # (O array se è un sistema)

# Tableau di Butcher
c = np.array([0.0, 1 / 3, 1 / 3, 2 / 3])
a = np.array([
    [0.0, 0.0, 0.0, 0.0],
    [1 / 3, 0.0, 0.0, 0.0],
    [0.0, 1 / 3, 0.0, 0.0],
    [0.0, 1 / 3, 1 / 3, 0.0],
])
b = np.array([1 / 4, 0.0, 0.0, 3 / 4])

# Definisci l'equazione differenziale y' = f(x, y)
def differential_equation(x, y):
    return 2 * (1 - x) * y

# Definisci la soluzione esatta se vuoi confrontarla e calcolare l'errore
def exact_solution(x):
    return np.exp(2 * x - x**2)

# Step size per la stima dell'ordine
step_sizes_for_order = np.array([0.1, 0.01, 0.001])
# Step size per il plot
plot_step_size = 0.1


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

def runge_kutta_butcher(f, x_start, y_start, x_end, step_size, c, a, b):
    x_values = np.arange(x_start, x_end + step_size / 2, step_size)
    y_values = np.zeros(len(x_values), dtype=float)
    y_values[0] = y_start
    stages = len(b)

    for i in range(len(x_values) - 1):
        k = np.zeros(stages, dtype=float)

        for stage in range(stages):
            y_stage = y_values[i]
            for j in range(stage):
                y_stage += step_size * a[stage, j] * k[j]
            k[stage] = f(x_values[i] + c[stage] * step_size, y_stage)

        y_values[i + 1] = y_values[i] + step_size * np.dot(b, k)

    return x_values, y_values


def estimate_order(step_sizes, errors):
    coefficients = np.polyfit(np.log(step_sizes), np.log(errors), 1)
    return coefficients[0]


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    
    # Esecuzione per il plot
    x_values, y_values = runge_kutta_butcher(
        differential_equation, x_start, y_start, x_end, plot_step_size, c, a, b
    )

    errors = np.zeros_like(step_sizes_for_order)

    for index, step_size in enumerate(step_sizes_for_order):
        _, y_numerical = runge_kutta_butcher(
            differential_equation, x_start, y_start, x_end, step_size, c, a, b
        )
        errors[index] = abs(y_numerical[-1] - exact_solution(x_end))

    order = estimate_order(step_sizes_for_order, errors)

    print("="*40)
    print("RISULTATI RUNGE-KUTTA DA BUTCHER TABLEAU")
    print("="*40)
    print("Valore finale (step size per plot):", y_values[-1])
    print("Step sizes usati per stimare ordine:", step_sizes_for_order)
    print("Errori globali:", errors)
    print("Ordine stimato:", order)
    print("Ordine arrotondato all'intero più vicino:", round(order))

    # Plot Soluzione
    x_plot = np.linspace(x_start, x_end, 500)
    plt.figure()
    plt.plot(x_values, y_values, "o", label=f"Numerica (h={plot_step_size})")
    plt.plot(x_plot, exact_solution(x_plot), label="Esatta")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.title("Confronto Soluzione Numerica vs Esatta")

    # Plot Errore
    plt.figure()
    plt.loglog(step_sizes_for_order, errors, "o-")
    plt.xlabel("h (step size)")
    plt.ylabel("Errore globale")
    plt.title(f"Stima dell'ordine (p ≈ {order:.2f})")
    plt.grid(True, which="both")
    
    plt.show()
