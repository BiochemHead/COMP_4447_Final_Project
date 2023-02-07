import pandas as pd
import numpy as np

# Read the hiking dataset pickle file  
df = pd.read_pickle("hike_project.pkl")

# Showing Datatypes 
df.dtypes

# Correcting DataTypes 
df['Trail Length'] = df['Trail Length'].astype(float)
df['Elev_Up'] = df['Elev_Up'].str.replace("'", "").str.replace(",", "").astype(float)
df['Elev_Down'] = df['Elev_Down'].str.replace("'", "").str.replace(",", "").astype(float)
df['Highest Elevation'] = df['Highest Elevation'].str.replace("'", "").str.replace(",", "").astype(float)
df['Lowest Elevation'] = df['Lowest Elevation'].str.replace("'", "").str.replace(",", "").astype(float)
df['Average Grade'] = df['Average Grade'].str.strip('%').astype(float) / 100
df['Max Grade'] = df['Max Grade'].str.strip('%').astype(float) / 100

df.dtypes

# Data cleaning on Trail Difficulty, Dogs and Features, Trail Rating, and User Rate Number
df['Trail Difficulty'] = df['Trail Difficulty'].apply(lambda x: x[0].split()[0])
df['Dogs and Features'] = df['Dogs and Features'].apply(lambda x: x[0].split()[0])
df['Dogs and Features'] = df['Dogs and Features'].replace("Unknown", np.nan)

if not np.issubdtype(df['Trail Rating'].dtype, np.dtype(str).type):
    df['Trail Rating'] = df['Trail Rating'].astype(str)
df['Trail Rating'] = pd.to_numeric(df['Trail Rating'].str.extract('(\d+\.\d+)')[0], errors='coerce')

if not np.issubdtype(df['User Rate Number'].dtype, np.dtype(str).type):
    df['User Rate Number'] = df['User Rate Number'].astype(str)
df['User Rate Number'] = df['User Rate Number'].str.extract('\((\d+)\)')[0]

# Difficulty mapping
difficulty_map = {
    'EASY': 1,
    'EASY/INTERMEDIATE': 2,
    'INTERMEDIATE': 3,
    'INTERMEDIATE/DIFFICULT': 4,
    'DIFFICULT': 5
}

# Create the Difficulty Number column
df['Difficulty Number'] = df['Trail Difficulty'].map(difficulty_map)

# Specify the desired order of columns
columns = df.columns.tolist()
columns.remove('Difficulty Number')
columns = columns[:3] + ['Difficulty Number'] + columns[3:]
df = df[columns]

df.sample(5)


