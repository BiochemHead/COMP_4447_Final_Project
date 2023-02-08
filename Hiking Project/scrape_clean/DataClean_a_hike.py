import pandas as pd
import numpy as np

# Read the hiking dataset pickle file  
df = pd.read_pickle("hike_project.pkl")

# adding State, City, Area and Site 
df['State'] = df['Trail Difficulty'].apply(lambda x: x[0].split('\n')[3])
df['City'] = df['Trail Difficulty'].apply(lambda x: x[0].split('\n')[4])
df['Area'] = df['Trail Difficulty'].apply(lambda x: x[0].split('\n')[5] if len(x[0].split('\n')) > 5 else np.nan)
df['Site'] = df['Trail Difficulty'].apply(lambda x: x[0].split('\n')[6] if len(x[0].split('\n')) > 6 else np.nan)

# Specify the desired order of columns
columns = df.columns.tolist()
columns.remove('State')
columns.remove('City')
columns.remove('Area')
columns.remove('Site')
columns = columns[:1] + ['State'] + ['City'] + ['Area'] + ['Site'] + columns[1:]
df = df[columns]

# Cleaning Trail rating, User rate number, and renaming User rate number to user review 
if not np.issubdtype(df['Trail Rating'].dtype, np.dtype(str).type):
    df['Trail Rating'] = df['Trail Rating'].astype(str)
df['Trail Rating'] = pd.to_numeric(df['Trail Rating'].str.extract('(\d+\.\d+)')[0], errors='coerce')

if not np.issubdtype(df['User Rate Number'].dtype, np.dtype(str).type):
    df['User Rate Number'] = df['User Rate Number'].astype(str)
df['User Rate Number'] = df['User Rate Number'].str.extract('\((\d+)\)')[0]

df = df.rename(columns={'User Rate Number': 'User Review'})

# Cleaninbg Trail Difficulty and mappping difficulty number 
df['Trail Difficulty'] = df['Trail Difficulty'].apply(lambda x: x[0].split()[0])

# Difficulty mapping
difficulty_map = {
    'EASY': 1,
    'EASY/INTERMEDIATE': 2,
    'INTERMEDIATE': 3,
    'INTERMEDIATE/DIFFICULT': 4,
    'DIFFICULT': 5
}

# Create and sort the Difficulty Number column 
df['Difficulty Number'] = df['Trail Difficulty'].map(difficulty_map)

columns = df.columns.tolist()
columns.remove('Difficulty Number')
columns = columns[:7] + ['Difficulty Number'] + columns[7:]
df = df[columns]

# Cleaning Dog and Features, and sort columns 
df['Features'] = df['Dogs and Features'].apply(lambda x: x[1] if len(x) > 1 else np.nan)

columns = df.columns.tolist()
columns.remove('Features')
columns = columns[:18] + ['Features'] + columns[18:]
df = df[columns]

df['Dogs and Features'] = df['Dogs and Features'].apply(lambda x: x[0].split()[0])
df['Dogs and Features'] = df['Dogs and Features'].replace("Unknown", np.nan)
df = df.rename(columns={'Dogs and Features': 'Dogs'})

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

# Showing after correction Datatypes 
df.dtypes

# save cleaned data frame as pkl file
df.to_pickle("hike_project_cln_data.pkl")
