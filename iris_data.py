import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn import tree
from joblib import dump

data = load_iris()

X = data['data']
y = data['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=45, shuffle=True)

iris_clf = tree.DecisionTreeClassifier().fit(X_train, y_train)
y_pred = iris_clf.predict(X_test)
print(accuracy_score(y_pred, y_test))
print(confusion_matrix(y_test, y_pred))
print(data['target_names'][y_pred])

dump(iris_clf, 'iris_classifier_model.joblib')
tree.plot_tree(iris_clf)
plt.show()
