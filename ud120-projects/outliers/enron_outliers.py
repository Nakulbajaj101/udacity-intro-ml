#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )


data_dict.pop("TOTAL", None)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

for _ in data_dict.keys():
    if data_dict[_]["salary"] != "NaN" and data_dict[_]["bonus"] != "NaN":
        if data_dict[_]["salary"] > 1000000:
            print(f"{_} has salary greated than 1m")
        if data_dict[_]["bonus"] > 5000000:
            print(f"{_} has bonus greated than 5m")

### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus, color="b" )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

