import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import numpy as np
import statsmodels.api as sm
df=pd.read_csv(r"C:\Users\anusha.raparthi\Downloads\kc_house_data.csv")
#print(df.columns)
df=df.drop(['id','date'],axis=1)
#print(df.columns)
#sns.pairplot(df,hue='bedrooms')
#plt.show()
x=df.drop(['price'],axis=1)
y=df['price']
#print(x,y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)
#print(x_train,x_test,y_train,y_test)
#scalar=StandardScaler()
#x_train=scalar.fit_transform(x_train)
#x_test=scalar.transform(x_test)
reg=LinearRegression().fit(x_train,y_train)
#y_pred=np.array([20])
#y_pred=y_pred.reshape(-1,1)
#y_pred=reg.predict(y_train)
#print(y_pred)
#x_train=x_train.reshape(-1,1)
#plt.scatter(y_train,y_pred)
#plt.show()
#print(x_train)
#print(reg.predict(x_train))
#print(x_train.shape)
#print(reg.predict(x_train).shape)
#print(y_train.shape)
#y_test_p=reg.predict(y_test)
#rscore=r2_score(y_test,y_test_p)
#print(rscore)
y_train_p=reg.predict(y_train)
rscore=r2_score(y_train,y_train_p)
print(rscore)