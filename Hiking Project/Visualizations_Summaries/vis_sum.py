"""
Summary: This script is for creating Visualizations and Summary Stats
Data Started: 02-04-2023
Author(s): Chris Kirchberg
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn import linear_model
import statsmodels.api as sm

# Read the cleaned hiking dataset pickle file  
df = pd.read_pickle("../scrape_clean/hike_project_cln_data.pkl")
for i in range(len(df)):
    if pd.isna(df.loc[i,'Features']) is False:
        df['Features'][i]=df['Features'][i].split(sep ='·')
        
df.info()
display(df.describe())

df['Dogs'].value_counts(dropna=False).plot.bar()
plt.show()

df['Trail Difficulty'].value_counts(dropna=False).plot.bar()
plt.show()

df['Features'].value_counts(dropna=False).plot.bar()
plt.show()

df.hist()

df.plot.scatter(x='Max Grade',y='Difficulty Number')

df.plot.scatter(x='Difficulty Number',y='Trail Rating')
