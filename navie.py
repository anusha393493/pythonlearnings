import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB
df=load_iris()
from sklearn.model_selection import  train_test_split,cross_val_score
from sklearn.metrics import accuracy_score,confusion_matrix

#print(df.head())
# sepal_length  sepal_width  petal_length  petal_width species
#print(df.info())
#print(df.isnull().sum())
x=df.data
y=df.target
#print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=1)
gnb=GaussianNB()
gnb.fit(x_train,y_train)
y_pred=gnb.predict(x_test)
#print(y_test,y_pred)
f=accuracy_score(y_test,y_pred)
#print(f*100)
confusion=confusion_matrix(y_test,y_pred)
ax=sns.heatmap(confusion,annot=True,cmap='BuPu')
ax.xaxis.set_ticklabels(['setosa','versicolor','virginica'])

ax.yaxis.set_ticklabels(['setosa','versicolor','virginica'])
plt.show()

score=cross_val_score(gnb,x,y,cv=10,scoring="accuracy")
#print(score)
scoremean=score.mean()
#print(scoremean)