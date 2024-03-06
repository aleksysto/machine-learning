import pandas as pd
df = pd.read_csv("iris.csv")

from sklearn.model_selection import train_test_split

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
#print(test_inputs, "\n\n\n", test_classes)
def classify_iris(sl, sw, pl, pw):
    if 1 < pl < 2:
        return("Setosa")
    elif sl >= 6 and pl > 4.8:
        return("Virginica")
    else:
        if pw <= 1.5:
            return("Versicolor")
        else:
            return("Virginica")
good_counter = 0
len = test_set.shape[0]

for i in range(len):
    sl = test_inputs[i][0]
    sw = test_inputs[i][1]
    pl = test_inputs[i][2]
    pw = test_inputs[i][3]
    if classify_iris(sl, sw, pl, pw) == test_classes[i]:
        good_counter = good_counter + 1
    else:
        print(sl, sw, pl, pw, classify_iris(sl, sw, pl, pw), test_classes[i])

print(good_counter)
print(good_counter/len*100, "%")