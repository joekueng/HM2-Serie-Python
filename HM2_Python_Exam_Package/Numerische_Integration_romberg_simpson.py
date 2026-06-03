import numpy as np

# =========================
# INPUT
# =========================

# --- SE HAI LA FUNZIONE ---
def function(x):
    # Esempio: f(x) = 6*x^2 - 2*x
    return 6 * x**2 - 2 * x

# Estremi di integrazione
a = 0.0
b = 4.0

# Numero di sottointervalli n per Trapezio e Simpson
# (Per Simpson, n deve essere PARI)
n_intervals = 4

# Numero di livelli per la tabella di Romberg (n = 2^(level-1) intervalli)
romberg_levels = 3


# --- SE HAI UNA TABELLA DI DATI (Es. senza funzione analitica) ---
# Usa questo per il metodo dei trapezi su dati tabellari
x_table = np.array([0.0, 0.5, 1.0, 1.5, 2.0], dtype=float)
y_table = np.array([2.0, np.sqrt(15) / 2, np.sqrt(3), np.sqrt(7) / 2, 0.0], dtype=float)


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

def summed_trapezoid_from_function(function, a, b, n):
    x_values = np.linspace(a, b, n + 1)
    y_values = function(x_values)
    h = (b - a) / n
    return h * (0.5 * y_values[0] + np.sum(y_values[1:-1]) + 0.5 * y_values[-1])

def summed_trapezoid_from_table(x_values, y_values):
    return np.trapezoid(y_values, x_values)

def summed_simpson_from_function(function, a, b, n):
    if n % 2 != 0:
        raise ValueError("Il metodo di Simpson richiede un numero PARI di intervalli (n).")

    x_values = np.linspace(a, b, n + 1)
    y_values = function(x_values)
    h = (b - a) / n
    return h / 3 * (
        y_values[0]
        + y_values[-1]
        + 4 * np.sum(y_values[1:-1:2])
        + 2 * np.sum(y_values[2:-1:2])
    )

def romberg_from_function(function, a, b, levels):
    table = np.zeros((levels, levels), dtype=float)

    for row in range(levels):
        n = 2**row
        table[row, 0] = summed_trapezoid_from_function(function, a, b, n)

        for column in range(1, row + 1):
            table[row, column] = (
                4**column * table[row, column - 1] - table[row - 1, column - 1]
            ) / (4**column - 1)

    return table

def max_step_trapezoid(error_bound, a, b, max_abs_second_derivative):
    # Error <= (b-a)/12 * h^2 * max |f''|
    return np.sqrt(12 * error_bound / ((b - a) * max_abs_second_derivative))


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    
    print("="*40)
    print("INTEGRAZIONE NUMERICA DA FUNZIONE")
    print("="*40)
    print(f"Intervallo: [{a}, {b}]")
    
    trap_res = summed_trapezoid_from_function(function, a, b, n=n_intervals)
    print(f"\\nTrapezi Sommato (n={n_intervals}): {trap_res}")
    
    try:
        simp_res = summed_simpson_from_function(function, a, b, n=n_intervals)
        print(f"Simpson Sommato (n={n_intervals}): {simp_res}")
    except ValueError as e:
        print(f"Simpson Sommato (n={n_intervals}): {e}")
        
    print(f"\\nTabella di Romberg (livelli={romberg_levels}):")
    romb_table = romberg_from_function(function, a, b, levels=romberg_levels)
    # Stampa la matrice nascondendo gli zeri
    for i in range(romberg_levels):
        row_str = "  ".join([f"{romb_table[i, j]:10.6f}" for j in range(i+1)])
        print(f"Livello {i}: {row_str}")
        
    print(f"\\nMiglior stima Romberg (R_{romberg_levels-1},{romberg_levels-1}): {romb_table[-1, -1]}")
    
    print("\\n" + "="*40)
    print("INTEGRAZIONE NUMERICA DA TABELLA DATI")
    print("="*40)
    trap_table_res = summed_trapezoid_from_table(x_table, y_table)
    print(f"Trapezi su dati tabellari: {trap_table_res}")
