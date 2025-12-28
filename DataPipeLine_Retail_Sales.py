import pandas as pd
import numpy as np

df=pd.read_csv("retail_store_sales.csv")

#dropping the Rows in which item is null
df=df.dropna(subset='Item')

#Conevrting The Quantity To Int
df['Quantity']=df['Quantity'].astype('Int64')

