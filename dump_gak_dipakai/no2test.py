from tabulate import tabulate


class Dijkstra:
    def __init__(self, start, end):
        self.nodes = ["A", "B", "C", "D", "E"]

        self.graph = {
            "A": {"B": 3},
            "B": {"D": 5, "E": 1},
            "C": {"A": 1, "B": 7, "D": 2},
            "D": {"E": 7},
            "E": {}
        }

        self.start = start
        self.end = end

        self.unvisited = list(self.nodes)
        self.shortest = {}
        self.previous = {}

        self.route = []

        self.headers = ["/"] + self.nodes

    def showTable(self, nodes):
        print(tabulate(nodes, self.headers, tablefmt="grid"))

    def connection(self, node):
        connections = []
        for outNode in self.nodes:
            if (self.graph[node].get(outNode, False) != False):
                connections.append(outNode)
        print(connections)
        return connections

    def algorithm(self):
        maxValue = 99
        for node in self.unvisited:
            self.shortest[node] = maxValue
        self.shortest[self.start] = 0

        while self.unvisited:
            currentMin = None
            for node in self.unvisited:
                tempRoute = []
                if (currentMin == None):
                    currentMin = node

                    tempRoute.append(node)
                    for i in range(len(self.shortest)):
                        tempRoute.append(self.shortest[self.nodes[i]])
                    self.route.append(tempRoute)
                    self.showTable(self.route)

                elif (self.shortest[node] < self.shortest[currentMin]):
                    currentMin = node

            neighbors = self.connection(currentMin)
            for next in neighbors:
                temporary = self.shortest[currentMin] + \
                    self.graph[currentMin][next]
                if (temporary < self.shortest[next]):
                    self.shortest[next] = temporary
                    self.previous[next] = currentMin

            self.unvisited.remove(currentMin)

    def result(self):
        self.algorithm()

        path = []
        node = self.end

        while (node != self.start):
            path.append(node)
            node = self.previous[node]

        path.append(self.start)

        print(f"Jarak terpendek ditemukan dengan jarak {self.shortest[self.end]}")
        print(" -> ".join(reversed(path)))


pp = Dijkstra("C", "E")
pp.result()
