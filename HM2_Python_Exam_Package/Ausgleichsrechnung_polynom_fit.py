import numpy as np
import matplotlib.pyplot as plt

# =========================
# INPUT
# =========================

# Dati
x_data = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], dtype=float)
y_data = np.array([999.9, 999.7, 998.2, 995.7, 992.2, 988.1, 983.2, 977.8, 971.8, 965.3, 958.4], dtype=float)

# Grado del polinomio da interpolare
poly_degree = 2


# =========================
# FUNZIONI (NON MODIFICARE)
# =========================

def compute_error_functional(measured_values, fitted_values):
    residual_values = measured_values - fitted_values
    return np.sum(residual_values ** 2)

def build_design_matrix(x_values, degree):
    # Ritorna la matrice di design (Vandermonde). 
    # Es: per grado 2 -> colonne: x^2, x^1, x^0
    return np.vander(x_values, degree + 1, increasing=False)

def main():
    design_matrix = build_design_matrix(x_data, poly_degree)
    observation_vector = y_data

    # a) Soluzione con le equazioni normali senza QR
    normal_equation_matrix = design_matrix.T @ design_matrix
    normal_equation_right_hand_side = design_matrix.T @ observation_vector
    coefficients_without_qr = np.linalg.solve(
        normal_equation_matrix,
        normal_equation_right_hand_side,
    )

    # b) Soluzione con le equazioni normali usando QR
    orthogonal_matrix, upper_triangular_matrix = np.linalg.qr(design_matrix)
    coefficients_with_qr = np.linalg.solve(
        upper_triangular_matrix,
        orthogonal_matrix.T @ observation_vector,
    )

    # c) Soluzione con la funzione di libreria polyfit
    coefficients_polyfit = np.polyfit(
        x_data,
        y_data,
        poly_degree,
    )

    # d) Numeri di condizionamento
    condition_number_ata = np.linalg.cond(normal_equation_matrix)
    condition_number_r = np.linalg.cond(upper_triangular_matrix)

    # Dati per il plot
    plot_x_values = np.linspace(np.min(x_data), np.max(x_data), 500)
    
    fitted_curve_without_qr = np.polyval(coefficients_without_qr, plot_x_values)
    fitted_curve_with_qr = np.polyval(coefficients_with_qr, plot_x_values)
    fitted_curve_polyfit = np.polyval(coefficients_polyfit, plot_x_values)

    fitted_data_without_qr = design_matrix @ coefficients_without_qr
    fitted_data_with_qr = design_matrix @ coefficients_with_qr
    fitted_data_polyfit = design_matrix @ coefficients_polyfit

    error_without_qr = compute_error_functional(observation_vector, fitted_data_without_qr)
    error_with_qr = compute_error_functional(observation_vector, fitted_data_with_qr)
    error_polyfit = compute_error_functional(observation_vector, fitted_data_polyfit)

    # Stampa Risultati
    print("="*40)
    print("RISULTATI FIT POLINOMIALE (Grado {})".format(poly_degree))
    print("="*40)
    print("\\na) Coefficienti SENZA QR (Equazioni Normali):")
    print(coefficients_without_qr)

    print("\\nb) Coefficienti CON QR:")
    print(coefficients_with_qr)
    
    print("\\nc) Coefficienti con numpy.polyfit():")
    print(coefficients_polyfit)

    print("\\n--- Numeri di condizionamento ---")
    print(f"cond(A^T A) = {condition_number_ata:.12e}")
    print(f"cond(R)     = {condition_number_r:.12e}")

    print("\\n--- Errori al quadrato (Residui) ---")
    print(f"Errore senza QR   = {error_without_qr:.12f}")
    print(f"Errore con QR      = {error_with_qr:.12f}")
    print(f"Errore con polyfit = {error_polyfit:.12f}")

    # Plot
    plt.figure(figsize=(9, 6))
    plt.plot(x_data, y_data, "o", label="Dati misurati")
    plt.plot(plot_x_values, fitted_curve_without_qr, label="Eq. normali senza QR")
    plt.plot(plot_x_values, fitted_curve_with_qr, "--", label="Eq. normali con QR")
    plt.plot(plot_x_values, fitted_curve_polyfit, ":", label="numpy.polyfit()")
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Fit Polinomiale di grado {poly_degree}")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
