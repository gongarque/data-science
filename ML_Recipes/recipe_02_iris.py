from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

iris = load_iris()


print(iris.data[0])
print(iris.target)

for i in range(len(iris.target)):
    print('Example %d: label %s, feature %s' % (i, iris.target[i], iris.data[i]))

test_idx = [0, 50, 100]

# training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)


# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print('Test Target: ' + str(test_target))
print('Test Data: ' + str(test_data))
print('Predict test data: ' + str(clf.predict(test_data)))

# viz code - visualization
from sklearn.externals.six import StringIO
import pydotplus

dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")


print('\n', test_data[1], test_target[1])
print(iris.feature_names)
print(iris.target_names)


