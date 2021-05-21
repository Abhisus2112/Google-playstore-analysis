#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('F:/Python/google play store/googleplaystore.csv')


# In[2]:


df.head(10)


# In[3]:


df.tail(10)


# In[4]:


df.shape


# In[6]:


print('Rows :',df.shape[0])
print('Columns :',df.shape[1])


# In[7]:


df.info()


# In[9]:


df.describe(include = 'all')


# # Total number of App Contains Astrology

# In[10]:


df.columns


# In[11]:


df[df['App'].str.contains('Astrology')]


# In[12]:


len(df[df['App'].str.contains('Astrology')])


# # Find Average App Rating

# In[13]:


df['Rating'].mean()


# # Find Total number of Unique Category

# In[14]:


df['Category'].nunique()


# # Which Category Getting the highest average rating?

# In[16]:


df.groupby('Category')['Rating'].mean().sort_values(ascending=False)


# # Find Total Number of Apps having 5 star rating

# In[17]:


len(df[df['Rating']==5.0])


# # Find Average Value of Review

# In[20]:


df[df['Reviews']== '3.0M']


# In[21]:


df['Reviews'] = df['Reviews'].replace('3.0M', 3.0)


# In[22]:


df['Reviews'] = df['Reviews'].astype('float')


# In[23]:


df['Reviews'].dtype


# In[24]:


df['Reviews'].mean()


# # Find Total number of free and paid apps

# In[25]:


df.columns


# In[30]:


#df.groupby('Type')['Price'].sum()


# In[31]:


df['Type'].value_counts()


# # Which app has maximum reviews?

# In[32]:


df.columns


# In[36]:


df['Reviews'].max()


# In[39]:


df[df['Reviews'].max()==df['Reviews']]


# In[40]:


df[df['Reviews'].max()==df['Reviews']]['App']


# # Display top 5 Apps has maximum reviews?

# In[48]:


Index = df['Reviews'].sort_values(ascending=False).head().index


# In[46]:


df.iloc[Index]


# In[49]:


df.iloc[Index]['App']


# # Find the Average rating of Free and Paid Apps

# In[50]:


df.groupby('Type')['Rating'].mean()


# # Display top 5 apps having maximum installs

# In[66]:


df['Install_1'] = df['Installs'].str.replace(',', '')


# In[67]:


df['Install_1']


# In[68]:


df.head(10)


# In[71]:


df['Install_1'] = df['Install_1'].replace('+', '')


# In[72]:


df['Install_1']


# In[73]:


df['Install_1'] = df['Install_1'].replace('Free','0')


# In[74]:


df['Install_1']


# In[75]:


df.head()


# In[76]:


Index1 = df['Install_1'].sort_values(ascending=False).head().index


# In[77]:


df.iloc[Index1]['App']


# In[78]:


import matplotlib.pyplot as plt


# In[79]:


df.boxplot()


# In[80]:


df.hist()


# In[81]:


df.isnull().sum()


# In[82]:


df[df['Rating']>5]


# In[83]:


df.drop([10472],inplace=True)


# In[84]:


df[10470:10475]


# In[85]:


df.boxplot()


# In[ ]:




