#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[4]:


pizza_data = pd.read_csv('./pizza_09.csv')
pizza_data


# In[5]:


sum_pizza_by_week = pizza_data.groupby('요일')['통화건수'].sum()
sum_pizza_by_week


# In[6]:


sorted_pizza_by_week = sum_pizza_by_week.sort_values(ascending=True)
sorted_pizza_by_week


# In[8]:


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.figure(figsize=(8,5))
plt.bar(sorted_pizza_by_week.index, sorted_pizza_by_week)
plt.xlabel('요일')
plt.ylabel('통화건수')
plt.show()


# In[9]:


sum_pizza_by_area = pizza_data.groupby('발신지_구')['통화건수'].sum()
sum_pizza_by_area


# In[10]:


sorted_sum_pizza_by_week = sum_pizza_by_area.sort_values(ascending=True)
sorted_sum_pizza_by_week


# In[11]:


plt.figure(figsize=(8,5))
plt.bar(sorted_sum_pizza_by_week.index, sorted_sum_pizza_by_week)
plt.xlabel('구')
plt.xticks(rotation=45)
plt.ylabel('통화건수')
plt.show()


# In[13]:


chicken07 = pd.read_csv('./chicken_07.csv')
chicken08 = pd.read_csv('./chicken_08.csv')
chicken09 = pd.read_csv('./chicken_09.csv')
chicken_data = pd.concat([chicken07,chicken08,chicken09])
chicken_data.reset_index(drop=True)
chicken_data


# In[15]:


sum_chicken_by_week = chicken_data.groupby('요일')['통화건수'].sum()
sorted_sum_chicken_by_week = sum_chicken_by_week.sort_values(ascending=True)
sorted_sum_chicken_by_week


# In[21]:


sum_pizza_by_week = pizza_data.groupby('요일')['통화건수'].sum()
sorted_sum_pizza_by_week = sum_pizza_by_week.sort_values(ascending=True)

plt.figure(figsize=(8,5))
plt.bar(sorted_sum_chicken_by_week.index, sorted_sum_chicken_by_week)
plt.bar(sorted_sum_pizza_by_week.index, sorted_sum_pizza_by_week)
plt.xlabel('요일')
plt.ylabel('통화건수')
plt.show()


# In[ ]:




