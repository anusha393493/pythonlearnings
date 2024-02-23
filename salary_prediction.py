import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df = pd.read_csv(r"C:\Users\anusha.raparthi\Downloads\Salary_Data.csv")
#print(df)
#plt.scatter(data=df,x='Salary',y='YearsExperience',)
fig=px.scatter(data_frame=df,x='Salary',y='YearsExperience',trendline='ols')

#fig.show()

#print(df.isnull().sum())
y=np.asanyarray(df[['Salary']])
x=np.asanyarray(df[['YearsExperience']])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
a=float(input("years of experience:"))
features=np.array([[a]])
print("predicted_salay=",model.predict(features))