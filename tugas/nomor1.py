import math

def f(x):
  return (4 * math.log(x) - x)

def df(x):
  return (4/x) - 1

def ddf(x):
  return (-4/(x**2))

def line():
  print("==========================")

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

print("Newton : ")
newton = NewtonMethod(6, 3)
newton.solve()

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

print("\nSteepest Descent : ")
steepest = SteepestDescent(6, 1/2, 3)
steepest.solve()

class PSO:
  #Step 1
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
    self.oldX = [0,0,0]
    
  #Step 2
  def determineFxi(self):
    self.fxi = [f(x) for x in self.x]
    
  #step 3
  def determineGBest(self):
    self.gBest = self.x[self.fxi.index(max(self.fxi))]

  #Step 4
  def determinePBest(self):
    if self.pBest == []:
      self.pBest = [x for x in self.x]
    else:
      for i in range(len(self.x)):
        if f(self.x[i]) >= f(self.oldX[i]):
          self.pBest[i] = self.x[i]
        else:
          self.pBest[i] = self.oldX[i]
  
  #Step 5
  def updateV(self):
    for i in range(len(self.v1)):
      self.v1[i] = (self.w * self.v1[i]) + (self.c[0]*self.r[0]*(self.pBest[i] - self.x[i])) + (self.c[1]*self.r[1]*(self.gBest - self.x[i]))

  #Step 6
  def updateX(self):
    for i in range(len(self.x)):
      self.oldX[i] = self.x[i]
      self.x[i] = self.x[i] + self.v1[i]

  def solve(self):
    try:
      for i in range(self.n):
        print(f"{i+1}=======================================================")
        self.determineFxi()
        self.determineGBest()
        self.determinePBest()
        self.updateV()
        self.updateX()
        print(f"x : {self.x}")
    except ZeroDivisionError:
      print("Pembagian nol di iterasi :", i)

print("\nPSO : ")
pso = PSO([1,2,6], 0, [1/2, 1], [1,1], 1, 3)
pso.solve()
