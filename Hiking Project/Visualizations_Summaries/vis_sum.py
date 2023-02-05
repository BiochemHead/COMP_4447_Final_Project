"""
Summary: This script is for creating Visualizations and Summary Stats
Data Started: 02-04-2023
Author(s): Chris Kirchberg
"""
import pandas as pd
import numpy as np
import matplotlib as plt

df_columns=['hike_id', 'hike_name','type','dist','elev_gain', 'elev_loss','ave_grade',
            'max_grade','difficulty','num_reviews','ave_rating','location','dogs',
            'features','description','rating_dist','diff_dist']
data=[]
letters = np.array(list(chr(ord('a') + i) for i in range(26)))
for i in range(5000):
    data.append([i+100,np.random.choice(letters),
                 np.random.choice(letters),np.random.uniform(1,25),
                 np.random.uniform(1,2500),np.random.uniform(0,2500),
                 np.random.uniform(0,100),np.random.uniform(0,100),
                 np.random.randint(6),np.random.randint(100),
                 np.random.randint(5),np.random.choice(letters),
                 np.random.choice(letters),np.random.choice(letters),
                 np.random.choice(letters),
                 np.random.uniform(0,100),np.random.uniform(0,100)])
    
hike_df = pd.DataFrame(data,columns=df_columns)