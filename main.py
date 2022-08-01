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
nombre = "ARK: Survival Evolved"
num_juego = 0

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

    #if num_juego == index - 1:
        
    if juego["Title"] == "ARK: Survival Evolved":
        num_juego = index

count_vectorizer = CountVectorizer(stop_words='english')
count_vectorizer = CountVectorizer()
matriz_dispersa = count_vectorizer.fit_transform(vector)
matriz = matriz_dispersa.todense()

for index, elemento in enumerate(matriz):
    if juegos[index] != juegos[num_juego]:
        print(juegos[index], ": ", cosine_similarity(numpy.array(matriz[num_juego]), numpy.array(elemento)))



#palabras = set(palabras)
#with open("nombres.txt", "w", encoding='utf-8') as p: 
#    for palabra in juegos:
#        p.write(palabra + "\n")
