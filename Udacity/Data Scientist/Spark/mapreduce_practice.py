#!/usr/bin/env python
# coding: utf-8

# # MapReduce
# 
# The MapReduce programming technique was designed to analyze massive data sets across a cluster. In this Jupyter notebook, you'll get a sense for how Hadoop MapReduce works; however, this notebook will run locally rather than on a cluster.
# 
# The biggest difference between Hadoop and Spark is that Spark tries to do as many calculations as possible in memory, which avoids moving data back and forth across a cluster. Hadoop writes intermediate calculations out to disk, which can be less efficient. Hadoop is an older technology than Spark and one of the cornerstone big data technologies.
# 
# If you click on the Jupyter notebook logo at the top of the workspace, you'll be taken to the workspace directory. There you will see a file called "songplays.txt". This is a text file where each line represents a song that was played in the Sparkify app. The MapReduce code will count how many times each song was played. In other words, the code counts how many times the song title appears in the list.
# 
# 
# # MapReduce versus Hadoop MapReduce
# 
# Don't get confused by the terminology! MapReduce is a programming technique. Hadoop MapReduce is a specific implementation of the programming technique.
# 
# Some of the syntax will look a bit funny, so be sure to read the explanation and comments for each section. You'll learn more about the syntax in later lessons. 
# 
# Run each of the code cells below to see the output.

# In[1]:


# Install mrjob library. This package is for running MapReduce jobs with Python
# In Jupyter notebooks, "!" runs terminal commands from inside notebooks 

get_ipython().system(' pip install mrjob')


# In[2]:


get_ipython().run_cell_magic('file', 'wordcount.py', '# %%file is an Ipython magic function that saves the code cell as a file\n\nfrom mrjob.job import MRJob # import the mrjob library\n\nclass MRSongCount(MRJob):\n    \n    # the map step: each line in the txt file is read as a key, value pair\n    # in this case, each line in the txt file only contains a value but no key\n    # _ means that in this case, there is no key for each line\n    def mapper(self, _, song):\n        # output each line as a tuple of (song_names, 1) \n        yield (song, 1)\n\n    # the reduce step: combine all tuples with the same key\n    # in this case, the key is the song name\n    # then sum all the values of the tuple, which will give the total song plays\n    def reducer(self, key, values):\n        yield (key, sum(values))\n        \nif __name__ == "__main__":\n    MRSongCount.run()')


# In[3]:


# run the code as a terminal command
get_ipython().system(' python wordcount.py songplays.txt')


# # Summary of what happens in the code.
# 
# There is a list of songs in songplays.txt that looks like the following:
# 
# Deep Dreams
# Data House Rock
# Deep Dreams
# Data House Rock
# Broken Networks
# Data House Rock
# etc.....
# 
# During the map step, the code reads in the txt file one line at a time. The map steps outputs a set of tuples that look like this:
# 
# (Deep Dreams, 1)  
# (Data House Rock, 1)  
# (Deep Dreams, 1)  
# (Data House Rock, 1)  
# (Broken Networks, 1)  
# (Data House Rock, 1)  
# etc.....
# 
# Finally, the reduce step combines all of the values by keys and sums the values:  
# 
# (Deep Dreams, \[1, 1, 1, 1, 1, 1, ... \])  
# (Data House Rock, \[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, ...\])  
# (Broken Networks, \[1, 1, 1, ...\]  
# 
# With the output 
# 
# (Deep Dreams, 1131)  
# (Data House Rock, 510)  
# (Broken Networks, 828)  

# In[ ]:




