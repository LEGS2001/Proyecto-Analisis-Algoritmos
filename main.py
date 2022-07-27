import json
import random
from scipy.spatial import distance
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

with open("juegos.json", "r") as f: 
    data = json.load(f)

comparar = data[0]["Genre"] + data[0]["specs"] + data[0]["tags"]

#palabras = []

vector = []
juegos = []
for juego in data:
    comparacion = []
    if "Genre" in juego:
        comparacion += juego["Genre"]
        #palabras += juego["Genre"]
    if "specs" in juego:
        comparacion += juego["specs"] 
        #palabras += juego["specs"]
    if "tags" in juego:
        comparacion += juego["tags"] 
        #palabras += juego["tags"]

    
    vector.append(" ".join(comparacion))
    juegos.append(juego["Title"])

count_vectorizer = CountVectorizer(stop_words='english')
count_vectorizer = CountVectorizer()
sparse_matrix = count_vectorizer.fit_transform(vector)

doc_term_matrix = sparse_matrix.todense()

print(doc_term_matrix[9])
df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names_out(), 
                  index=juegos)

#palabras = set(palabras)
#with open("palabras.txt", "w") as p: 
#    for palabra in palabras:
#        p.write(palabra + "\n")
