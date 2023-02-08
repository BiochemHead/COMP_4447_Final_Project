"""
Summary: This script is for creating Visualizations and Summary Stats
Data Started: 02-04-2023
Author(s): Chris Kirchberg
"""
import pandas as pd
import numpy as np
import matplotlib as plt

# Read the cleaned hiking dataset pickle file  
df = pd.read_pickle("../scrape_clean/hike_project_cln_data.pkl")

df.info()
df.describe()