from prettytable import PrettyTable
from sympy import *

def z(x1,x2):
  return 8*x1 + 6*x2

def fb1(x1, x2):
  return 4 * x1 + 2 * x2 <= 60

def fb2(x1, x2):
    return 2 * x1 + 4 * x2 >= 48

table = PrettyTable()
testa = ""
# menampilkan tableau
def refreshTable(basics = False, ratios = True):
  table.clear()
  table.field_names = ["z", "x1", "x2", "s1", "s2", "Y", "rhs", "ratio"]
  for x in b:
    table.add_row(x)
  
  # Menampilkan tableau dengan ratio
  if ratios == False:
    table.clear()
    table.field_names = ["z", "x1", "x2", "s1", "s2", "Y", "rhs"]
    for x in b:
      table.add_row(x[:-1])

  global basic
  # Menampilkan tableau dengan basis
  if basics:
    basic = determineBasics()
    table._field_names.insert(0, "Basic")
    table._align["Basic"] = 'c'
    table._valign["Basic"] = 't'
    for i, _ in enumerate(table._rows):
      table._rows[i].insert(0, basic[i])

  print(table)

# menentukan basis
def determineBasics():
  basicIndex = []
  basic = []
  for x in b:
    for i in range(len(x[:-2])):
      if x[i] == 1:
        basicIndex.append(x.index(x[i]))

  for x in basicIndex:
    if x == 0:
      basic.append("z")
    elif x == 1:
      basic.append("x1")
    elif x == 2:
      basic.append("x2")
    elif x == 3:
      basic.append("s1")
    elif x == 4: 
      basic.append("s2")
    elif x == 5:
      basic.append("Y")

  return basic

class SimplexMethod:
  def __init__(self, b):
    self.b = b
    self.x1 = 0
    self.x2 = 0

    print("\033[31mKanonik\033[0m")
    refreshTable(ratios=False)
    print()
  
  # Mencari nilai paling kecil pada b0
  def findMinValue(self):
    minValue = []
    minValueIndex = []
    for i,x in enumerate(self.b[0][:-2]):
      if x != 0: 
        minValue.append(str(x))  
        minValueIndex.append(i)
    listMinValue = []
    listMinValueIndex = []
    for i, y in enumerate(minValue):
      if y[0] == '-':
        newInt = ""
        for s in y:
          if s not in ['+', m, '*', 0]:
            newInt += s
          else:
            break
        listMinValue.append(float(newInt))
        listMinValueIndex.append(minValueIndex[i])
    columnKey = listMinValueIndex[listMinValue.index(min(listMinValue))]
    return columnKey
    
  #kalkulasi pada tableau
  def calculateTableau(self):
    refreshTable(True,True)
    print("\nMencari nilai Ratio dan Unsur Kunci")
    index = self.findMinValue()
    if self.b[1][index] > 0:
      self.b[1][-1] = self.b[1][-2] / self.b[1][index]
    else:
      print(f"{self.b[1][-2]} / {self.b[1][index]}, penyebut bernilai negatif (Diabaikan)")
    if self.b[2][index] > 0:
      self.b[2][-1] = self.b[2][-1] / self.b[2][index]
    else:
      print(f"{self.b[2][-2]} / {self.b[2][index]}, penyebut bernilai negatif (Diabaikan)")
    key = 2
    minRatio = self.b[2][-1]
    if self.b[1][index] != 0:
      if self.b[1][index] > self.b[2][index]:
        key = 1
    rowKey = 1
    minRatio = min(self.b[1][-1], self.b[2][-1])
    if self.b[1][-1] == 0:
      minRatio = self.b[2][-1]
      rowKey = 2
    elif self.b[2][-1] == 0:
      minRatio = self.b[1][-1]
      rowKey = 1
    
    print(f"Ratio terkecil : {minRatio} dengan Unsur Kunci : {self.b[rowKey][index]}")
    refreshTable(True,True)
    self.obd(key,index) #melakukan operasi baris dasar

  def obd(self, key, index):
    x = [0,1,2]
    print("\nOBD")
    div = self.b[key][index] #pembagi unsur kunci menjadi 1
    print(f"1/{div} * b{x[key]}")
    #membagi seluruh baris unsur kunci
    for i in range(len(self.b[key])-1):
      self.b[key][i] = self.b[key][i]/div

    timesBy = self.b[key-1][index] #penentu pembentuk 0
    print(f"b{x[key-1]} - ({timesBy}b{key})")
    for i in range(len(self.b[key])-1):
      self.b[key-1][i] = self.b[key-1][i] - (timesBy*self.b[key][i])
    
    timesBy = self.b[key-2][index] #penentu pembentuk 0
    print(f"b{x[key-2]} - ({timesBy}b{key})")
    for i in range(len(self.b[key])-1):
      self.b[key-2][i] = self.b[key-2][i] - (timesBy*self.b[key][i])

    self.clearRatio()
    refreshTable(True, False)

  #membuat seluruh nilai ratio menjadi 0
  def clearRatio(self):
    for i in range(len(self.b)):
      self.b[i][-1] = 0

  #mengecek apakah b0 tidak memiliki nilai negatif
  def b0NoNegative(self):
    negative = True
    minValue = []
    for x in self.b[0][:-2]:
      if x != 0: 
        minValue.append(str(x)) 
    for value in minValue:
      if value[0] == '-':
        negative = False
    return negative

  def flattenZ(self):
    for i in range(len(self.b[0])):
      self.b[0][i] = self.b[0][i] - m*self.b[2][i]

  def solve(self):
    n = 1
    self.flattenZ()
    while True:
        print(f"\033[31mTableau {n}\033[0m")
        self.calculateTableau()
        print()
        # jika tabel kanonik beridentitas 1 untuk z,x1,x2 maka perulangan berhenti
        if self.b0NoNegative():
          break
        n += 1
    if 'x1' in basic:
      self.x1 = self.b[1][-2]
    if 'x2' in basic:
      self.x2 = self.b[2][-2]
    print("Didapatkan : ")
    print(f"\tx1 = {self.x1}")
    print(f"\tx2 = {self.x2}")
    print(f"\tZ = {self.b[0][-2]}")

    print("Fungsi Batas : ")
    print(f"\tfb1({self.x1}, {self.x2}) = {fb1(self.x1, self.x2)}")
    print(f"\tfb2({self.x1}, {self.x2}) = {fb2(self.x1, self.x2)}")
    print(f"\tz({self.x1}, {self.x2}) = {z(self.x1, self.x2)}")
 
m = Symbol("M")
b = [
  [1, -8, -6, 0, 0, m, 0, 0],
  [0, 4, 2, 1, 0, 0, 60, 0],
  [0, 2, 4, 0, -1, 1, 48, 0]
]

nomor1 = SimplexMethod(b)
nomor1.solve()