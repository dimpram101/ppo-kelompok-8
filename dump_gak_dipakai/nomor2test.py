# import math

# mulai = "C"

# graph = {
#   "A" : {"B" : 3},
#   "B" : {"D" : 5, "E" : 1},
#   "C" : {"B" : 7, "D" : 2},
#   "D" : {"E" : 7},
#   "E" : {"E" : 0}
# }

# jarak = {}
# posisi = {}

# for node in graph:
#   jarak[node] = 99
#   posisi[node] = {}

# jarak[mulai] = 0

# print(graph)
# print("\n")
# print(jarak)

infinity = float("infinity")
mulai = "C"     # lokasi awal
berhenti = "E"  # lokasi tujuan

# graph atau titik lokasi direpresentasikan dengan menggunakan dictionary di dalam dictionary,
lokasi = {
  "A" : {"B" : 3},
  "B" : {"D" : 5, "E" : 1},
  "C" : {"A" : 1, "B" : 7, "D" : 2},
  "D" : {"E" : 7},
  "E" : {"E" : 0}
}


distance = {}                   # distance = jarak yg perlu ditempuh
city = {}                 # city = data lokasi, Situbondo, Bondowoso, Banyuwangi, Jember
for node in lokasi:          # looping data pendefinisian lokasi
    # print('Lokasi:', node) # debug
    distance[node] = infinity   # inisialisasi dist dengan nilai infinity (anggapannya node ini blm di kunjungi)
    city[node] = {}       # inisialisasi parent tanpa node {}
 
distance[mulai] = 0             # atur jarak pertama dengan nilai 0

def find_cheapest_node(distance, not_checked):                     # algoritma untuk mencari nilai node yang memiliki jarak terpendek
    lowest_dist = infinity                                      # katakanlah lowest_dist = infinity, artinya lowest_dist nya memiliki nilai awal maksimal/infinity.
    cheapest_node = ""                                          # cheapest_node kosong
    for node in distance:                                          # looping node untuk setiap distance
        if node in not_checked and distance[node] <= lowest_dist:  # check apakah node belum pernah dikunjungi / not_checked dan biaya/jarak untuk node ini lebih kecil dari lowest_dist.
            lowest_dist = distance[node]                           # lowest dist ditemukan dengan node sekarang.
            cheapest_node = node                                # set nilai cheapest_node dengan node yang sekarang.
 
    return cheapest_node                                        # mengembalikan nilai node dengan jarak paling kecil
 
### 
### Algoritma Dijkstra
###

not_checked = [node for node in distance]                          # not_checked = unvisited nodes. / node yang blm pernah di check.
node = find_cheapest_node(distance, not_checked)              # cari jarak minimal dari distance[mulai]. nilai ini berdasarkan variable awal yang ada di atas.
while not_checked:                                              # me-looping ketika semua nodes blm di cekprint(distance)
    print(distance)
    dist = distance[node]                                          # jarak untuk node yang sekarang.
    print(dist)
    child_dist = lokasi[node]                                   # list jarak untuk node yang terhubung oleh node yg sekarang dalam perulangan dan akan dikunjungi.
    for c in child_dist:                                        # looping untuk setiap koneksi pada node ini
        if distance[c] > dist + child_dist[c]:                     # apabila jarak koneksi lebih dari dengan nilai dist + child_dist[c]
            distance[c] = dist + child_dist[c]                     # mengubah nilai distance[c] dengan nilai dist ditambah dengan jarak konesi ke child lainya.
            city[c] = node                                   # mengubah nilai city[c] dengan node sekarang

    not_checked.pop(not_checked.index(node))                    # menghapus nilai node sekarang dari antrian not_checked (karena node ini sudah di cek)
    node = find_cheapest_node(distance, not_checked)               # set nilai node lagi dengan cara mencari jarak terkecil dengan list not_checked yang terbaru
enter = " "
print (enter)
print(f"Jarak tempuh terpendek dari {mulai} ke {berhenti} sejauh {distance[berhenti]} km!") #mencetak total jarak terefisien dari titik mulai ke titik henti

print(distance)
# bagian percetakan rute terefisien
if distance[berhenti] < infinity:                                  # apabila nilai jarak kurang dari infinity, maka alur pasti ditemukan
    alur = [berhenti]
    i = 0
    while mulai not in alur:
        alur.append(city[alur[i]])
        i += 1

    barrier =  ">"
    print (barrier*50)
    print(f"Alur nya adalah {alur[::-1]}")
else:
    print("Alur tidak dapat ditemukan")