import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn.naive_bayes import GaussianNB
df = sns.load_dataset('iris')
#print(df.head())
#print(df['species'].unique())
#print(df[df['species']=='virginica'] )
#print(df.shape)
df=df[df['species']!='virginica']
#print(df.isnull().sum())
#df=df.replace({'species':{'setosa':1,'versicolor':0}})
#print(df['species'].unique())
df['species']=df['species'].map({'setosa':1,'versicolor':0})
#print(df['species'].unique())
#print(df.columns)
#sns.boxplot(df['sepal_length'])
#plt.show()
#print(df.corr())
y=df['species']
x=df.drop(['species'],axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
model=LogisticRegression()
model.fit(x,y)
#print(model.intercept_,model.coef_)
y_pred=model.predict(x_test)
#print(y_pred)
#forest_params=[{'max_depth':list(range(10,15)),'max_features':list(range())}]
confusion=confusion_matrix(y_test,y_pred)
#print(confusion)
ax=sns.heatmap(confusion,annot=True,cmap='BuPu')
ax.set_title('Classification of flowers')
ax.xaxis.set_ticklabels(['setosa','versicolor'])
ax.yaxis.set_ticklabels(['setosa','versicolor'])
#plt.show()
gnb=GaussianNB()
gnb.fit(x,y)
y_pred1=gnb.predict(x_test)
a=accuracy_score(y_test,y_pred1)
print(a*100)
b=accuracy_score(y_test,y_pred)
print(b*100)

