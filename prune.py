import re
import pandas as pd

#opening spreadsheets
workbook1 = pd.read_csv('emails_one.csv')
workbook2 = pd.read_csv('emails_two.csv')

#get first column of data only
sheet1 = workbook1.iloc[:,0]
sheet2 = workbook2.iloc[:,0]

#flatten column to get list of emails
#Url list initialization
st1 = sheet1.values.flatten()
st2 = sheet2.values.flatten()

pruned = set(st2) - set(st1)

#saving pruned sheet to a new csv file
pd.DataFrame(pruned).to_csv("pruned.csv", header=None, index=None)

#print(final)
