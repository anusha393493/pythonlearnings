import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
df=pd.read_excel(r"C:\Users\anusha.raparthi\Desktop\datasets\cancer patient´s care transitions dataset (1).xlsx")
#print(df.columns)
#print(df.info())
m=df.mean()
df.fillna(m,inplace=True)
#print(df.isnull().sum())
#print(df.shape)
df=df.drop_duplicates()
#print(df.shape)
#sns.boxplot(df['Gender'])
#plt.show()
#print(df.corr())
y=df['Type of Treatment ']
x=df.drop(['Type of Treatment '],axis=1)
#print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=40)
model=LinearRegression()
model.fit(x,y)
#print(model.intercept_,model.coef_)
print(df['Type of Treatment '].unique())