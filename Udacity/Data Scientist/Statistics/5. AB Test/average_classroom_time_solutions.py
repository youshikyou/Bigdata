#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

np.random.seed(42)


# In[2]:


df = pd.read_csv('classroom_actions.csv')
df.head()


# In[3]:


# get the average classroom time for control group
control_mean = df.query('group == "control"').total_days.mean()

# get the average classroom time for experiment group
experiment_mean = df.query('group == "experiment"').total_days.mean()

# display average classroom time for each group
control_mean, experiment_mean


# In[4]:


# compute observed difference in classroom time
obs_diff = experiment_mean - control_mean

# display observed difference
obs_diff


# In[5]:


# create sampling distribution of difference in average classroom times
# with boostrapping
diffs = []
size = df.shape[0]
for _ in range(10000):
    b_samp = df.sample(size, replace=True)
    control_mean = b_samp.query('group == "control"').total_days.mean()
    experiment_mean = b_samp.query('group == "experiment"').total_days.mean()
    diffs.append(experiment_mean - control_mean)


# In[6]:


# convert to numpy array
diffs = np.array(diffs)


# In[7]:


# plot sampling distribution
plt.hist(diffs);


# In[8]:


# simulate distribution under the null hypothesis
null_vals = np.random.normal(0, diffs.std(), diffs.size)


# In[9]:


# plot null distribution
plt.hist(null_vals)

# plot line for observed statistic
plt.axvline(obs_diff, c='red')


# In[10]:


# compute p value
(null_vals > obs_diff).mean()


# In[ ]:




