#!/usr/bin/env python
# coding: utf-8

# ### Housing Analysis
# 
# In this notebook, you will be replicating much of what you saw in this lesson using the housing data shown below.
# 
# After you complete this notebook and the set of quizzes that follow, you will be set to try out your skills on a couple new datasets to gain some additional practice.  **Ignore the warning message**.

# In[1]:


import numpy as np
import pandas as pd
import statsmodels.api as sm;

df = pd.read_csv('./house_price_area_only.csv')
df.head()


# `1.` Use the documentation [here](http://www.statsmodels.org/dev/regression.html) and the **statsmodels** library to fit a linear model to predict **price** based on **area**.  Obtain a summary of the results, and use them to answer the following quiz questions. Don't forget to add an intercept.

# In[2]:


df['intercept'] = 1
endog = df['price']
exog = sm.add_constant(df[['area','intercept']])

# Fit and summarize OLS model
mod = sm.OLS(endog, exog)
res = mod.fit()
print(res.summary())


# In[ ]:




