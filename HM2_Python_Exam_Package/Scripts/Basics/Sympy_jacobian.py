import sympy as sp

x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)


f_a = sp.Matrix([
    5 * x1 * x2,
    x1**2 * x2**2 + x1 + 2 * x2
])

D_f_a = f_a.jacobian(sp.Matrix([x1, x2]))
D_f_a_at_point = D_f_a.subs({x1: 1, x2: 2})

print("D_f_a(x) =")
sp.pprint(D_f_a)


print("Aufgabe 2a:")

sp.pprint(D_f_a_at_point)


f_b = sp.Matrix([
    sp.log(x1**2 + x2**2) + x3**2,
    sp.exp(x2**2 + x3**2) + x1**2,
    1 / (x3**2 + x1**2) + x2**2
])

D_f_b = f_b.jacobian(sp.Matrix([x1, x2, x3]))
D_f_b_at_point = D_f_b.subs({x1: 1, x2: 2, x3: 3})

print("\nD_f_b(x) =")
sp.pprint(D_f_b)

print("\nAufgabe 2b:")
sp.pprint(sp.simplify(D_f_b_at_point))