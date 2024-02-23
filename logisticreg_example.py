import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel(r"C:\Users\anusha.raparthi\Downloads\CET_dataset.xlsx")
#print(df)
#print(df.isnull().sum())
#print(df.shape)
#df=df.dropna()
#print(df.shape)
#print(df.columns)
#print(df['age'])
#print(df.head())
#print(df.describe())
sns.boxplot(df['CET_score'])
plt.show()