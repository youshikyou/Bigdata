#!/usr/bin/env python
# coding: utf-8

# ### Confidence Intervals - Part I
# 
# First let's read in the necessary libraries and the dataset.  You also have the full and reduced versions of the data available.  The reduced version is an example of you would actually get in practice, as it is the sample.  While the full data is an example of everyone in your population.



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

np.random.seed(42)

coffee_full = pd.read_csv('../data/coffee_dataset.csv')
coffee_red = coffee_full.sample(200) #this is the only data you might actually get in the real world.


# `1.` What is the proportion of coffee drinkers in the sample?  What is the proportion of individuals that don't drink coffee?

coffee_red['drinks_coffee'].mean() # Drink Coffee


1 - coffee_red['drinks_coffee'].mean() # Don't Drink Coffee


# `2.` Of the individuals who do not drink coffee, what is the average height?

coffee_red[coffee_red['drinks_coffee'] == False]['height'].mean()


# `3.` Simulate 200 "new" individuals from your original sample of 200.  What are the proportion of coffee drinkers in your bootstrap sample?  How about individuals that don't drink coffee?

bootsamp = coffee_red.sample(200, replace = True)

bootsamp['drinks_coffee'].mean() # Drink Coffee and 1 minus gives the don't drink


# `4.` Now simulate your bootstrap sample 10,000 times and take the mean height of the non-coffee drinkers in each sample.  Plot the distribution, and pull the values necessary for a 95% confidence interval.  What do you notice about the sampling distribution of the mean in this example?

boot_means = []
for _ in range(10000):
    bootsamp = coffee_red.sample(200, replace = True)
    boot_mean = bootsamp[bootsamp['drinks_coffee'] == False]['height'].mean()
    boot_means.append(boot_mean)
    
plt.hist(boot_means); # Looks pretty normal

np.percentile(boot_means, 2.5), np.percentile(boot_means, 97.5)



# `5.`  Did your interval capture the actual average height of coffee drinkers in the population?  Look at the average in the population and the two bounds provided by your 95% confidence interval, and then answer the final quiz question below.


coffee_full[coffee_full['drinks_coffee'] == False]['height'].mean() 

# Captured by our interval, but not the exact same as the sample mean






"""
For 10,000 iterations bootstrap your sample data, 
compute the difference in the average height for coffee drinkers and the average height non-coffee drinkers for individuals under 21 years old. 
Using your sampling distribution, build a 95% confidence interval. 
"""
diffs_coff_under21 = []
for _ in range(10000):
    bootsamp = sample_data.sample(200, replace = True)
    under21_coff_mean = bootsamp.query("age == '<21' and drinks_coffee == True")['height'].mean()
    under21_nocoff_mean = bootsamp.query("age == '<21' and drinks_coffee == False")['height'].mean()
    #bootsamp[(bootsamp['age']=='<21')&(bootsamp['drinks_coffee']==False)]['height'].mean()也可以
    diffs_coff_under21.append(under21_nocoff_mean - under21_coff_mean)
    
np.percentile(diffs_coff_under21, 2.5), np.percentile(diffs_coff_under21, 97.5)
# For the under21 group, we have evidence that the non-coffee drinkers are on average taller


