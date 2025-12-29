import pandas as pd
import numpy as np

df=pd.read_csv("retail_store_sales.csv")

total_rows=df.shape[0]
print(total_rows)

#dropping the Rows in which item is null
df=df.dropna(subset='Item')

#dropping discount applied column
df.drop('Discount Applied',axis=1,inplace=True)

#Converting The Quantity To Int
df['Quantity']=df['Quantity'].astype('Int64')

#Converting the null rows in the total spent into quantity * price per unit
mask=(
    df['Quantity'].notna() &
    df['Price Per Unit'].notna() &
    df['Total Spent'].isna()
)
df.loc[mask,'Total Spent']=df.loc[mask,'Quantity'] * df.loc[mask,'Price Per Unit']

#Converting The null rows in quantity into total spent / price per unit
maskq=(
    df['Quantity'].isna() &
    df['Price Per Unit'].notna() &
    df['Total Spent'].notna()
)
df.loc[maskq,'Quantity']=df.loc[maskq,'Total Spent'] / df.loc[maskq,'Price Per Unit']

#Converting the null rows in price per unit column into total spent / quantity
maskp=(
    df['Price Per Unit'].isna() &
    df['Quantity'].notna() &
    df['Total Spent'].notna()
)
df.loc[maskp,'Price Per Unit']=df.loc[maskp,'Total Spent'] / df.loc[maskp,'Quantity']

#dropping the null rows
df=df.dropna(subset='Quantity')
df=df.dropna(subset='Total Spent')
df=df.dropna(subset='Price Per Unit')

remaining_rows=df.shape[0]
deleted_rows=total_rows-remaining_rows
print('Deleted Rows: ',deleted_rows)

df.to_csv('Cleaned_Retail_Data.csv',index=False)




