import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs
from sklearn.cluster import KMeans


plt.rcParams["figure.figsize"] = (12, 5)
plt.rcParams['figure.titlesize'] = 'large'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize']=15


np.random.seed(0)

batch_size = 45
centers = [[1, 1], [-1, -1], [1, -1]]
n_clusters = len(centers)
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.7)

#Cálculo de 4 Cluster
kmeans_1 = KMeans(n_clusters=4, random_state=42)
K_4=kmeans_1.fit_predict(X)

#Cálculo de 6 Cluster
kmeans_2 = KMeans(n_clusters=6, random_state=42)
K_6=kmeans_2.fit_predict(X)


y0 = np.choose(labels_true, ['b', 'g', 'r']).astype(np.object)
y1 = np.choose(K_4, ['b', 'g', 'r','y']).astype(np.object)
y2 = np.choose(K_6, ['b', 'g', 'r','y','k','c']).astype(np.object)


plt.subplot(2,2,1)
plt.scatter(X[:,0],X[:,1],c='b')
#plt.title("Gráfica de dos variables")
plt.ylabel("Segunda Variable")
plt.xlabel("Primera Variable")

plt.subplot(2,2,2)
plt.scatter(X[:,0],X[:,1],c=y0)
#plt.title("Gráfica de dos variables")
plt.ylabel("Segunda Variable")
plt.xlabel("Primera Variable")


plt.subplot(2,2,3)
plt.scatter(X[:,0],X[:,1],c=y1)
#plt.title("Gráfica de dos variables")
plt.ylabel("Segunda Variable")
plt.xlabel("Primera Variable")

plt.subplot(2,2,4)
plt.scatter(X[:,0],X[:,1],c=y2)
#plt.title("Gráfica de dos variables")
plt.ylabel("Segunda Variable")
plt.xlabel("Primera Variable")

plt.show()
