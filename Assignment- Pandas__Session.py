#!/usr/bin/env python
# coding: utf-8

# # Import the necessary libraries

# In[1]:


#install lib

import pandas as pd
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'


# # Import the dataset

# In[2]:


df = pd.read_csv(url,sep='|')
df


# # Assign it to a variable called users and use the 'user_id' as index

# In[3]:


users = pd.read_csv(url,sep='|', index_col='user_id')
users


# # first 10 and last 10 entries

# In[4]:


print("*******First 10 entries*********")
users.head(10)


# In[5]:


print("*******Last 10 entries*********")
users.tail(10)


# # number of observations in the dataset

# In[6]:


print("Number of observations:",len(users.index))


# # What is the number of columns in the dataset?

# In[7]:


print("Number of Columns:",len(users.columns))


# # Print the name of all the columns

# In[8]:


users.keys()


# # How is the dataset indexed?

# In[9]:


users.index


# # What is the data type of each column?

# In[10]:


users.info()


# # Print only the occupation column

# In[11]:


users.occupation


# # How many different occupations are in this dataset?

# In[12]:


users["occupation"].value_counts().count()


# # What is the most frequent occupation?

# In[13]:


display(users['occupation'].mode())


# # DataFrame Info.

# In[14]:


users.info()


# # Describe all the columns

# In[15]:


users.describe(include="all")


# # Summarize only the occupation column

# In[16]:


users["occupation"].value_counts().sort_values(ascending=False)


# # What is the mean age of users?

# In[17]:


users.age.mean()


# # What is the age with least occurrence?

# In[18]:


a=users.age.value_counts()
b=a.index[-5]
b

