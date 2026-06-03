import numpy as np
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Dati in input
x_data = np.array([-2.0, -1.0, 1.0, 2.0])
y_data = np.array([-5.5, -5.0, 5.0, 5.5])

# Scegli il tipo di approssimazione: "custom" oppure "polynom"
fit_type = "custom" 

# --- SE "polynom" ---
# Grado del polinomio
polynomial_degree = 4

# --- SE "custom" ---
# Definisci qui le tue funzioni di base
# Esempio: f(x) = alpha * (1/x) + beta * (x)
def get_basis_functions(x_val):
    # Ritorna una lista/tupla contenente le varie funzioni applicate a x_val
    # (ogni elemento sarà una colonna della matrice di design)
    return [
        1.0 / x_val,
        x_val
    ]
parameter_names = ["alpha", "beta"] # Nomi per la stampa

# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

def solve_least_squares_qr(design_matrix, y_values):
    q_matrix, r_matrix = np.linalg.qr(design_matrix)
    coefficients = np.linalg.solve(r_matrix, q_matrix.T @ y_values)
    error_functional = np.linalg.norm(design_matrix @ coefficients - y_values, ord=2) ** 2
    return coefficients, error_functional

def polynomial_design_matrix(x_values, degree):
    # increasing=False significa che ordina da x^d fino a x^0
    return np.vander(x_values, degree + 1, increasing=False)


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    
    if fit_type == "polynom":
        design_matrix = polynomial_design_matrix(x_data, polynomial_degree)
    else:
        basis = get_basis_functions(x_data)
        design_matrix = np.column_stack(basis)

    coefficients, error = solve_least_squares_qr(design_matrix, y_data)

    print("="*30)
    print("RISULTATI MINIMI QUADRATI (QR)")
    print("="*30)
    
    if fit_type == "polynom":
        print(f"Coefficienti polinomio (grado {polynomial_degree}, da x^d a costante):")
        print(coefficients)
    else:
        for name, val in zip(parameter_names, coefficients):
            print(f"{name} = {val}")
            
    print(f"Errore al quadrato (Residuo) = {error}")

    # --- Plotting ---
    # Creazione asse X (evitiamo lo 0 per non dividere per zero se c'è 1/x)
    x_plot = np.linspace(np.min(x_data), np.max(x_data), 500)
    
    if fit_type == "polynom":
        y_plot = np.polyval(coefficients, x_plot)
    else:
        basis_plot = get_basis_functions(x_plot)
        y_plot = np.zeros_like(x_plot)
        for c, basis_func_vals in zip(coefficients, basis_plot):
            y_plot += c * basis_func_vals
    
    # Rimuoviamo eventuali outlier grafici dovuti a divisioni per zero
    y_plot = np.clip(y_plot, np.min(y_data)*2, np.max(y_data)*2)

    plt.figure()
    plt.plot(x_data, y_data, "o", label="Dati misurati")
    plt.plot(x_plot, y_plot, label="Fit Minim. Quadrati")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()
