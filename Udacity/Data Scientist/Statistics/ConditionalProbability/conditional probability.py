import numpy as np
import pandas as pd

# load dataset
df = pd.read_csv('cancer_test_data.csv')

# What proportion of patients who tested positive has cancer?

(df.query('has_cancer == True')['test_result'] == 'Positive').mean() # this is wrong! this means cancer then test result is postive
df.query('test_result == \"Positive\"')['has_cancer'].mean() # this is right! this means test positive then has cancer!

# What proportion of patients who tested positive doesn't have cancer?
1-(df.query('has_cancer == True')['test_result'] == 'Positive').mean() #wrong
1 - df.query('test_result == \"Positive\"')['has_cancer'].mean() # right

# What proportion of patients who tested negative has cancer?
(df.query('has_cancer == True')['test_result'] == 'Negative').mean() #wrong
df.query('test_result == \"Negative\"')['has_cancer'].mean() # right

# What proportion of patients who tested negative doesn't have cancer?
1-(df.query('has_cancer == True')['test_result'] == 'Negative').mean() # wrong
1-df.query('test_result == \"Negative\"')['has_cancer'].mean() # right
