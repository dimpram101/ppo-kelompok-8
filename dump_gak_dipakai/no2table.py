from prettytable import PrettyTable

tableData = [
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0],
  [0,0,0,0,0]
]
field = ['A', 'B', 'C', 'D', 'E']
graph = {
  "A" : {"B" : 3},
  "B" : {"D" : 5, "E" : 1},
  "C" : {"A" : 1, "B" : 7, "D" : 2},
  "D" : {"E" : 7},
  "E" : {"E" : 0}
}
start = "C"
end = "E"

table = PrettyTable()
firstCol = [start, "-", "-", "-", "-"]

def refreshTable():
  table.clear()
  table.field_names = field
  table.add_rows(tableData)

  table._field_names.insert(0, "/")
  table._align["/"] = 'c'
  table._valign["/"] = 't'
  for i, _ in enumerate(table._rows):
    table._rows[i].insert(0, firstCol[i])
  print(table)

def updateTable(i):
  table.clear()
  table.field_names = field
  for n in range(4):
    table.add_row(tableData[n])
  
  table._field_names.insert(0, "/")
  table._align["/"] = 'c'
  table._valign["/"] = 't'
  for n in range(4):
    table._rows[n].insert(0, firstCol[n])
  print(table)

distance = {}
titik = {}
notVisited = [node for node in distance]

for point in graph:
  distance[point] = 99
  titik[point] = {}
distance[start] = 0


it=0
for i in range(len(tableData)):
  new = []

  for key, value in graph[start].items():
    new.append(value)
    tableData[it][field.index(key)] = value
  for key in graph[start]:
    if graph[start][key] == min(new):
      if i > 0:
        firstCol[i] = f"{firstCol[i-1]} {start}"
      start = key
      break
  updateTable(i)
  it+=1

# refreshTable()