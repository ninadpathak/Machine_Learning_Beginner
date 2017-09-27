from sklearn.naive_bayes import GaussianNB
import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3,-2], [1,1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
clf = GaussianNB()
clf.fit(X, Y)
print(clf.predict([[3, 5]]))

clf_pf = GaussianNB()
clf_pf.partial_fit(X, Y, np.unique(Y))
print(clf_pf.predict([[-0.8, -1]]))
