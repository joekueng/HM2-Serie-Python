import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Valori iniziali (vettore di partenza)
start_vector = np.array([0.2, 0.8], dtype=float)

# Parametri dell'algoritmo
tolerance = 1e-8
max_iterations = 50

def define_system():
    """
    Definisci qui le equazioni del sistema non lineare f(x) = 0.
    Ritorna:
        param_symbols: lista dei simboli delle variabili (es. x, y, z)
        system_exprs: lista delle equazioni (espressioni che devono essere uguali a zero)
    """
    x, y = sp.symbols('x y')
    param_symbols = [x, y]
    
    # Esempio:
    # f1: 4x^3 - 4xy + 20x - 8.4 = 0
    # f2: -2x^2 + 2y = 0
    eq1 = 4 * x**3 - 4 * x * y + 20 * x - 8.4
    eq2 = -2 * x**2 + 2 * y
    
    system_exprs = [eq1, eq2]
    
    return param_symbols, system_exprs


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

param_symbols, system_exprs = define_system()

# Calcolo automatico dello Jacobiano (matrice nxn)
jacobian_exprs = []
for eq in system_exprs:
    row = [sp.diff(eq, p) for p in param_symbols]
    jacobian_exprs.append(row)

# Funzioni numeriche (più veloci)
# lambdify accetta una lista di variabili e ritorna una funzione numerica
f_num = [sp.lambdify(param_symbols, eq, 'numpy') for eq in system_exprs]
jac_num = [[sp.lambdify(param_symbols, expr, 'numpy') for expr in row] for row in jacobian_exprs]

def f_function(vector):
    return np.array([func(*vector) for func in f_num], dtype=float)

def jacobian_function(vector):
    J = np.zeros((len(system_exprs), len(param_symbols)), dtype=float)
    for i in range(len(system_exprs)):
        for j in range(len(param_symbols)):
            J[i, j] = jac_num[i][j](*vector)
    return J

def newton_system(start_vector, tolerance=1e-8, max_iterations=50):
    current_vector = np.array(start_vector, dtype=float)

    for iteration in range(1, max_iterations + 1):
        function_value = f_function(current_vector)
        J = jacobian_function(current_vector)
        
        try:
            newton_step = np.linalg.solve(J, -function_value)
        except np.linalg.LinAlgError:
            raise RuntimeError(f"Lo Jacobiano è singolare all'iterazione {iteration} per {current_vector}")

        current_vector = current_vector + newton_step
        error = np.linalg.norm(f_function(current_vector), ord=np.inf)

        print(
            f"Iterazione {iteration:2d}: "
            f"x = {current_vector}, step_norm = {np.linalg.norm(newton_step):.3e}, "
            f"error_inf = {error:.3e}"
        )

        if error < tolerance:
            return current_vector, iteration

    raise RuntimeError("Il metodo di Newton non è conversato (raggiunto limite iterazioni)")


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    print("Inizio iterazioni di Newton...")
    solution, iterations = newton_system(start_vector, tolerance, max_iterations)

    print("\\n" + "="*40)
    print("RISULTATO NEWTON (SISTEMI NON LINEARI)")
    print("="*40)
    print("Soluzione approssimata:")
    for sym, val in zip(param_symbols, solution):
        print(f"  {sym} = {val}")
    print(f"\\nNumero di iterazioni = {iterations}")
    print(f"Valore di f(soluzione) = {f_function(solution)}")
    print(f"Norma infinito errore = {np.linalg.norm(f_function(solution), ord=np.inf)}")
