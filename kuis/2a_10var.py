from numpy import matrix, linalg, random

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
    self.xyvector = [matrix([[self.x[i]], [self.y[i]]]) for i in range(len(self.x))]

  def determineDf(self):
    self.Df = [matrix([[f_dx(self.x[i], self.y[i])], [f_dy(self.x[i], self.y[i])]]) for i in range(len(self.x))]

  def determineH(self):
    self.H = [matrix([[f_dx_dx(self.x[i], self.y[i]), f_dx_dy(self.x[i], self.y[i])],
                      [f_dy_dx(self.x[i], self.y[i]), f_dy_dy(self.x[i], self.y[i])]]) for i in range(len(self.x))]
    self.inversH = [linalg.inv(self.H[i]) for i in range(len(self.H))]


  def determineNewVector(self):
    vctN = [self.xyvector[i] - self.inversH[i] * self.Df[i] for i in range(len(self.xyvector))]

    for i in range(len(self.x)):
      self.x[i] = vctN[i][0, 0]
      self.y[i] = vctN[i][1, 0]

  def showFandFx(self):
    for j in range(len(self.x)):
      print(f"x{j} = {self.x[j], self.y[j]}")
    df = [f(self.x[i], self.y[i]) for i in range(len(self.x))]
    print(f"f(x) = {df}")

  def solve(self, n):
    for i in range(n):
      print("==========================================")
      self.determineXyVector()
      self.determineDf()
      self.determineH()
      self.determineNewVector()
      self.showFandFx()




x = [random.randint(-5,5) for i in range(10)]
y = [random.randint(-5,5) for i in range(10)]

print("Newton : ")
newton = NewtonMethod(x,y)
newton.solve(10)