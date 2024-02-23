import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml
import seaborn as sns
df=fetch_openml('titanic',version=1,as_frame=True)['data']
#print(df.columns)
#print(df['age'].isnull().sum())
#print(df['body'].head(30))
#print(df.info())
#print(df.age.count())
m=df['age'].median()
#print(m)
df['age_median']=df['age'].fillna(m)
#print(df['age_median'])
#print(df['age_median'].isnull().sum())
sns.kdeplot(df['age'])
sns.kdeplot(df['age_median'])
#plt.show()
df['AgeRandom']=df['age']
random_sample=df['age'].dropna().sample(df['age'].isnull().sum(),random_state=0)
random_sample.index=df[df['age'].isnull()].index
df.loc[df['age'].isnull(),'AgeRandom']=random_sample
print(df['AgeRandom'].isnull().sum())
sns.kdeplot((df['age']))
sns.kdeplot(df['AgeRandom'])