"""
Summary: This script is for creating Visualizations and Summary Stats
Data Started: 02-04-2023
Author(s): Chris Kirchberg
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the cleaned hiking dataset pickle file  
df_o = pd.read_pickle("../scrape_clean/hike_project_cln_data.pkl")
df=df_o.copy(deep=True)
for i in range(len(df)):
    if pd.isna(df.loc[i,'Features']) is False:
        df['Features'][i]=df['Features'][i].split(sep ='·')

df['Difficulty Number']=df['Difficulty Number'].astype('category')

df.info()
display(df.describe())

df['Dogs'].value_counts(dropna=False).plot.bar()
plt.show()

df['Trail Difficulty'].value_counts(dropna=False).sort_index().plot.bar()
plt.show()

df['Features'].value_counts(dropna=False).plot.bar()
plt.show()

df.hist()
plt.show()

plt.subplot(221)
sns.boxplot(x='Difficulty Number',y='Trail Rating',data=df)

plt.subplot(222)
sns.regplot(x='Max Grade',y='Difficulty Number',data=df,dropna = True)

plt.subplot(223)
sns.regplot(x='Max Grade',y='Trail Rating',data=df,dropna = True)
plt.show()
