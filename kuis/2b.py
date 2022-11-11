from numpy import matrix, linalg

def f(x,y):
  return ((2-x)**2) + (200*(y-x**2)**2)

def f_dx(x,y):
  return (800*x**3) + (2-800*y) * x - 4

def f_dy(x,y):
  return 400*(y-x**2)

def f_dx_dx(x,y):
  return 2400*x**2 - 800*y + 2

def f_dx_dy(x,y):
  return -800*x

def f_dy_dx(x,y):
  return -800*x

def f_dy_dy(x,y):
  return 400

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
  
  def solve(self, n):
    print(f"x0 : ({self.x},{self.y})")
    for i in range(n):
      self.determineXYVector()
      self.determineDf()
      self.updateXY()
      print(f"x{i+1} : ({self.x},{self.y})")


std = SteepestDescent(1,1, 1/4)
std.solve(10)