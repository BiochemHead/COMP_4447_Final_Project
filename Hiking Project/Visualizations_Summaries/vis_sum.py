"""
Summary: This script is for creating Visualizations and Summary Stats
Data Started: 02-04-2023
Author(s): Chris Kirchberg
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import cycle, islice
from IPython.core.display import display

# Read the cleaned hiking dataset pickle file
df_o = pd.read_pickle("../scrape_clean/hike_project_cln_data.pkl")
df = df_o.copy(deep=True)
for i in range(len(df)):
    if pd.isna(df.loc[i, 'Features']) is False:
        df['Features'][i] = df['Features'][i].split(sep='·')

df['Difficulty Number'] = df['Difficulty Number'].astype('category')

df.info()
display(df.describe())

plt.rcParams["figure.figsize"] = [5.5, 8]
plt.rcParams["figure.autolayout"] = True
ax = plt.GridSpec(2, 1)
ax.update(wspace=0.5, hspace=0.2)

ax1 = plt.subplot(ax[0, 0])
sns.countplot(y=df['Dogs'])

ax2 = plt.subplot(ax[1, 0])
sns.countplot(y=df['Trail Difficulty'],
              order=['EASY', 'EASY/INTERMEDIATE','INTERMEDIATE',
                     'INTERMEDIATE/DIFFICULT' ,'DIFFICULT'])
plt.show()

my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'c','m']), None, len(df)))
df['Features'].value_counts(dropna=True).plot.barh(color=my_colors)
plt.show()

df.hist()
plt.show()

plt.subplot(221)
sns.boxplot(x='Difficulty Number', y='Trail Rating', data=df)

plt.subplot(222)
sns.regplot(x='Max Grade', y='Difficulty Number', data=df, dropna=True)

plt.subplot(223)
sns.regplot(x='Max Grade', y='Trail Rating', data=df, dropna=True)
plt.show()
