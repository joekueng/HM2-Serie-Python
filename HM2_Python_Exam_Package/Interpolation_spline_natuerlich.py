import numpy as np
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Nodi (devono essere ordinati per t_nodes crescente)
t_nodes = np.array([0.0, 0.5, 2.0, 3.0], dtype=float)
x_nodes = np.array([1.0, 2.0, 2.5, 0.0], dtype=float)

# Punto/i in cui calcolare il valore (può essere un singolo numero o array)
query_time = np.array([1.0])


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

def natural_cubic_spline_coefficients(x_values, y_values):
    x_values = np.asarray(x_values, dtype=float)
    y_values = np.asarray(y_values, dtype=float)
    n = len(x_values) - 1
    h = np.diff(x_values)

    matrix = np.zeros((n + 1, n + 1), dtype=float)
    rhs = np.zeros(n + 1, dtype=float)
    
    # Spline naturale: derivata seconda ai bordi nulla
    matrix[0, 0] = 1.0
    matrix[n, n] = 1.0

    for i in range(1, n):
        matrix[i, i - 1] = h[i - 1]
        matrix[i, i] = 2 * (h[i - 1] + h[i])
        matrix[i, i + 1] = h[i]
        rhs[i] = 3 * (
            (y_values[i + 1] - y_values[i]) / h[i]
            - (y_values[i] - y_values[i - 1]) / h[i - 1]
        )

    c_full = np.linalg.solve(matrix, rhs)
    a = y_values[:-1]
    b = np.zeros(n, dtype=float)
    c = c_full[:-1]
    d = np.zeros(n, dtype=float)

    for i in range(n):
        b[i] = (y_values[i + 1] - y_values[i]) / h[i] - h[i] * (2 * c_full[i] + c_full[i + 1]) / 3
        d[i] = (c_full[i + 1] - c_full[i]) / (3 * h[i])

    return a, b, c, d

def evaluate_spline(x_nodes, coefficients, x_query, derivative=0):
    a, b, c, d = coefficients
    x_query = np.atleast_1d(np.asarray(x_query, dtype=float))
    result = np.zeros_like(x_query, dtype=float)

    for index, x_value in np.ndenumerate(x_query):
        # Trova l'intervallo a cui appartiene x_value
        interval = np.searchsorted(x_nodes, x_value, side="right") - 1
        interval = min(max(interval, 0), len(a) - 1)
        dx = x_value - x_nodes[interval]

        if derivative == 0: # Funzione
            result[index] = a[interval] + b[interval] * dx + c[interval] * dx**2 + d[interval] * dx**3
        elif derivative == 1: # Prima derivata (Velocità)
            result[index] = b[interval] + 2 * c[interval] * dx + 3 * d[interval] * dx**2
        elif derivative == 2: # Seconda derivata (Accelerazione)
            result[index] = 2 * c[interval] + 6 * d[interval] * dx
        else:
            raise ValueError("derivative must be 0, 1, or 2")

    if result.size == 1:
        return result[0]
    return result


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    coefficients = natural_cubic_spline_coefficients(t_nodes, x_nodes)
    
    print("="*40)
    print("RISULTATI SPLINE CUBICA NATURALE")
    print("="*40)
    
    labels = ["a", "b", "c", "d"]
    print("Coefficienti dei polinomi per ogni intervallo:")
    for label, values in zip(labels, coefficients):
        print(f"  {label} =", values)

    position = evaluate_spline(t_nodes, coefficients, query_time, derivative=0)
    velocity = evaluate_spline(t_nodes, coefficients, query_time, derivative=1)
    acceleration = evaluate_spline(t_nodes, coefficients, query_time, derivative=2)

    print("\\nValutazione nel punto t =", query_time)
    print(f"  s(t)   [Posizione]    =", position)
    print(f"  s'(t)  [Velocità]     =", velocity)
    print(f"  s''(t) [Accelerazione]=", acceleration)

    # Plot
    t_plot = np.linspace(t_nodes[0], t_nodes[-1], 400)
    pos_plot = evaluate_spline(t_nodes, coefficients, t_plot, derivative=0)
    vel_plot = evaluate_spline(t_nodes, coefficients, t_plot, derivative=1)

    plt.figure()
    plt.plot(t_plot, pos_plot, "b-", label="Posizione s(t)")
    plt.plot(t_plot, vel_plot, "r--", label="Velocità s'(t)")
    plt.plot(t_nodes, x_nodes, "ko", label="Nodi (Dati originali)")
    
    # Segna il punto richiesto se è uno solo
    if np.atleast_1d(query_time).size == 1:
        plt.plot(query_time, position, "gs", markersize=8, label="Punto calcolato")
        
    plt.xlabel("t")
    plt.grid(True)
    plt.legend()
    plt.title("Interpolazione con Spline Naturale")
    plt.show()
