# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 21:50:37 2022

@author: dindi
"""

#Topic ---- Case Study - Denco - Manufacturing Firm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%%case details
#%%Objective
#Expand Business by encouraging loyal customers to Improve repeated sales
#Maximise revenue from high value parts
#%%Information Required
#Who are the most loyal Customers - Improve repeated sales, Target customers with low sales Volumes
#Which customers contribute the most to their revenue - How do I retain these customers & target incentives
#What part numbers bring in to significant portion of revenue - Maximise revenue from high value parts
#What parts have the highest profit margin - What parts are driving profits & what parts need to build further
#%%%
#see all columns
pd.set_option('display.max_columns',15)
#others - max_rows, width, precision, height, date_dayfirst, date_yearfirst
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.2f}'.format
#read data
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
df = pd.read_csv('C:/analytics/projects/pyanalytics/.spyproject/denco.csv')
df = pd.read_csv(url)
#see properties of data
df
#print(df)

df.groupby('custname').count
df['custname'].unique().count()
df.custname.unique()

df.index
df.head

CN=df.groupby('custname')
CN.count()
CN.custname.unique().count()
df.size()

#Loyal Customers 
df["custname"].value_counts().head(20)
df["custname"].value_counts().tail(50)

df.index
df.["custname"]
df.head()
df.groupby(['custname']).sum().sort_values(by="revenue").tail(5)

df.shape
type(df)
df.columns
df.dtypes()
df.dtypes
df['region']
#convert to categorical data 
df['region']= df['region'].astype('category')#converted to category
df.dtypes   
#%%%
# Find loyal customers 
df["custname"].value_counts().head(20) 
#Most unloyal customers
df["custname"].value_counts().sort_values(ascending=True)[0:5]
#%%%%
#Customers who contribute the most revenues 
df.groupby(['custname']).sum().sort_values(by="revenue").tail(5)
df.groupby(['custname']).sum()
#answer by Sir
df.groupby('custname').aggregate({'revenue':np.sum}).sort_values(by='revenue',ascending= False).head(5).plot(kind='bar')
#%%%
#Which part number got in most revenue
df.groupby('partnum').aggregate({'revenue':np.sum}).sort_values(by='revenue',ascending= False).head(5).plot(kind='bar')
df.groupby('partnum').aggregate({'revenue':np.sum}).sort_values(by='revenue',ascending= False).head(5)

df[['partnum','revenue']].groupby('partnum').aggregate([np.sum,'size','min','max'])
df[df['partnum'] == 715000000]
#%%%
# Which part has the highest margin
df[['partnum','margin']].groupby('partnum').aggregate([np.sum,'size','min','max'])

#%%%
#Which region gives the most revenue
df[['margin','region']].groupby('region').aggregate([np.sum])
df[['margin','region']].groupby('region').aggregate([np.sum,'size'])
df[['margin','region']].groupby('region').aggregate([np.sum])

