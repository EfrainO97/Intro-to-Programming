#!/usr/bin/env python
# coding: utf-8

# In[26]:


#Question 1 (15 Points)
#Compute the euclidean distance between series (points) p and q, without using a packaged formula.
#Input
p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


#Question 2 (15 Points)
#Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.
#Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))


#Question 3 (15 Points)
#Change the order of columns of a dataframe.  Create a generic function to interchange two columns, without hardcoding column names.
#Input
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))


#Question 4 (15 Points)
#Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
#Input
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df
#>          random
#> 0  3.474280e-03
#> 1  3.951517e-05
#> 2  7.469702e-02
#> 3  5.541282e-28
#Desired Output
#>    random
#> 0  0.0035
#> 1  0.0000
#> 2  0.0747
#> 3  0.0000


#Question 5 (15 Points)
#Create a new column that contains the row number of nearest column by euclidean distance. Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
#Input
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
df
#     p   q   r   s
# a  57  77  13  62
# b  68   5  92  24
# c  74  40  18  37
# d  80  17  39  60
# e  93  48  85  33
# f  69  55   8  11
# g  39  23  88  53
# h  63  28  25  61
# i  18   4  73   7
# j  79  12  45  34
#Desired Output
df
#    p   q   r   s nearest_row   dist
# a  57  77  13  62           i  116.0
# b  68   5  92  24           a  114.0
# c  74  40  18  37           i   91.0
# d  80  17  39  60           i   89.0
# e  93  48  85  33           i   92.0
# f  69  55   8  11           g  100.0
# g  39  23  88  53           f  100.0
# h  63  28  25  61           i   88.0
# i  18   4  73   7           a  116.0
# j  79  12  45  34           a   81.0


#Question 6 (15 Points)

#Correlation is a statistical technique that shows how two variables are related. 
#Pandas dataframe.corr() method is used for creating the correlation matrix. 
#It is used to find the pairwise correlation of all columns in the dataframe. Any na values are automatically excluded. 
#For any non-numeric data type columns in the dataframe it is ignored.

#Input
data = {'A': [45, 37, 0, 42, 50], 'B': [38, 31, 1, 26, 90], 'C': [10, 15, -10, 17, 100], 'D': [60, 99, 15, 23, 56], 'E': [76, 98, -0.03, 78, 90]}



# In[27]:


import numpy as np
import pandas as pd


# In[7]:


#Question 1 (15 Points)
#Compute the euclidean distance between series (points) p and q, without using a packaged formula.

p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

e_dist = ((p - q) ** 2).sum()**0.5
print(e_dist)


# In[10]:


#Question 2 (15 Points)
#Change the order of columns of a dataframe. Interchange columns 'a' and 'c'.

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

cols = list(df.columns)
cols[0], cols[2] = cols[2], cols[0]
df = df[cols]
print(df)


# In[11]:


#Question 3 (15 Points)
#Change the order of columns of a dataframe.  Create a generic function to interchange two columns, without hardcoding column names.

df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

def switch_columns(df, col1, col2):
    colnames = df.columns.tolist()
    i, j = colnames.index(col1), colnames.index(col2)
    colnames[i], colnames[j] = colnames[j], colnames[i]
    return df[colnames]

print(switch_columns(df, 'a', 'c'))


# In[18]:


#Question 4 (15 Points)
#Format or suppress scientific notations in a pandas dataframe. Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
#input
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
print(df)
#>          random
#> 0  3.474280e-03
#> 1  3.951517e-05
#> 2  7.469702e-02
#> 3  5.541282e-28
#Desired Output
#>    random
#> 0  0.0035
#> 1  0.0000
#> 2  0.0747
#> 3  0.0000

print(df.round(4))



# In[21]:


#Question 5 (15 Points)
#Create a new column that contains the row number of nearest column by euclidean distance. 
#Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
#Input
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
df
#     p   q   r   s
# a  57  77  13  62
# b  68   5  92  24
# c  74  40  18  37
# d  80  17  39  60
# e  93  48  85  33
# f  69  55   8  11
# g  39  23  88  53
# h  63  28  25  61
# i  18   4  73   7
# j  79  12  45  34
#Desired Output
df
#    p   q   r   s nearest_row   dist
# a  57  77  13  62           i  116.0
# b  68   5  92  24           a  114.0
# c  74  40  18  37           i   91.0
# d  80  17  39  60           i   89.0
# e  93  48  85  33           i   92.0
# f  69  55   8  11           g  100.0
# g  39  23  88  53           f  100.0
# h  63  28  25  61           i   88.0
# i  18   4  73   7           a  116.0
# j  79  12  45  34           a   81.0



df = pd.DataFrame([[57,77,13,62],[68,5,92,24],[74,40,18,37],[80,17,39,60],[93,48,85,33],
                   [69,55,8,11],[39,23,88,53],[63,28,25,61],[18,4,73,7],[79,12,45,34]],
                  columns=list('pqrs'), index=list('abcdefghij'))
print(df)


nearest, dists = [], []
for i, row_i in df.iterrows():
    best, best_d = None, np.inf
    for j, row_j in df.iterrows():
        if i == j:
            continue
        d = np.sqrt(((row_i - row_j) ** 2).sum())
        if d < best_d:
            best, best_d = j, d
    nearest.append(best)
    dists.append(round(best_d, 1))

df['nearest_row'] = nearest
df['dist'] = dists
print(df)


# In[23]:


#Question 6 (15 Points)

#Correlation is a statistical technique that shows how two variables are related. 
#Pandas dataframe.corr() method is used for creating the correlation matrix. 
#It is used to find the pairwise correlation of all columns in the dataframe. Any na values are automatically excluded. 
#For any non-numeric data type columns in the dataframe it is ignored.

data = {'A': [45, 37, 0, 42, 50], 'B': [38, 31, 1, 26, 90], 'C': [10, 15, -10, 17, 100], 'D': [60, 99, 15, 23, 56], 'E': [76, 98, -0.03, 78, 90]}

df = pd.DataFrame(data)
print(df.corr())


# In[ ]:




