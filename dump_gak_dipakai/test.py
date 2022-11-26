# from numpy import matrix, linalg
# import sympy as sp

# def f(x,y):
#   return (100*((y-0.01*x**2)**(1/2)))

# def f_dx(x,y):
#   return (-10*x)/((100*y-x**2)**(1/2))

# def f_dy(x,y):
#   return (500)/((100*y-x**2)**(1/2))

# class SteepestDescent:
#   def __init__(self, x, y, t):
#     self.x = x
#     self.y = y
#     self.t = t

#     self.xyVector = None
#     self.Df = None

#   def determineXYVector(self):
#     self.xyVector = matrix([[self.x], [self.y]])

#   def determineDf(self):
#     self.Df = matrix([[f_dx(self.x, self.y)], [f_dy(self.x, self.y)]])
  
#   def updateXY(self):
#     newXYVector = self.xyVector - self.t * self.Df
#     self.x = newXYVector[0,0]
#     self.y = newXYVector[1,0]

#   def determineT(self):
#     t = sp.Symbol("t")
    
#     xyVector = matrix([[self.x], [self.y]])
#     df = matrix([[f_dx(self.x, self.y)], [f_dy(self.x, self.y)]])
#     formula = xyVector - t * df
#     tMatrix = matrix([[f_dx(formula[0,0], formula[1,0])], [f_dy(formula[0,0], formula[1,0])]])

#     disambiguation = (-tMatrix[0,0]) * df[0,0] + (-tMatrix[1,0]) * df[1,0]

#     newT = float(sp.solveset(disambiguation, t).args[0])
#     self.t = newT
    
#     print(f"t = {self.t}")
#     return newT

#   def solve(self, n):

#     print(f"x0 : ({self.x},{self.y})")
#     for i in range(n):
#       print("======================")
#       self.determineXYVector()
#       self.determineDf()
#       self.updateXY()        
#       # self.determineT()
#       print(f"x{i+1} : ({self.x},{self.y})")
#       print(f"f(x) : {f(self.x, self.y)}")


# std = SteepestDescent(1,1, 0.25)
# std.solve(3)

# import random

# a = [[1,2,3,4,5], [2,1,6,9,3], [2,5, 1,7,4]]

# breaker = [False, False, False]

# for i in range(len(a)):
#   for j in range(3):
#     if a[i][j] == 1:
#       breaker[j] = True

# print(breaker)

# nodes = ('1', '2', '3', '4', '5', '6')

# distances = {
#  '1': {'1': 0, '2': int(input('enter distance from 1 to 2')), '4': int(input('enter distance from 1 to 4'))},
# '2': {'2': 0, '1': int(input('enter distance from 2 to 1')), '3':  int(input('enter distance from 2 to 3')), '4' : int(input('enter distance from 2 to 4')), '5':  int(input('enter distance from 2 to 5'))},
# '3': {'3': 0, '2': int(input('enter distance from 3 to 2')), '4': int(input('enter distance from 3 to 4')), '5': int(input('enter distance from 3 to 5')), '6':int(input('enter distance from 3 to 6'))},
# '4': {'4': 0, '1': int(input('enter distance from 4 to 1')), '2':int(input('enter distance from 4 to 2')), '3':int(input('enter distance from 4 to 3')), '5':int(input('enter distance from 4 to 5'))},
# '5': {'5': 0, '3': int(input('enter distance from 5 to 3')), '4': int(input('enter distance from 5 to 4')), '2':int(input('enter distance from 5 to 2')), '6':int(input('enter distance from 5 to 6'))},
# '6': {'6': 0, '3': int(input('enter distance from 6 to 3')), '5': int(input('enter distance from 6 to 5')), }

# }
# a=input('enter current')
# unvisited = {node: None for node in nodes} #using None as +inf
# visited = {}
# current = a
# currentDistance = 0
# unvisited[current] = currentDistance 

# while True:
#   for neighbour, distance in distances[current].items():
#     if neighbour not in unvisited: continue
#     newDistance = currentDistance + distance
#     if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
#         unvisited[neighbour] = newDistance
#   visited[current] = currentDistance
#   del unvisited[current]
#   if not unvisited: break
#   candidates = [node for node in unvisited.items() if node[1]]
#   current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

# print(visited)

test = {
  "A" : {"B" : "daw"},
  "B" : {"C" : "Daw"}
 }

print("A" in test)


#dijskra
con = True
temp = self.graph[self.start]
for x in range(len(colTemp)):
  if colTemp[x] in temp:
    temp = self.graph[colTemp[x]]
    con = True
  else:
    con = False

if i > 1:
  if not con:
    firstCol[i] = f"{firstCol[i-2]} -> {data[i-1]}"
  elif con and conTemp == False:
    firstCol[i] = f"{firstCol[i-1]} -> {data[i-1]}"
    conTemp = True
  elif con and conTemp == True:
    firstCol[i] = f"{firstCol[i-2]} -> {data[i-1]}"
    conTemp = False
else:
  firstCol[i] = f"{firstCol[i-i]} -> {data[i-1]}"