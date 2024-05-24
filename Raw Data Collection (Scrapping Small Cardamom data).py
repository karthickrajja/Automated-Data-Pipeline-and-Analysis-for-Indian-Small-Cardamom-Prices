#!/usr/bin/env python
# coding: utf-8

# ### Data Collection

# In[1]:


import pandas as pd
import requests
from datetime import datetime


# ##### Enter number of page that need to be scrapped in range start page and end page

# In[2]:


kf = pd.DataFrame()
for i in range(1, 2):
    url = f"http://www.indianspices.com/indianspices/marketing/price/domestic/daily-price-small.html?page={i}"
    response = requests.get(url)
    df = pd.read_html(response.content)[1]
    df.columns = df.iloc[0]
    df = df[1:]
    df['Created_date'] = datetime.now()
    kf = pd.concat([kf, df], ignore_index=True)


# In[3]:


kf.to_csv("file_name.csv")


# In[ ]:




