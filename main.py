import numpy as np
import pandas as pd
df = pd.read_csv('tmdb_5000_movies.csv')
df.head()
#tfidfvectorizer expects one string per "document"
# Transform the strings using TF-IDF
#Assume query is an existing movie in database
#If a user likes for example scream 3, recommend other movies like this
# Get TFIDF representation of Scream 3
#Compute similarity between Scream 3 and all other vectors
#Sort by similarity
#Print out top 5 closest movies



