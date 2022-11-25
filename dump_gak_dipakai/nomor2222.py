from prettytable import PrettyTable

graph = {
  "A" : {"B" : 3},
  "B" : {"D" : 5, "E" : 1},
  "C" : {"A" : 1, "B" : 7, "D" : 2},
  "D" : {"E" : 7},
  "E" : {"E" : 0}
}
start = "C"
end = "E"
distance = {}
listDistance = []
titik = {}

tableData = [
  [0,0,0,0,0],
]
table = PrettyTable()
field = ['C', 'A', 'B', 'D', 'E']
firstCol = ["-", '-', '-', '-', '-']
data = []

def updateData(dic, i, cheapPoint):
  if i >= len(tableData) or i >= len(firstCol):
    tableData.append([0,0,0,0,0])
    firstCol.append('-')

  for key, value in dic.items():
      index = field.index(key)
      tableData[i][index] = value
  
  if i == 0:
    firstCol[i] = start
  else:
    firstCol[i] = f"{data[i-1]}"
  data.append(cheapPoint)

def updateTable():
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


for point in graph:
  distance[point] = 99
  titik[point] = {}
distance[start] = 0
# print(distance)
# print(titik)

def findCheapestPoint(distance, notVisited):
  lowestDist = 99
  cheapestPoint = ""

  for point in distance:
    if point in notVisited and distance[point] <= lowestDist:
      lowestDist = distance[point]
      cheapestPoint = point
  
  return cheapestPoint

notVisited = [node for node in distance]
cheapPoint = findCheapestPoint(distance, notVisited)

i = 0
while notVisited:
  dist = distance[cheapPoint]
  destinationDist = graph[cheapPoint]
  for dot in destinationDist:
    if distance[dot] > dist + destinationDist[dot]:
      distance[dot] = dist + destinationDist[dot]
      titik[dot] = cheapPoint

  notVisited.pop(notVisited.index(cheapPoint))
  cheapPoint = findCheapestPoint(distance, notVisited)
  updateData(distance, i, cheapPoint)
  updateTable()
  i += 1
  # print(distance)
alur = [end]

try:
  i = 0
  while start not in alur:
    alur.append(titik[alur[i]])
    i += 1

  jalur = ""
  print(f"jarak dari {start} ke {end} : {distance[end]}")
  for i,huruf in enumerate(alur[::-1]):
    if i == len(alur)-1:
      jalur += f" {huruf}"
    else:
      jalur += f" {huruf} ->"
  print(f"Alurnya adalah {jalur}")
except:
  print("Alur tidak dapat ditemukan")