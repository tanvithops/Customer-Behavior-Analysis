#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_csv("customer_shopping_behavior.csv")


# In[3]:


df 


# In[4]:


df.head(5)


# In[5]:


df.info()


# In[6]:


df.describe(include='all')


# In[7]:


df.isnull().sum()


# In[8]:


#Filling null values of 'Review Rating' with median grouped by 'category' so there isnt any bias.


# In[9]:


df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))


# In[10]:


df.isnull().sum()


# In[11]:


# Snake Casing all column names for making it easier to deal with in future.


# In[12]:


df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')


# In[13]:


df.columns


# In[14]:


df=df.rename(columns={'purchase_amount_(usd)':'purchase_amount'}) #Fixing one of the column names


# In[15]:


df.columns


# In[16]:


#Creating a new column called age_group to group customers by age: adult,young etc


# In[17]:


labels=['Young Adult','Adult','Middle Aged','Senior']
df['age_group']=pd.qcut(df['age'],q=4,labels=labels)


# In[18]:


df.head(5)


# In[19]:


df[['age','age_group']].head(10)


# In[20]:


# Creating 'purchase_freq_days' from 'frequency_of_purchases'


# In[21]:


frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
df['purchase_frequency_days']=df['frequency_of_purchases'].map(frequency_mapping)


# In[22]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[23]:


df[['discount_applied','promo_code_used']].head(10) #checking redundant columns


# In[24]:


(df['discount_applied']==df['promo_code_used']).all() #checks if cols have the same values.


# In[25]:


df=df.drop('promo_code_used',axis=1)


# In[26]:


df.columns


# In[27]:


#connecting mysql and jupyter


# In[28]:


pip install pymysql sqlalchemy


# In[29]:


import pandas as pd
import pymysql
from sqlalchemy import create_engine


# In[30]:


engine = create_engine("mysql+pymysql://root:tanvi@localhost/customer_shopping")


# In[31]:


df_test = pd.read_sql("SELECT 1 as test_col", engine)
df_test


# In[32]:


df.to_sql("customer_shopping_data", con=engine, if_exists="replace", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




