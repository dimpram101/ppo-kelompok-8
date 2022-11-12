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

class NewtonMethod:
  def __init__(self, x, y):
    self.x = x
    self.y = y

    self.xyvector = None
    self.Df = None
    self.H = None
    self.inversH = None

  def determineXyVector(self):
    self.xyvector = matrix([[self.x], [self.y]])

  def determineDf(self):
    self.Df = matrix([[f_dx(self.x, self.y)], [f_dy(self.x, self.y)]])
    print(f"Df = \n {self.Df}")

  def determineH(self):
    self.H = matrix([[f_dx_dx(self.x, self.y), f_dx_dy(self.x, self.y)],
                      [f_dy_dx(self.x, self.y), f_dy_dy(self.x, self.y)]])
    self.inversH = linalg.inv(self.H)
    print(f"H = \n{self.H}")
    print(f"H^-1 = \n{self.inversH}")


  def determineNewVector(self):
    vctN = self.xyvector - self.inversH * self.Df

    self.x = vctN[0, 0]
    self.y = vctN[1, 0]

  def solve(self, n):
    print(f"x0 = ({self.x},{self.y})")
    print(f"f(x) = {f(self.x, self.y)}")
    for i in range(n):
      print("==========================================")
      self.determineXyVector()
      self.determineDf()
      self.determineH()
      self.determineNewVector()

      print(f"x{(i+1)} = ({self.x},{self.y})")
      print(f"f(x) = {f(self.x,self.y)}")

print("Newton : ")
newton = NewtonMethod(1,1)
newton.solve(3)