from numpy import matrix

def f(x,y):
  return ((2-x)**2) + (200*(y-x**2)**2)

class PSO:
  def __init__(self, x, y, v, c, r, w):
    self.x = x
    self.y = y
    self.v = v
    self.c = c
    self.r = r
    self.w = w

    self.gBest = 0
    self.gBestY = 0
    self.pBest = []
    self.pBestY = []
    self.fxi = []
    self.v1 = [0,0,0]
    self.v1y = [0,0,0]
    self.oldX = [0,0,0]
    self.oldY = [0,0,0]
    
  #Step 2 menentukan F(xi)
  def determineFxi(self):
    self.fxi = [f(self.x[i], self.y[i]) for i in range(len(self.x))]
    # print(f"fxi : \n{self.fxi}")
    
  #step 3 Menentukan Gbest
  def determineGBest(self):
    self.gBest = self.x[self.fxi.index(min(self.fxi))]
    self.gBestY = self.y[self.fxi.index(min(self.fxi))]
    # print(f"gBestX : {self.gBest}")
    # print(f"gBestY : {self.gBestY}")

  #Step 4 Menentukan PBest 
  def determinePBest(self):
    if self.pBest == []: #untuk iterasi 1
      self.pBest = [x for x in self.x]
      self.pBestY = [y for y in self.y]
    else: #untuk iterasi selanjutnya
      for i in range(len(self.x)):
        if f(self.x[i], self.y[i]) <= f(self.oldX[i], self.oldY[i]):
          self.pBest[i] = self.x[i]
          self.pBestY[i] = self.y[i]
        else:
          self.pBest[i] = self.oldX[i]
          self.pBestY[i] = self.oldY[i]
    # print(f"pBestX : \n{self.pBest}")
    # print(f"pBestY : \n{self.pBestY}")
       
  
  #Step 5 Memperbaharui nilai v
  def updateV(self):
    for i in range(len(self.v1)):
      self.v1[i] = (self.w * self.v1[i]) + (self.c[0]*self.r[0]*(self.pBest[i] - self.x[i])) + (self.c[1]*self.r[1]*(self.gBest - self.x[i]))
      self.v1y[i] = (self.w * self.v1y[i]) + (self.c[0]*self.r[0]*(self.pBest[i] - self.y[i])) + (self.c[1]*self.r[1]*(self.gBest - self.y[i]))
    # print(f"v1x : \n{self.v1}")
    # print(f"v1y : \n{self.v1y}")

  #Step 6 Memperbaharui nilai x
  def updateX(self):
    for j in range(len(self.oldX)):
      self.oldX[j] = self.x[j]
      self.oldY[j] = self.y[j]
    for i in range(len(self.x)):
      self.x[i] = self.x[i] + self.v1[i]
      self.y[i] = self.y[i] + self.v1y[i]

  def showXandFx(self, i):
    print(f"x{i+1} : ", end="")
    for p in range(len(self.x)):
      print(f"{self.x[p], self.y[p]}", end="")
      if p == len(self.x) - 1:
        print()
      
    print(f"f(x) : ", end="")  
    for q in range(len(self.x)):
      print(f"({f(self.x[q], self.y[q])})", end="")
      if q == len(self.x) - 1:
        print()
    

  def solve(self, n):
    print(f"x0 : ", end="")
    for j in range(len(self.x)):
      print(f"{self.x[j], self.y[j]}", end="")
      if j == len(self.x) - 1:
        print()
    for i in range(n):
      print(f"=======================================================")
      self.determineFxi()
      self.determineGBest()
      self.determinePBest()
      self.updateV()
      self.updateX()

      self.showXandFx(i)
      

pso = PSO([1, 1, 0], [1, -1, 0], 0, [1, 1/2], [1, 1], 1)
pso.solve(3)