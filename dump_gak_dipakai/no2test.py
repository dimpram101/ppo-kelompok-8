from tabulate import tabulate

class Dijkstra: #Kelas Metode Dijkstra
    #Inisiasi graf dan rute
    def __init__(self, start, end):
        self.nodes = ["A", "B", "C", "D", "E"] #Node graf

        self.graph = { #Graf atau arah Node dengan nilainya
            "A" : {"B" : 3},
            "B" : {"D" : 5, "E" : 1},
            "C" : {"A" : 1, "B" : 7, "D" : 2},
            "D" : {"E" : 7},
            "E" : {}
        }

        self.start = start #Node start (Dimulai)
        self.end = end #Node end (Dituju)

        self.unvisited = list(self.nodes) #Node yang belum dituju
        self.shortest = {} #Node dengan jarak terkecil
        self.previous = {} #Node sebelum jarak terkecil

        self.route = []

        self.headers = ["/"] + self.nodes

    #Menampilkan tabel
    def showTable(self, nodes):
        print(tabulate(nodes, self.headers, tablefmt="grid") + "\n")

    #Mencari koneksi antar node
    def connection(self, node):
        connections = []
        for outNode in self.nodes:
            if(self.graph[node].get(outNode, False) != False):
                 connections.append(outNode)
        return connections #Node yang terhubung dengan node parameter

    #Algoritma dijkstra
    def algorithm(self):
        maxValue = 99 #Nilai maksimum (infinity dimisalkan 99)
        for node in self.unvisited:
            self.shortest[node] = maxValue #Nilai setiap node yang belum dikunjungi adalah maximum
        self.shortest[self.start] = 0 #Nilai node dimulai adalah 0

        while self.unvisited: #Jika node telah dikunjungi maka perulangan akan berhenti
            currentMin = None
            for node in self.unvisited: #Perulangan untuk mencari node dengan nilai kecil
                tempRoute = []
                if(currentMin == None): #Jika node minimal adalah none
                    currentMin = node #Maka node minimal adalah node yang belum dikunjungi
                    tempRoute.append(node)
                    for i in range(len(self.shortest)):
                        tempRoute.append(self.shortest[self.nodes[i]])
                    self.route.append(tempRoute)
                    self.showTable(self.route) #Menampilkan tabel
                elif(self.shortest[node] < self.shortest[currentMin]): #Jika node yang belum dikunjungi lebih kecil dari node minimal
                    currentMin = node #Maka node minimal adalah node yang belum dikunjungi

            neighbors = self.connection(currentMin) #Mencari node yang terhubung
            for next in neighbors: #Perulangan untuk setiap node yang terhubung
                temporary = self.shortest[currentMin] + self.graph[currentMin][next] #Memperbarui nilai jarak
                if(temporary < self.shortest[next]): #Jika nilai jarak lebih kecil dari node yang terhubung
                    self.shortest[next] = temporary #Memperbarui nilai node jalur terkecil
                    self.previous[next] = currentMin
            self.unvisited.remove(currentMin) #Menghapus node yang telah dikunjungi

    #Menampilkan hasil jarak terkecil
    def result(self):
        self.algorithm() #Menjalankan algoritma dijkstra

        path = []
        node = self.end
        
        while(node != self.start): #Jika node adalah bukan node dimulai
            path.append(node)
            node = self.previous[node]
        
        path.append(self.start)

        print(f"Jarak terpendek ditemukan dengan jarak {self.shortest[self.end]}")
        print(" -> ".join(reversed(path)))

pp = Dijkstra("C", "E")
pp.result()