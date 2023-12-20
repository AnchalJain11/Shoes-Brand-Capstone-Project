#!/usr/bin/env python
# coding: utf-8

#  Phase 3 of Capstone project

# In[4]:


import pandas as pd
x = pd.read_csv("Table1.csv")
y = pd.read_csv("Table2.csv")
z = pd.read_csv("Table3.csv")


# In[5]:


com = pd.merge(x,y)


# In[6]:


com


# In[7]:


combined=pd.merge(com,z)
combined


# In[8]:


combined.to_csv('Table.csv')
combined=pd.read_csv('Table.csv')


# In[ ]:





# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[12]:


combined.shape


# In[13]:


combined.info()


# In[16]:


combined.drop(['Unnamed: 0'], axis=1, inplace=True)


# In[17]:


combined.info()


# In[18]:


pd.isnull(combined).sum()


# In[19]:


combined['price'] = combined['price'].astype('int')


# In[20]:


combined['price'].dtype


# In[21]:


combined.info()


# In[23]:


combined.describe()


# In[26]:


combined.columns


# In[80]:


sns.barplot(x='star_rating',y='price',data=combined)


# Barplot showing which shows that the star rating does not have any influence on price and vice versa

# In[ ]:





# In[70]:


star_rating_counts = combined['star_rating'].value_counts()
plt.pie(star_rating_counts, labels=star_rating_counts.index)
plt.axis('equal')
plt.title('Distribution of star_ratings')
plt.figure(figsize=(80, 80))
plt.show()


# Piechart of distribution of star rating of shoes where most of the shoes have rating of 4-5 and around 25% of shoes does not have any rating.

# In[71]:


comfort_counts = combined['comfort'].value_counts()
plt.pie(comfort_counts, labels=comfort_counts.index)
plt.axis('equal')
plt.title('Distribution of comfort')
plt.figure(figsize=(80, 80))
plt.show()


# Piechart of distribution of comfort. After conducting a comprehensive analysis of the comfort ratings for various shoe models, it is evident that a majority of the surveyed customers highly favor and praise the exceptional comfort levels

# In[ ]:





# In[72]:


sns.barplot(x='comfort',y='price',data=combined)


# After the analysis that we made, it is clear that as the price of the shoe increases the comfort level also increases and demonstrates a positive relationship.

# In[ ]:





# In[85]:


top_shoes = combined.groupby(['shoes'], as_index=False)['price'].sum().sort_values(by='price', ascending=False).head(10)
sns.barplot(data=top_shoes, x='price', y='shoes')


# The top 10 shoes with the highest prices showcase premium quality, exquisite designs, and exclusive features, appealing to a luxury-seeking consumer base.

# In[ ]:





# Phase 4 of Capstone project

# In[29]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, accuracy_score
import joblib
import seaborn as sns


# In[5]:


data = pd.read_csv('Table.csv')


# In[6]:


data


# In[27]:


data.head()


# In[28]:


data.tail()


# In[7]:


x_price= data.drop(['price'], axis=1)
y_price= data['price']


# In[15]:


x_rating= data.drop(['star_rating'], axis=1)
y_rating= data['star_rating']


# In[16]:


x_price_train, y_price_test, x_price_train, y_price_test=train_test_split(x_price, y_price, test_size=0.2, random_state=42)


# In[17]:


x_rating_train, x_rating_test, y_rating_train, y_rating_test=train_test_split(x_rating, y_rating, test_size=0.2, random_state=42)


# In[23]:


scaler = StandardScaler()
x_price_train_scaled = scaler.fit_transform(x_price_train)
x_price_test_scaled = scaler.transform(x_price_test)


# In[32]:


sns.barplot(x='star_rating',y='price',data=data)


# In[ ]:





# In[ ]:




