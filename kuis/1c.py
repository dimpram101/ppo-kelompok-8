from math import sqrt

def f(x):
  return 1/3*sqrt(x**2 + 25)

def df(x):
  return x/(3*sqrt(x**2 + 25))

def ddf(x):
  return 25/(3*((x**2 + 25)**(3/2)))

class PSO:
  #Step 1
  def __init__(self, x, v, c, r, w):
    self.x = x
    self.v0 = v
    self.c = c
    self.r = r
    self.w = w

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
    self.gBest = self.x[self.fxi.index(min(self.fxi))]

  #Step 4 Menentukan PBest 
  def determinePBest(self):
    if self.pBest == []: #untuk iterasi 1
      self.pBest = [x for x in self.x]
    else: #untuk iterasi selanjutnya
      for i in range(len(self.x)):
        if f(self.x[i]) <= f(self.oldX[i]):
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

  def showFx(self):
    fx = [f(self.x[i]) for i in range(len(self.x))]
    print(f"f(x) = {fx}")

  def solve(self, n):
    print(f"x0 : {self.x}")
    for i in range(n):
      print(f"{i+1}=======================================================")
      self.determineFxi()
      self.determineGBest()
      self.determinePBest()
      self.updateV()
      self.updateX()
      print(f"x{i+1} : {self.x}")
      self.showFx()
      

print("PSO :")
pso = PSO([-1, 1.5, 2], 0, [1/2, 1], [1/2, 1/2], 1)
pso.solve(10)