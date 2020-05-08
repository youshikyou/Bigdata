#!/usr/bin/env python
# coding: utf-8

# # Cancer Test Results


# load dataset
import pandas as pd

cancer_data = pd.read_csv('cancer_test_data.csv')



# number of patients
cancer_data.describe
#cancer_data.shape

# number of patients with cancer
num_patients_w_cancer = cancer_data[cancer_data['has_cancer']]['has_cancer'].count()
#cancer_data.has_cancer.sum()
print(num_patients_w_cancer)


# number of patients without cancer
num_patients_wo_cancer=cancer_data[~cancer_data['has_cancer']]['has_cancer'].count()
# (cancer_data.has_cancer == False).sum()
print(num_patients_wo_cancer)


# proportion of patients with cancer
prop_w_cancer = num_patients_w_cancer/cancer_data.shape[0]

#cancer_data.has_cancer.mean()
print(prop_w_cancer)




# proportion of patients without cancer
prop_wo_cancer = num_patients_wo_cancer/cancer_data.shape[0]

# 1 - cancer_data.has_cancer.mean()
print(prop_wo_cancer)


# proportion of patients with cancer who test positive
num_patients_w_cancer_p = cancer_data[(cancer_data['has_cancer'])&(cancer_data['test_result']=='Positive')]['has_cancer'].count()
print(num_patients_w_cancer_p/num_patients_w_cancer)




# proportion of patients with cancer who test negative
num_patients_w_cancer_n = cancer_data[(cancer_data['has_cancer'])&(cancer_data['test_result']=='Negative')]['has_cancer'].count()
print(num_patients_w_cancer_n/num_patients_w_cancer)



# proportion of patients without cancer who test positive
num_patients_wo_cancer_p = cancer_data[(~cancer_data['has_cancer'])&(cancer_data['test_result']=='Positive')]['has_cancer'].count()
print(num_patients_wo_cancer_p/num_patients_wo_cancer)

#(cancer_data.query('has_cancer == False')['test_result'] == 'Negative').mean()


# proportion of patients without cancer who test negative
num_patients_wo_cancer_n = cancer_data[(~cancer_data['has_cancer'])&(cancer_data['test_result']=='Negative')]['has_cancer'].count()
print(num_patients_wo_cancer_n/num_patients_wo_cancer)
