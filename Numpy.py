#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This assignment consists of five questions for a total of 75 points. Submit your results as a .py file via your GitHub repository.

#1. Import numpy as np and print the version number. 





#2. Create a 1D array of numbers from 0 to 9. Desired output:

#> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])






#3. Import a dataset with numbers and texts keeping the text intact in python numpy. Use the iris dataset available from Iris dataset. (20 Points)





#4. Find the position of the first occurrence of a value greater than 1.0 in petalwidth 4th column of iris dataset. 
#Use the iris dataset available from Iris dataset. 





#5. From the array a, replace all values greater than 30 to 30 and less than 10 to 10.

#Input:

#np.random.seed(100)
#a = np.random.uniform(1,50, 20)


# In[1]:


#1
import numpy as np 
print(np.__version__)

#2
arr=np.arange(10)
print(repr(arr))

#3
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
iris = np.genfromtxt(url, delimiter=',', dtype="object")
print(iris[:1])

#4
petalwidth = iris[:,3].astype(float)
petalwidth[:10]

first_pos = np.argmax(petalwidth > 1.0)
print(first_pos) 

#5
np.random.seed(100)
a = np.random.uniform(1,50,20)
print(a)

result = np.clip(a,10,30)
print(result)




# In[ ]:




