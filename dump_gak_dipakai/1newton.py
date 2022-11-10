import sympy as sp

sym = sp.symbols("x")

def f(x):
    return 4 * (sp.ln(x)) - x 
    # (4 * (np.log(x))) - x

def df(x):
    return sp.diff(f(x), x)
    # (4/x) - 1

def ddf(x):
    return sp.diff(df(x), x)
    # (-4/(x**2))

def newton(x, n):
    print(f"f(x) = {f(sym)}")
    print(f"f'(x) = {df(sym)}")
    print(f"f''(x) = {ddf(sym)}")

    print(f"x0 = {float(x)}")

    for i in range(0, n):
        x = x - (df(sym).subs(sym, x) / ddf(sym).subs(sym, x)) # Rumusnya debateable :v
        print(df(sym).subs(sym, x))
        print(f"x{i + 1} = {float(sp.N(x))}")

    max = f(sym).subs(sym, x)

    print(f"Nilai Maximumnya adalah {float(sp.N(max))}")

newton(6, 3)