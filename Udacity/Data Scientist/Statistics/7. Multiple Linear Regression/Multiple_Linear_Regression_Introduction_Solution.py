#!/usr/bin/env python
# coding: utf-8

# ### Multiple Linear Regression Introduction
# 
# In this notebook (and following quizzes), you will be creating a few simple linear regression models, as well as a multiple linear regression model, to predict home value.
# 
# Let's get started by importing the necessary libraries and reading in the data you will be using.

# In[2]:


import numpy as np
import pandas as pd
import statsmodels.api as sms;

df = pd.read_csv('./house_prices.csv')
df.head()


# `1.` Using statsmodels, fit three individual simple linear regression models to predict price.  You should have a model that uses **area**, another using **bedrooms**, and a final one using **bathrooms**.  You will also want to use an intercept in each of your three models.
# 
# Use the results from each of your models to answer the first two quiz questions below.

# In[3]:


df['intercept'] = 1
lm_bath = sms.OLS(df['price'], df[['intercept', 'bathrooms']])
results_bath = lm_bath.fit()
results_bath.summary()


# In[4]:


lm_bed = sms.OLS(df['price'], df[['intercept', 'bedrooms']])
results_bed = lm_bed.fit()
results_bed.summary()


# In[5]:


lm_area = sms.OLS(df['price'], df[['intercept', 'area']])
results_area = lm_area.fit()
results_area.summary()


# `2.` Now that you have looked at the results from the simple linear regression models, let's try a multiple linear regression model using all three of these variables  at the same time.  You will still want an intercept in this model.

# In[6]:


mlr = sms.OLS(df['price'], df[['intercept', 'area', 'bedrooms', 'bathrooms']])
results_mlr = mlr.fit()
results_mlr.summary()


# `3.` Along with using the **area**, **bedrooms**, and **bathrooms** you might also want to use **style** to predict the price.  Try adding this to your multiple linear regression model.  What happens?  Use the final quiz below to provide your answer.

# In[7]:


mlr2 = sms.OLS(df['price'], df[['intercept', 'area', 'bedrooms', 'bathrooms', 'style']])
results_mlr2 = mlr2.fit()
results_mlr2.summary()


# In[ ]:




