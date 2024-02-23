import inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.metrics import r2_score
import statsmodels.api as sm

df=pd.read_csv(r"C:\Users\anusha.raparthi\Downloads\height-weight.csv")
#print(df)
plt.scatter(df['Weight'],df['Height'])
plt.xlabel('weight')
plt.ylabel('height')
#plt.show()
#sns.pairplot(df)
#plt.show()
x=df[['Weight']]
y=df[['Height']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
#print(x_train,x_test,y_train,y_test)
#print(x_train.shape)
scalar=StandardScaler()
x_train=scalar.fit_transform(x_train)
x_test=scalar.transform(x_test)
#print(x_train)
reg=LinearRegression().fit(x_train,y_train)
print(reg.coef_)
print(reg.intercept_)
plt.scatter(x_train,y_train)
plt.plot(x_train,reg.predict(x_train))
#plt.show()
y_test_p=reg.predict(x_test)
print(y_test_p)
print(y_test)


mse=mean_squared_error(y_test,y_test_p)
mae=mean_absolute_error(y_test,y_test_p)
rmse=np.sqrt(mse)
#print(mse)
#print(mae)
#print(rmse)
score=r2_score(y_test,y_test_p)
#print(score)
model=sm.OLS(y_train,x_train).fit()
p_model=model.predict(x_test)
#print(p_model)
#print(model.summary())
#print(reg.predict([[72]]))