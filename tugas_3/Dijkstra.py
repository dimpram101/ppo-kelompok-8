from prettytable import PrettyTable

table = PrettyTable()
data = []
tableData = [
  [0,0,0,0,0],
]
field = ["C", "A", "B", "D", "E"]
firstCol = ["-", "-", "-", "-", "-"]

class Dijkstra:
  def __init__(self, graph, start, end):
    self.graph = graph
    self.start = start
    self.end = end

    self.distance = {}
    self.path = {}

    for dot in self.graph:
      self.distance[dot] = 99
      self.path[dot] = {}
    self.distance[self.start] = 0

    self.notVisited = [node for node in self.distance]

  def updateData(self, dic, i, cheapPoint):
    if i >= len(tableData) or i >= len(firstCol):
      tableData.append([0,0,0,0,0])
      firstCol.append('-')

    values = []
    for key, value in dic.items():
      values.append(value)
      index = field.index(key)
      tableData[i][index] = value
    
    if i == 0:
      firstCol[i] = self.start
    else:
      firstCol[i] = f"{data[i-1]}"
    data.append(cheapPoint)

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

  def findShortestPoint(self, distance, notVisited):
    lowestDistance = 99
    shortestPoint = ""
    for dot in distance:
      if dot in notVisited and distance[dot] <= lowestDistance:
        lowestDistance = distance[dot]
        shortestPoint = dot
    return shortestPoint

  def solve(self):
    shortPoint = self.findShortestPoint(self.distance, self.notVisited)

    n = 0
    while self.notVisited:
      dist = self.distance[shortPoint]
      
      destination = graph[shortPoint]
      for dot in destination:
        if self.distance[dot] > dist + destination[dot]:
          self.distance[dot] = dist + destination[dot]
          self.path[dot] = shortPoint
      
      self.notVisited.pop(self.notVisited.index(shortPoint))
      shortPoint = self.findShortestPoint(self.distance, self.notVisited)
      self.updateData(self.distance, n, shortPoint)
      self.updateTable()
      n+=1

    pathList = [self.end]
    i = 0
    while self.start not in pathList:
      pathList.append(self.path[pathList[i]])
      i += 1

    print(f"Jarak terpendek dari {self.start} menuju {self.end} adalah {self.distance[self.end]}")
    print(" -> ".join(reversed(pathList)))


graph = {
  "A" : {"B" : 3},
  "B" : {"D" : 5, "E" : 1},
  "C" : {"A" : 1, "B" : 7, "D" : 2},
  "D" : {"E" : 7},
  "E" : {"E" : 0}
}

dijsktra = Dijkstra(graph, "C", "E")
dijsktra.solve()