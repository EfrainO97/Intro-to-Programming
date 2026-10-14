#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
#This is to be done with a while loop. Note: the input will contain only integers or lists.


def inner_plus_one(input_list):
    level = [input_list]
    while True:
        next_level = []
        for lst in level:
            for item in lst:
                if isinstance(item, list):
                    next_level.append(item)
        if not next_level:
            break
        level=next_level
    return [x + 1 for x in level[0]]

input_list = [10,11,12,13,[14,15,16,[17,18]]]
print(inner_plus_one(input_list))


# In[ ]:





# In[ ]:




