import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from scipy import stats
#df=load_diabetes(as_frame=True)
df=fetch_openml('titanic',version=1,as_frame=True)['data']
#print(df)
#df=df.frame
#print(df.columns)
#print(df['age'])
#sns.histplot(data=df['age'],kde=True)
#plt.show()
m=df['age'].mean()
#print(m)
#print(df['age'].isnull().sum())
df['ages']=df['age']
df['ages'].fillna(m,inplace=True)
#df['ages']=ages
#print(df['ages'].isnull().sum())
#print(stats.skew(df))
sns.histplot(data=df['age'],kde=True,bins=30)
sns.histplot(data=df['ages'],kde=True,bins=30)
#plt.show()
#print(df['ages'])
#sns.histplot(data=df['age'],kde=True,bins=30)
#plt.show()