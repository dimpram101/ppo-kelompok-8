from prettytable import PrettyTable

def z(x1,x2):
  return 8*x1 + 6*x2

table = PrettyTable()

def refreshTable():
  table.clear()
  table.field_names = ["z", "x1", "x2", "s1", "s2", "rhs", "ratio"]
  for x in b:
    table.add_row(x)
  print(table)

def refreshTableNoR():
  table.clear()
  table.field_names = ["z", "x1", "x2", "s1", "s2", "rhs"]
  for x in b:
    table.add_row(x[:-1])
  print(table)


class SimplexMethod:
  def __init__(self, b):
    self.b = b

    print("Kanonik")
    refreshTable()
    print()
  
  def findMinValue(self):
    minValue = []
    for x in self.b:
      minValue.append(min(x))

    return min(minValue)
  
  def calculateTableau(self):
    minValue = self.findMinValue()
    key = 0
    index = 0
    if minValue in self.b[0]:
      index = self.b[0].index(minValue)
      self.b[1][-1] = self.b[1][-2] / self.b[1][index]
      self.b[2][-1] = self.b[2][-2] / self.b[2][index]

      minRatio = min(self.b[1][-1], self.b[2][-1])
      key = 1 if minRatio in self.b[1] else 2
    elif minValue in self.b[1]:
      index = self.b[1].index(minValue)
      self.b[0][-1] = self.b[0][-2] / self.b[0][index]
      self.b[2][-1] = self.b[2][-2] / self.b[2][index]
      
      minRatio = min(self.b[0][-1], self.b[2][-1])
      key = 0 if minRatio in self.b[0] else 2
    elif minValue in self.b[2]:
      index = self.b[2].index(minValue)
      self.b[0][-1] = self.b[0][-2] / self.b[0][index]
      self.b[1][-1] = self.b[1][-2] / self.b[1][index]

      minRatio = min(self.b[0][-1], self.b[1][-1])
      key = 0 if minRatio in self.b[0] else 1
    
    refreshTable()
    self.obd(key,index)

  def obd(self, key, index):
    print("OBD")
    div = self.b[key][index]
    print(f"1/{div} * b{key}")
    for i in range(len(self.b[key])-1):
      self.b[key][i] = self.b[key][i]/div

    timesBy = self.b[key-1][index]
    print(f"b{key-1} - {timesBy}b{key}")
    for i in range(len(self.b[key])-1):
      self.b[key-1][i] = self.b[key-1][i] - (timesBy*self.b[key][i])
    
    timesBy = self.b[key-2][index]
    print(f"b{2 if key-2 == -1 else 0} - {timesBy}b{key}")
    for i in range(len(self.b[key])-1):
      self.b[key-2][i] = self.b[key-2][i] - (timesBy*self.b[key][i])

    refreshTableNoR()

  def clearRatio(self):
    for i in range(len(self.b)):
      self.b[i][-1] = 0


  def solve(self):
    x1 = x2 = 0
    n = 1
    while True:
      print(f"Tableau {n}")
      self.calculateTableau()
      print()

      if self.b[0][0] == 1 and self.b[1][1] == 1 and self.b[2][2] == 1:
        x1 = self.b[1][-2]
        x2 = self.b[2][-2]
        break
      
      n += 1
    
    print("Didapatkan : ")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    print(f"Z = {z(x1,x2)}")
 

b = [
  [1, -8, -6, 0, 0, 0, 0],
  [0, 4, 2, 1, 0, 60, 0],
  [0, 2, 4, 0, 1, 48, 0]
]

nomor1 = SimplexMethod(b)
nomor1.solve()