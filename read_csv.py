#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Replace 'your_file.csv' with your actual file path
file_path = 'C:/Users/mli44/Downloads/electricity-ml-models-main/electricity-ml-models-main/data/data.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(df.head())


# In[3]:


columns_to_drop = ['DATETIME', 'MIIN', 'MARKETDAY', 'PEAKTYPE', 'MONTH', 'YEAR']
df = df.drop(columns=columns_to_drop)

# Display the first few rows of the updated dataframe
print(df.head())


# In[5]:


correlations = df.corr(method='pearson')['PEORIA_7_N001 (DALMP)']

# Display the correlations
print(correlations)


# In[ ]:




