#!/usr/bin/env python
# coding: utf-8

# ### Regression Carats vs. Price
# 
# In this notebook, you will perform a similar analysis to the one you did in the previous notebook, but using a dataset holding the weight of a diamond in carats, and the price of the corresponding diamond in dollars.
# 
# To get started, let's read in the necessary libraries and the dataset.

# In[3]:


import numpy as np
import pandas as pd
import statsmodels.api as sms;
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv('./carats.csv', header= None)
df.columns = ['carats', 'price']
df.head()


# `1.` Similar to the last notebook, fit a simple linear regression model to predict price based on the weight of a diamond.  Use your results to answer the first question below.  Don't forget to add an intercept.

# In[4]:


df['intercept'] = 1

lm = sms.OLS(df['price'], df[['intercept', 'carats']])
results = lm.fit()
results.summary()


# `2.` Use [scatter](https://matplotlib.org/devdocs/gallery/lines_bars_and_markers/scatter_symbol.html#sphx-glr-gallery-lines-bars-and-markers-scatter-symbol-py) to create a scatterplot of the relationship between price and weight.  Then use the scatterplot and the output from your regression model to answer the second quiz question below.

# In[7]:


plt.scatter(df['carats'], df['price']);
plt.xlabel('Carats');
plt.ylabel('Price');
plt.title('Price vs. Carats');


# In[ ]:




