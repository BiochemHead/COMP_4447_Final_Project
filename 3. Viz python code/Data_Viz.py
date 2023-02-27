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
#df = pd.read_pickle("hike_project_cleaned.pkl")

#Get basic information about the data
df.info()
display(df.describe())
df.isna().sum()

# Plot count data of Dogs and Trail Difficulty on Bar Graphs
plt.rcParams["figure.figsize"] = [9, 5]
sns.set_style("whitegrid")
fig, axs = plt.subplots(nrows=2,sharex=True)
sns.countplot(y=df['Dogs'],order=['Leashed', 'Off-leash', 'No Dogs', 'Unknown'],ax=axs[0])
sns.countplot(y=df['Trail Difficulty'],
               order=['EASY', 'EASY/INTERMEDIATE', 'INTERMEDIATE',
                      'INTERMEDIATE/DIFFICULT', 'DIFFICULT'],ax=axs[1])
fig.suptitle('Trail Count of Dog Status and Difficulty Ratings', fontsize=14)

plt.show()

features = df[['Birding', 'Fall Colors', 'River/Creek', 'Views', 'Wildflowers',
               'Spring', 'Swimming', 'Lake', 'Geological Significance', 'Wildlife',
               'No Features']].apply(pd.value_counts)

# Plot count data of Features on Bar Graphs
plt.rcParams["figure.figsize"] = [6, 6]
fig , ax = plt.subplots()
my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'c', 'm']), None, len(df)))
ax = features.loc[True].plot.barh(color=my_colors)
plt.xlabel('Trail Count')
plt.ylabel('Features')
plt.title('Trail Count of Features')
plt.show()

# Plot count data of numeric columns on Histograms
plt.rcParams["figure.figsize"] = [9, 9]
df.select_dtypes(include=['float64']).hist();

# Plot Box Plot for Trail Rating vs. Trail Difficulty and Dog Status
plt.rcParams["figure.figsize"] = [6, 10]
sns.set_style("whitegrid")
fig, axs = plt.subplots(nrows=2)
g = sns.boxplot(data=df, x='Trail Difficulty', y='Overall Trail Rating',order=['EASY', 'EASY/INTERMEDIATE', 'INTERMEDIATE',
                      'INTERMEDIATE/DIFFICULT', 'DIFFICULT'], ax=axs[1])
g1 = sns.boxplot(data=df, x='Dogs', y='Overall Trail Rating', order=['Leashed', 'Off-leash', 'No Dogs', 'Unknown'],ax=axs[0])
g.tick_params(axis='x', rotation=90)
fig.suptitle('Trail Rating  by Dog Status and Trail Difficulty', y=0.92,fontsize=14)
plt.show()

# Make a paired plot of float64/numeric columns to explore relationships and include histograms
sns.set_style("whitegrid")
g = sns.pairplot(df.select_dtypes(include=['float64']),diag_kind="kde",
                 plot_kws={'s':2,'color':'blue'},height = 1.5);
g.map_offdiag(sns.regplot,line_kws={'color':'red'},scatter= False)
g.fig.suptitle('Comparison of Numeric (float64) Columns with Regression Lines',y=1.01,fontsize=18)
plt.show()
