from math import sqrt
from numpy import random

def f(x):
  return 1/3*sqrt(x**2 + 25)

def df(x):
  return x/(3*sqrt(x**2 + 25))

class SteepestDescent:
  def __init__(self, x, t):
    self.x = x
    self.t = t

  def showFx(self):
    df = [f(x[i]) for i in range(len(self.x))]
    print(f"f(x) =",df)

  def solve(self, n):
    print(f"x0 = {self.x}")
    self.showFx()
    # print(f"f(x) = {f(self.x)}")
    for i in range(1, n+1):
      print("==========================")
      # Memperbaharui nilai x dengan menggunakan rumus x = xi + (t * f'(x))
      for j in range(len(self.x)):
        self.x[j] = self.x[j] - (self.t * df(self.x[j]))
      print(f"x{i} = {self.x}")
      self.showFx()

x = [random.randint(-5,5) for i in range(10)]

steepest = SteepestDescent(x,1/4)
steepest.solve(300)