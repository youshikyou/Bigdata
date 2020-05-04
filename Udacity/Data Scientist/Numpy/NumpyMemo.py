#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# narray attibute
# shape,dtype

# narray method
# max(),min(),std()


# In[10]:


import numpy as np

x = np.array ([1,2,3,4,5]) 

x.dtype  # return the data type of the elements in that array
print(x.shape) # return the row collums of the array, note！！！ shape,size are attribute of the object, no bracket


# In[ ]:


x = np.array(([1,2.5,2.7],[2.6,7,9.1]), dtype = np.int64) # can define the datatype
print(x.shape)
print(x.dtype)


# In[18]:


x = np.array([2,3,4,5])
np.save('my_array',x)  #save the array to the current directory

y = np.load('my_array.npy')  # load the array but don't forget the npy suffix
print(y)


# In[20]:


x = np.zeros([3,4])  # create a 3*4 zeros array, to set the datatype x = np.zeros([3,4], dtype = int64)
print(x)


# In[21]:


x = np.ones([5,6]) # create a 5*6 with 1
print(x)


# In[26]:


x = np.full([5,5],10.0)  # fill a array with the number you want
print(x)


# In[27]:


x = np.eye(5)  # identity matrix 

x = np.diag([1,2,3,4,5])  # diagonal matrix
print(x)


# In[29]:


x = np.arange(10)  # 0~9 
print(x)


# In[31]:


x = np.arange(3, 10) # [3,10) array
print(x)


# In[32]:


x = np.arange(1,12,3) #[1,12,3] starting from 1 to 12 exclusive step = 3
print(x)


# In[35]:


x = np.linspace(0,25,10) # [0,25] starting 0 to 25 inclusive get 10 numbers.
print(x)


# In[36]:


x = np.linspace(0,25,10, endpoint=False) # exclude the endpoint
print(x)


# In[37]:


x = np.arange(20)
x = np.reshape(x,[4,5]) # reshape into 4*5
print(x)


# In[40]:


x = np.arange(20).reshape([10,2])
print(x)


# In[41]:


x = np.linspace(0,25,10, endpoint=False).reshape(5,2) # exclude the endpoint
print(x)


# In[43]:


x = np.random.random([3,4])  # generate 0~1 randomly by 3*4
print(x)


# In[128]:


x = np.random.randint(1,10,size = (4,4))# lowerbound inclusive, upperbound exclusive, shape
print(x)


# In[129]:


x = np.random.normal(0,0.1,size = (10,10))  # mean, standard deviation,shape


# In[54]:


# change the number by index
x = np.arange(1,10).reshape((3,3))
x[0,1] = 10  
print(x)


# In[57]:


# delete row or collumn by delete function with axis to manipulate the row or collumn
x = np.arange(1,10).reshape((3,3))
y = np.delete(x,0,axis = 0)
print(y)
w = np.delete(x,[0,2],axis = 1)
print(w)


# In[66]:


# append 
x = np.arange(5)
x = np.append(x,5)
x = np.append(x,[6,7])
print(x)

# append the row and collumn to the array
x = np.arange(1,10).reshape((3,3))
x = np.append(x,[[11,12,13],[1,3,6]],axis = 0)  # note the square bracket
x = np.append(x,[[10],[20],[30],[40],[50]], axis = 1)
print(x)


# In[72]:


# insert, (array,index,value)
x = np.arange(5)
x = np.insert(x,3,[9,10])
print(x)

# insert,(array, index, axis)
x = np.arange(1,10).reshape((3,3))

x = np.insert(x,1,[9,9,9],axis = 0)
x = np.insert(x,1,9,axis = 0)
x = np.insert(x,0,6,axis = 1)


# In[82]:


# stack, vstack,hstack

x = np.arange(3)

y = np.array(([9,9,9],[8,8,8])) 

w = np.vstack((x,y))
print(w)

z = np.arange(1,7).reshape((2,3))
w = np.hstack((y,z))
print(w)


# In[89]:


# slice
# narray[start:end], narray[start:], narray[:end], start index is included and end index is excluded
x = np.arange(1,21).reshape(4,5)
print(x)
y = x[1:4,2:5]
print(y)
w = x[1:,2:]
print(w)
z = x[:3,2:]
print(z)

# compare below to methods
h = x[:,2]
print(h)
# We select all the elements in the 3rd column but return a rank 2 ndarray
r = x[:,2:3]
print(r)


# In[100]:


# copy, 
#slice is a shallow copy. Any change in slice array will affact the original one.
x = np.arange(1,21).reshape(4,5)
z = x [1:,2:]
z [2,2] = 555

# to have deep copy
x = np.arange(1,21).reshape(4,5)
print(x)
z = x[1:,2:].copy()
z[2,2]=555
print(z)
print(x)


# In[105]:


# array slice
x = np.arange(1,21).reshape(4,5)
indices = np.array([1,3])
print(x)

y = x[indices,:]
print(y)

z = x[:,indices]
print(z)

# array diagnol extraction

w = np.diag(x)
print(w)

w = np.diag(x,k=1) # k is the arg to choose the diagnal ,negative is below, positive above the main diagnol
print(w)


# In[107]:


# unique function find the unique number
x = np.array([[1,2,3],[3,4,5],[3,2,1]])
w = np.unique(x)
print(w)


# In[113]:


#  Boolean extraction
x = np.arange(25).reshape(5,5)

y = x[x>7]
print(y)

z = x[x<10]
print(z)

w = x[(x>10)&(x<20)]
print(w)

x[(x>10)&(x<15)] = 1
print(x)


# In[121]:


# array intersaction,different,unition
x = np.array([2,3,4,5,6,7])
y = np.array([3,4,5,6])
z = np.array([5,6,7,8])

print(np.intersect1d(x,y))
print(np.setdiff1d(y,z))
print(np.union1d(x,z))


# In[136]:


# sort function , sort function would NOT affect the original array
x = np.random.randint(1,10,size=(9,))
print(np.sort(x))
print(x)
print(np.sort(np.unique(x)))
print('-'*20)

# sort function for array by row or collumn
x = np.random.randint(1,10,(3,3))
print(x)
print(np.sort(x,axis=0))
print(np.sort(x,axis=1))


print('-'*20)
# sort method, sort method would affect the original array
x = np.array([3,4,5,2,1])
print(x)
x.sort()
print(x)
print(x)


# In[138]:


# arithmetic operation and broadcastings

x = np.array([1,2,3,4])
y = np.array([5.5,6.5,7.5,8.5])

print('x + y = ', x + y)
print('add(x,y) = ', np.add(x,y))
print()
print('x - y = ', x - y)
print('subtract(x,y) = ', np.subtract(x,y))
print()
print('x * y = ', x * y)
print('multiply(x,y) = ', np.multiply(x,y))
print()
print('x / y = ', x / y)
print('divide(x,y) = ', np.divide(x,y))


# In[139]:


X = np.array([1,2,3,4]).reshape(2,2)
Y = np.array([5.5,6.5,7.5,8.5]).reshape(2,2)
print('X + Y = \n', X + Y)
print()
print('add(X,Y) = \n', np.add(X,Y))
print()
print('X - Y = \n', X - Y)
print()
print('subtract(X,Y) = \n', np.subtract(X,Y))
print()
print('X * Y = \n', X * Y)
print()
print('multiply(X,Y) = \n', np.multiply(X,Y))
print()
print('X / Y = \n', X / Y)
print()
print('divide(X,Y) = \n', np.divide(X,Y))


# In[171]:


# We create a rank 1 ndarray
x = np.array([1,2,3,4]).reshape((2,2))

print()
print('EXP(x) =', np.exp(x))
print()
print('SQRT(x) =',np.sqrt(x))
print()
print('POW(x,2) =',np.power(x,2)) # We raise all elements to the power of 2

print('each element + 2= ', x+2)
print('each element -2 = ', x-2)
print('each element *2 = ', x*2)
print('each element /2 = ', x/2)

y = np.array([1,10])  # y's 1st collumn to add to all elements in x's 1st collumn , y's 2nd collumn to add to all elements in x's 2nd column
print(x+y)

z = np.array([[10],[20]])  # add to x's 1st row vice versa
print(x+z)


# In[152]:


x = np.array(([1,2],[3,4]))
print(x)
print('average of collumn: ', x.mean(axis=0,dtype=np.int64))
print('average of row: ',x.mean(axis=1))
print('Average of all elements in x:', x.mean())
print()
print('Sum of all elements in x:', np.sum(x))
print('Sum of all elements in the columns of x:', x.sum(axis=0))
print('Sum of all elements in the rows of x:', x.sum(axis=1))
print()
print('Standard Deviation of all elements in x:', x.std())
print('Standard Deviation of all elements in the columns of x:', np.std(x,axis=0))
print('Standard Deviation of all elements in the rows of x:', x.std(axis=1))
print()
print('Median of all elements in x:', np.median(x))
print('Median of all elements in the columns of x:', np.median(x,axis=0))
print('Median of all elements in the rows of x:', np.median(x,axis=1))
print()
print('Maximum value of all elements in x:', x.max())
print('Maximum value of all elements in the columns of x:', x.max(axis=0))
print('Maximum value of all elements in the rows of x:', x.max(axis=1))
print()
print('Minimum value of all elements in x:', x.min())
print('Minimum value of all elements in the columns of x:', x.min(axis=0))
print('Minimum value of all elements in the rows of x:', x.min(axis=1))


# In[ ]:


# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc.. 

X = np.ones((4,4))*np.arange(1,5)
print(X)

