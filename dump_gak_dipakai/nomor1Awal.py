from prettytable import PrettyTable

def z(x1,x2):
  return 8*x1 + 6*x2

table = PrettyTable()
b = [
  [1, -8, -6, 0, 0, 0, 0],
  [0, 4, 2, 1, 0, 60, 0],
  [0, 2, 4, 0, 1, 48, 0]
]


def refreshTable():
  table.clear()
  table.field_names = ["z", "x1", "x2", "s1", "s2", "rhs", "ratio"]
  for x in b:
    table.add_row(x)
  print(table)

# print("Kanonik")
# refreshTable()


def findMinValue():
  minValue = []
  for x in b:
    minValue.append(min(x))

  return min(minValue)

def calculateTableau():
  minValue = findMinValue()
  key = 0
  index = 0
  if minValue in b[0]:
    index = b[0].index(minValue)
    b[1][-1] = b[1][-2] / b[1][index]
    b[2][-1] = b[2][-2] / b[2][index]

    minRatio = min(b[1][-1], b[2][-1])
    key = 1 if minRatio in b[1] else 2
  elif minValue in b[1]:
    index = b[1].index(minValue)
    print(index)
    b[0][-1] = b[0][-2] / b[0][index]
    b[2][-1] = b[2][-2] / b[2][index]
    
    minRatio = min(b[0][-1], b[2][-1])
    key = 0 if minRatio in b[0] else 2
  elif minValue in b[2]:
    index = b[2].index(minValue)
    print(index)
    b[0][-1] = b[0][-2] / b[0][index]
    b[1][-1] = b[1][-2] / b[1][index]
    minRatio = min(b[0][-1], b[1][-1])
    key = 0 if minRatio in b[2] else 1

  refreshTable()
  obd(key,index)

def obd(key, index):
  div = b[key][index]
  for i in range(len(b[key])-1):
    b[key][i] = b[key][i]/div

  timesBy = b[key-1][index]
  for i in range(len(b[key])-1):
    b[key-1][i] = b[key-1][i] - (timesBy*b[key][i])
  
  
  timesBy = b[key-2][index]
  for i in range(len(b[key])-1):
    b[key-2][i] = b[key-2][i] - (timesBy*b[key][i])

  refreshTable()

print("\nTableau 1")
calculateTableau()
print("\nTableau 2")
calculateTableau()

x1 = b[1][-2]
x2 = b[2][-2]
print(f"x1 = {x1}")
print(f"x2 = {x2}")

print(f"z = {z(x1,x2)}")