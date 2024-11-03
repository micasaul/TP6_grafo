# 14. Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:

from Grafo import Graph
from random import randint

grafo = Graph(dirigido=False)

# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
casa=["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2", "habitacion 1", "habitacion 2", "sala de estar", "terraza", "patio"]

for ambiente in casa:
    grafo.insert_vertice(ambiente)

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista 
# es la distancia entre los ambientes, se debe cargar en metros;
for ambiente in casa:
    adyacentes=[]
    cantidad_aristas = 5 if ambiente in ["sala de estar", "patio"] else 3
    while len(adyacentes)<cantidad_aristas:
        destino=casa[randint(0,len(casa)-1)]
        arista1=grafo.search_arista(destino, ambiente)
        arista2=grafo.search_arista(ambiente, destino)
        if destino!=ambiente and destino not in adyacentes and arista1 is None:
            adyacentes.append(destino)
    for destino in adyacentes:
        grafo.insert_arista(ambiente, destino, randint(3,20))

# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
cable=0

for nodo in grafo.kruskal("sala de estar")[0].split(';'):
    cable += int(nodo.split('-')[-1])
print(f"Se necesitan {cable} metros de cable")
print("")

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv.
camino=grafo.dijkstra("habitacion 1")
destino="sala de estar"
camino_completo=[]
peso=0
while camino.size()>0:
    ambiente= camino.pop()
    if ambiente[1][0] == destino:
        camino_completo.append(ambiente[1][0])
        peso+=ambiente[0]
        destino=ambiente[1][2]
camino_completo.reverse()        
print(f"El camino mas corto desde la habitacion 1 hasta la sala de estar es {camino_completo}, y {peso} metros de cable seran necesarios.")