# 15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas
# y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
from Grafo import Graph
from random import randint

# f. deberá utilizar un grafo no dirigido.
grafo = Graph(dirigido=False)

# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
arquitectonicas=[
    {'nombre': 'Chichén Itzá', 'other_values': {'pais': 'México', 'tipo': 'arquitectónica'}},
    {'nombre': 'Cristo Redentor', 'other_values': {'pais': 'Brasil', 'tipo': 'arquitectónica'}},
    {'nombre': 'Machu Picchu', 'other_values': {'pais': 'Perú', 'tipo': 'arquitectónica'}},
    {'nombre': 'Gran Muralla China', 'other_values': {'pais': 'China', 'tipo': 'arquitectónica'}},
    {'nombre': 'Petra', 'other_values': {'pais': 'Jordania', 'tipo': 'arquitectónica'}},
    {'nombre': 'Coliseo', 'other_values': {'pais': 'Italia', 'tipo': 'arquitectónica'}},
    {'nombre': 'Taj Mahal', 'other_values': {'pais': 'India', 'tipo': 'arquitectónica'}}
]

naturales=[
    {'nombre': 'Amazonas', 'other_values': {'pais': 'Brasil', 'tipo': 'natural'}},
    {'nombre': 'Bahía de Ha-Long', 'other_values': {'pais': 'Vietnam', 'tipo': 'natural'}},
    {'nombre': 'Cataratas del Iguazú', 'other_values': {'pais': 'Argentina', 'tipo': 'natural'}},
    {'nombre': 'Isla Jeju', 'other_values': {'pais': 'Corea del Sur', 'tipo': 'natural'}},
    {'nombre': 'Parque Nacional de Komodo', 'other_values': {'pais': 'Indonesia', 'tipo': 'natural'}},
    {'nombre': 'Río Subterráneo de Puerto Princesa', 'other_values': {'pais': 'Filipinas', 'tipo': 'natural'}},
    {'nombre': 'Montaña de la Mesa', 'other_values': {'pais': 'Sudáfrica', 'tipo': 'natural'}}
]

for h in range (2):
    maravillas = arquitectonicas if h == 0 else naturales
    for maravilla in maravillas:
        grafo.insert_vertice(maravilla['nombre'], maravilla['other_values'])

# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
for h in range (2):
    maravillas = arquitectonicas if h == 0 else naturales
    for i in range(0, len(maravillas)-1):
        for j in range(i+1, len(maravillas)):
            grafo.insert_arista(maravillas[i]['nombre'], maravillas[j]['nombre'], randint(500, 20000))

# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
for h in range (2):
    maravillas = arquitectonicas if h == 0 else naturales
    for i in range(0, len(maravillas)-1):
        print(f"El arbol de expansion minimo de {maravillas[i]['nombre']} es {grafo.kruskal(maravillas[i]['nombre'])}")
print("")

# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
pais_arquitectonica= []
pais_natural= []
for h in range (2):
    maravillas = arquitectonicas if h == 0 else naturales
    pais= pais_arquitectonica if h == 0 else pais_natural
    for maravilla in maravillas:
        value=grafo.search_other(maravilla['nombre'], None)
        pais.append(value)

for i in pais_arquitectonica:
    for j in pais_natural:
        if i['pais']==j['pais']:
            print(f"En {i['pais']} existen maravillas arquitectonicas y naturales")
print("")

# e. determinar si algún país tiene más de una maravilla del mismo tipo;
for h in range (2):
    pais = pais_arquitectonica if h == 0 else pais_natural
    tipo = "arquitectonica" if h == 0 else "natural"    
    for i in range (0, len(pais)-1):
        for j in range (i+1, len(pais)):
            if pais[i]['pais']==pais[j]['pais']:
                print(f"En {pais[i]['pais']} hay mas de una maravilla {tipo}")
