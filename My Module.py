#!/usr/bin/env python
# coding: utf-8

# In[1]:


greet = lambda name : print(f"Good Morning {name}!")


# In[3]:


greet("Soumya")


# In[5]:


even = lambda L : [x for x in L if x%2 ==0]


# In[7]:


my_list = [100,3,9,34,5,77,89,44,20]
even(my_list)


# In[13]:


odd = lambda L : [x for x in L if x%2 !=0]


# In[15]:


my_list = [100,3,9,34,5,77,89,44,20]
odd(my_list)


# In[ ]:




