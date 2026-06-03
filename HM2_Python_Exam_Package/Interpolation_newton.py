import numpy as np
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Nodi di interpolazione
x_nodes = np.array([-1, 0, 1, 2], dtype=float)
y_nodes = np.array([3, -4, 5, -6], dtype=float)

# Punto/i in cui valutare l'interpolazione
x_query = 0.5


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

def newton_divided_differences(x, y):
    """
    Calcola le differenze divise di Newton.
    Ritorna i coefficienti del polinomio di Newton.
    """
    n = len(x)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef[0, :]

def evaluate_newton(coef, x_data, x):
    """
    Valuta il polinomio di Newton in un punto x.
    """
    x = np.atleast_1d(x)
    n = len(x_data) - 1 
    p = coef[n] * np.ones_like(x)
    
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
        
    if p.size == 1:
        return p[0]
    return p

# =========================
# MAIN
# =========================

if __name__ == "__main__":
    
    # Calcolo coefficienti (Differenze Divise)
    coefficients = newton_divided_differences(x_nodes, y_nodes)
    
    # Valutazione nel punto richiesto
    y_query = evaluate_newton(coefficients, x_nodes, x_query)

    print("="*40)
    print("RISULTATO INTERPOLAZIONE NEWTON")
    print("="*40)
    print("Differenze Divise (Coefficienti):")
    print(coefficients)
    
    if np.isscalar(x_query) or np.atleast_1d(x_query).size == 1:
        print(f"\\nPunto richiesto: x = {x_query}")
        print(f"Valore interpolato: y = {y_query}")
    else:
        print("\\nPunti valutati:")
        for x_val, y_val in zip(x_query, y_query):
            print(f"  x = {x_val:.4f} -> y = {y_val:.4f}")

    # Plot
    x_plot = np.linspace(np.min(x_nodes) - 1, np.max(x_nodes) + 1, 500)
    y_plot = evaluate_newton(coefficients, x_nodes, x_plot)

    plt.figure()
    plt.plot(x_nodes, y_nodes, "ro", label="Nodi (Dati originali)")
    plt.plot(x_plot, y_plot, "b-", label="Polinomio di Newton")
    
    if np.isscalar(x_query) or np.atleast_1d(x_query).size == 1:
        plt.plot(x_query, y_query, "gs", markersize=8, label=f"Punto stimato x={x_query}")
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interpolazione di Newton (Differenze Divise)")
    plt.grid(True)
    plt.legend()
    plt.show()
