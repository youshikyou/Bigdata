#create a column that 
df = df.assign(new_column=(df[feature] == 'condition').astype(int))
