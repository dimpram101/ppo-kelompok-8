from sympy import *
from prettytable import PrettyTable

table = PrettyTable()
m = Symbol("M")
headers = ["Basic", "Z", "x1", "x2", "s1", "s2", "Y", "Rhs", "Ratio"]

def z(x1, x2):
    return 8 * x1 + 6 * x2

def fb1(x1, x2):
    return 4 * x1 + 2 * x2 <= 60

def fb2(x1, x2):
    return 2 * x1 + 4 * x2 >= 48

def refreshTable():
  table.clear()
  table.field_names = headers
  table.add_rows(b)
  print(table)

class SimplexMethod:
  def __init__(self, b):
    self.b = b
    self.x1 = 0
    self.x2 = 0
    self.columnKey = 0
    self.rowKey = 0
    self.ratio = 0

  # Membuat baris Z (b0) menjadi konsisten dengan baris yang lainnya
  def flattenZ(self):
    for i in range(1, len(self.b[0][1:])):
      self.b[0][i] = self.b[0][i] - m*self.b[2][i]
    self.columnKey = 3

  # Mencari kolom kunci
  def findColumnKey(self):
    xCol = []
    minCol = []
    cKey = 0
    for row in self.b:
      minCol.clear()
      for i in range(1,6):
        minCol.append(row[i])
      xCol.append(min(x for x in minCol if x != 0))
    for i in range(len(self.b)):
      if (min(xCol) in self.b[i]):
        cKey = self.b[i].index(min(xCol))
    self.columnKey = cKey

  # Mencari nilai ratio dan unsur kunci
  def findRowKey(self):
    ratioCol = []
    for i in range(1,3):
      ratio = self.b[i][-2] / self.b[i][self.columnKey]
      self.b[i][-1] = ratio
      ratioCol.append(ratio)
    self.ratio = min(ratioCol)
    self.rowKey = ratioCol.index(min(r for r in ratioCol if r > 0)) + 1
    print(f"Ratio terkecil : {self.ratio}, dengan Unsur kunci : {self.b[self.rowKey][self.columnKey]},")

  # Operasi Baris Dasar
  def obd(self):
    def determineBasic():
      if (2 <= self.columnKey <= 3):
        self.b[self.rowKey][0] = f"x{self.rowKey}"
      elif (4 <= self.columnKey <= 5):
        self.b[self.rowKey][0] = f"s{self.rowKey}"
    key = self.b[self.rowKey][self.columnKey]
    for i in range(1, len(self.b[self.rowKey])-1):
      self.b[self.rowKey][i] = self.b[self.rowKey][i]/key
    determineBasic()
    for i in range(1, 3):
      timesBy = self.b[self.rowKey - i][self.columnKey]
      print(f"b{self.b.index(self.b[self.rowKey - i])} - ({timesBy}*b{self.rowKey})")
      for n in range(1, len(self.b[self.rowKey]) - 1):
        self.b[self.rowKey - i][n] = self.b[self.rowKey - i][n] - (timesBy * self.b[self.rowKey][n])
    for i in range(2):
      self.b[i-1][-1] = 0
      
  def run(self):
    print("Tableau 1")
    refreshTable()
    self.flattenZ()
    print("Mengkonsistenkan Baris Z")
    refreshTable()
    print("Mencari Ratio dan Unsur Kunci")
    self.findRowKey()
    refreshTable()
    print("OBD")
    self.obd()
    refreshTable()

    print("\nTableau 2")
    self.findColumnKey()
    self.findRowKey()
    refreshTable()
    print("\nMelakukan Operasi Baris Dasar")
    self.obd()
    refreshTable()
    
    print("\nTableau 3")
    self.findColumnKey()
    self.findRowKey()
    refreshTable()
    print("\nMelakukan Operasi Baris Dasar")
    self.obd()
    refreshTable()

    # Mengambil nilai x1 dan x2 dalam tableau
    for i in range(len(self.b)):
      if (self.b[i][0] == "x1"):
        self.x1 = self.b[i][7]
      elif(self.b[i][0] == "x2"):
        self.x2 = self.b[i][7]

    print("\nDidapatkan : ")
    print(f"Nilai maksimum dari Z adalah {self.b[0][-2]}")
    print(f"X1 = {self.x1}")
    print(f"X2 = {self.x2}")
    print("Fungsi Batas : ")
    print(f"\tfb1({self.x1}, {self.x2}) = {fb1(self.x1, self.x2)}")
    print(f"\tfb2({self.x1}, {self.x2}) = {fb2(self.x1, self.x2)}")
    print(f"\tz({self.x1}, {self.x2}) = {z(self.x1, self.x2)}")


b = [
  ["Z", 1, -8, -6, 0, 0, m, 0, 0],
  ["s1", 0, 4, 2, 1, 0, 0, 60, 0],
  ["Y", 0, 2, 4, 0, -1, 1, 48, 0]
]
simplex = SimplexMethod(b)
simplex.run()