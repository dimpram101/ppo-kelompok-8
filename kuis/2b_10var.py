from numpy import matrix, linalg, random
import sympy as sp

def f(x,y):
  return ((2-x)**2) + (200*(y-x**2)**2)

def f_dx(x,y):
  return (800*x**3) + (2-800*y) * x - 4

def f_dy(x,y):
  return 400*(y-x**2)

class SteepestDescent:
  def __init__(self, x, y, t):
    self.x = x
    self.y = y
    self.t = t

    self.xyVector = None
    self.Df = None

  def determineXYVector(self):
    self.xyVector = [matrix([[self.x[i]], [self.y[i]]]) for i in range(len(self.x))]

  def determineDf(self):
    self.Df = [matrix([[f_dx(self.x[i], self.y[i])], [f_dy(self.x[i], self.y[i])]]) for i in range(len(self.x))]
  
  def updateXY(self):
    newXYVector = [self.xyVector[i] - self.t * self.Df[i] for i in range(len(self.x))]
    
    for i in range(len(self.x)):
      self.x[i] = newXYVector[i][0,0]
      self.y[i] = newXYVector[i][1,0]

  def determineT(self):
    t = sp.Symbol("t")
    
    xVector = [matrix([[self.x[i]], [self.y[i]]]) for i in range(len(self.x))]
    df = [matrix([[f_dx(self.x[i], self.y[i])], [f_dy(self.x[i], self.y[i])]]) for i in range(len(self.x))]
    formula = [xVector[i] - t * df[i] for i in range(len(xVector))]
    tMatrix = [matrix([[f_dx(formula[i][0,0], formula[i][1,0])], [f_dy(formula[i][0,0], formula[i][1,0])]]) for i in range(len(formula))]

    disambiguation = [(-tMatrix[i][0,0]) * df[i][0,0] + (-tMatrix[i][1,0]) * df[i][1,0] for i in range(len(tMatrix))]

    newT = float(sp.solveset(disambiguation, t).args[0])
    self.t = newT
    print(f"t = {self.t}")
    return newT

  def solve(self, n):

    print(f"x0 : ({self.x},{self.y})")
    print(f"t0 = {self.t}")
    for i in range(n):
      self.determineXYVector()
      self.determineDf()
      self.updateXY()
      self.determineT()
      print(f"x{i+1} : ({self.x},{self.y})")

x = [random.randint(-5,5) for i in range(10)]
y = [random.randint(-5,5) for i in range(10)]

std = SteepestDescent(x,y, 1/4)
std.solve(10)