"""
HM2 exam search index.

Apri questo file o cerca nel progetto una parola del testo d'esame.
Ogni riga punta allo script top-level da adattare.

Suchbegriffe importanti:
Jacobi-Matrix, Jacobian, Linearisierung, linearization,
Newton-Verfahren, Newtonverfahren, ohne Daempfung, ohne Dämpfung,
gedaempft, gedämpft, vereinfachtes Newton, Nullstelle, Gleichungssystem,
Minimalstelle, Minimum, Gradient, Hessian, contour, Höhenlinien,
Interpolation, Lagrange, dividierte Differenzen, Newton-Interpolation,
polyfit, polyval, verschobene x-Werte, shift, Spline, kubische Spline,
natuerlich, natürlich, not-a-knot, clamped, periodic, Randbedingungen,
Ausgleichsrechnung, kleinste Fehlerquadrate, least squares, QR,
Normalgleichungen, Kondition, linearisiert, Gauss-Newton, gedämpftes
Gauss-Newton, Residuen, Dämpfungsfaktor,
Rechteckregel, Mittelpunkt-Rechteckregel, Trapezregel, Simpsonregel,
Romberg, Romberg-Extrapolation, Gauss-Legendre, Fehlerabschätzung,
Schrittweite, h, n, nicht aequidistant, nicht äquidistant, Tabelle,
Differentialgleichung, DGL, ODE, Richtungsfeld, Euler, expliziter Euler,
klassischer Euler, modifizierter Euler, Heun, Mittelpunktverfahren,
Runge-Kutta, RK4, Butcher-Tableau, Ordnung, Fehlerordnung, Stabilität,
System erster Ordnung, DGL n-ter Ordnung, Rakete, Boeing,
plot_surface, plot_wireframe, contour, SymPy.
"""


EXAM_CASES = [
    (
        "3D plotting, Flaechen, Wurfweite, ideales Gas, contour, surface, wireframe",
        "S1_Flaechen_3D.py",
    ),
    (
        "Wellengleichung w(x,t), v(x,t), plot_wireframe",
        "S1_Wellengleichung_3D.py",
    ),
    (
        "SymPy Jacobi-Matrix, Jacobian, partielle Ableitungen",
        "Sympy_jacobian.py",
    ),
    (
        "Linearisierung f(x0)+Df(x0)(x-x0)",
        "Sympy_linearisierung.py",
    ),
    (
        "Newton 1D, Nullstelle einer Funktion, Tangentenverfahren",
        "Nichtlineare_Gleichung_newton_1d.py",
    ),
    (
        "Newton-Verfahren fuer Systeme ohne Daempfung",
        "Nichtlineare_Gleichungssysteme_newton.py",
    ),
    (
        "Minimum, Minimalstelle, Gradient gleich 0, Hessian, contour f1=0 f2=0",
        "Newton_minimum_contour.py",
    ),
    (
        "vereinfachtes Newton-Verfahren, fixe Jacobi-Matrix",
        "Nichtlineare_Gleichungssysteme_newton_vereinfacht.py",
    ),
    (
        "gedaempftes Newton-Verfahren, Dämpfung",
        "Nichtlineare_Gleichungssysteme_newton_gedaempft.py",
    ),
    (
        "Lagrange Interpolation",
        "Interpolation_lagrange.py",
    ),
    (
        "Newton Interpolation, dividierte Differenzen",
        "Interpolation_newton.py",
    ),
    (
        "polyfit polyval verschobene x-Werte shifted interpolation plot",
        "Interpolation_polynom_shift_plot.py",
    ),
    (
        "natuerliche kubische Spline, s(t), s'(t), s''(t)",
        "Interpolation_spline_natuerlich.py",
    ),
    (
        "Spline Randbedingungen natural not-a-knot clamped periodic SciPy CubicSpline",
        "Interpolation_spline_randbedingungen.py",
    ),
    (
        "lineare Ausgleichsrechnung QR, custom basis, polynomial least squares",
        "Ausgleichsrechnung_minimi_quadrati_qr.py",
    ),
    (
        "polynomial fit, Normalgleichungen, QR, polyfit, Kondition",
        "Ausgleichsrechnung_polynom_fit.py",
    ),
    (
        "linearisierter Fit, transformierte Daten, Moore, exponential/power law",
        "Ausgleichsrechnung_linearisiert.py",
    ),
    (
        "multivariate lineare Ausgleichsrechnung, Designmatrix mehrere Variablen",
        "Ausgleichsrechnung_linear.py",
    ),
    (
        "Gauss-Newton gedaempft, nonlinear least squares, Residuen",
        "Ausgleichsrechnung_gauss_newton_gedaempft.py",
    ),
    (
        "Rechteck Trapez Simpson exakter Fehler Fehlerabschaetzung h n",
        "Integration_error_bounds.py",
    ),
    (
        "Trapez Simpson Romberg Tabelle aus Funktion oder Daten",
        "Numerische_Integration_romberg_simpson.py",
    ),
    (
        "nicht aequidistante Tabelle Trapezregel Messdaten",
        "Integration_trapez_tabelle_nichtaequidistant.py",
    ),
    (
        "Gauss-Legendre Quadratur Knoten Gewichte leggauss",
        "Numerische_Integration_gauss_legendre.py",
    ),
    (
        "kumulative Trapezregel Beschleunigung Geschwindigkeit Hoehe Rakete",
        "Integration_rakete_kumulativ.py",
    ),
    (
        "Richtungsfeld slope field DGL y'=f(x,y)",
        "DGL_euler_richtungsfeld.py",
    ),
    (
        "Euler Mittelpunkt modifizierter Euler Heun DGL 1. Ordnung",
        "DGL_euler_mittelpunkt_heun.py",
    ),
    (
        "DGL n-ter Ordnung in System erster Ordnung Euler Mittelpunkt",
        "DGL_system_euler_mittelpunkt.py",
    ),
    (
        "Runge-Kutta RK4 klassisch custom RK Vergleich Fehler",
        "DGL_rk4_euler_mod.py",
    ),
    (
        "Butcher-Tableau Runge-Kutta Ordnung Fehlerordnung",
        "DGL_runge_kutta_butcher_ordnung.py",
    ),
    (
        "Rakete System RK4 vs modifizierter Euler",
        "DGL_rakete_rk4_vs_euler_mod.py",
    ),
    (
        "Boeing Mittelpunktverfahren Bremsweg Stopp",
        "DGL_boeing_midpoint_stopp.py",
    ),
    (
        "Stabilitaet Stabilität Schrittweite globaler Fehler Ordnung",
        "DGL_stabilita_schrittweite.py",
    ),
]


if __name__ == "__main__":
    print("HM2 exam script search index\n")
    for keywords, script in EXAM_CASES:
        print(f"{script:48s}  <- {keywords}")
