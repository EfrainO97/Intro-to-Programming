#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


filename = 'diabetic_data.csv'


# In[4]:


df = pd.read_csv(filename)
df


# In[5]:


#MELT
#combines metformin and insulin into one column making it easier to compare between the two. 
df_long = df.melt(
    id_vars=['encounter_id', 'age', 'time_in_hospital', 'readmitted'],
    value_vars=['metformin', 'insulin'],
    var_name='medication',
    value_name='dose_status')

df_long = df_long[df_long['dose_status'] != 'No']
df_long


# In[12]:


#PIVOT
#pivot changing long into wide reversing the melt. 
df_wide = df_long.pivot(index='encounter_id', columns='medication', values='dose_status')

df_wide
#encounters per drug
print(df_wide.notna().sum())  


# In[7]:


#Pivot_table
#average stay for patients on vs off diabetes medication 
df_wide2=df.pivot_table(index='diabetesMed', values='time_in_hospital', aggfunc='mean')

df_wide2


# In[8]:


#Aggregation
#shows statistical summary for the time_in_hospital column 
df['time_in_hospital'].agg(['mean', 'median', 'std', 'min', 'max'])



# In[9]:


#Different statistics for different columns in one call
df.agg({
    'time_in_hospital': ['mean', 'max'],
    'num_medications': ['mean', 'max'],
    'num_lab_procedures': ['mean', 'median']
})


# In[10]:


#ITERATION
# loops through the first few entries and prints a oneline summary of each. 
for idx, row in df.head(5).iterrows():
    print(f"Encounter {row['encounter_id']}: age {row['age']}, "
          f"stayed {row['time_in_hospital']} days")


# In[11]:


#GROUPBY
# Average stay per age bracket
df.groupby('age')['time_in_hospital'].mean()

