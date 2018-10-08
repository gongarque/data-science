from sklearn import tree

# 2nd feature
SMOOTH = 1
BUMPY = 0

# labels
APPLE = 0
ORANGE = 1

features = [[140, SMOOTH], [130, SMOOTH], [150, BUMPY], [170, BUMPY]]
labels = [APPLE, APPLE, ORANGE, ORANGE]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

prediction = clf.predict([[110, 1]])
print(prediction)