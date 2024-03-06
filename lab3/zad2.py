import pandas as pd
df = pd.read_csv("iris.csv")
from sklearn import tree
from sklearn.model_selection import train_test_split
import graphviz
# podzial na zbior testowy 0% i treningowy 70% z ziarnem 13
#podzial na zbior testowy (30%) i treningowy (70%), ziarno losowosci = 13
(train_set, test_set) = train_test_split(df.values, 
train_size=0.7, 
random_state=281195)

print(test_set)
print(test_set.shape[0])

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_inputs, train_classes)
print(clf.predict([[5.1, 3.8, 1.9, 0.4]]))
tree.plot_tree(clf)

dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") 