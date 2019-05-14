#!/usr/bin/env python
# coding: utf-8

# In[126]:


import pandas as pd
import numpy as np
import math


# In[127]:


import os
os.chdir('C://Users/Jaskeet/Downloads/Applications/US Real Co/Data Challenge/raw_data')


# In[128]:


xls = pd.ExcelFile('MSA1.xlsx')
df1 = pd.read_excel(xls,'Property Status',header=4)
xls2 = pd.ExcelFile('MSA2.xlsx')
df2 = pd.read_excel(xls2,'Property Status',header=4)


# In[129]:


def ret_cnt(prop_status_np):
    cnt = 0
    for i in range(prop_status_np.shape[0]):
        if(prop_status_np[i,0]=='S'):
            for j in range(1,prop_status_np[i].shape[0]):
                if(type(prop_status_np[i][j]) != type('str')):
                    continue
                elif(prop_status_np[i][j] == 'S' or prop_status_np[i][j] == 'R'):
                    break
                else:
                    cnt += 1
                    break
    return cnt


# In[130]:


cols = [i for i in df1.columns]
cols2 = [i for i in df2.columns]


# In[ ]:





# In[131]:


prop_status_1 = df1.iloc[:,26:]
prop_status_2 = df2.iloc[:,26:]


# In[132]:


prop_status_np_1 = prop_status_1.values
prop_status_np_2 = prop_status_2.values


# In[133]:


print(prop_status_np_2.shape)


# In[136]:


cnt1 = ret_cnt(prop_status_np_1)
cnt2 = ret_cnt(prop_status_np_2)
print("Market 1 delivered count is: ",cnt1)
print("Market 2 delivered count is: ", cnt2)
print("Total delivered count across both the markets is: ",cnt1+cnt2)


# In[ ]:


#The above is the solution to Part 1


# In[139]:


def ret_new_cnt(prop_status_np):
    cnt = 0
    for i in range(prop_status_np.shape[0]):
        if(prop_status_np[i,0]=='S'):
            for j in range(1,prop_status_np[i].shape[0]):
                if(type(prop_status_np[i][j]) != type('str') or prop_status_np[i][j] == 'S' or prop_status_np[i][j] == 'R'):
                    continue
                else:
                    cnt += 1
    return cnt


# In[145]:


cnt1 = ret_new_cnt(prop_status_np_1)
cnt2 = ret_new_cnt(prop_status_np_2)
print("Market 1 average lease-up time is: ",cnt1/(prop_status_np_1.shape[0]-6), " months")
print("Market 2 average lease-up time is: ", cnt2/(prop_status_np_2.shape[0]-6), " months")
print("Average lease-up time across both the markets is: ",(cnt1+cnt2)/(prop_status_np_1.shape[0]+prop_status_np_2.shape[0]-12), " months")


# In[ ]:




