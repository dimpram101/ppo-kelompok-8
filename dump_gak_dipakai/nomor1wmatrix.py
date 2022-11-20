import numpy as np
from prettytable import PrettyTable

def z(x1,x2):
  return 8*x1 + 6*x2

table = PrettyTable()

b0 = [1, -8, -6, 0, 0, 0, 0]
b1 = [0, 4, 2, 1, 0, 60, 0]
b2 = [0, 2, 4, 0, 1, 48, 0]

def refreshTable():
  table.clear()
  table.field_names = ["z", "x1", "x2", "s1", "s2", "rhs", "ratio"]
  table.add_row(b0)
  table.add_row(b1)
  table.add_row(b2)
  print(table)

def calculate1stTableau():
  minimal = min(min(b0), min(b1), min(b2)) 
  index = 0
  if minimal in b0:
    index = b0.index(minimal)
    b1[-1] = b1[-2] / b1[index]
    b2[-1] = b2[-2] / b2[index]
    minRatio = min(b1[-1], b2[-1])
    key = 1 if minRatio in b1 else 2
    print(key)
  elif minimal in b1:
    index = b1.index(minimal)
    b0[-1] = b0[-2] / b0[index]
    b2[-1] = b2[-2] / b2[index]
  elif minimal in b2:
    index = b2.index(minimal)
    b0[-1] = b0[-2] / b0[index]
    b1[-1] = b1[-2] / b1[index]

         

  print("Tableau 1")
  refreshTable()

calculate1stTableau()