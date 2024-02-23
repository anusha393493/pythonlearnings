import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import  seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,mean_squared_error
pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',1000)
pd.set_option('display.width',3000)
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\diabetes.csv")
#Insulin is a hormone that lowers the level of glucose (a type of sugar) in the blood.
#Bmi=
#print(df)
#print(df.isnull().sum())
correlation=df.corrwith(df['Outcome']).abs().sort_values(ascending=False)
#print(correlation)

#print(x)
#plt.Figure(figsize=(14,5))
#plt.subplot(1,8,1)
#sns.boxplot(data=df,y='Glucose',x='Outcome')
#plt.subplot(1,8,2)
#sns.boxplot(data=df,x='BMI',y='Outcome')
#plt.subplot(1,8,3)
#sns.boxplot(data=df,x='Age',y='Outcome')
#plt.subplot(1,8,4)
#ns.boxplot(data=df,x='Pregnancies',y='Outcome')
#plt.subplot(1,8,5)
#sns.boxplot(data=df,x='DiabetesPedigreeFunction',y='Outcome')
#plt.subplot(1,8,6)
#sns.boxplot(data=df,x='Insulin',y='Outcome')
#plt.subplot(1,8,7)
#sns.boxplot(data=df,x='BloodPressure',y='Outcome')
#plt.subplot(1,8,8)
#sns.boxplot(data=df,x='SkinThickness',y='Outcome')
#plt.show()
x=np.array(df[['Age','Glucose','BMI','Pregnancies','DiabetesPedigreeFunction','Insulin','BloodPressure']])
y=np.array(df[['Outcome']])
model=DecisionTreeClassifier(criterion='entropy',max_depth=3)
model=model.fit(x,y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
#print(df.info())
#print(max(df['Insulin']))

a=int(input("enter your Age:"))
b=int(input("enter Glucose(upto 200):"))
c=float(input("enter BMI(upto 67.1)Weight(kg)/Height(m):"))
d=int(input("enter number of  Pregnancies:"))
e=float(input("enter DiabetesPedigreeFunction(0.0 to 3)a function which scores likelihood of diabetes based on family history:"))
f=int(input("enter Insulin(upto 846)Insulin is a hormone that lowers the level of glucose (a type of sugar) in the blood:"))
g=int(input("enter BloodPressure:"))
features=np.array([[a,b,c,d,e,f,g]])
prediction=model.predict(features)
if prediction==1:
    print("Sorry,you are diabetic!")
else:
    print("Congrats,you dont have diabetics!")
#y=y.map({'1':"sorry!,you are diabetic",'0':"congrats,you dont have diabetic!"})
#print("your diabetic level is :",model.predict(features),"(1 means you have diabetis, 0 means you dont have!)")
#mse=mean_squared_error(y_test,prediction)
#print("mean squared error:",mse)
#rmse=np.sqrt(mse)
#print("root meansquare error is :",rmse)
#accuracy=accuracy_score(x_test,prediction)
#print("accracy is:",accuracy)
#1	85	66	29	0	26.6	0.351	31	0
