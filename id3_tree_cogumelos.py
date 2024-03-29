# -*- coding: utf-8 -*-
"""ID3 Tree - Cogumelos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j3PCTS4EI7BYnVFWbqFldHULnyRP9Ezn
"""

import pandas as pd
import numpy as np
import math

#Carregando dataset

dataset = pd.read_csv("agaricus-lepiota.data") #não consegui botar o link para baixar o dataset então upei manualmente aqui pro colab
dataset

#Transformar nossos queridinhos em números
from sklearn.preprocessing import LabelEncoder
dataset = dataset.apply(LabelEncoder().fit_transform)
dataset

def find_entropy(dataset):
    
    #Returns the entropy of the class or features 
    #formula: - ∑ P(X)logP(X)
    
    entropy = 0
    for i in range(dataset.nunique()):
        x = dataset.value_counts()[i]/dataset.shape[0] 
        entropy += (- x * math.log(x,2))
    return round(entropy,3)

def information_gain(dataset, data_):
    
    #Returns the information gain of the features
    
    info = 0
    for i in range(data_.nunique()):
        df = dataset[data_ == data_.unique()[i]]
        w_avg = df.shape[0]/dataset.shape[0]
        entropy = find_entropy(df.play)
        x = w_avg * entropy
        info += x
    ig = find_entropy(dataset.play) - info
    return round(ig, 3)   

#Or the "easy way">>>>>>

from sklearn.model_selection import train_test_split

X = dataset.drop(columns=['target'])[['odor']]
#X = dataset.drop(columns=['target'])
#X = dataset.copy()
y = dataset['target']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33)

from sklearn.tree import DecisionTreeClassifier
#clf = DecisionTreeClassifier()
clf = DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X_train, y_train)
clf.get_params()

X_test

predictions = clf.predict(X_test)
predictions

clf.predict_proba(X_test)

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report

accuracy_score(y_test, predictions)

confusion_matrix(y_test, predictions, labels = [0, 1])

precision_score(y_test, predictions)

recall_score(y_test, predictions)

print(classification_report(y_test, predictions, target_names = ['poisonous - p', 'edible - e']))

feature_names = X.columns
feature_names

clf.feature_importances_

from sklearn import tree
from matplotlib import pyplot as plt

fig = plt.figure(figsize = (25, 20))
_ = tree.plot_tree(clf,
                   feature_names=feature_names,
                   class_names = {0: 'Poisonous', 1: 'Edible'},
                   filled = True,
                   fontsize = 12)