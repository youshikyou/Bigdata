#!/usr/bin/env python
# coding: utf-8

# ### Interpreting Results of Logistic Regression
# 
# In this notebook (and quizzes), you will be getting some practice with interpreting the coefficients in logistic regression.  Using what you saw in the previous video should be helpful in assisting with this notebook.
# 
# The dataset contains four variables: `admit`, `gre`, `gpa`, and `prestige`:
# 
# * `admit` is a binary variable. It indicates whether or not a candidate was admitted into UCLA (admit = 1) our not (admit = 0).
# * `gre` is the GRE score. GRE stands for Graduate Record Examination.
# * `gpa` stands for Grade Point Average.
# * `prestige` is the prestige of an applicant alta mater (the school attended before applying), with 1 being the highest (highest prestige) and 4 as the lowest (not prestigious).
# 
# To start, let's read in the necessary libraries and data.

# In[15]:


import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("./admissions.csv")
df.head()


# There are a few different ways you might choose to work with the `prestige` column in this dataset.  For this dataset, we will want to allow for the change from prestige 1 to prestige 2 to allow a different acceptance rate than changing from prestige 3 to prestige 4.
# 
# 1. With the above idea in place, create the dummy variables needed to change prestige to a categorical variable, rather than quantitative, then answer quiz 1 below.

# In[16]:


df[['prest_1', 'prest_2', 'prest_3','prest_4',]] = pd.get_dummies(df['prestige'])


# In[17]:


df.head()


# In[18]:


df['prestige'].astype(str).value_counts()


# `2.` Now, fit a logistic regression model to predict if an individual is admitted using `gre`, `gpa`, and `prestige` with a baseline of the prestige value of `1`.  Use the results to answer quiz 2 and 3 below.  Don't forget an intercept.

# In[20]:



df['intercept'] = 1

logit_mod = sm.Logit(df['admit'], df[['intercept','gre', 'gpa', 'prest_2', 'prest_3', 'prest_4']])
results = logit_mod.fit()
results.summary()


# In[22]:


np.exp(results.params)


# In[23]:


1/_


# In[24]:


df.groupby('prestige').mean()['admit']


# In[5]:


0.21/0.5


# In[ ]:




