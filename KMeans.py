from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs


# Génération de données
X, y = make_blobs(n_samples=100, centers=3, cluster_std=0.4, random_state=0)
plt.scatter(X[:,0], X[:,1])
plt.show()

# Generation et entrainement du model
model = KMeans(n_clusters=3)
model.fit(X)
model.predict(X)
print(model.predict(X))

# affichage du resulta
plt.scatter(X[:,0], X[:,1], c=model.predict(X))
plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], c='r')
plt.show()
print("inertia =",model.inertia_)