#!/usr/bin/env python
# coding: utf-8

# In[9]:


import ast
import sys

def deepest(lst, depth=0):
    best = (depth, lst)
    for item in lst:
        if isinstance(item, list):
            candidate = deepest(item, depth + 1)
            if candidate[0] > best[0]:
                best = candidate
    return best


def inner_plus_one(input_list):
    _, inner = deepest(input_list)
    return [x + 1 for x in inner]

if __name__ == "__main__":
    if len(sys.argv) > 1 and not sys.argv[1].startswith("-"):
        data = ast.literal_eval(sys.argv[1])
    else:
        data = [1,2,3,4,[5,6,7,[8,9]]]
    print(inner_plus_one(data))


# In[ ]:





# In[ ]:




