import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random
data= pd.read_csv('machinelearning/movies.csv')
impfeatures=['genres','keywords','tagline','cast', 'director']
for i in impfeatures:
    data[i]=data[i].fillna("")
combiningdata=data['genres']+" "+data['keywords']+" "+data['tagline']+" "+data['cast']+" "+data['director']
vector=TfidfVectorizer()
datavector=vector.fit_transform(combiningdata)
similarity=cosine_similarity(datavector)
listofmovies=data['title'].tolist()

class Recommend:
 
  def available():
    stream= random.sample(listofmovies, 10)
    return stream
  def run(viewd):
    name=viewd
    similarword=difflib.get_close_matches(name,listofmovies)
    correctword=similarword[0]
    findindex=data[data.title==correctword]['index'].values[0]
    similarity_bw_vector=list(enumerate(similarity[findindex]))
    closestmatches=sorted(similarity_bw_vector, key=lambda x: x[1], reverse=True) 
    suggest=[]
    i=1
    for detail in closestmatches:
        index=detail[0]
        moviename=data[data.index==index]["title"].values[0]
        if(i<6):
            suggest.append(moviename)
            i+=1
        else:
            break
    return suggest

