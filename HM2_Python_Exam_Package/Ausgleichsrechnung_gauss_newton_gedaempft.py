import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Dati in input
x_data = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
y_data = np.array([0.39, 0.89, 1.45, 1.23, 0.86, 0.83, 0.58, 0.50, 0.44, 0.34])

# Valori iniziali per i parametri
start_parameters = np.array([8.0, 8.0, 0.0, 8.0])

# Parametri dell'algoritmo
tolerance = 1e-5
max_iterations = 200
max_damping_p = 10  # pmax per il damping

def define_model():
    """
    Definisci qui la tua equazione e i parametri.
    Ritorna:
        x_sym: il simbolo per la variabile indipendente (es. x)
        param_symbols: lista dei simboli dei parametri
        model_expr: l'equazione del modello scritta in Sympy
    """
    x_sym = sp.Symbol('x')
    a_sym, b_sym, p_sym, q_sym = sp.symbols('a b p q')
    param_symbols = [a_sym, b_sym, p_sym, q_sym]

    # Esempio FS25: T(x) = (A*x + B) / (x^2 + p*x + q)
    model_expr = (a_sym * x_sym + b_sym) / (x_sym**2 + p_sym * x_sym + q_sym)

    return x_sym, param_symbols, model_expr


# =========================
# FUNZIONI DI SUPPORTO (NON MODIFICARE)
# =========================

x_sym, param_symbols, model_expr = define_model()
jacobian_exprs = [sp.diff(model_expr, p) for p in param_symbols]

model_num = sp.lambdify((x_sym, param_symbols), model_expr, 'numpy')
jacobian_num_funcs = [sp.lambdify((x_sym, param_symbols), expr, 'numpy') for expr in jacobian_exprs]

def model(x_values, parameters):
    res = model_num(x_values, parameters)
    if np.isscalar(res) and not np.isscalar(x_values):
        return np.full_like(x_values, res, dtype=float)
    return res

def residual(parameters):
    return model(x_data, parameters) - y_data

def jacobian(parameters):
    J_cols = []
    for f in jacobian_num_funcs:
        col = f(x_data, parameters)
        if np.isscalar(col) or (isinstance(col, np.ndarray) and col.ndim == 0):
            col = np.full_like(x_data, float(col), dtype=float)
        J_cols.append(col)
    return np.column_stack(J_cols)

def error_function(parameters):
    return np.linalg.norm(residual(parameters), ord=2) ** 2

def gauss_newton_damped(start_parameters, tolerance=1e-5, max_iterations=100, pmax=10):
    parameters = np.array(start_parameters, dtype=float)

    for iteration in range(1, max_iterations + 1):
        J = jacobian(parameters)
        res = residual(parameters)
        step = np.linalg.lstsq(J, -res, rcond=None)[0]
        damping_power = 0

        while damping_power <= pmax:
            candidate = parameters + step / (2**damping_power)
            if error_function(candidate) < error_function(parameters):
                break
            damping_power += 1

        if damping_power > pmax:
            raise RuntimeError("Nessuno step di damping ha ridotto l'errore. Verifica i valori iniziali.")

        damped_step = step / (2**damping_power)
        parameters = parameters + damped_step

        print(
            f"Iterazione {iteration:2d}: parametri = {parameters}, "
            f"norma_step = {np.linalg.norm(damped_step):.3e}, "
            f"p = {damping_power}, errore = {error_function(parameters):.3e}"
        )

        if np.linalg.norm(damped_step, ord=2) <= tolerance:
            return parameters, iteration

    raise RuntimeError("Gauss-Newton non ha raggiunto la convergenza")

def minimal_required_pmax(start_parameters, tolerance, max_iterations, maximum_to_test=10):
    best_result = None
    for candidate_pmax in range(maximum_to_test + 1):
        try:
            print(f"\\n--- Test con pmax = {candidate_pmax} ---")
            parameters, iterations = gauss_newton_damped(
                start_parameters,
                tolerance=tolerance,
                max_iterations=max_iterations,
                pmax=candidate_pmax,
            )
            best_result = candidate_pmax, parameters, iterations
            break
        except RuntimeError as e:
            print(f"Fallito: {e}")
            continue

    if best_result is None:
        raise RuntimeError("Nessun pmax testato ha portato a convergenza")

    return best_result


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    print("Inizio calcolo Gauss-Newton (Ricerca automatica del pmax minimo necessaria se damping abilitato)...")
    pmax_req, fitted_parameters, iterations = minimal_required_pmax(
        start_parameters, tolerance, max_iterations, max_damping_p
    )

    print("\\n" + "="*30)
    print("RISULTATO FINALE")
    print("="*30)
    print("pmax minimo richiesto =", pmax_req)
    print("Parametri calcolati =", fitted_parameters)
    for sym, val in zip(param_symbols, fitted_parameters):
        print(f"  {sym} = {val}")
    print("Numero iterazioni   =", iterations)
    print("Errore (residuo^2)  =", error_function(fitted_parameters))

    x_plot = np.linspace(np.min(x_data), np.max(x_data), 500)
    y_plot = model(x_plot, fitted_parameters)

    plt.figure()
    plt.plot(x_data, y_data, "o", label="Dati misurati")
    plt.plot(x_plot, y_plot, label="Curva adattata (Fit)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.title("Gauss-Newton Fit")
    plt.show()
