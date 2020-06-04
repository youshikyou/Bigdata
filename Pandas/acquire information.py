#read csv
X = pd.read_csv('../input/train.csv', index_col='Id') 

#show the first five rows
X.head()
X.tail()

#each column statistic information
X.describe()

#column list
X.columns
