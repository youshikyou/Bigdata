#create a column that 
df = df.assign(new_column=(df[feature] == 'condition').astype(int))

#select columns
df.loc[:, ["col1", "col2", "col3"]]
