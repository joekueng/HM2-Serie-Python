import sympy as sp

x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)

x = sp.Matrix([x1, x2, x3])

f = sp.Matrix([
    x1 + x2**2 - x3**2 - 13,
    sp.log(x2 / 4) + sp.exp(sp.Rational(1, 2) * x3 - 1) - 1,
    (x2 - 3)**2 - x3**3 + 7
])

x0 = sp.Matrix([
    sp.Rational(3, 2),
    3,
    sp.Rational(5, 2)
])

substitution_dictionary = {
    x1: x0[0],
    x2: x0[1],
    x3: x0[2]
}

function_value_at_x0 = f.subs(substitution_dictionary)
jacobian_matrix = f.jacobian(x)
jacobian_matrix_at_x0 = jacobian_matrix.subs(substitution_dictionary)

linearized_function = sp.simplify(
    function_value_at_x0 + jacobian_matrix_at_x0 * (x - x0)
)

print("f(x0) =")
sp.pprint(function_value_at_x0)

print("\nDf(x) =")
sp.pprint(jacobian_matrix)

print("\nDf(x0) =")
sp.pprint(jacobian_matrix_at_x0)

print("\nL(x) =")
sp.pprint(linearized_function)