# import pandas as pd
# import matplotlib.pyplot as plt
# import json

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
# df = pd.read_csv('tmdb_5000_movies.csv')
# df.head()


# x = df.iloc[0]

# x['genres']

# print(x['keywords'])

# j = json.loads(x['genres'])

# ' '.join(''.join(jj['name'].split()) for jj in j)

# def genres_and_keywords_to_string(row):
#   genres = json.loads(row['genres'])
#   genres = ' '.join(''.join(j['name'].split()) for j in genres)

#   keywords = json.loads(row['keywords'])
#   keywords = ' '.join(''.join(j['name'].split()) for j in keywords)
#   return "%s %s" % (genres, keywords)

# df['string'] = df.apply(genres_and_keywords_to_string, axis=1)

# tfidf = TfidfVectorizer(max_features=2000)

# X = tfidf.fit_transform(df['string'])

# movie2idx = pd.Series(df.index, index=df['title'])

# idx = movie2idx['Scream 3']
# query = X[idx]
# query.toarray()
# scores = cosine_similarity(query, X)
# scores = scores.flatten()
# plt.plot(scores)
# plt.show()