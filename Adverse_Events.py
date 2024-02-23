import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',1000)
pd.set_option('display.width',3000)
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\AECASE_DATA.csv",on_bad_lines='skip')
#print(df.head(10))
#print(df.info())
#df=df.drop_duplicates()
#print(df.isnull().sum())print(df.isnull().sum())
#print(df.shape)
#df.dropna(inplace=True)
#print(df.shape)
'''
for i in df['description']:
    if df[i]=='AE':
        df['Target']='AE'

label=LabelEncoder()
for column in df.columns:
    if df[column].dtype=='object':
        df[column]=label.fit_transform(df[column])
'''

#print(df.head(10))
#print(df['description'].unique())
#df['Target']='AE'