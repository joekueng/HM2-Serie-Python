# HM2 Python

Struttura in stile HM1: script importanti direttamente nel top-level,
materiale completo in `Scripts/`, compiti d'esame in `exam/`, prove e
vecchi esercizi in `exam-prova/`.

## Script da aprire per primi

- `00_HM2_EXAM_SEARCH_INDEX.py`
- `S1_Flaechen_3D.py`
- `S1_Wellengleichung_3D.py`
- `Sympy_jacobian.py`
- `Sympy_linearisierung.py`
- `Nichtlineare_Gleichung_newton_1d.py`
- `Nichtlineare_Gleichungssysteme_newton.py`
- `Newton_minimum_contour.py`
- `Nichtlineare_Gleichungssysteme_newton_gedaempft.py`
- `Nichtlineare_Gleichungssysteme_newton_vereinfacht.py`
- `Ausgleichsrechnung_gauss_newton_gedaempft.py`
- `Ausgleichsrechnung_linear.py`
- `Ausgleichsrechnung_linearisiert.py`
- `Ausgleichsrechnung_minimi_quadrati_qr.py`
- `Ausgleichsrechnung_polynom_fit.py`
- `Interpolation_lagrange.py`
- `Interpolation_polynom_shift_plot.py`
- `Interpolation_spline_natuerlich.py`
- `Interpolation_spline_randbedingungen.py`
- `Integration_error_bounds.py`
- `Integration_trapez_tabelle_nichtaequidistant.py`
- `Integration_rakete_kumulativ.py`
- `Numerische_Integration_romberg_simpson.py`
- `DGL_euler_richtungsfeld.py`
- `DGL_euler_mittelpunkt_heun.py`
- `DGL_methodenvergleich.py`
- `DGL_system_euler_mittelpunkt.py`
- `DGL_boeing_midpoint_stopp.py`
- `DGL_rakete_rk4_vs_euler_mod.py`
- `DGL_runge_kutta_butcher_ordnung.py`
- `DGL_rk4_vs_custom.py`
- `DGL_stabilita_schrittweite.py`

## Come cercare durante l'esame

1. Apri `00_HM2_EXAM_SEARCH_INDEX.py`.
2. Cerca una parola del testo d'esame, per esempio `ohne Dämpfung`,
   `Romberg`, `Spline Randbedingungen`, `Butcher-Tableau`, `Richtungsfeld`.
3. Apri lo script indicato e cambia solo input, funzione, dati, start vector,
   intervallo, passo, Jacobiana o tableau.

## Cartelle

- `Scripts/Basics`: SymPy, plotting e operazioni base.
- `Scripts/Kapitel_5`: sistemi non lineari e Newton.
- `Scripts/Kapitel_6`: interpolazione, spline e Ausgleichsrechnung.
- `Scripts/Kapitel_7`: integrazione numerica.
- `Scripts/Kapitel_8`: DGL, Euler, Heun, Mittelpunkt, RK e Butcher.
- `exam`: script FS25 pronti da adattare.
- `exam-prova`: prove, vecchi esercizi e notebook secondari.

## Promozioni top-level intenzionali

Questi file esistono anche in `Scripts/`, ma sono copiati nel top-level per
non doverli cercare durante l'esame:

- `Sympy_jacobian.py`
- `Sympy_linearisierung.py`
- `Interpolation_polynom_shift_plot.py`
- `Ausgleichsrechnung_linear.py`
- `Ausgleichsrechnung_linearisiert.py`
- `Integration_trapez_tabelle_nichtaequidistant.py`
- `Integration_rakete_kumulativ.py`
- `DGL_methodenvergleich.py`
- `DGL_euler_mittelpunkt_heun.py`
- `DGL_euler_richtungsfeld.py`
- `DGL_rakete_rk4_vs_euler_mod.py`
- `DGL_rk4_vs_custom.py`

Il backup della vecchia struttura e nella cartella sibling
`HM2_Python_Exam_Package_backup_before_hm1_style_20260530_103806`.
