#select certain column with certain row categories.
df.loc[df.col1.isin(['cat1','cat2'])]

#select certain row 
df.loc[['row1']]

