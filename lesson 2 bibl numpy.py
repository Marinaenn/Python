#!/usr/bin/env python
# coding: utf-8

# Lesson 2 Numpy,Pandas work #1
# -

# In[6]:


import numpy as np
import pickle
import pandas as pd
a=np.array([[1,6],[2,8],[3,11],[3,10],[1,7]]) 
a


# In[3]:


a.shape


# In[4]:


type(a)


# In[7]:


a_mean=a.mean(axis=0)
a_mean


# Work #2
# 
# 

# In[10]:


a_cent=a-a_mean
a_cent


# Work #3

# In[12]:


a_cent_sp=np.dot(a_cent[:,0],a_cent[:,1])
a_cent_sp


# In[13]:


a_cent_spt=a_cent_sp/(len(a_cent)-1)
a_cent_spt


# Работа с данными пандос

# Work# 1
# 

# In[23]:


authors=pd.DataFrame({"author_id":[1,2,3],"author_name":["Тургеньев","Чехов","Островский"]})
authors


# In[19]:


book=pd.DataFrame({"author_id":[1,1,1,2,2,3,3],"book_litle":["Отцы и дети","Рудин","Дворянское гнездо","Толстый и тонкий",
                                                             "Дама с собачкой ","Гроза","Таланты и поклонники"],"price":[450,
                                                            300,350,500,450,370,290]})
book
                  


# work#2

# In[25]:


authors_price=pd.merge(authors,book,on="author_id",how="outer")
authors_price


# work#3

# In[28]:


b=authors_price.groupby("author_name")
author_stat=pd.DataFrame({"min_price":b["price"].min(),"max_price":b["price"].max(),"mean_price":b["price"].mean()})
author_stat


# In[ ]:





# In[ ]:




