# HM2 Python Script Audit
## Sintesi tecnica
- File Python trovati: **76**
- Notebook trovati: **4**
- `py_compile`: **OK su tutti**

## Copertura per serie / argomento

| Area | Richiesta | Stato | File rilevanti / nota |
|---|---|---:|---|
| S1 Aufg1 | 3D surface/wireframe/contour: Wurfweite + ideales Gas | OK | `S1_Flaechen_3D.py`, `Scripts/Basics/Plotting_2d_3d.py`, `exam-prova/Flaechen.ipynb` |
| S1 Aufg2b | Wellengleichung w(x,t), v(x,t) in 3D | OK | `S1_Wellengleichung_3D.py` |
| S2 Aufg2 | Jacobi-Matrix con SymPy | OK | `Sympy_jacobian.py`, `Scripts/Basics/Sympy_jacobian.py` |
| S2 Aufg3 | Linearisierung f(x0)+Df(x0)(x-x0) | OK | `Sympy_linearisierung.py`, `Scripts/Basics/Sympy_linearisierung.py` |
| S3 Aufg2 | Newton per 4 intersezioni delle iperboli | OK | `Scripts/Kapitel_5/Newton_systeme.py`, `exam-prova/Newton_system_hyperbeln.py` |
| S3 Aufg3 | Gedämpftes Newton 3x3 | OK | `Nichtlineare_Gleichungssysteme_newton_gedaempft.py`, `Scripts/Kapitel_5/Newton_gedaempft.py`: formula corretta a `log(x2 / 4)` |
| S4 Aufg2 | Lagrange interpolation | OK | `Interpolation_lagrange.py`, `Scripts/Kapitel_6/Interpolation_lagrange.py` |
| S4 Aufg3 | polyfit/polyval with shifted x + Lagrange vector | OK | `Interpolation_polynom_shift_plot.py`, `Scripts/Kapitel_6/Interpolation_polynom_shift_plot.py` |
| S5 Aufg2-3 | natural cubic spline + SciPy comparison + polyfit | OK | `Interpolation_spline_natuerlich.py`, `Scripts/Kapitel_6/Spline_natuerlich*.py` |
| S6 Aufg1 | linear LS quadratic, normal equations, QR, polyfit, condition | OK | `Ausgleichsrechnung_polynom_fit.py`, `Scripts/Kapitel_6/Ausgleichsrechnung_polynom_qr.py` |
| S6 Aufg2 | linear LS multivariate vapour data | OK | `Scripts/Kapitel_6/Ausgleichsrechnung_linear.py` |
| S7 | Gauss-Newton damped/undamped + fmin | OK | `Ausgleichsrechnung_gauss_newton_gedaempft.py`, `Scripts/Kapitel_6/Ausgleichsrechnung_gauss_newton_gedaempft.py`, notebook |
| S8 Aufg2 | rectangle/trapezoid/Simpson + exact integral + absolute errors | OK | `Integration_error_bounds.py`, `Numerische_Integration_romberg_simpson.py` |
| S8 Aufg3 | non-equidistant trapezoid + earth mass | OK | `Scripts/Kapitel_7/Integration_trapez_erde.py` |
| S9 Aufg1 | error bounds h/n for rectangle/trapezoid/Simpson | OK | `Integration_error_bounds.py` |
| S9 Aufg3 | Romberg extrapolation | OK | `Scripts/Kapitel_7/Integration_romberg.py`, top-level integration script |
| S10 | Boeing Romberg + rocket trapezoid cumulative | OK | `Scripts/Kapitel_7/Integration_boeing_romberg.py`, `Integration_rakete_kumulativ.py` |
| S11 | direction field + Euler/Mittelpunkt/mod Euler | OK | `DGL_euler_mittelpunkt_heun.py`, `DGL_euler_richtungsfeld.py`, `Scripts/Kapitel_8/DGL_euler_mittelpunkt_heun.py` |
| S12 | RK4 + custom RK + method comparison/errors | OK | `DGL_rk4_euler_mod.py`, `DGL_runge_kutta_butcher_ordnung.py`, `DGL_rakete_rk4_vs_euler_mod.py`, `Scripts/Kapitel_8/DGL_methodenvergleich.py` |
| Kap.5 simplified Newton | vereinfachtes Newton-Verfahren | OK | `Nichtlineare_Gleichungssysteme_newton_vereinfacht.py` |
| Kap.8 stability/step control | Stabilität/Schrittweitensteuerung | OK | `DGL_stabilita_schrittweite.py` |

