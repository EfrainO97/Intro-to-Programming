#!/usr/bin/env python
# coding: utf-8

# In[13]:


# -*- coding: utf-8 -*-

#%% Libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% Importing Data
flights_data = pd.read_csv('flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('weather.csv')
weather_data_np = weather_data_pd.to_numpy()
#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data


# In[2]:


#Question 1 How many flights were there from JFK to SLC? Int
q_1 = int(((flights_data['origin']=='JFK') & (flights_data['dest'] == 'SLC')).sum())

print(q_1)
#here we used boolean operator AND, we selected for values that orignated in JFK AND had a destination to SLC then we used sum
#to add all the Trues or 1's and got the total for flights from JFK to SLC


# In[3]:


#Question 2 How many airlines fly to SLC? Should be int
q_2 = int(flights_data.loc[flights_data['dest'] == 'SLC','carrier'].nunique())
print(q_2)
# here we filter to flight with a destination to SLC, then take the carrier column and count the distinct airlines using .nunique


# In[4]:


#Question 3 What is the average arrival delay for flights to RDU? float
q_3 = float((flights_data.loc[flights_data['dest'] == 'RDU', 'arr_delay'].mean()))
print(q_3)
#here we filtered flights to RDU and then took the arr_delay column and used .mean to average it 


# In[5]:


#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
sea_flights = flights_data[flights_data['dest'] == 'SEA']
portion = sea_flights['origin'].isin(['LGA', 'JFK']).sum()
q_4 = float(portion/len(sea_flights))
print(q_4)
#here we defined sea_flights as the flights with a destination to SEA
#then we kept the flights with an origin of LGA or JFK and summed and called that portion 
#then we dived the portion by the whole and got the proportion


# In[6]:


#Question 5 Which date has the largest average depature delay? Pd slice with date and float
#please make date a column. Preferred format is 2013/1/1 (y/m/d)
flights_data['date'] = (flights_data['year'].astype(str) + '/' +
                        flights_data['month'].astype(str) + '/' +
                        flights_data['day'].astype(str))
flights_data['date'].head()

avg_dep = flights_data.groupby('date', as_index=False)['dep_delay'].mean()
avg_dep.head()

q_5=avg_dep.nlargest(1,'dep_delay')
print(q_5)
#first we set the date column into the y/m/d format by defining it as year + a / as str type, month + a / as str type and then day
#then we group the flights by date using .groupby and average the dep_delay using .mean().
#as_index=False keeps date as normal column
#lastly largest(1, 'dep_delay') keeps the single row with the largest average delay


# In[7]:


#Question 6 Which date has the largest average arrival delay? pd slice with date and float
avg_arr = flights_data.groupby('date', as_index=False)['arr_delay'].mean()
avg_arr.head()

q_6=avg_arr.nlargest(1,'arr_delay')
print(q_6)
#this is the same as q5 excpet for arrival delay instead od departure delay. 
#I kept the same code and changed the entity to arrival delay 


# In[8]:


#Question 7 Which flight departing LGA or JFK in 2013 flew the fastest? pd slice with tailnumber and speed
#speed = distance/airtime
nyc_2013 = flights_data[flights_data['origin'].isin(['LGA','JFK'])&(flights_data['year']==2013)].copy()
nyc_2013['speed'] = nyc_2013['distance']/nyc_2013['air_time']
q_7=nyc_2013.nlargest(1,'speed')[['tailnum','speed']]
print(q_7)
#first we filter for flights with an origin of LGA or JFK that happened during the year 2013, 
#we use the .copy() to avoid a warning and from altering the original data set
#Then create a new speed column in nyc_2013 and make it equal to distance/air_time
#lastly we use .nlargest to find the largest value in the speed column
#[['tailnum','speed']] keeps the tailnum and speed columns


# In[9]:


#Question 8 Replace all nans in the weather pd dataframe with 0s. Pd with no nans
q_8 = weather_data_pd.fillna(0)
print(q_8)
#Here we use the .fillna to replace all the missing values with 0



# In[10]:


#Question 9 How many observations were made in Feburary? Int
cols = list(weather_data_pd.columns)
month = weather_data_np[:, cols.index('month')].astype(float)
feb_mask = month == 2
q_9 = int(np.sum(feb_mask))
print(q_9)
#


# In[11]:


#Question 10 What was the mean for humidity in February? Float
humid = weather_data_np[:, cols.index('humid')].astype(float)
q_10 = float(np.nanmean(humid[feb_mask]))
print(q_10)
#first we convert every row in the humid column into floats
#then we use the mask for q9 to keep only Feburary rows and take the average using .nanmean()
#.nanmean() skips empty values


# In[12]:


#Question 11 What was the std for humidity in February? Float
q_11 = float(np.nanstd(humid[feb_mask]))
print(q_11)
#Here we use the np.nanstd() function to get the STD for February again using the mask from q9
#.nanstd() skips over empty values


# In[ ]:




