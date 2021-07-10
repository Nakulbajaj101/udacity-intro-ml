#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
total_data=len(enron_data)
#print(len(total_data))
#print(enron_data.keys())

first_value=list(enron_data.values())[0]
print(first_value)

print(len(first_value))

counter=0
for key in enron_data.keys():
    poi=enron_data[key]['poi']
    if poi:
        counter+=1
        print(f"{key} is person of interest")
    else:
        print(f"{key} is not a person of interest")


print(f"Total persons of interest are {counter} out of {total_data}")

def get_stock_value(person_of_interest=""):
    return enron_data[person_of_interest]["total_stock_value"]
def get_stock_options(person_of_interest=""):
    return enron_data[person_of_interest]["exercised_stock_options"]
def get_num_emails(person_of_interest=""):
    return enron_data[person_of_interest]["from_this_person_to_poi"]

for key in enron_data.keys():
    if "prentice" in key.lower() and "james" in key.lower():
        stock_value=get_stock_value(key)
        print(f"stock value of {key} is {stock_value}")

for key in enron_data.keys():
    if "colwell" in key.lower() and "wesley" in key.lower():
        emails=get_num_emails(key)
        print(f"total emails sent by {key} to poi are {emails}")

for key in enron_data.keys():
    if "skilling" in key.lower() and "jeffrey" in key.lower():
        stock_options=get_stock_options(key)
        print(f"stock options of {key} are {stock_options}")
def main_names():
    names = ["jeffrey","lay","fastow","skilling"]
    matches=[]
    for name in names:
        full_name = [s for s in enron_data.keys() if name in s.lower()][0]
        matches.append(full_name)
    return matches

print(main_names())
        

max_payment = max([enron_data[key]["total_payments"] for key in main_names()])
print(max_payment)

for key in enron_data.keys():
    if enron_data[key]["total_payments"] != "NaN":
        if enron_data[key]["total_payments"] == max_payment:
            print(f"{key} took home the most {max_payment}")



quantified_salary=sum([1 for key in enron_data.keys() if enron_data[key]["salary"] != "NaN"])
quantified_email=sum([1 for key in enron_data.keys() if enron_data[key]["email_address"] != "NaN"])

print(f"total people who had quantified_salary and email are {quantified_salary}, {quantified_email} respectively")

unquantified_total_payments_perc=sum([1 for key in enron_data.keys() if enron_data[key]["total_payments"] == "NaN"])/total_data
print(f"percentage of people who didnt have total payments are {unquantified_total_payments_perc}")

unquantified_total_payments_poi_perc=sum([1 for key in enron_data.keys() if enron_data[key]["total_payments"] == "NaN" and enron_data[key]['poi']])/counter
print(f"percentage of poi people who didnt have total payments are {unquantified_total_payments_poi_perc}")



print(max([enron_data[key]["exercised_stock_options"] for key in enron_data.keys() if enron_data[key]["exercised_stock_options"] != "NaN"]))
print(min([enron_data[key]["exercised_stock_options"] for key in enron_data.keys() if enron_data[key]["exercised_stock_options"] != "NaN"]))