from numpy import log as ln

def f(x):
  return 4 * ln(x) - x

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
    for i in range(0, self.n):
      line()  
      #memperbaharui nilai x dengan menggunakan rumus xi - f'(x)/f''(x)
      self.x = self.x - (df(self.x)/ddf(self.x)) 
      print(f"x{i+1} = {self.x}")
    print(f"f(x) = {f(self.x)}")

print("Newton : ")
newton = NewtonMethod(6, 10)
newton.solve()

class SteepestDescent:
  def __init__(self, x, t, n):
    self.x = x
    self.t = t
    self.n = n
    
  def solve(self):
    print(f"x0 = {self.x}")
    print(f"f(x) = {f(self.x)}")
    for i in range(0, self.n):
      line()
      # Memperbaharui nilai x dengan menggunakan rumus x = xi + (t * f'(x))
      self.x = self.x + (self.t * df(self.x))
      print(f"x{i+1} = {self.x}")
    print(f"f(x) = {f(self.x)}")

print("\nSteepest Descent : ")
steepest = SteepestDescent(6, 1/2, 50)
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
    
  #Step 2 menentukan F(xi)
  def determineFxi(self):
    self.fxi = [f(x) for x in self.x]
    
  #step 3 Menentukan Gbest
  def determineGBest(self):
    self.gBest = self.x[self.fxi.index(max(self.fxi))]

  #Step 4 Menentukan PBest 
  def determinePBest(self):
    if self.pBest == []: #untuk iterasi 1
      self.pBest = [x for x in self.x]
    else: #untuk iterasi selanjutnya
      for i in range(len(self.x)):
        if f(self.x[i]) > f(self.oldX[i]):
          self.pBest[i] = self.x[i]
        else:
          self.pBest[i] = self.oldX[i]
  
  #Step 5 Memperbaharui nilai v
  def updateV(self):
    for i in range(len(self.v1)):
      self.v1[i] = (self.w * self.v1[i]) + (self.c[0]*self.r[0]*(self.pBest[i] - self.x[i])) + (self.c[1]*self.r[1]*(self.gBest - self.x[i]))

  #Step 6 Memperbaharui nilai x
  def updateX(self):
    for j in range(len(self.oldX)):
      self.oldX[j] = self.x[j]
    for i in range(len(self.x)):
      self.x[i] = self.x[i] + self.v1[i]

  def solve(self):
    print(f"x : {self.x}")
    print(f"f(x) = {f(self.x)}")
    for i in range(self.n):
      print(f"{i+1}=======================================================")
      self.determineFxi()
      self.determineGBest()
      self.determinePBest()
      self.updateV()
      self.updateX()
      print(f"x : {self.x}")
    print(f"f(x) = {f(self.x)}")

print("\nPSO : ")
pso = PSO([1,2,6], 0, [1/2, 1], [1,1], 1, 10)
pso.solve()
