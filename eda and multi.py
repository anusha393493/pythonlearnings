import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import  mean_squared_error,mean_absolute_error
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\insurance.csv")
#print(df.columns)
#print(df.info())
df=df.drop(['region'],axis=1)
#print(df.columns)
#print(df.isnull().sum())
#print(df.shape)
df=df.drop_duplicates()
#print(df.shape)
#print(df.corr(numeric_only=True))
label=preprocessing.LabelEncoder()
df['sex']=label.fit_transform(df['sex'])
df['smoker']=label.fit_transform(df['smoker'])

x=df.drop(['charges'],axis=1)
y=df['charges']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
scalar=StandardScaler()
x_train=scalar.fit_transform(x_train)
x_test=scalar.fit(x_test)
reg=LinearRegression()
reg.fit(x_train,y_train)
cof=reg.coef_
#print(x_train[1])
#print(cof)
#print(df.columns)
plt.scatter(x_train[1],y_train)
plt.plot(x_train[1],reg.predict(x_train))
plt.show()
