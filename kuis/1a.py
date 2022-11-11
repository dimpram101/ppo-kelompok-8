from math import sqrt

def f(x):
  return 1/3*sqrt(x**2 + 25)

def df(x):
  return x/(3*sqrt(x**2 + 25))

def ddf(x):
  return 25/(3*((x**2 + 25)**(3/2)))

class NewtonMethod:
  def __init__(self, x):
    self.x = x

  def solve(self, n):
    print(f"x0 = {self.x}")
    print(f"f(x) = {f(self.x)}")
    for i in range(n):
      print("=============================")
      self.x = self.x - (df(self.x)/ddf(self.x))
      print(f"x{i+1} = {self.x}")
    print(f"f(x) = {f(self.x)}")


nomor1a = NewtonMethod(1)
nomor1a.solve(100)