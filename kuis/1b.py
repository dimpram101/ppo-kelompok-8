from math import sqrt

def f(x):
  return 1/3*sqrt(x**2 + 25)

def df(x):
  return x/(3*sqrt(x**2 + 25))

class SteepestDescent:
  def __init__(self, x, t):
    self.x = x
    self.t = t

  def solve(self, n):
    print(f"x0 = {self.x}")
    # print(f"f(x) = {f(self.x)}")
    for i in range(1, n+1):
      print("==========================")
      # Memperbaharui nilai x dengan menggunakan rumus x = xi + (t * f'(x))
      self.x = self.x - (self.t * df(self.x))
      print(f"x{i} = {self.x}")
    print(f"f(x) = {f(self.x)}")

steepest = SteepestDescent(1,1/4)
steepest.solve(100)