#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create DataFrame from your pasted data
data = {
    "Rank": [1,2,3,4,5,6,7,8,9,10],
    "Brand": ["Evergreens","Clean Juice","Slapfish","Clean Eatz","Pokeworks",
              "Playa Bowls","The Simple Greek","Melt Shop","Creamistry","Joella's Hot Chicken"],
    "City": ["Seattle, Wash.","Charlotte, N.C.","Huntington Beach, Calif.","Wilmington, N.C.","Irvine, Calif.",
             "Belmar, N.J.","Blue Bell, Pa.","New York, N.Y.","Yorba Linda, Calif.","Louisville, Ky."],
    "Units_2017": [24,44,21,25,49,39,24,20,24,29],
    "YOY_2017": ["130.50%","121.90%","81.00%","79.70%","77.10%","62.90%","52.50%","39.60%","36.80%","35.50%"],
    "Units_2018": [26,105,21,46,50,76,36,19,60,17],
    "YOY_2018": ["116.70%","94.40%","90.90%","58.60%","56.30%","28.80%","33.30%","35.70%","27.70%","30.80%"],
    "Sales": [1150,560,1370,685,1210,580,775,1260,465,1930],
    "Franchise": ["No","Yes","Yes","Yes","Yes","Yes","Yes","Yes","Yes","No"]
}

df = pd.DataFrame(data)

# 2. Clean percentage columns (remove % and convert to float)
df["YOY_2017"] = df["YOY_2017"].str.replace("%","").astype(float)
df["YOY_2018"] = df["YOY_2018"].str.replace("%","").astype(float)

# 3. Histogram of Sales
sns.histplot(df["Sales"], bins=10, kde=True)
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# 4. Boxplot of YOY growth vs Sales
sns.boxplot(x="Franchise", y="YOY_2018", data=df)
plt.title("YOY Growth (2018) by Franchise Status")
plt.show()


# In[ ]:




