import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
#df=pd.read_excel(r"C:\Users\anusha.raparthi\Desktop\datasets\PCOS.xlsx")
df=pd.read_excel(r"C:\Users\anusha.raparthi\Desktop\datasets\PCOS_data_without_infertility.xlsx")
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 10000)

pd.set_option('display.width', 2000)
#print(df['PCOS (Y/N)'])
#print(df.head())
df.dropna(inplace=True)
#df=df.drop('Unnamed',axis=1)
'''
label=LabelEncoder()
for column in df.columns:
    if df[column].dtype=='object':
        df[column]=label.fit_transform(df[column])
print(df.info())
'''
#print(df.isnull().sum())
#correlation=df.corr()
#print(correlation)
#print(df['PCOS (Y/N)'])


correlation=df.corrwith(df['PCOS (Y/N)']).abs().sort_values(ascending=False)
print(correlation)