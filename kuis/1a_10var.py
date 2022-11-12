from math import sqrt
from numpy import random

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
    for h in range(len(self.x)):
      print(f"f(x) = {f(self.x[h])}")
    for i in range(n):
      print("=============================")
      for j in range(len(self.x)):
        self.x[j] = self.x[j] - (df(self.x[j])/ddf(self.x[j]))
      print(f"x{i+1} = {self.x}")
      for k in range(len(self.x)):
        print(f"f(x{k+1}) = {f(self.x[k])}")


x = [random.randint(-5, 5) for i in range(10)]
nomor1a = NewtonMethod(x)
nomor1a.solve(10)

# print(df(-0.4))
# print(ddf(-0.4))
# print(df(-0.4)/ddf(-0.4))