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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print (enron_data.keys())
count = 0
count1 = 0 
print (list(enron_data.values())[0])
for i in enron_data.keys():
    
    if  enron_data[i]['poi']==True:
        count = count + 1
print count
names = open("../final_project/poi_names.txt", "r")
print (names.readlines())
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print enron_data['SKILLING JEFFREY K']['total_payments']
print enron_data['LAY KENNETH L']['total_payments']
print enron_data['FASTOW ANDREW S']['total_payments']
for i in enron_data.keys():
    
    if  enron_data[i]['email_address']<>'NaN':
        count1 = count1 + 1
print count1
count2 = 0
for i in enron_data.keys():
    
    if  (enron_data[i]['total_payments']=='NaN'):# and enron_data[i]['poi'] ==True) :
        count2 = count2 + 1
        #count2 = (count2/146.0)*100
print count2
print (125.0/146.0)*100.0