#!/usr/bin/env python
# coding: utf-8

# ### Interpreting Coefficients
# 
# It is important that not only can you fit complex linear models, but that you then know which variables you can interpret. 
# 
# In this notebook, you will fit a few different models and use the quizzes below to match the appropriate interpretations to your coefficients when possible.
# 
# In some cases, the coefficients of your linear regression models wouldn't be kept due to the lack of significance. But that is not the aim of this notebook - **this notebook is strictly to assure you are comfortable with how to interpret coefficients when they are interpretable at all**.

# In[1]:


import numpy as np
import pandas as pd
import statsmodels.api as sm;

df = pd.read_csv('./house_prices.csv')
df.head()


# We will be fitting a number of different models to this dataset throughout this notebook.  For each model, there is a quiz question that will allow you to match the interpretations of the model coefficients to the corresponding values.  If there is no 'nice' interpretation, this is also an option!
# 
# ### Model 1
# 
# `1.` For the first model, fit a model to predict `price` using `neighborhood`, `style`, and the `area` of the home.  Use the output to match the correct values to the corresponding interpretation in quiz 1 below.  Don't forget an intercept!  You will also need to build your dummy variables, and don't forget to drop one of the columns when you are fitting your linear model. It may be easiest to connect your interpretations to the values in the first quiz by creating the baselines as neighborhood C and home style **lodge**.

# In[2]:


dummies1_df = pd.get_dummies(df['neighborhood'])
dummies2_df = pd.get_dummies(df['style'])
new_df = df.join(dummies1_df)
newer_df = new_df.join(dummies2_df)
newer_df.head()


# In[5]:


newer_df['intercept'] = 1
lm = sm.OLS(newer_df['price'], newer_df[['intercept', 'A', 'B', 'ranch', 'victorian', 'area']])
results = lm.fit()
results.summary()


# ### Model 2
# 
# `2.` Now let's try a second model for predicting price.  This time, use `area` and `area squared` to predict price.  Also use the `style` of the home, but not `neighborhood` this time. You will again need to use your dummy variables, and add an intercept to the model. Use the results of your model to answer quiz questions 2 and 3.

# In[6]:


newer_df['area squared'] = newer_df['area']*newer_df['area']


# In[9]:


lm = sm.OLS(newer_df['price'], newer_df[['intercept', 'ranch', 'victorian', 'area squared', 'area']])
results = lm.fit()
results.summary()


# In[10]:


# Trying one more model, with neighborhoods also, responding to
#   prompt in question 3
lm = sm.OLS(newer_df['price'], newer_df[['intercept', 'A', 'B', 'ranch', 'victorian', 'area squared', 'area']])
results = lm.fit()
results.summary()


# In[11]:


Notice the R-squared value is 0.919 again, same as in model #1, 
  and the area-squared coefficient remains very low

