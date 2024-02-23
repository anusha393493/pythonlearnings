import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,f1_score,r2_score
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\Heart_Disease_Prediction.csv")
#print(df)
#print(df.columns)
#print(df.isnull().sum())
#sns.boxplot(df['Age'])
#plt.show()
m=df['Age'].mean()
df['Age'].fillna(m,inplace=True)
outliers=[]
q1=np.percentile(df['Age'],25)
q3=np.percentile(df['Age'],75)
iqr=q3-q1
lf=q1-(1.5*iqr)
uf=q3+(1.5*iqr)
for i in df['Age']:
    if(i<lf or i>uf):
        outliers.append(i)
#print(outliers)
#df['Age'].drop(outliers,inplace=True)

for p in df['Age']:
    if p in outliers:
        df['Age'].replace(p,m,inplace=True)
#print(df['Age'])

#df['Age'].drop(index=uf,inplace=True)
#df['Age'].drop(index=lf,inplace=True)
#sns.boxplot(df['Age'])
#plt.show()
df.fillna(m,inplace=True)
#print(df.isnull().sum())
#print(df['Heart Disease'].unique())
df['Heart Disease']=df['Heart Disease'].map({'Presence':1,'Absence':0})
#print(df['Heart Disease'].unique())
y=df['Heart Disease']
x=df.drop(['Heart Disease'],axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
model=LogisticRegression()
model.fit(x,y)
y_pred=model.predict(x_test)
#print(y_pred)
cofusion=confusion_matrix(y_test,y_pred)
ax=sns.heatmap(cofusion,annot=True,cmap='BuPu')
ax.xaxis.set_ticklabels(['Presence','Absence'])
ax.yaxis.set_ticklabels(['Presence','Absence'])
#plt.show()
f1=f1_score(y_test,y_pred)
#print(f1)
r=r2_score(y_test,y_pred).
print(r)