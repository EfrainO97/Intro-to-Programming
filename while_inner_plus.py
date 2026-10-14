#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Write a python program that, given an input list of any level of complexity/nestedness, will return the inner most list plus 1. 
#This is to be done with a while loop. Note: the input will contain only integers or lists.

import ast
import sys

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

if __name__ == "__main__":
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        data = ast.literal_eval(sys.argv[1])
    else:
        data = [1,2,3,4,[5,6,7,[8,9]]]
    print(inner_plus_one(data))


# In[ ]:





# In[ ]:




