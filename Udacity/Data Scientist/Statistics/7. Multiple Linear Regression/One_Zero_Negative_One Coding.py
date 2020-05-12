#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.read_csv('./house_prices.csv')
df2 = df.copy()
df.head()


# In[10]:


## The below function creates 1, 0, -1 coded dummy variables.

def dummy_cat(df, col):
    '''
    INPUT:
    df - the dataframe where col is stored
    col - the categorical column you want to dummy (as a string)
    OUTPUT:
    df - the dataframe with the added columns
         for dummy variables using 1, 0, -1 coding
    '''
    for idx, val_0 in enumerate(df[col].unique()):
        if idx + 1 < df[col].nunique():            
            df[val_0] = df[col].apply(lambda x: 1 if x == val_0 else 0)
        else:    
            df[val_0] = df[col].apply(lambda x: -1 if x == val_0 else 0)
            for idx, val_1 in enumerate(df[col].unique()):
                if idx + 1 < df[col].nunique():
                    df[val_1] = df[val_0] + df[val_1]
                else:
                    del df[val_1]
    return df


# In[11]:


new_df = dummy_cat(df, 'style') # Use on style
new_df.head(10)


# In[12]:


new_df['intercept'] = 1

lm = sm.OLS(new_df['price'], new_df[['intercept', 'ranch', 'victorian']])
results = lm.fit()
results.summary()


# In[15]:


642100 + 66950 - 404000


# In[ ]:





# In[13]:


style_dummies = pd.get_dummies(df['style'])
new_df2 = df2.join(style_dummies)
new_df2.head(10)


# In[44]:


new_df2['intercept'] = 1

lm2 = sm.OLS(new_df2['price'], new_df2[['intercept', 'ranch', 'victorian']])
results2 = lm2.fit()
results2.summary()


# In[ ]:




