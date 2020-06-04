pd.get_dummies(X['feature list'])  # new column name will have the categories which are in each column.
#for example col is Street and this column has two unique categories: Grv1,Pave.
The dummied result in column name is like 'Street_Grvl', 'Street_Pave'
