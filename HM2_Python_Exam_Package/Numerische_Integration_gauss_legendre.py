import numpy as np

# =========================
# INPUT
# =========================

# Definisci qui la funzione da integrare
def function(x):
    # Esempio: f(x) = e^x
    return np.exp(x)

# Estremi di integrazione
a = 0.0
b = 1.0

# Numero di punti per la Quadratura di Gauss (n)
# Di solito n = 2, 3, 4, 5
n_points = 3


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

def gauss_legendre_quadrature(f, a, b, n):
    """
    Calcola l'integrale definito di f da a a b utilizzando
    la formula di quadratura di Gauss-Legendre a n punti.
    """
    # Ottieni i nodi (x_i) e i pesi (w_i) standard per l'intervallo [-1, 1]
    # np.polynomial.legendre.leggauss restituisce nodi e pesi per il grado n
    nodes_standard, weights = np.polynomial.legendre.leggauss(n)
    
    # Mappatura dei nodi dall'intervallo [-1, 1] all'intervallo [a, b]
    nodes_mapped = 0.5 * (b - a) * nodes_standard + 0.5 * (a + b)
    
    # Valuta la funzione nei nodi mappati
    f_values = f(nodes_mapped)
    
    # Applica la formula di quadratura: (b-a)/2 * sum(w_i * f(x_i))
    integral = 0.5 * (b - a) * np.sum(weights * f_values)
    
    return integral, nodes_standard, weights, nodes_mapped


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    
    result, nodes_std, weights, nodes_mapped = gauss_legendre_quadrature(function, a, b, n_points)
    
    print("="*40)
    print(f"QUADRATURA DI GAUSS-LEGENDRE (n={n_points})")
    print("="*40)
    print(f"Intervallo: [{a}, {b}]")
    print(f"\\nValore stimato dell'integrale = {result}")
    
    print("\\nDettagli del calcolo:")
    print("  Nodi standard [-1, 1]:", nodes_std)
    print("  Pesi (w_i):           ", weights)
    print("  Nodi mappati [a, b]:  ", nodes_mapped)
    
    print("\\nSommatoria: (b-a)/2 * sum(w_i * f(x_mapped_i))")
