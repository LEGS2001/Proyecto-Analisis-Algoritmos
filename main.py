import json
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import time
import random

def sacarMatriz():
    # Recorre el archivo json de juegos y lo guarda en un dict
    with open("juegos.json", "r") as f: 
        data = json.load(f)

    # Arreglo con los Genres, specs y tags de todos los juegos
    vector = []

    # Arreglo de los nombres de todos los juegos
    juegos = []

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

    count_vectorizer = CountVectorizer(stop_words='english')
    count_vectorizer = CountVectorizer()
    matriz_dispersa = count_vectorizer.fit_transform(vector)
    matriz = matriz_dispersa.todense()
    return juegos, matriz 

def recomendarJuegos(indice_juego, juegos, matriz):
    comparaciones = {}
    for index, elemento in enumerate(matriz):
        if juegos[index] != juegos[indice_juego - 1]:
            comparaciones[juegos[index]] = cosine_similarity(numpy.array(matriz[indice_juego - 1]), numpy.array(elemento))

    print("El juego actual es:", juegos[indice_juego - 1])
    for juego in (sorted(comparaciones, key=comparaciones.get, reverse=True)[:5]):
        print(juego, comparaciones[juego])

juegos, matriz = sacarMatriz()
start = time.time_ns()
for i in range(10000):
    print("Usuario:", i)
    num = random.randint(0, 23409)
    recomendarJuegos(num, juegos, matriz)
print("Tiempo de ejecucion: ", (time.time_ns() - start)/1000000000, "secs")


# 10 usuarios = 42.5313201 secs
# 100 usuarios = 445.2973613 secs
# 1000 usuarios = 4471.0025635 secs