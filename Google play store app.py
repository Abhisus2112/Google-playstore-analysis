#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df = pd.read_csv('F:/Python/google play store/googleplaystore.csv')


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.shape


# In[6]:


print ("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])


# In[7]:


df.info()


# In[8]:


df.describe(include='all')


# In[9]:


##total number of App Contain Astrolory
df.columns


# In[13]:


df[df['App'].str.contains('Astrology')]


# In[14]:


len(df[df['App'].str.contains('Astrology')])


# In[16]:


##Find Average App Rati

df['Rating'].mean()


# In[18]:


##Find Total number of Unique Category

df['Category'].nunique()


# In[22]:


##Which Category Getting the highest average rating?

df.groupby('Category')['Rating'].mean().sort_values(ascending=False)


# In[27]:


##Find Totl Number of Apps having 5 star rating

len(df[df['Rating']==5.0])


# In[30]:


## Find Average Value of Review

df[df['Reviews']=='3.0M']


# In[31]:


df['Reviews'] = df['Reviews'].replace('3.0M', 3.0)


# In[33]:


df['Reviews'] = df['Reviews'].astype('float')


# In[35]:


df['Reviews'].dtype


# In[36]:


df['Reviews'].mean()


# In[37]:


##Find Total Number of Free and Paid Apps

df.groupby('Type')['Price'].sum()


# In[38]:


df['Type'].value_counts()


# In[42]:


##Which App has Maximum Reviews?

df[df['Reviews'].max()==df['Reviews']]['App']


# In[10]:


##Display top 5 Apps Having Highest Reviews
df['Reviews'].sort_values(ascending=False).head().index


# In[11]:


index = df['Reviews'].sort_values(ascending=False).head().index


# In[12]:


df.iloc[index]['App']


# In[56]:


## Find the Average rating of Free and Paid Apps

df.groupby('Type')['Rating'].mean()


# In[57]:


df.columns


# In[66]:


##Display Top 5 Apps Having Maximum Installs
df['Installs_1'] = df['Installs'].str.replace(',','')


# In[67]:


df['Installs_1']


# In[68]:


df.head(1)


# In[70]:


df['Installs_1'] = df['Installs_1'].str.replace('+','')


# In[71]:


df['Installs_1']


# In[72]:


df['Installs_1'] = df['Installs_1'].str.replace('Free','0')


# In[74]:


df.head()


# In[75]:


df['Installs_1'].astype('int')


# In[77]:


Index = df['Installs_1'].sort_values(ascending=False).head().index


# In[80]:


df.iloc[index]['App']


# In[82]:


import matplotlib.pyplot as plt


# In[83]:


df.boxplot()


# In[84]:


df.hist()


# In[85]:


df.isnull().sum()


# In[86]:


df[df['Rating']>5]


# In[87]:


df.drop([10472],inplace=True)


# In[88]:


df[10470:10475]


# In[89]:


df.boxplot()


# In[ ]:




