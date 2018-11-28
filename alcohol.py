import csv
import plotly.plotly as py
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import plotly.tools as tls
from matplotlib.ticker import MultipleLocator
import matplotlib.pyplot as plt

code = {'S92000003':"Scotland", 'S12000033':"Aberdeen City", 'S12000034':"Aberdeenshire", 'S12000041':"Angus", 'S12000035':"Argyll & Bute", 'S12000008':"East Ayrshire", 'S12000021':"North Ayrshire", 'S12000028':"South Ayrshire", 'S12000026':"Scottish Borders",
 'S12000005':"Clackmannanshire", 'S12000006':"Dumfries & Galloway", 'S12000045':"East Dumbartonshire", 'S12000039':"West Dumbartonshire", 'S12000042':"Dundee City", 'S12000036':"City of Edinburgh", 'S12000014':"Falkirk", 'S12000015':"Fife", 'S12000046':"Glasgow City",
 'S12000017':"Highlands", 'S12000018':"Inverclyde", 'S12000044':"North Lanarkshire", 'S12000029':"South Lanarkshire", 'S12000010':"East Lothian", 'S12000040':"West Lothian", 'S12000019':"Midlothian",
 'S12000020':"Moray", 'S12000013':"Eilean Siar", 'S12000023':"Orkney Islands", 'S12000024':"Perth & Kinross", 'S12000038':"Renfrewshire", 'S12000011':"East Renfrewshire", 'S12000027':"Shetland Islands", 'S12000030':"Stirling"}
total = 0
with open('local_area.csv') as local_area:
    csv_reader = csv.DictReader(local_area)
    dict = {}
    location_stay = {}
    location_count = {}
    location_patient ={}



    count = 0
    total = 0
    for row in csv_reader:
        if (row['NumberOfStays'] != " " and row['NumberOfPatients'] != " "):
            if (row['CA2011'] not in location_stay.keys()):
                stays = int(row['NumberOfStays'])
                patients = int(row['NumberOfPatients'])
                count=1

                location_patient[row['CA2011']] = patients
                location_stay[row['CA2011']] = stays
                location_count[row['CA2011']] = count

                temp1 = {key : (location_stay[key],location_count[key]) for key in location_stay}
                temp2 = {key : (location_patient[key],location_count[key]) for key in location_patient}
                dict = temp1, temp2


            else:
                stays = int(row['NumberOfStays'])
                patients = int(row['NumberOfPatients'])
                count=1

                location_patient[row['CA2011']] += patients
                location_stay[row['CA2011']] += stays
                location_count[row['CA2011']] += count

                temp1 = {key : (location_stay[key],location_count[key]) for key in location_stay}
                temp2 = {key : (location_patient[key],location_count[key]) for key in location_patient}
                dict = temp1, temp2


        else:
            continue
    dict = {key : (temp1[key],temp2[key]) for key in temp1}
temp = {}
for keys, (value1, value2) in dict.items():
    temp[code[keys]] = (value1, value2)
    # dict[code[keys]] = "code[keys]"
dict = temp


for files, data in dict.items():
    one = data[0][0]/data[0][1]
    two = data[1][0]/data[1][1]
    dict[files] = one, two
stays = {}
patients = {}
location  =[]
for keys, (values1, values2) in dict.items():
    stays[keys] = values1
    patients[keys] = values2
    location.append(keys)



ml = MultipleLocator(100)
plt.xticks(rotation=90)
plt.axes().yaxis.set_minor_locator(ml)
plt.xlabel( 'Area Code')
plt.ylabel('Average Number of stays over years' )
plt.title("Average Number of stays in hospital per Scottish district from 2007 to 2018")
plt.bar(stays.keys(), stays.values(), color='b' )

plt.show()

ml = MultipleLocator(100)
plt.xticks(rotation=90)
plt.axes().yaxis.set_minor_locator(ml)
plt.xlabel( 'Area Code')
plt.ylabel('Average Number of patients.')
plt.title("Average Number of patients per Scottish district from 2007 to 2018")
plt.bar(patients.keys(), patients.values(), color='b' )

plt.show()
