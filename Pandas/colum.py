#create a column that 
df = df.assign(new_column=(df[feature] == 'condition').astype(int))

#select columns
df.loc[:, ["col1", "col2", "col3"]]

df1 = df.query('col1 == "category1"').copy()



pandas.DataFrame.select_dtypes
DataFrame.select_dtypes(self, include=None, exclude=None) #Return a subset of the DataFrame’s columns based on the column dtypes.
