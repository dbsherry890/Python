from sklearn.datasets import load_iris
from sklearn.utils import all_estimators
from sklearn import svm  # support vector machine
import pandas as pd

# iris = load_iris()
# print(iris.data.shape)

# clf = svm.LinearSVC()
# learn from the data
# clf.fit(iris.data, iris.target)
# predict for unseen data
# clf.predict([[5.0,  3.6,  1.3,  0.25]])
# Parameters of model can be changed by using the attributes ending with an underscore
# print(clf.intercept_)
# df = pd.DataFrame(all_estimators('classifier'))
# print(df)

from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generate a dataset with 3 clusters, 2 features, and 100 samples
X, y = make_blobs(n_samples=10, n_features=2, centers=5,
                  cluster_std=1, random_state=42)
print(X, y)

# Visualize the generated data
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Generated Blobs")
plt.show()
# ftr1 = pd.Series([1, 2, 3, 4, 5, 6, 7])
# ftr2 = pd.Series([5, 7, 8, 22, 45, 11, 45])
# plt.scatter(ftr1, ftr2)
# plt.show()
