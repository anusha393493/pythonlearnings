import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
train=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\train.csv")
test=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\test.csv")
#print(train)
#print(train.columns)
targets=train['SalePrice']

#print(train.shape)
train=train.drop('SalePrice',axis=1)
#print(train.shape)
all_data=pd.concat([train,test])
#print(all_data.shape)
#print(train.isnull().sum())
train=pd.get_dummies(train)
test=pd.get_dummies(test)
all_data = pd.get_dummies(all_data)
X = all_data.as_matrix()
#train.fillna('0',inplace=True)

#test.fillna('0',inplace=True)
#print(test.isnull().sum())
#model=Lasso(alpha=1.0)
#model.fit(train,test)
#print(train.dtypes)
#print(all_data)
X_train = X[:int(train.shape[0] * 0.8)]
print(X_train)