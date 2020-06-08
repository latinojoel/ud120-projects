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

emails=0
sal=0
pay=0
c=0
for k,v in enron_data.items():
    if enron_data[k]['poi'] is True:
        c+=1
    if 'NaN' != enron_data[k]['email_address']:
        emails+=1
    if 'NaN' != enron_data[k]['salary']:
        sal+=1
    if 'NaN' == enron_data[k]['total_payments'] and enron_data[k]['poi'] is True:
        pay+=1
    if c == 1:
        print enron_data[k]


print sal
print emails
print pay
print c
print float(pay/c)
