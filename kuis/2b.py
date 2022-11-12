from numpy import matrix, linalg
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
    self.xyVector = matrix([[self.x], [self.y]])

  def determineDf(self):
    self.Df = matrix([[f_dx(self.x, self.y)], [f_dy(self.x, self.y)]])
  
  def updateXY(self):
    newXYVector = self.xyVector - self.t * self.Df
    self.x = newXYVector[0,0]
    self.y = newXYVector[1,0]

  def determineT(self):
    t = sp.Symbol("t")
    
    xyVector = matrix([[self.x], [self.y]])
    df = matrix([[f_dx(self.x, self.y)], [f_dy(self.x, self.y)]])
    formula = xyVector - t * df
    tMatrix = matrix([[f_dx(formula[0,0], formula[1,0])], [f_dy(formula[0,0], formula[1,0])]])

    disambiguation = (-tMatrix[0,0]) * df[0,0] + (-tMatrix[1,0]) * df[1,0]

    newT = round(float(sp.solveset(disambiguation, t).args[0]), 6)
    self.t = newT
    
    print(f"t = {self.t}")
    return newT

  def solve(self, n):

    print(f"x0 : ({self.x},{self.y})")
    print(f"f(x) : {f(self.x, self.y)}")
    for i in range(n):
      print("======================")
      self.determineXYVector()
      self.determineDf()
      self.determineT()
      self.updateXY()        
      print(f"x{i+1} : ({self.x},{self.y})")
      print(f"f(x) : {f(self.x, self.y)}")

std = SteepestDescent(1,1, None)
std.solve(3)