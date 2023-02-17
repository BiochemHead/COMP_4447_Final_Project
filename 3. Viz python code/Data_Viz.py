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

# Read the cleaned hiking dataset pickle file
df_o = pd.read_pickle("../Clean python code/hike_project_cln_data.pkl")
df = df_o.copy(deep=True)
df['Difficulty Number'] = df['Difficulty Number'].astype('category')
df['Split_feats']=df.Features.str.split(' · ')
df_f=pd.get_dummies(df['Split_feats'].apply(pd.Series).stack()).groupby(level=0).sum()
feats=df_f.sum(axis=0)
feats_name=list(df_f)
df=df.join(df_f)

# Get basic information about the data
df.info()
df.describe()

#Plot count data of Dogs and Trail Difficulty on Bar Graphs
plt.rcParams["figure.figsize"] = [9, 5]
fig, axs = plt.subplots(nrows=2,sharex=True)
sns.countplot(y=df['Dogs'],ax=axs[0])

sns.countplot(y=df['Trail Difficulty'],
               order=['EASY', 'EASY/INTERMEDIATE', 'INTERMEDIATE',
                      'INTERMEDIATE/DIFFICULT', 'DIFFICULT'],ax=axs[1])
fig.suptitle('Trail Count of Dog Status and Difficulty Ratings', fontsize=14)

plt.show()

# Plot count data of Features on Bar Graphs
plt.rcParams["figure.figsize"] = [9, 9]
ax = plt.GridSpec(1, 1)
my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'c', 'm']), None, len(df)))
ax = feats.plot.barh(color=my_colors)
plt.xlabel('Trail Count')
plt.ylabel('Features')
plt.title('Trail Count of Features')
plt.show()

# Plot count data of numeric columns on Histograms
plt.rcParams["figure.figsize"] = [9, 9]
df[df.columns[~df.columns.isin(feats_name)]].hist()
plt.show()

# Plot Box Plot for Difficulty Number vs. Trail Rating
ax = plt.GridSpec(2, 2)
plt.rcParams["figure.figsize"] = [9, 9]
ax1 = plt.subplot(ax[0, 0])
sns.boxplot(x='Difficulty Number', y='Trail Rating', data=df)

# Plot regression lines and scatter plots for Max Grade vs.
# Difficulty Number and Trail Rating
ax2 = plt.subplot(ax[1, 1])
sns.regplot(x='Max Grade', y='Difficulty Number', data=df, dropna=True)

ax3 = plt.subplot(ax[1, 0])
sns.regplot(x='Max Grade', y='Trail Rating', data=df, dropna=True)
plt.show()
