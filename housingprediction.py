import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score
from sklearn.tree import DecisionTreeRegressor
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\housing.csv")
#print(df.info())
#print(df.head())
# print(df['ocean_proximity'].value_counts())
m=df['total_bedrooms'].mean()
df['total_bedrooms'].fillna(m,inplace=True)
#print(df.isnull().sum())
#fig=px.bar(df,x='longitude',y='median_hou se_value')
#fig.show()
#fig=px.bar(df,x='ocean_proximity',y='median_house_value', color='median_house_value')
#fig.show()
#fig=go.Figure()
#fig.add_trace(go.Bar(x=df['median_house_value'],y=df['total_rooms'],name='total rooms',marker='indianred'))
#fig.add_trace(go.Bar(x=df['median_house_value'],y=df['total_bedrooms'],name='total bedrooms',marker='lightsalmon'))
#fig.update_layout(barmode='group', xaxis_tickangle=-45)
#fig.show()
label=LabelEncoder()
df['ocean_proximity']=label.fit_transform(df['ocean_proximity'])
#print(df['ocean_proximity'].unique())
x=df.drop(['total_bedrooms'],axis=1)
y=df['total_bedrooms']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
model=LinearRegression()
model.fit(x,y)
y_pred=model.predict(x_test)
#print(y_test,y_pred)
accuracy=r2_score(y_test,y_pred)
#print(accuracy)
error=mean_squared_error(y_test,y_pred)
print(np.sqrt(error))
decision=DecisionTreeRegressor()
decision.fit(x,y)
dec_pred=decision.predict(x_test)
#print(y_test,dec_pred)
dt_mse=mean_squared_error(y_test,y_pred)
dt_rmse=np.sqrt(dt_mse)
print(dt_rmse)
