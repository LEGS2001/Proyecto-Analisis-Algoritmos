import json
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Recorre el archivo json de juegos y lo guarda en un dict
with open("juegos.json", "r") as f: 
    data = json.load(f)

# Arreglo con los Genres, specs y tags de todos los juegos
vector = []

# Arreglo de los nombres de todos los juegos
juegos = []

#IDEA: dar la lista y que el usuario ingrese el numero
#Recordar bajarle uno al index porque la lista empieza en 1

indice_juego = int(input("Ingrese el numero de juego con el que desea comprar (Use nombres.txt) \n"))
# num_juegos = int(input("Ingrese la cantidad de juegos similares que desea ver \n"))

for index, juego in enumerate(data):
    comparacion = []
    if "Genre" in juego:
        comparacion += juego["Genre"]
    if "specs" in juego:
        comparacion += juego["specs"] 
    if "tags" in juego:
        comparacion += juego["tags"] 
 
    vector.append(" ".join(comparacion))
    juegos.append(juego["Title"])

    if indice_juego - 1 == index:
        juego_actual = juego["Title"]

count_vectorizer = CountVectorizer(stop_words='english')
count_vectorizer = CountVectorizer()
matriz_dispersa = count_vectorizer.fit_transform(vector)
matriz = matriz_dispersa.todense()

comparaciones = {}
for index, elemento in enumerate(matriz):
    if juegos[index] != juego_actual:
        comparaciones[juegos[index]] = cosine_similarity(numpy.array(matriz[indice_juego - 1]), numpy.array(elemento))

for juego in (sorted(comparaciones, key=comparaciones.get, reverse=True)[:5]):
    print(juego, comparaciones[juego])

#palabras = set(palabras)
#with open("nombres.txt", "w", encoding='utf-8') as p: 
#    for palabra in juegos:
#        p.write(palabra + "\n")
