#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


data= pd.read_csv('C:/Users/HP/Downloads/Titanic.csv')


# In[4]:


data.head()


# In[5]:


data.info()


# In[6]:


#we describe the dataset
data.describe()


# In[9]:


data.isnull().sum()


# In[10]:


#find the mean of Age 
d1=data['Age'].mean()


# In[11]:


d1


# In[12]:


d1=round(d1)
d1


# In[13]:


#fill the rounded value with missing value using fillna() method
data['Age']=data['Age'].fillna(d1)


# In[14]:


data.isnull().sum()


# In[15]:


#same process for Fare column that has missing value
d2=round(data['Fare'].mean())
data['Fare']=data['Fare'].fillna(d2)
data.isnull().sum()


# In[17]:


data['Cabin'].unique()


# In[22]:


data['Cabin'].value_counts()


# In[18]:


#‘ffill’ stands for ‘forward fill’ and will propagate last valid observation forward.
data['Cabin'] = data['Cabin'].ffill()
data.isnull().sum()


# In[19]:


#bfill() will backward fill the NaN values that are present in the pandas dataframe
data['Cabin'] = data['Cabin'].bfill()
data.isnull().sum()


# In[21]:


#lets check our preprocessed dataset without any missing values
data.head()


# In[ ]:




