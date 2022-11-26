from prettytable import PrettyTable

#variabel yang berhubungan dengan tabel
table = PrettyTable()
data = []
tableData = [
  [0,0,0,0,0],
]
field = ["C", "A", "B", "D", "E"]
firstCol = ["-"]
lowestTemp = 0
class Dijkstra:
  def __init__(self, graph, start, end):
    self.graph = graph
    self.start = start
    self.end = end
    
    self.distance = {} #jarak antar titik
    self.path = {} #rute yang digunakan

    #membuat distance setiap titik menjadi 99 (infinite)
    for dot in self.graph:
      self.distance[dot] = 99
      self.path[dot] = {}
    self.distance[self.start] = 0

    self.notVisited = [node for node in self.distance]

  #meng-update data untuk ditampilkan di table
  def updateData(self, dic, i, cheapPoint):
    global lowestTemp

    if i >= len(tableData) or i >= len(firstCol):
      tableData.append([0,0,0,0,0])
      firstCol.append('-')
    tempVal = 0
    for key, value in dic.items():
      index = field.index(key)
      if value == lowestDist:
        value = f"\033[31m{value}\033[0m"
        tempVal = value
      tableData[i][index] = value
    
    if i == 0:
      firstCol[i] = self.start
    else:
        if i > 1:
          if tableData[i].index(tempVal) == 0:
            firstCol[i] = f"{firstCol[i-1]} -> {data[i-1]}"
          elif tableData[i].index(tempVal) < lowestTemp:
            firstCol[i] = f"{firstCol[i-2]} -> {data[i-1]}"
          else:
            firstCol[i] = f"{firstCol[i-2]} -> {data[i-1]}"
        else:
          firstCol[i] = f"{firstCol[i-1]} -> {data[i-1]}"
    data.append(cheapPoint)
    lowestTemp = tableData[i].index(tempVal)

  #menampilkan table
  def updateTable(self):
    table.clear()
    table.field_names = field
    for x in tableData:
      table.add_row(x)
    table._field_names.insert(0, "/")
    table._align["/"] = 'c'
    table._valign["/"] = 't'
    for i,x in enumerate(table._rows):
      table._rows[i].insert(0, firstCol[i])
    print(table)

  #fungsi untuk mencari titik terdekat berdasarkan jarak antar titik
  def findShortestPoint(self, distance, notVisited):
    lowestDistance = 99
    shortestPoint = ""
    for dot in distance:
      if dot in notVisited and distance[dot] <= lowestDistance:
        lowestDistance = distance[dot]
        shortestPoint = dot
        
    global lowestDist
    lowestDist = lowestDistance 
    return shortestPoint

  def solve(self):
    shortPoint = self.findShortestPoint(self.distance, self.notVisited)
    n = 0
    #melakukan perulangan selama notVisited belum kosong
    while self.notVisited:
      dist = self.distance[shortPoint]
      destination = graph[shortPoint]
      for dot in destination:
        #membandingkan jarak antar titik
        if self.distance[dot] > dist + destination[dot]:
          self.distance[dot] = dist + destination[dot]
          self.path[dot] = shortPoint
      self.notVisited.pop(self.notVisited.index(shortPoint))
      shortPoint = self.findShortestPoint(self.distance, self.notVisited)
      self.updateData(self.distance, n, shortPoint)
      self.updateTable()
      n+=1

    try:
      #Mencari rute berdasarkan susunan rute terpendek yang telah dihitung
      pathList = [self.end]
      i = 0
      while self.start not in pathList:
        pathList.append(self.path[pathList[i]])
        i += 1

      print(f"Jarak terpendek dari {self.start} menuju {self.end} adalah {self.distance[self.end]}")
      print(" -> ".join(reversed(pathList)))
    except:
      #Jika saat mencari rute menemukan kesalahan, artinya titik awal tidak memiliki akses ke titik akhir
      #melalui titik manapun
      print("Alur tidak ditemukan!")

graph = {
  "A" : {"B" : 3},
  "B" : {"D" : 5, "E" : 1},
  "C" : {"A" : 1, "B" : 7, "D" : 2},
  "D" : {"E" : 7},
  "E" : {"E" : 0}
}

dijsktra = Dijkstra(graph, "C", "E")
dijsktra.solve()