## Correzioni applicate

1. Corretta la formula in `Nichtlineare_Gleichungssysteme_newton_gedaempft.py`, `Scripts/Kapitel_5/Newton_gedaempft.py` e `exam-prova/Newton_system_gedaempft_3x3.py`: `log(x2 / 4)` con derivata `1 / x2`.
2. Aggiunto `Integration_error_bounds.py` con midpoint rectangle, trapezoid, Simpson, errore assoluto e formule per h/n.
3. Aggiunto `DGL_stabilita_schrittweite.py` per ordine globale, fattore di riduzione di h e stabilita Euler esplicito.
4. Aggiunti `S1_Wellengleichung_3D.py` e `S1_Flaechen_3D.py`.
5. Copiati nel top-level gli script nascosti indicati: SymPy, interpolazione shifted, DGL Euler/Mittelpunkt/Heun, Richtungsfeld e razzo RK4 vs Euler modificato.

## Promozioni top-level intenzionali

- `Sympy_jacobian.py` = `Scripts/Basics/Sympy_jacobian.py`
- `Sympy_linearisierung.py` = `Scripts/Basics/Sympy_linearisierung.py`
- `Interpolation_polynom_shift_plot.py` = `Scripts/Kapitel_6/Interpolation_polynom_shift_plot.py`
- `DGL_euler_mittelpunkt_heun.py` = `Scripts/Kapitel_8/DGL_euler_mittelpunkt_heun.py`
- `DGL_euler_richtungsfeld.py` = `Scripts/Kapitel_8/DGL_euler_richtungsfeld.py`
- `DGL_rakete_rk4_vs_euler_mod.py` = `Scripts/Kapitel_8/DGL_rakete_rk4_vs_euler_mod.py`

## Duplicati identici trovati

- `DGL_boeing_midpoint_stopp.py` = `Scripts/Kapitel_8/DGL_boeing_mittelpunkt.py`
- `exam-prova/Spline_natuerlich.py` = `Scripts/Kapitel_6/Spline_natuerlich.py`
- `exam-prova/Ausgleichsrechnung_linear_masse.py` = `Scripts/Kapitel_6/Ausgleichsrechnung_linear.py`
- `exam-prova/Interpolation_polynom_verschoben.py` = `Scripts/Kapitel_6/Interpolation_polynom_shift_plot.py`
- `exam-prova/Gauss_Newton_originaldaten.py` = `Scripts/Kapitel_6/Ausgleichsrechnung_gauss_newton_gedaempft.py`
- `exam-prova/Integration_boeing_romberg.py` = `Scripts/Kapitel_7/Integration_boeing_romberg.py`
- `exam-prova/Newton_system_gedaempft_3x3.py` = `Scripts/Kapitel_5/Newton_gedaempft.py`
- `exam-prova/Spline_natuerlich_vs_scipy.py` = `Scripts/Kapitel_6/Spline_natuerlich_vs_scipy.py`
- `exam-prova/DGL_methodenvergleich.py` = `Scripts/Kapitel_8/DGL_methodenvergleich.py`
- `exam-prova/DGL_rk4_vs_custom.py` = `Scripts/Kapitel_8/DGL_rk4_vs_custom.py`
- `exam-prova/Newton_system_hyperbeln.py` = `Scripts/Kapitel_5/Newton_systeme.py`
- `exam-prova/Integration_rakete_trapez.py` = `Scripts/Kapitel_7/Integration_rakete_kumulativ.py`
- `exam-prova/Ausgleichsrechnung_quadratisch_qr.py` = `Scripts/Kapitel_6/Ausgleichsrechnung_polynom_qr.py`
- `exam-prova/Ausgleichsrechnung_linearisiert_moore.py` = `Scripts/Kapitel_6/Ausgleichsrechnung_linearisiert.py`
- `exam-prova/Daten_gauss_newton.py` = `Scripts/Kapitel_6/Daten_gauss_newton.py`
- `Scripts/Kapitel_8/DGL_butcher_fs25.py` = `exam/Aufgabe6_runge_kutta_butcher.py`
