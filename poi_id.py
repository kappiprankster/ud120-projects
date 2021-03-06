#!/usr/bin/python

import sys
import pickle
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi','bonus','exercised_stock_options','total_payments'] # You will need to use more features

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers
data_dict.pop('TOTAL')
 
"""for i in data_dict.keys():
    if data_dict[i]['from_poi_to_this_person'] >= 500 and data_dict[i]['from_poi_to_this_person'] <> 'NaN':
        print i
    else:
        pass"""
### Task 3: Create new feature(s)

### Store to my_dataset for easy export below.
my_dataset = data_dict
print data_dict['LAY KENNETH L']
### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)


from sklearn.preprocessing import MinMaxScaler
m1 = MinMaxScaler()
m1.fit(features)
features = m1.transform(features)


from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.2,random_state = 42)
"""for point in data:
    salary = point[0]
    bonus = point[3]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()"""
### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html
from sklearn.feature_selection import SelectKBest, f_classif
selector =  SelectKBest(f_classif, k=3)
selector.fit(features_train, labels_train)
print selector.pvalues_
scores = -np.log10(selector.pvalues_)
plt.bar(range(3),scores)
#plt.xticks(range(len(features)), features, rotation='vertical')
plt.show()

# Provided to give you a starting point. Try a variety of classifiers.
"""from sklearn.model_selection import KFold,cross_val_score
Vec = np.arange(0,len(features))
kfold = KFold(len(features),shuffle = False)
for train_index,test_index in enumerate(kfold.split(Vec),start = 0):
    X_train,X_test = features[train_index],features[test_index]
    #Y_train,Y_test = labels[train_index],labels[test_index]
    print train_index
"""


from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train,labels_train)
clf.fit(features_train,labels_train)
print clf.score(features_train,labels_train)
print clf.score(features_test,labels_test)
pred = clf.predict(features_test)
from sklearn.metrics import recall_score, precision_score
print recall_score(labels_test,pred)
print precision_score(labels_test,pred)
### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)