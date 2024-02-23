import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\diamonds.csv")
#print(df.isnull().sum())
#print(df.info())
for column in df.columns:
    if df[column].dtype=='int64':
        m = df[column].mean()
        df.fillna(m, inplace=True)

#print(df.isnull().sum())



#print(df['clarity'].unique())
#df['cut']=pd.get_dummies(df, columns=['cut'])clarity
#print(df['cut'])
#
df["size"]=df["x"]*df["y"]*df["z"]
#print(df['size'])
df['cut']=df['cut'].map({'Ideal':1,'Premium':2,'Good':3,'Very Good':4,'Fair':5})
df['color']=df['color'].map({'E':1,'I':2,'J':3,'H':4,'G':5,'D':6})
df['clarity']=df['clarity'].map({'SI2':1,'SI1':2,'VS1':3,'VS2':4,'VVS2':5,'VVS1':6,'I1':7,'IF':8})
#print(df['clarity'].unique())

correlation=df.corr()
#print(correlation['price'].sort_values(ascending=False))
x=df[['carat','cut','size']]
y=df[['price']]
#print(x['size'])
label=LabelEncoder()
x['cut']=label.fit_transform(x['cut'])
#x['color']=label.fit_transform(x['color'])
#print(x['cut'].unique())

#print(x.isnull().sum())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
#print(len(x_train))
#print(len(y_train))

model=LinearRegression()
model.fit(x_train,y_train)
a = float(input("Carat Size: "))
b = int(input("Cut Type (Ideal: 1, Premium: 2, Good: 3, Very Good: 4, Fair: 5): "))
c = float(input("Size: "))
features=np.array([[a,b,c]])
print("diamonds price=",model.predict(features))
