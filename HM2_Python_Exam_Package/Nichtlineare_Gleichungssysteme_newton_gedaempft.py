import numpy as np
import sympy as sp

# =========================
# INPUT
# =========================

# Valori iniziali (vettore di partenza)
start_vector = np.array([1.5, 3.0, 2.5], dtype=float)

# Parametri dell'algoritmo
tolerance = 1e-5
max_iterations = 100
min_damping_factor = 1e-8 # Se il damping scende sotto questa soglia, si ferma

def define_system():
    """
    Definisci qui le equazioni del sistema non lineare f(x) = 0.
    """
    x1, x2, x3 = sp.symbols('x1 x2 x3')
    param_symbols = [x1, x2, x3]
    
    # Esempio
    eq1 = x1 + x2**2 - x3**2 - 13
    eq2 = sp.log(x2 / 4) + sp.exp(0.5 * x3 - 1) - 1
    eq3 = (x2 - 3)**2 - x3**3 + 7
    
    system_exprs = [eq1, eq2, eq3]
    
    return param_symbols, system_exprs


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

param_symbols, system_exprs = define_system()

jacobian_exprs = []
for eq in system_exprs:
    row = [sp.diff(eq, p) for p in param_symbols]
    jacobian_exprs.append(row)

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

def damped_newton_method(start_vector, tolerance=1e-5, max_iterations=100):
    current_vector = np.array(start_vector, dtype=float)

    for iteration in range(1, max_iterations + 1):
        current_f = f_function(current_vector)
        current_norm = np.linalg.norm(current_f, ord=2)

        if current_norm < tolerance:
            return current_vector, iteration, current_norm

        J = jacobian_function(current_vector)
        
        try:
            newton_step = np.linalg.solve(J, -current_f)
        except np.linalg.LinAlgError:
            raise RuntimeError(f"Lo Jacobiano è singolare all'iterazione {iteration}")

        damping_factor = 1.0

        while damping_factor > min_damping_factor:
            candidate_vector = current_vector + damping_factor * newton_step
            candidate_f = f_function(candidate_vector)
            
            # Se la norma 2 del candidato è minore della norma 2 attuale, accetta il passo
            if np.linalg.norm(candidate_f, ord=2) < current_norm:
                current_vector = candidate_vector
                break
                
            damping_factor /= 2.0

        print(f"Iterazione {iteration:2d}: x = {current_vector}, damping = {damping_factor:.2e}, error_L2 = {np.linalg.norm(candidate_f, ord=2):.3e}")

        if damping_factor <= min_damping_factor:
            print("Attenzione: Damping factor sceso sotto la soglia minima senza miglioramenti.")
            break

    final_f = f_function(current_vector)
    return current_vector, max_iterations, np.linalg.norm(final_f, ord=2)


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    print("Inizio iterazioni di Newton Smorzato (Damped Newton)...")
    solution, iterations, final_norm = damped_newton_method(start_vector, tolerance, max_iterations)

    print("\n" + "="*40)
    print("RISULTATO NEWTON SMORZATO")
    print("="*40)
    print("Soluzione approssimata:")
    for sym, val in zip(param_symbols, solution):
        print(f"  {sym} = {val}")
    print(f"\nIterazioni effettuate = {iterations}")
    print(f"Norma 2 dell'errore ( ||f(x)|| ) = {final_norm}")
