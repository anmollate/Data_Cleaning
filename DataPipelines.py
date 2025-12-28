import pandas as pd
import numpy as np

#importing the csv file
df=pd.read_csv('dirty_cafe_sales.csv')

total_rows=df.shape[0]
print(total_rows)

#dropping the rows which do not have item names
df=df.dropna(subset='Item')
df=df[df['Item']!='UNKNOWN']
df=df[df['Item']!='UNKNOWN']


#replacing the string rows such as 'UNKNOWN' and 'ERROR' with null in Quantity Column to convert it further into "INT"
df['Quantity']=df['Quantity'].replace('UNKNOWN',np.nan)
df['Quantity']=df['Quantity'].replace('ERROR',np.nan)


#replacing the string rows such as 'UNKNOWN' and 'ERROR' with null in Total Spent Column to convert it further into "INT"
df['Total Spent']=df['Total Spent'].replace('UNKNOWN',np.nan)
df['Total Spent']=df['Total Spent'].replace('ERROR',np.nan)

#replacing the string rows such as 'UNKNOWN' and 'ERROR' with null in Price Per Unit Column to convert it further into "INT"
df['Price Per Unit']=df['Price Per Unit'].replace('UNKNOWN',np.nan)
df['Price Per Unit']=df['Price Per Unit'].replace('ERROR',np.nan)


#Converting the datatype of the columns
df['Quantity']=df['Quantity'].astype('Int64')
df['Total Spent']=df['Total Spent'].astype('Float64')
df['Price Per Unit']=df['Price Per Unit'].astype('Float64')

#Replacing those null rows in quantity which have non null columns for Total Spent and Price Per Unit
# Quantity=Total Spent/Price Per Unit
mask=(
    df['Quantity'].isna() &
    df['Total Spent'].notna() &
    df['Price Per Unit'].notna()
)
df.loc[mask,'Quantity']=df.loc[mask,'Total Spent'] / df.loc[mask,'Price Per Unit']
#Now Dropping The Remaining Rows in Quantity Column
df=df.dropna(subset='Quantity')


#Replacing Those rows in the total spent column which have non null rows in both column for Quantity and price per unit
maskt=(
    df['Total Spent'].isna() &
    df['Price Per Unit'].notna() &
    df['Quantity'].notna()
)
df.loc[maskt,'Total Spent']=df.loc[maskt,'Quantity'] * df.loc[maskt,'Price Per Unit']
#Now Dropping the null rows in the Total Spent
df=df.dropna(subset='Total Spent')


#Replacing those rows in the price per unit column which have non null rows in both column for Quantity and total spent
maskp=(
    df['Price Per Unit'].isna() &
    df['Total Spent'].notna() &
    df['Quantity'].notna()
)
df.loc[maskp,'Price Per Unit']=df.loc[maskp,'Total Spent'] / df.loc[maskp,'Quantity']
#Now Dropping the null rows in the Price per unit column
df=df.dropna(subset='Price Per Unit')


#Replacing the null and 'ERROR' rows in the Payment Method Column with Unknown
df['Payment Method']=df['Payment Method'].replace('ERROR','UNKNOWN')
df['Payment Method']=df['Payment Method'].replace(np.nan,'UNKNOWN')

#same for Location column
df['Location']=df['Location'].replace(np.nan,'UNKNOWN')
df['Location']=df['Location'].replace('ERROR','UNKNOWN')

#same for Transaction Date Column
df['Transaction Date']=df['Transaction Date'].replace(np.nan,'UNKNOWN')
df['Transaction Date']=df['Transaction Date'].replace('ERROR','UNKNOWN')

remaining_rows=df.shape[0]
print(remaining_rows)

deleted_rows=total_rows-remaining_rows
print("Deleted Rows: ",deleted_rows)

#Saving The Cleaned Data
df.to_csv('DataPipeLine_Output1.csv',index=False)







