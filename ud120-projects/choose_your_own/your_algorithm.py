#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.neighbors import KNeighborsClassifier as KNC
from sklearn.ensemble import AdaBoostClassifier as ABC
from sklearn.ensemble import VotingClassifier as VC
from sklearn.metrics import accuracy_score 


jobs=-1
seed=42

print("Fitting Random Forest")
model1=RFC(criterion="entropy", 
          min_samples_split=5, 
          oob_score=True,
          n_jobs=jobs, 
          random_state=seed).fit(features_train, labels_train)

print("Fitting KNN")
model2=KNC(n_jobs=jobs, weights="distance", n_neighbors=3).fit(features_train, labels_train)

print("Fitting Ada boost")
model3=ABC(random_state=seed).fit(features_train, labels_train)


predict1=model1.predict(features_test)
predict2=model2.predict(features_test)
predict3=model3.predict(features_test)


accuracy1=accuracy_score(labels_test, predict1)
accuracy2=accuracy_score(labels_test, predict2)
accuracy3=accuracy_score(labels_test, predict3)

print(f"accuracy of model 1 with Random forest is {accuracy1}")
print(f"accuracy of model 2 with KNN is {accuracy2}")
print(f"accuracy of model 3 with Adaboost is {accuracy3}")

combinedmodel = VC(estimators=[("rf", model1), ("knn", model2), ("ada", model3)],
                   voting="hard",
                   weights=[1,3,2])
combinedmodel.fit(features_train, labels_train)
combinedpredition=combinedmodel.predict(features_test)
combinedaccuracy=accuracy_score(labels_test, combinedpredition)

print(f"accuracy of combined model with all classifiers is  {combinedaccuracy}")


try:
    prettyPicture(combinedmodel, features_test, labels_test)
except NameError:
    pass
