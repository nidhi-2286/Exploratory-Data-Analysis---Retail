#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("seaborn")


# In[7]:


#Importing dataset
df = pd.read_csv("C:/Users/user/OneDrive/Desktop/SampleSuperstore.csv")
df


# In[8]:


df.head()


# In[9]:


#Chechking null values
df.isnull().sum()


# In[10]:


df.shape


# In[15]:


#Count of each category under shipment mode
df["Ship Mode"].value_counts()


# In[16]:


df["State"].nunique()


# In[17]:


df["City"].nunique()


# In[18]:


df["Segment"].nunique()


# In[19]:


#Dropping columns which didnt affect profit much
df = df.drop(["Country", "Postal Code"], axis = 1)


# In[20]:


df


# In[21]:


#Checking for duplicate values
df.duplicated().sum()


# In[23]:


#Dropping duplicate values
df.drop_duplicates(inplace = True)


# In[24]:


df


# In[26]:


#Visualizing through Graphs
sns.distplot(df["Quantity"])
plt.show()


# In[27]:


sns.distplot(df["Discount"])
plt.show()


# In[28]:


sns.distplot(df["Profit"])
plt.show()


# In[29]:


corr = df.corr()
corr


# In[32]:


sns.heatmap(corr,annot = True)


# In[33]:


#State VS Profit
sales_df = df.groupby("State")["Profit"].sum()
sales_df = sales_df.reset_index()
sales_df.head()


# In[38]:


plt.figure(figsize = (12, 7))
sns.barplot(x = sales_df["State"], y = sales_df["Profit"])
plt.xlabel("Profit")
plt.ylabel("State")
plt.show()


# In[39]:


#Category VS Profit
category_df = df.groupby("Category")["Profit"].sum()
category_df = category_df.reset_index()
category_df


# In[45]:


plt.figure(figsize = (5, 5))
sns.barplot(x = category_df["Category"], y = category_df["Profit"])
plt.xlabel("Profit")
plt.ylabel("Category")
plt.show()


# In[48]:


#Segment VS Count
sns.countplot("Segment", data = df)
plt.show()


# In[53]:


#Sub category VS Region
plt.figure(figsize = (15, 7))
sns.countplot(x = "Sub-Category", hue = "Region", data = df)
plt.xticks(rotation = "vertical")
plt.plot()


# In[57]:


# Sales per State
df_state = df.groupby("State")["Sales"].sum().sort_values(ascending = False)
df_state = df_state.to_frame().reset_index()
df_state.head()


# In[59]:


df_state.plot(kind = "bar", x = "State", y = "Sales", figsize = (12, 8))
plt.ylabel("Sales")


# In[62]:


#Profit VS Sales for Sub categories
sub_df = df.groupby("Sub-Category")["Profit", "Sales"].sum()
sub_df.plot(kind = "bar", figsize = (12, 8))
plt.show()

