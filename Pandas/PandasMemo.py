#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

# create a Pandas series
groceries = pd.Series(data = [30,6,'Yes','No'], index = ['eggs','apples','milk','bread'])
groceries

# get pandas series information

print('Groceries has shape:', groceries.shape)
print('Groceries has dimension:', groceries.ndim)
print('Groceries has a total of', groceries.size, 'elements')

# get index and data of Groceries
print('The data in Groceries is:', groceries.values)
print('The index of Groceries is:', groceries.index)

# check whether bananas is a food item (an index) in Groceries
x = 'bananas' in groceries

# check whether bread is a food item (an index) in Groceries
y = 'bread' in groceries

#  print the results
print('Is bananas an index label in Groceries:', x)
print('Is bread an index label in Groceries:', y)


# In[ ]:


# We access elements in Groceries using index labels:

# We use a single index label
print('How many eggs do we need to buy:', groceries['eggs'])
print()

# we can access multiple index labels
print('Do we need milk and bread:\n', groceries[['milk', 'bread']]) 
print()

# we use loc to access multiple index labels
print('How many eggs and apples do we need to buy:\n', groceries.loc[['eggs', 'apples']]) 
print()

# We access elements in Groceries using numerical indices:

# we use multiple numerical indices
print('How many eggs and apples do we need to buy:\n',  groceries[[0, 1]]) 
print()

# We use a negative numerical index
print('Do we need bread:\n', groceries[[-1]]) 
print()

# We use a single numerical index
print('How many eggs do we need to buy:', groceries[0]) 
print()
# we use iloc to access multiple numerical indices
print('Do we need milk and bread:\n', groceries.iloc[[2, 3]]) 


# In[ ]:


# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We change the number of eggs to 2

groceries.loc['eggs'] = 2
groceries['eggs'] = 16
groceries[['eggs']] =10 

# We display the changed grocery list
print()
print('Modified Grocery List:\n', groceries)


# In[ ]:


# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list. The drop function removes elements out of place
print()
print('We remove apples (out of place):\n', groceries.drop('apples'))

# When we remove elements out of place the original Series remains intact. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples out of place:\n', groceries)

# We display the original grocery list
print('Original Grocery List:\n', groceries)

# We remove apples from our grocery list in place by setting the inplace keyword to True
groceries.drop('apples', inplace = True)

# When we remove elements in place the original Series its modified. To see this
# we display our grocery list again
print()
print('Grocery List after removing apples in place:\n', groceries)


# In[ ]:


# We create a Pandas Series that stores a grocery list of just fruits
fruits= pd.Series(data = [10, 6, 3,], index = ['apples', 'oranges', 'bananas'])

# We display the fruits Pandas Series
fruits

# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)

# We perform basic element-wise operations using arithmetic symbols
print()
print('fruits + 2:\n', fruits + 2) # We add 2 to each item in fruits
print()
print('fruits - 2:\n', fruits - 2) # We subtract 2 to each item in fruits
print()
print('fruits * 2:\n', fruits * 2) # We multiply each item in fruits by 2 
print()
print('fruits / 2:\n', fruits / 2) # We divide each item in fruits by 2
print()


# In[ ]:


# We print fruits for reference
print('Original grocery list of fruits:\n ', fruits)
print()

# We add 2 only to the bananas
print('Amount of bananas + 2 = ', fruits['bananas'] + 2)
print()

# We subtract 2 from apples
print('Amount of apples - 2 = ', fruits.iloc[0] - 2)
print()

# We multiply apples and oranges by 2
print('We double the amount of apples and oranges:\n', fruits[['apples', 'oranges']] * 2)
print()

# We divide apples and oranges by 2
print('We half the amount of apples and oranges:\n', fruits.loc[['apples', 'oranges']] / 2)
print()
# We multiply our grocery list by 2
print('double the list: ',groceries * 2)


# In[ ]:


# We create a dictionary of Pandas Series 
items = {'Bob' : pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
         'Alice' : pd.Series(data = [40, 110, 500, 45], index = ['book', 'glasses', 'bike', 'pants'])}

# We print the type of items to see that it is a dictionary
print(type(items))

# We create a Pandas DataFrame by passing it a dictionary of Pandas Series
shopping_carts = pd.DataFrame(items)

# We display the DataFrame
shopping_carts

# We print some information about shopping_carts
print('shopping_carts has shape:', shopping_carts.shape)
print('shopping_carts has dimension:', shopping_carts.ndim)
print('shopping_carts has a total of:', shopping_carts.size, 'elements')
print()
print('The data in shopping_carts is:\n', shopping_carts.values)
print()
print('The row index in shopping_carts is:', shopping_carts.index)
print()
print('The column index in shopping_carts is:', shopping_carts.columns)


# We Create a DataFrame that only has Bob's data
bob_shopping_cart = pd.DataFrame(items, columns=['Bob'])

# We display bob_shopping_cart
bob_shopping_cart

# We Create a DataFrame that only has selected items for both Alice and Bob
sel_shopping_cart = pd.DataFrame(items, index = ['pants', 'book'])

# We display sel_shopping_cart
sel_shopping_cart

# We Create a DataFrame that only has selected items for Alice
alice_sel_shopping_cart = pd.DataFrame(items, index = ['glasses', 'bike'], columns = ['Alice'])

# We display alice_sel_shopping_cart
alice_sel_shopping_cart


# In[ ]:


# We create a dictionary of Pandas Series without indexes
data = {'Bob' : pd.Series([245, 25, 55]),
        'Alice' : pd.Series([40, 110, 500, 45])}

# We create a DataFrame
df = pd.DataFrame(data)

# We display the DataFrame
df


# In[ ]:


#create DataFrames from a dictionary of lists (arrays),all the lists (arrays) in the dictionary must be of the same length

# create a dictionary of lists (arrays)
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}

# We create a DataFrame 
df = pd.DataFrame(data)

# We display the DataFrame
df


# In[ ]:


# We create a dictionary of lists (arrays)   be note the different from the create a list of dictionaries!!!!
data = {'Integers' : [1,2,3],
        'Floats' : [4.5, 8.2, 9.6]}

# We create a DataFrame and provide the row index
df = pd.DataFrame(data, index = ['label 1', 'label 2', 'label 3'])

# We display the DataFrame
df


# In[ ]:


# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame 
store_items = pd.DataFrame(items2)

# We display the DataFrame
store_items


# In[ ]:


# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35}, 
          {'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2'])

# We display the DataFrame
store_items


# In[ ]:


# We print the store_items DataFrame
print(store_items)

# We access rows, columns and elements using labels
print()
print('How many bikes are in each store:\n', store_items[['bikes']])
print()
print('How many bikes and pants are in each store:\n', store_items[['bikes', 'pants']])
print()
print('What items are in Store 1:\n', store_items.loc[['store 1']])
print()


"""
It is important to know that when accessing individual elements in a DataFrame, 
as we did in the last example above, the labels should always be provided with the column label first, 
i.e. in the form dataframe[column][row]. For example, when retrieving the number bikes in store 2, 
we first used the column label bikes and then the row label store 2. If you provide the row label first you will get an error.
"""

print('How many bikes are in Store 2:', store_items['bikes']['store 2'])

# We add a new column named shirts to our store_items DataFrame indicating the number of
# shirts in stock at each store. We will put 15 shirts in store 1 and 2 shirts in store 2
store_items['shirts'] = [15,2]

# We display the modified DataFrame
store_items

# We make a new column called suits by adding the number of shirts and pants
store_items['suits'] = store_items['pants'] + store_items['shirts']

# We display the modified DataFrame
store_items


# In[ ]:


# We create a dictionary from a list of Python dictionaries that will number of items at the new store

#!!!! be aware of this definition with 
new_items = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]

# We create new DataFrame with the new_items and provide and index labeled store 3
new_store = pd.DataFrame(new_items, index = ['store 3']) 

# We display the items at the new store
new_store

# We append store 3 to our store_items DataFrame
store_items = store_items.append(new_store)

# We display the modified DataFrame
store_items



# In[ ]:


# We add a new column using data from particular rows in the watches column
store_items['new watches'] = store_items['watches'][1:]

# We display the modified DataFrame
store_items


# In[ ]:


"""
It is also possible, to insert new columns into the DataFrames anywhere we want.
The dataframe.insert(loc,label,data) method allows us to insert a new column in the dataframe at location loc, 
with the given column label, and given data. Let's add new column named shoes right before the suits column.
Since suits has numerical index value 4 then we will use this value as loc. Let's see how this works:
"""
# We insert a new column with label shoes right before the column with numerical index 4
store_items.insert(4, 'shoes', [8,5,0])

# we display the modified DataFrame
store_items


# In[ ]:


"""
Just as we can add rows and columns we can also delete them. 
To delete rows and columns from our DataFrame we will use the .pop() and .drop() methods. 
The .pop() method only allows us to delete columns, 
while the .drop() method can be used to delete both rows and columns by use of the axis keyword
"""
# We remove the new watches column
store_items.pop('new watches')

# we display the modified DataFrame
store_items

# We remove the watches and shoes columns
store_items = store_items.drop(['watches', 'shoes'], axis = 1)

# we display the modified DataFrame
store_items

# We remove the store 2 and store 1 rows
store_items = store_items.drop(['store 2', 'store 1'], axis = 0)

# we display the modified DataFrame
store_items


# In[ ]:


# We change the column label bikes to hats
store_items = store_items.rename(columns = {'bikes': 'hats'})

# we display the modified DataFrame
store_items

# We change the row label from store 3 to last store
store_items = store_items.rename(index = {'store 3': 'last store'})

# we display the modified DataFrame
store_items


# In[ ]:


# change the index to be one of the columns in the DataFrame
   
# We change the row index to be the data in the pants column
store_items = store_items.set_index('pants')

# we display the modified DataFrame
store_items


# In[ ]:


# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

# We display the DataFrame
store_items


# In[ ]:


# We count the number of NaN values in store_items
x =  store_items.isnull().sum().sum()

# We print x
print('Number of NaN values in our DataFrame:', x)


# In[ ]:


"""
In the above example, the .isnull() method returns a Boolean DataFrame of the same size 
as store_items and indicates with True the elements that have NaN values and with False the elements that are not. 
"""
store_items.isnull()

"""
In Pandas, logical True values have numerical value 1 and logical False values have numerical value 0.
Therefore, we can count the number of NaN values by counting the number of logical True values. 
In order to count the total number of logical True values we use the .sum() method twice. 
We have to use it twice because the first sum returns a Pandas Series with the sums of logical True values along columns, as we see below:

"""
store_items.isnull().sum()  #The second sum will then add up the 1s in the above Pandas Series.


# We print the number of non-NaN values in our DataFrame
print()
print('Number of non-NaN values in the columns of our DataFrame:\n', store_items.count())


# We drop any rows with NaN values,it is out of place, if you want to in place should set inplace=True
store_items.dropna(axis = 0)

# We drop any columns with NaN values
store_items.dropna(axis = 1)


# We replace all NaN values with 0
"""
Notice that the .fillna() method replaces (fills) the NaN values out of place. 
This means that the original DataFrame is not modified. 
You can always replace the NaN values in place by setting the keyword inplace = True inside the fillna() function.
"""

store_items.fillna(0)

# We replace NaN values with the previous value in the column
store_items.fillna(method = 'ffill', axis = 0)

# We replace NaN values with the previous value in the row
store_items.fillna(method = 'ffill', axis = 1)

# We replace NaN values with the next value in the column
store_items.fillna(method = 'backfill', axis = 0)

# We replace NaN values with the next value in the row
store_items.fillna(method = 'backfill', axis = 1)

# We replace NaN values by using linear interpolation using column values
store_items.interpolate(method = 'linear', axis = 0)

# We replace NaN values by using linear interpolation using row values
store_items.interpolate(method = 'linear', axis = 1)


# In[ ]:


df = pd.DataFrame({'age': [5, 6, np.NaN],
                   'born': [pd.NaT, pd.Timestamp('1939-05-27'),
                            pd.Timestamp('1940-04-25')],
                   'name': ['Alfred', 'Batman', ''],
                   'toy': [None, 'Batmobile', 'Joker']})
df.notna()


# In[ ]:


pd.set_option('precision', 1)



books = pd.Series(data = ['Great Expectations', 'Of Mice and Men', 'Romeo and Juliet', 'The Time Machine', 'Alice in Wonderland' ])
authors = pd.Series(data = ['Charles Dickens', 'John Steinbeck', 'William Shakespeare', ' H. G. Wells', 'Lewis Carroll' ])

user_1 = pd.Series(data = [3.2, np.nan ,2.5])
user_2 = pd.Series(data = [5., 1.3, 4.0, 3.8])
user_3 = pd.Series(data = [2.0, 2.3, np.nan, 4])
user_4 = pd.Series(data = [4, 3.5, 4, 5, 4.2])

# Users that have np.nan values means that the user has not yet rated that book.
# Use the data above to create a Pandas DataFrame that has the following column
# labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3', 'User 4'. Let Pandas
# automatically assign numerical row indices to the DataFrame. 

# Create a dictionary with the data given above
dat = {'Authors':authors,'Books Title':books,'User 1':user_1,'User 2':user_2,'User 3':user_3,'User 4':user_4}


# Use the dictionary to create a Pandas DataFrame
book_ratings = pd.DataFrame(dat)


# If you created the dictionary correctly you should have a Pandas DataFrame
# that has column labels: 'Author', 'Book Title', 'User 1', 'User 2', 'User 3',
# 'User 4' and row indices 0 through 4.

# Now replace all the NaN values in your DataFrame with the average rating in
# each column. Replace the NaN values in place. HINT: you can use the fillna()
# function with the keyword inplace = True, to do this. Write your code below:
#book_ratings.notna().sum()
book_ratings.fillna(book_ratings.mean(), inplace = True)   # default is row mean, specify axis=0 is by collumn


# In[ ]:


"""
In machine learning you will most likely use databases from many sources to train your learning algorithms. 
Pandas allows us to load databases of different formats into DataFrames. 
One of the most popular data formats used to store databases is csv. 
CSV stands for Comma Separated Values and offers a simple format to store data. 
We can load CSV files into Pandas DataFrames using the pd.read_csv() function.
Let's load Google stock data into a Pandas DataFrame. The GOOG.csv file contains Google stock data from 8/19/2004 till 10/13/2017 taken from Yahoo Finance.
"""
# We load Google stock data in a DataFrame
Google_stock = pd.read_csv('./GOOG.csv')

# We print some information about Google_stock
print('Google_stock is of type:', type(Google_stock))
print('Google_stock has shape:', Google_stock.shape)


"""
When dealing with large datasets like this one, it is often useful just to take a look at the first few rows of data instead of the whole dataset. 
We can take a look at the first 5 rows of data using the .head() method, as shown below
"""
Google_stock.head()
Google_stock.tail()  # the last 5 rows of data,We can also optionally use .head(N) or .tail(N) to display the first and last N rows of data, respectively.

"""
Let's do a quick check to see whether we have any NaN values in our dataset. 
To do this, we will use the .isnull() method followed by the .any() method to check whether any of the columns contain NaN values.
"""
Google_stock.isnull().any()

"""
When dealing with large datasets, it is often useful to get statistical information from them. 
Pandas provides the .describe() method to get descriptive statistics on each column of the DataFrame. 
Let's see how this works:
"""
# We get descriptive statistics on our stock data
Google_stock.describe()

# We get descriptive statistics on a single column of our DataFrame
Google_stock['Adj Close'].describe()

# We print information about our DataFrame  
print()
print('Maximum values of each column:\n', Google_stock.max())
print()
print('Minimum Close value:', Google_stock['Close'].min())
print()
print('Average value of each column:\n', Google_stock.mean())

"""
Another important statistical measure is data correlation. 
Data correlation can tell us, for example, if the data in different columns are correlated. 
We can use the .corr() method to get the correlation between different columns, as shown below:
"""
# We display the correlation between columns
Google_stock.corr()


# In[ ]:


"""
The .groupby() method allows us to group data in different ways. Let's see how we can group data to get different types of information. 
For the next examples we are going to load fake data about a fictitious company.
"""
# We load fake Company data in a DataFrame
data = pd.read_csv('./fake_company.csv')

data

"""
Let's calculate how much money the company spent in salaries each year. To do this, 
we will group the data by Year using the .groupby() method and then we will add up the salaries of all the employees by using the .sum() method.
"""
# We display the total amount of money spent in salaries each year
data.groupby(['Year'])['Salary'].sum()

"""
Now, let's suppose I want to know what was the average salary for each year. In this case, we will group the data by Year using the .groupby() method, 
just as we did before, and then we use the .mean() method to get the average salary.
Let's see how this works
"""
# We display the average salary per year
data.groupby(['Year'])['Salary'].mean()



# We display the total salary each employee received in all the years they worked for the company
data.groupby(['Name'])['Salary'].sum()


"""
Now let's see what was the salary distribution per department per year. In this case we will group 
the data by Year and by Department using the .groupby() method and then we will add up the salaries for each department. 
Let's see the result
"""
# We display the salary distribution per department per year.
data.groupby(['Year', 'Department'])['Salary'].sum()


# Read timestamp convert into int
# Add new columns for timestamp features day, hour, minute, and second
clicks = click_data.copy()
clicks['day'] = clicks['click_time'].dt.day.astype('uint8')
clicks['hour'] = clicks['click_time'].dt.hour.astype('uint8')





