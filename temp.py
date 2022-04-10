data = 0
new_data = 0

from sklearn.cluster import KMeans

kmeans = KMeans(4)
kmeans.fit(data)
kmeans.predict(new_data)