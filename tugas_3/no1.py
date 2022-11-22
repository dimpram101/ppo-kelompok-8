from prettytable import PrettyTable

def z(x1,x2):
  return 8*x1 + 6*x2

table = PrettyTable()

# menampilkan table untuk tableau
def refreshTable(basics = False, ratios = True):
  table.clear()
  table.field_names = ["z", "x1", "x2", "s1", "s2", "rhs", "ratio"]
  for x in b:
    table.add_row(x)
  
  # Menampilkan table dengan ratio
  if ratios == False:
    table.clear()
    table.field_names = ["z", "x1", "x2", "s1", "s2", "rhs"]
    for x in b:
      table.add_row(x[:-1])

  # Menampilkan table dengan basis
  if basics:
    basic = determineBasics()
    table._field_names.insert(0, "Basic")
    table._align["Basic"] = 'c'
    table._valign["Basic"] = 't'
    for i, _ in enumerate(table._rows):
      table._rows[i].insert(0, basic[i])

  print(table)

# menentukan basis dari kanonik
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

  return basic

class SimplexMethod:
  def __init__(self, b):
    self.b = b

    print("\033[31mKanonik\033[0m")
    refreshTable(ratios=False)
    print()
  
  # Mencari nilai paling kecil pada kanonik
  def findMinValue(self):
    minValue = []
    for x in self.b:
      minValue.append(min(x))

    return min(minValue)      

  def calculateTableau(self):
    refreshTable(True,True)
    minValue = self.findMinValue()
    key = 0 #key untuk mencari baris ratio terkecil
    index = 0 #posisi unsur kunci
    if minValue in self.b[0]:
      index = self.b[0].index(minValue)
      # menghitung ratio kanonik
      self.b[1][-1] = self.b[1][-2] / self.b[1][index]
      self.b[2][-1] = self.b[2][-2] / self.b[2][index]

      # mencari nilai ratio terkecil
      minRatio = min(self.b[1][-1], self.b[2][-1]) 
      # menentukan baris ratio terkecil
      key = 1 if minRatio in self.b[1] else 2
    elif minValue in self.b[1]:
      index = self.b[1].index(minValue)
      # menghitung ratio kanonik
      self.b[0][-1] = self.b[0][-2] / self.b[0][index]
      self.b[2][-1] = self.b[2][-2] / self.b[2][index]
      
      # mencari nilai ratio terkecil
      minRatio = min(self.b[0][-1], self.b[2][-1])
      # menentukan baris ratio terkecil
      key = 0 if minRatio in self.b[0] else 2
    elif minValue in self.b[2]:
      index = self.b[2].index(minValue)
      # menghitung ratio kanonik
      self.b[0][-1] = self.b[0][-2] / self.b[0][index]
      self.b[1][-1] = self.b[1][-2] / self.b[1][index]

      # mencari nilai ratio terkecil
      minRatio = min(self.b[0][-1], self.b[1][-1])
      # menentukan baris ratio terkecil
      key = 0 if minRatio in self.b[0] else 1
    
    print(f"\nKolom Kunci: Kolom-{index+2}, Unsur Kunci: {b[key][index]} (baris basic {determineBasics()[index]}), Ratio Terkecil: {minRatio}")
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
    print(f"b{x[key-1]} - {timesBy}b{key}")
    for i in range(len(self.b[key])-1):
      self.b[key-1][i] = self.b[key-1][i] - (timesBy*self.b[key][i])
    
    timesBy = self.b[key-2][index] #penentu pembentuk 0
    print(f"b{x[key-2]} - {timesBy}b{key}")
    for i in range(len(self.b[key])-1):
      self.b[key-2][i] = self.b[key-2][i] - (timesBy*self.b[key][i])

    self.clearRatio()
    refreshTable(True, False)

  #membuat seluruh nilai ratio menjadi 0
  def clearRatio(self):
    for i in range(len(self.b)):
      self.b[i][-1] = 0

  #mengecek apakah tabel kanonik beridentitas 1 untuk z, x1, x2
  def isKanonikIdentity(self):
    identity = [False, False, False]
    for i in range(len(self.b)):
      for j in range(3):
        if self.b[i][j] == 1 and (self.b[i-1][j] == 0 and self.b[i-2][j] == 0):
          identity[j] = True
    return all(identity)

  def solve(self):
    x1 = x2 = 0
    n = 1
    while True:
      print(f"\033[31mTableau {n}\033[0m")
      self.calculateTableau()
      print()
      # jika tabel kanonik beridentitas 1 untuk z,x1,x2 maka perulangan berhenti
      if self.isKanonikIdentity():
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