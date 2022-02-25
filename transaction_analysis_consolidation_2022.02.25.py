# -*- coding: utf-8 -*-
"""
Project: XXXX
Title: Convert Text files to csv
Author: Malcolm McCabe
Created: 2/24/2022
Last Updated: 2/25/2022
"""

"""
The following script utilizes a pre-cleaned text file that has been converted to a csv
based on a fixed width delimiter. This pre-cleaned text file is then further cleaned in 
this script and converted to a consolidated csv file allowing for a synthesized
report simplying the transaction analysis
"""

#Import necessary packages
import pandas as pd
import re
import math


#Instantiate df
df = pd.read_csv("XXX.csv", header=None, names=["Supplier", "Supplier Name", "Invoice", "Invoice date", 
             "Reference", "Gross amount", "Discount", "Net Amount", "Amount", "Number"])


#Set data types for relevant columns
df["Supplier"] = df["Supplier"].astype(str)
df["Supplier Name"] = df["Supplier Name"].astype(str)
df["Discount"] = df["Discount"].astype(str)
df["Invoice"] = df["Invoice"].astype(str)
df["Invoice date"] = df["Invoice date"].astype(str)
df["Reference"] = df["Reference"].astype(str)
df["Net Amount"] = df["Net Amount"].astype(str)
df["Invoice"] = df["Invoice"].astype(str)
df["Amount"] = df["Amount"].astype(str)
df["Number"] = df["Number"].astype(str)


#print(df)

#Precleaning steps
for i in range(len(df)):
    if "Total" in df["Reference"].iloc[i]:
        df_no_total = df.drop(df.index[i])
print(df_no_total["Reference"])

df_final = df_no_total

for i in range(len(df_no_total)):  
    if "Check" in df_no_total["Net Amount"].iloc[i]:
        df_final["Number"].iloc[i] = df_no_total["Amount"].iloc[i]
    


#Clean Invoice Date column
for i in range(1, len(df_final["Invoice date"])):
    if df_final["Invoice date"].iloc[i] != 'nan' and df_final["Invoice date"].iloc[i-1] != 'nan' and "/" in df_final["Invoice date"].iloc[i-1]:
        df_final["Invoice date"].iloc[i-1] = df_final["Invoice date"].iloc[i-1] + df_final["Invoice date"].iloc[i]

for i in range(len(df_final)):
    if "/" not in df_final["Invoice date"].iloc[i]:
        df_final["Invoice date"].iloc[i] = ""

df_final["Invoice date"] = df_final["Invoice date"]


#Clean Invoice column
for i in range(1, len(df_final)):
    if math.isnan(df_final["Gross amount"].iloc[i-1]) == False:
        counter = i-1
        df_final["Invoice"].iloc[counter] = df_final["Invoice"].iloc[counter] + df_final["Invoice"].iloc[i]
    elif math.isnan(df_final["Gross amount"].iloc[i]) == True:
        df_final["Invoice"].iloc[counter] = df_final["Invoice"].iloc[counter] + df_final["Invoice"].iloc[i]       
    else:
        pass


for i in range(len(df_final)):
    if math.isnan(df_final["Gross amount"].iloc[i]) == True:
        df_final["Invoice"].iloc[i] = ""



#Clean Reference column
df_final["Reference"] = df_final["Reference"].astype(str)

for i in range(1, len(df_final)):
    if math.isnan(df_final["Gross amount"].iloc[i-1]) == False:
        counter = i-1
        df_final["Reference"].iloc[counter] = df_final["Reference"].iloc[counter] + df_final["Reference"].iloc[i]
    elif math.isnan(df_final["Gross amount"].iloc[i]) == True:
        df_final["Reference"].iloc[counter] = df_final["Reference"].iloc[counter] + df_final["Reference"].iloc[i]
            
    else:
        pass

for i in range(len(df_final)):
    if math.isnan(df_final["Gross amount"].iloc[i]) == True:
        df_final["Reference"].iloc[i] = ""

df_final["Reference"] = df_final["Reference"]
#df["Invoice"] = df["Invoice"].astype(str)

print(df_final)
df_final.to_csv("output.csv")










