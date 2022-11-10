import math
import numpy as np

class NewtonMethod:
  def __init__(self, func, df, ddf, x, n):
    self.func = func
    self.df = df
    self.ddf = ddf
    self.x = x
    self.n = n
    
    self.sub = {
      'ln' : np.log,
      'x' : self.x
    }

  def diff1(self):
    return self.df

  def diff2(self):
    return self.ddf
  
  def solve(self):
    for i in range(0, self.n):
      self.x = self.x - round(eval(self.df, self.sub), 2)/round(eval(self.ddf, self.sub), 2)
      print(f"----{i+1}----")
      print(eval(self.df, self.sub))
      print(eval(self.ddf, self.sub))
      print(f"x{i+1} = {self.x}")


soal1 = NewtonMethod("4*ln(x)-x", "(4/x)-1", "-1*(4/x**2)", 6, 3)

soal1.solve()