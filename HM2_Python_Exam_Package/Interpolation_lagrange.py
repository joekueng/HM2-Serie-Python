import numpy as np
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Nodi di interpolazione
x_nodes = np.array([0, 2500, 5000, 10000], dtype=float)
y_nodes = np.array([1013, 747, 540, 226], dtype=float)

# Punto/i in cui valutare l'interpolazione
x_query = 3750


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

def lagrange_int(x, y, x_int):
    # Supporta x_int come scalare o array
    x_int = np.atleast_1d(x_int)
    y_int = np.zeros_like(x_int, dtype=float)

    for k, xi in enumerate(x_int):
        s = 0
        for i in range(len(x)):
            L = 1
            for j in range(len(x)):
                if i != j:
                    L = L * (xi - x[j]) / (x[i] - x[j])
            s = s + y[i] * L
        y_int[k] = s

    # Se l'input era uno scalare, ritorniamo uno scalare
    if y_int.size == 1:
        return y_int[0]
    return y_int

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    y_query = lagrange_int(x_nodes, y_nodes, x_query)

    print("="*40)
    print("RISULTATO INTERPOLAZIONE LAGRANGE")
    print("="*40)
    
    if np.isscalar(x_query) or np.atleast_1d(x_query).size == 1:
        print(f"Punto richiesto: x = {x_query}")
        print(f"Valore interpolato: y = {y_query}")
    else:
        print("Punti valutati:")
        for x_val, y_val in zip(x_query, y_query):
            print(f"  x = {x_val:.4f} -> y = {y_val:.4f}")

    # Plot
    x_plot = np.linspace(np.min(x_nodes), np.max(x_nodes), 500)
    y_plot = lagrange_int(x_nodes, y_nodes, x_plot)

    plt.figure()
    plt.plot(x_nodes, y_nodes, "ro", label="Nodi (Dati originali)")
    plt.plot(x_plot, y_plot, "b-", label="Polinomio di Lagrange")
    
    if np.isscalar(x_query) or np.atleast_1d(x_query).size == 1:
        plt.plot(x_query, y_query, "gs", markersize=8, label=f"Punto stimato x={x_query}")
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolazione di Lagrange")
    plt.grid(True)
    plt.legend()
    plt.show()