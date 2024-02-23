import matplotlib.pyplot as plt
import matplotlib.axes as ax
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model  import LinearRegression
import statsmodels.api as sm
from sklearn.metrics  import r2_score
from sklearn.model_selection import train_test_split

data=pd.read_csv(r"C:\Users\anusha.raparthi\Downloads\data_for_lr.csv")
#print(data)
#print(data.shape)
data=data.dropna()
#print(data.shape)
print(data)
#train_input,train_output,test_input,test_output=train_test_split(data['x'],data['y'],test_size=0.33, random_state=42)
#print(train_input)


#print(data.corr())
plt.scatter(data['x'],data['y'])
#plt.show()



age=data[['x']]
#print(age)
#print(type(age))
height=data['y']
#print(height)
#print(type(height))


train_input,train_output,test_input,test_output=train_test_split(age,height,test_size=0.33, random_state=42)
#print(train_input)
scalar=StandardScaler()
#print(scalar.fit_transform(train_input))
#print(scalar.fit_transform(train_output))

reg=LinearRegression().fit(age,height)
#print(reg.coef_)
#print(reg.intercept_)
result = sm.OLS(height,age).fit()
#print(result.summary())
r_square=r2_score(age,height)
#print(r_square)
#regression=LinearRegression()
#model=regression.fit(train_input,train_output)

#ypred=model.predict(train_input)


