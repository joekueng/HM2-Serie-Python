import sympy as sp


def main():
    x = sp.symbols("x")
    function = sp.exp(-x**2) * sp.sin(x)

    derivative = sp.diff(function, x)
    second_derivative = sp.diff(function, x, 2)
    indefinite_integral = sp.integrate(sp.sin(x) ** 2, x)
    definite_integral = sp.integrate(sp.sin(x) ** 2, (x, 0, sp.pi))

    print("f(x) =")
    sp.pprint(function)
    print("\nf'(x) =")
    sp.pprint(sp.simplify(derivative))
    print("\nf''(x) =")
    sp.pprint(sp.simplify(second_derivative))
    print("\nIntegral sin(x)^2 dx =")
    sp.pprint(indefinite_integral)
    print("\nIntegral_0^pi sin(x)^2 dx =")
    sp.pprint(definite_integral)


if __name__ == "__main__":
    main()
