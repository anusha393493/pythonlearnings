import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\INFY.csv")
#print(df.columns)

label=LabelEncoder()
for column in df.columns:
    df[column] =label.fit_transform(df[column])
#print(df.info())
#m=df.mean()
#f.fillna(m,inplace=True)

#print(df['Turnover'])0
#print(df.isnull().sum())
#sns.boxplot(df['Open'])
#plt.show()
y=df['Open']
x=df.drop(['Open'],axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=1)
#print(len(x_train))
#print(len(y_train))

model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
#sns.kdeplot(y_test)
#sns.kdeplot(y_pred)
plt.scatter(y_test,y_pred)
#plt.show()
#print(y_test,y_pred)
#print(r2_score(y_test,y_pred),mean_squared_error(y_test,y_pred))
#data=np.array(['30/05/2021','INFY','EQ','1356.35','2346.3','3373.9','9345.9','0348.6','8354.35','1261.16','1354677','1.1379E+15','921718','1468183','0.76493'])
#print(df1.dtype)
#y_pred1=model.predict(data)
#print(x_test)
#x_test1=x_test[x_test['Date']==3756]
#x_test1['Trades']=x_test1['Trades'].replace(1009,2709)
#x_test1['Volume']=x_test1['Volume'].replace(3373,5009)
#y_pred1=model.predict(x_test1)
#print(y_pred1)
#print(x_test1.info())
