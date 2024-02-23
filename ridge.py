import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import RepeatedKFold
from sklearn.model_selection import cross_val_score
url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv'
df=pd.read_csv(url)
data=df.values
#print(data.dtype)
#print(df.shape)
#print(df.isnull().sum())
#print(df.info())
#print(df.corr())
#print(df.head())
x=data[:,:-1]
y=data[:,-1]
#print(y)
model=Ridge(alpha=1.0)
cv=RepeatedKFold(n_repeats=3,n_splits=10,random_state=1)
score=cross_val_score(model,x,y,scoring='neg_mean_absolute_error',cv=cv,n_jobs=1)
score=np.absolute(score)
print(score)
print(np.mean(score),np.std(score))


