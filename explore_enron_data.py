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

enron_data = pickle.load(open("\\Udacity\\machine-learning\\projects\\Enron\\final_project\\final_project_dataset.pkl", "r"))

# Quiz questions
# Q13 - How many data points (people) are in the dataset?
print '13. Quiz: Size of the Enron Dataset?',len(enron_data)

# Q14 - For each person, how many features are available?
print '14. Quiz: Features in the Enron Dataset?',len(enron_data["SKILLING JEFFREY K"])

# Q15 - How many POIs are there in the E+F dataset?
count = 0
for person in enron_data:
    if enron_data[person]["poi"]==True:
        count+=1
print '15. Quiz: Finding POIs in the Enron Data?',count

# Q16 - How many POI's were there total?
poi_names = open("\\Udacity\\machine-learning\\projects\\Enron\\final_project\\poi_names.txt", "r")
count = 0
while 1:
    line=poi_names.readline() # check for EOF
    if not line: break
    if line[0:3] == '(y)' or line[0:3] == '(n)':
        count+=1
poi_names.close()
print '16. Quiz: POIs:',count

# Q18 What is the total value of the stock belonging to James Prentice?
print '18. Quiz: Value of the stock belonging to James Prentice:',enron_data['PRENTICE JAMES']["total_stock_value"]

# Q19 How many email messages do we have from Wesley Colwell to persons of interest?
print '19. Quiz: Email messages from Wesley Colwell to POI:',enron_data['COLWELL WESLEY']["from_this_person_to_poi"]

# Q20 What's the value of stock options exercised by Jeffrey K Skilling?
print '19. Quiz: Stock options exercised by Jeffrey K Skilling:',enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

# Q25 Of these three individuals (Lay, Skilling and Fastow), who took home the most money?
print '25. Quiz: SKILLING received:',enron_data["SKILLING JEFFREY K"]["total_payments"]
print '25. Quiz: LAY received     :',enron_data["LAY KENNETH L"]["total_payments"]
print '25. Quiz: FASTOW received  :',enron_data["FASTOW ANDREW S"]["total_payments"]

# Q27a How many folks in this dataset have a quantified salary?
count = 0
for person in enron_data:
    if enron_data[person]["salary"]<>"NaN":
        count+=1
print '27a. Quiz: Folks with a quantified salary:',count

# Q27b How many folks in this dataset have a known email address?
count = 0
for person in enron_data:
    if enron_data[person]["email_address"]<>"NaN":
        count+=1
print '27b. Quiz: Folks with a known email address:',count

# Q29a How many people in the have "NaN" for their total payments?
# Q29b What percentage of people in the dataset as a whole is this?
count = 0
count_total = 0
for person in enron_data:
    count_total+=1
    if enron_data[person]["total_payments"]=="NaN":
        count+=1
print '29a. Quiz: People with "NaN" total payments:',count
print '29b. Quiz: Total of the whole dataset:',count_total

# Q30 How many POIs in the E+F dataset have "NaN" for their total payments?
# Q30 What percentage of POI's as a whole is this?
count = 0
count_total = 0
for person in enron_data:
    if enron_data[person]["poi"]==True:
        count_total+=1
        if enron_data[person]["total_payments"]=="NaN":
            count+=1
print '30a. Quiz: POI with "NaN" total payments:',count
print '30b. Quiz: Total of the POI dataset:',count_total



print 'EOF'