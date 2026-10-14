#!/usr/bin/env python
# coding: utf-8

# In[5]:


def filter_list(numbers, threshold):
    result = []
    for n in numbers:
        if n <= threshold:
            result.append(n)
    return result


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4, 4, 4, 20, 1 ]
limit = 4
print(filter_list(nums, limit))


# In[ ]:




