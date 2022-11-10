import math
import numpy as np
import traceback

def f(x):
  return (4 * math.log(x) - x)

def df(x):
  return (4/x) - 1

def ddf(x):
  return (-4/(x**2))

def line():
  print("==========================")

# def newton(x, n):
#   print(f"x0 = {x}")
#   print(f"f(x) = {f(x)}")
#   line()  
#   for i in range(0, n):
#     x = x - (df(x)/ddf(x))
#     print(f"x{i+1} = {x}")
#     print(f"f(x) = {f(x)}")
#     line()

# print("Newton")
# newton(6, 9)

# def steepest(x, t, n):
#   print(f"x0 = {x}")
#   print(f"f(x) = {f(x)}")
#   line()
#   for i in range(0, n):
#     x = x - t * df(x)
#     print(f"x{i+1} = {x}")
#     print(f"f(x) = {f(x)}")
#     line()

# print("\nSteepest")
# steepest(6, 1/2, 10)

# def pso(f, x, c, r, w, v, n):
#   for i in range(0, n):
#     obj = f(x)

class NewtonMethod:
  def __init__(self, x, n):
    self.x = x
    self.n = n

  def solve(self):
    print(f"x0 = {self.x}")
    print(f"f(x) = {f(self.x)}")
    line()  
    for i in range(0, self.n):
      self.x = self.x - (df(self.x)/ddf(self.x))
      print(f"x{i+1} = {self.x}")
      print(f"f(x) = {f(self.x)}")
      line()

# print("Newton : ")
# newton = NewtonMethod(6, 3)
# newton.solve()

class SteepestDescent:
  def __init__(self, x, t, n):
    self.x = x
    self.t = t
    self.n = n
    
  def solve(self):
    print(f"x0 = {self.x}")
    print(f"f(x) = {f(self.x)}")
    line()
    for i in range(0, self.n):
      self.x = self.x - self.t * df(self.x)
      print(f"x{i+1} = {self.x}")
      print(f"f(x) = {f(self.x)}")
      line()

# print("\nSteepest Descent : ")
# steepest = SteepestDescent(6, 1/2, 3)
# steepest.solve()

class PSO:
  def __init__(self, x, v, c, r, w, n):
    self.x = x
    self.v0 = v
    self.c = c
    self.r = r
    self.w = w
    self.n = n

    self.gBest = 0
    self.pBest = []
    self.fxi = []
    self.v1 = [0,0,0]
    self.oldX = x
    self.test = x
    self.x_old = {
      'x0' : 0,
      'x1' : 0,
      'x2' : 0
    }

  #Step 2
  def determineFxi(self):
    self.fxi = [f(x) for x in self.x]
    
  #step 3
  def determineGBest(self):
    if self.fxi[0] >= self.fxi[1] and self.fxi[0] >= self.fxi[2]:
      self.gBest = self.x[0]
    elif self.fxi[1] >= self.fxi[0] and self.fxi[1] >= self.fxi[2]:
      self.gBest = self.x[1]
    elif self.fxi[2] >= self.fxi[0] and self.fxi[2] >= self.fxi[1]:
      self.gBest = self.x[2]

  #Step 4
  def determinePBest(self):
    if self.pBest == []:
      self.pBest = [x for x in self.x]
    else:
      for i in range(len(self.x)):
        if f(self.x[i]) >= f(self.x_old[f'x{i}']):
          self.pBest[i] = self.x[i]
        else:
          self.pBest[i] = self.x_old[f'x{i}']
  
  #Step 5
  def updateV(self):
    for i in range(len(self.v1)):
      # print(f"({self.w} * {self.v1[i]}) + ({self.c[0]}*{self.r[0]}*({self.pBest[i]} - {self.x[i]})) + ({self.c[1]}*{self.r[1]}*({self.gBest} - {self.x[i]}))")
      self.v1[i] = (self.w * self.v1[i]) + (self.c[0]*self.r[0]*(self.pBest[i] - self.x[i])) + (self.c[1]*self.r[1]*(self.gBest - self.x[i]))

  #Step 6
  def updateX(self):
    for i in range(len(self.x)):
      self.x_old[f'x{i}'] = self.x[i]
      self.x[i] = self.x[i] + self.v1[i]

  def solve(self):
    try:
      for i in range(self.n):
        print(f"{i+1}=======================================================")
        # print(self.x_old)
        self.determineFxi()
        # print(f"Fxi : {self.fxi}")
        self.determineGBest()
        # print(f"gBest : {self.gBest}")
        self.determinePBest()
        # print(f"pBest : {self.pBest}")
        self.updateV()
        # print(f"v : {self.v1}")
        self.updateX()
        print(f"oldX = {self.oldX}")
        print(f"x : {self.x}")
    except ZeroDivisionError:
      print("Pembagian nol di iterasi :", i)
    # except Exception as e:
    #   print(e)
    #   print("ALLAHU AKBAR")

print("\nPSO : ")
pso = PSO([1,2,6], 0, [1/2, 1], [1,1], 1, 10)
pso.solve()
