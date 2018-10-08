# import a dataset
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

print(X)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= .5)

# DECISION TREE CLASSIFIER
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier

for my_classifier in [tree.DecisionTreeClassifier(), KNeighborsClassifier()]:
    my_classifier.fit(X_train, y_train)

    predictions = my_classifier.predict(X_test)
    print('Size of training data',len(y_train))
    print('Size of testing data',len(y_test))
    print(predictions)

    from sklearn.metrics import accuracy_score
    print(accuracy_score(y_test, predictions))



