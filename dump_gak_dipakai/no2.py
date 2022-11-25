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
titik = {}

for point in graph:
  distance[point] = 99
  titik[point] = {}
distance[start] = 0

def findCheapestPoint(distance, notVisited):
  lowestDist = 99
  cheapestPoint = ""

  for titik in distance:
    if titik in notVisited and distance[titik] <= lowestDist:
      lowestDist = distance[titik]
      cheapestPoint = titik
  
  return cheapestPoint

notVisited = [node for node in distance]
cheapPoint = findCheapestPoint(distance, notVisited)

while notVisited:
  print(distance)
  dist = distance[cheapPoint]
  # print(dist)
  destinationDist = graph[cheapPoint]
  for dot in destinationDist:
    if distance[dot] > dist + destinationDist[dot]:
      distance[dot] = dist + destinationDist[dot]
      titik[dot] = cheapPoint

  notVisited.pop(notVisited.index(cheapPoint))
  cheapPoint = findCheapestPoint(distance, notVisited)

alur = [end]

i = 0
while start not in alur:
  alur.append(titik[alur[i]])
  i += 1
print(titik)
print("distance :", distance)
print(f"jarak dari {start} ke {end} : {distance[end]}")
print(f"Alurnya adalah {alur[::-1]}")