import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_excel(r"C:\Users\anusha.raparthi\Desktop\datasets\cancer patient´s care transitions dataset (1).xlsx")
#print(df)
#print(df.info())
#print(df.isnull().sum())
m=df.mean()
#print(m)
df.fillna(m,inplace=True)
#print(df.isnull().sum())
#print(df.shape)
df.drop_duplicates(inplace=True)
#print(df.shape)
#print(df.columns)
#sns.boxplot(df['Age Range '])
#plt.show()