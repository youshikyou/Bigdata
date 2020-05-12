#!/usr/bin/env python
# coding: utf-8

# ### Fitting Logistic Regression
# 
# In this first notebook, you will be fitting a logistic regression model to a dataset where we would like to predict if a transaction is fraud or not.
# 
# To get started let's read in the libraries and take a quick look at the dataset.

# In[5]:


import numpy as np
import pandas as pd
import statsmodels.api as sm


df = pd.read_csv('./fraud_dataset.csv')
df.head()


# `1.` As you can see, there are two columns that need to be changed to dummy variables.  Replace each of the current columns to the dummy version.  Use the 1 for `weekday` and `True`, and 0 otherwise.  Use the first quiz to answer a few questions about the dataset.

# In[6]:


df['weekday'] = pd.get_dummies(df['day'])['weekday']
df[['not_fraud','fraud']] = pd.get_dummies(df['fraud'])
df = df.drop('not_fraud', axis=1)


# In[7]:


print(df['fraud'].mean())
print(df['weekday'].mean())
print(df.groupby('fraud').mean()['duration'])


# `2.` Now that you have dummy variables, fit a logistic regression model to predict if a transaction is fraud using both day and duration.  Don't forget an intercept!  Use the second quiz below to assure you fit the model correctly.

# In[4]:


df['intercept'] = 1
log_mod = sm.Logit(df['fraud'], df[['intercept', 'weekday', 'duration']])
results = log_mod.fit()
results.summary()


# In[ ]:




