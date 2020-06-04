#drop some columns with certain type
drop_X_train = X_train.select_dtypes(exclude=['object'])

#drop columns with column name
X_train.drop(['col1','col2'], axis=1,inplace=True)

#drop rows with null in certain column
X.dropna(axis=0, subset=['col'], inplace=True)
