from math import *
import numpy as np

def newton(func, funcd1, funcd2, x, n, decimal_count):
  dictNotations = {
    'ln': np.log,
    'x': x,
  }

  for i in range(0, n):
    eq1 = round(eval(funcd1, dictNotations),decimal_count)
    eq2 = round(eval(funcd2, dictNotations),decimal_count)
    h = x - round( float(eq1/eq2),decimal_count )
    x = h
    print(f"x{i} = {x}")
  print(f"Nilai Maximum: {eval(func, dictNotations)}")

newton("4*ln(x)-x", "(4/x)-1", "-1*(4/x**2)", 6, 3,12)