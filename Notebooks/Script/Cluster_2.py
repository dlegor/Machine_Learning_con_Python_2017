import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

plt.rcParams["figure.figsize"] = (12, 5)
plt.rcParams['figure.titlesize'] = 'large'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize']=15

np.random.seed(0)

batch_size = 45
centers = [[1, 1], [-1, -1], [1, -1]]
n_clusters = len(centers)
X, labels_true = make_blobs(n_samples=3000, centers=centers, cluster_std=0.7)

y = np.choose(labels_true, ['b', 'g', 'r']).astype(np.object)
plt.scatter(X[:,0],X[:,1],c=y)
plt.title("Gráfica de dos variables")
plt.ylabel("Segunda Variable")
plt.xlabel("Primera Variable")
plt.show()
