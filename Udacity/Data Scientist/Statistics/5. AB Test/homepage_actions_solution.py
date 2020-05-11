#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df = pd.read_csv('homepage_actions.csv')
df.head()

df.shape

df.nunique()

df.groupby('group').nunique()

df.action.value_counts()

df.query('action == "click"').id.nunique() / df.query('action == "view"').id.nunique()

df.timestamp.max(), df.timestamp.min()



