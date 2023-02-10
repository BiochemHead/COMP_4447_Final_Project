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
df=df_o.copy(deep=True)
df.replace({'Features':' · '},',',regex=True,inplace=True)
df['Difficulty Number']=df['Difficulty Number'].astype('category')

# Get basic information about the data
df.info()
df.describe()

# Plot count data of Dogs and Trail Difficulty on Bar Graphs
plt.rcParams["figure.figsize"] = [9, 5]

ax = plt.GridSpec(2, 1)
ax.update(wspace=0.25, hspace=0.25)

ax1 = plt.subplot(ax[0, 0])
sns.countplot(y=df['Dogs'])

ax2 = plt.subplot(ax[1, 0])
sns.countplot(y=df['Trail Difficulty'],
              order=['EASY', 'EASY/INTERMEDIATE','INTERMEDIATE',
                     'INTERMEDIATE/DIFFICULT' ,'DIFFICULT'])
plt.show()

# Plot count data of Features on Bar Graphs
plt.rcParams["figure.figsize"] = [9, 9]
ax.update(wspace=0.25, hspace=0.25)
my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'c','m']), None, len(df)))
df['Features'].value_counts(dropna=True).plot.barh(color=my_colors)
plt.xlabel('Count')
plt.ylabel('Features')
plt.title('Count of Features')
plt.show()

# Plot count data of numeric columns on Histograms
plt.rcParams["figure.figsize"] = [9, 9]
df.hist()
plt.show()

# Plot Box Plot for Difficulty Number vs. Trail Rating
plt.rcParams["figure.figsize"] = [9, 9]
ax = plt.GridSpec(2, 2)

ax1 = plt.subplot(ax[0, 0])
sns.boxplot(x='Difficulty Number',y='Trail Rating',data=df)

# Plot regression lines and scatter plots for Max Grade vs.
# Difficulty Number and Trail Rating
ax2 = plt.subplot(ax[1, 1])
sns.regplot(x='Max Grade',y='Difficulty Number',data=df,dropna = True)

ax3 = plt.subplot(ax[1, 0])
sns.regplot(x='Max Grade',y='Trail Rating',data=df,dropna = True)
plt.show()