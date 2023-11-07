import numpy as np
import pandas as pd
import json
import math
df = pd.read_csv('tmdb_5000_movies.csv')

#Genres, keywords, overview

genreObjects = df['genres'].tolist()
genres = []
keywordsObjects = df['keywords'].tolist()
keywords = []

for o in genreObjects:
    genres.append([])
    for genre in json.loads(o):
        genres[-1].append(genre["name"])

for o in keywordsObjects:
    keywords.append([])
    for keyword in json.loads(o):
        keywords[-1].append(keyword["name"])

overview = df['overview'].tolist()
print(genres)

titles = df['title'].tolist()
words = [genres[i] + keywords[i] for i in range(len(titles))]
# for i in range(len(titles)):
#     words.append([])
totWords = []
for row in words:
    totWords.extend(row)
totWords = list(set(totWords))

movie = input("Enter a movie name: ")
movieIndex = titles.index(movie)

def assignVectors(index):
    vector = []

    for word in totWords:
        wordCount = 0
        for wordArr in words:
            if word in wordArr:
                wordCount+=1
            
        tf = words[index].count(word)
        idf = math.log(len(titles) / wordCount)
        vector.append(tf * idf)
    return vector

assignVectors(movieIndex)




#tfidfvectorizer expects one string per "document"
# Transform the strings using TF-IDF
#Assume query is an existing movie in database
#If a user likes for example scream 3, recommend other movies like this
# Get TFIDF representation of Scream 3
#Compute similarity between Scream 3 and all other vectors
#Sort by similarity
#Print out top 5 closest movies



