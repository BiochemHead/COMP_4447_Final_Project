import pandas as pd
import numpy as np

# Read the hiking dataset pickle file  
df = pd.read_pickle("hike_project.pkl")

# Showing Datatypes 
#df.dtypes

# Correcting DataTypes 
df['Trail Name'] = df['Trail Name'].astype("string")
df['Trail Length'] = df['Trail Length'].astype(float)
df['Trail Type'] = df['Trail Type'].astype("string")
df['Elev_Up'] = df['Elev_Up'].str.replace("'", "").str.replace(",", "").astype(float)
df['Elev_Down'] = df['Elev_Down'].str.replace("'", "").str.replace(",", "").astype(float)
df['Highest Elevation'] = df['Highest Elevation'].str.replace("'", "").str.replace(",", "").astype(float)
df['Lowest Elevation'] = df['Lowest Elevation'].str.replace("'", "").str.replace(",", "").astype(float)
df['Average Grade'] = df['Average Grade'].str.strip('%').astype(float) / 100
df['Max Grade'] = df['Max Grade'].str.strip('%').astype(float) / 100

# Data cleaning on Trail Difficulty, Dogs and Features, Trail Rating, and User Rate Number
df['Trail Difficulty'] = df['Trail Difficulty'].apply(lambda x: x[0].split()[0])
df['Dogs'] = df['Dogs and Features'].apply(lambda x: x[0].split()[0])
df['Dogs'] = df['Dogs'].replace("Unknown", np.nan)
df['Dogs'] = df['Dogs'].astype("string")

if not np.issubdtype(df['Trail Rating'].dtype, np.dtype(str).type):
    df['Trail Rating'] = df['Trail Rating'].astype(str)
df['Trail Rating'] = pd.to_numeric(df['Trail Rating'].str.extract('(\d+\.\d+)')[0], errors='coerce')

if not np.issubdtype(df['User Rate Number'].dtype, np.dtype(str).type):
    df['User Rate Number'] = df['User Rate Number'].astype(str)
df['User Rate Number'] = df['User Rate Number'].str.extract('\((\d+)\)')[0]

# Convert data type to int
df['User Rate Number'] = df['User Rate Number'].astype('Int64')


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

# Convert datatype to string
df['Trail Difficulty'] = df['Trail Difficulty'].astype("string")

# Specify the desired order of columns
columns = df.columns.tolist()
columns.remove('Difficulty Number')
columns.remove('Dogs')
columns = columns[:3] + ['Difficulty Number'] + columns[3:12] + ['Dogs'] + columns[12:]
df = df[columns]

# df.sample(5)

# save cleaned data frame as pkl file
df.to_pickle("hike_project_cln_data.pkl")
