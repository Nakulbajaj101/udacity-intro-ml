#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

training_start = time()

for c in [10000.0]:
    model=SVC(C=c, kernel='rbf',gamma='auto')

    #features_train = features_train[:int(len(features_train)/100)]
    #labels_train = labels_train[:int(len(labels_train)/100)]

    model.fit(features_train, labels_train)

    print ("training time:", round(time()-training_start, 3), "s")

    prediction=model.predict(features_test)
    accuracy=accuracy_score(labels_test, prediction)
    print("accuracy is: {} with cost of {}".format(accuracy, c))
    print(prediction[10])
    print(prediction[26])
    print(prediction[50])
    print(confusion_matrix(labels_test, prediction))
    print(list(prediction).count(1))
#########################################################


