import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\onlinefood.csv")
#print(df.head)

#analysis based on Age
#sns.histplot(data=df,x="Age",hue="Output")
#plt.show()



#based on family size
#sns.histplot(data=df,x='Family size',hue='Output')
#plt.show()


buying_again=df.query("Output=='Yes'")
#print(buying_again)

#based on gender
gender=buying_again['Gender'].value_counts()
#print(gender)
label=gender.index
counts=gender.values
colors=['gold','lightgreen']
#fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
#fig.show()
#print(label)



#print(df['Marital Status'].unique())
marital=buying_again['Marital Status'].value_counts()
label=marital.index
counts=marital.values
#fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
#fig.show()7

#based on income
income=buying_again['Monthly Income'].value_counts()
label=income.index
counts=income.values
#fig=go.Figure(data=[go.Pie(labels=label,values=counts)])
#fig.show()
label = LabelEncoder()

for column in df.columns:
    if df[column].dtype=='object':
        df[column]=label.fit_transform(df[column])
#print(df.info())
y=df['Output']
x=df.drop(['Output'],axis=1)
#print(x,y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
model=LogisticRegression()
model.fit(x_train,y_train)
#y_pred=model.predict(x_test)
#print(y_pred)

#talking input
#print(df.columns)
a=int(input("enter Age:"))
b=int(input("gender(Male-1,Female-0):"))
c=int(input("Marital Status(Single=1, Married=2, Not revelaed=3):"))
d=int(input("Occupation(Student = 1,Employee = 2,Self Employeed = 3,House wife = 4):)"))
e=int(input("Monthly Income:"))
f=int(input("Educational Qualifications(Graduate = 1, Post Graduate = 2, Ph.D = 3, School = 4, Uneducated = 5):)"))
g=int(input("Family size:"))
h=int(input("Pin code:"))
i=input(input("Feedback of last order(1 = Positive, 0 = Negative):"))
features=np.array([a,b,c,d,e,f,g,h,i])
print(" The customer will oredr again or not:",model.predict(features))