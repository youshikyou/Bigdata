#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('homepage_actions.csv')
df.head()


# In[3]:


df.shape


# In[4]:


df.nunique()


# In[6]:


df.groupby('group').nunique()


# In[6]:


df.action.value_counts()


# In[7]:


df.query('action == "click"').id.nunique() / df.query('action == "view"').id.nunique()


# In[10]:


df.timestamp.max(), df.timestamp.min()


# In[ ]:




