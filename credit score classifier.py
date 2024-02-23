import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import  GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\train.csv")
print(df['Credit_Score'].unique())
#print(df.head())
#print(df.columns)
#print(df.isnull().sum())
#['ID', 'Customer_ID', 'Month', 'Name', 'Age', 'SSN', 'Occupation',
#'Annual_Income', 'Monthly_Inhand_Salary', 'Num_Bank_Accounts',
# 'Num_Credit_Card', 'Interest_Rate', 'Num_of_Loan', 'Type_of_Loan',
# 'Delay_from_due_date', 'Num_of_Delayed_Payment', 'Changed_Credit_Limit',
# 'Num_Credit_Inquiries', 'Credit_Mix', 'Outstanding_Debt',
 # 'Credit_Utilization_Ratio', 'Credit_History_Age',
#'Payment_of_Min_Amount', 'Total_EMI_per_month',
#'Amount_invested_monthly', 'Payment_Behaviour', 'Monthly_Balance',
# 'Credit_Score'
#sns.boxplot(df['Num_of_Loan'])
#plt.show()
#fig=px.bar(df,x='Occupation',color='Credit_Score')
#fig.show()
#fig=px.box(df,x="Occupation",color="Credit_Score",color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Annual_Income',color='Credit_Score',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Monthly_Inhand_Salary',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Num_Bank_Accounts',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Num_Credit_Card',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Interest_Rate',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Num_of_Loan',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Delay_from_due_date',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Num_of_Delayed_Payment',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Outstanding_Debt',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Credit_Utilization_Ratio',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Credit_History_Age',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Total_EMI_per_month',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Amount_invested_monthly',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#fig=px.box(df,x='Credit_Score',y='Monthly_Balance',color_discrete_map={'Poor':'red','Standard':'yellow','Good':'green'})
#df['Credit_Mix']=df['Credit_Mix'].map({"Standard": 1, "Good": 2, "Bad": 0})
#fig.show()
df['Credit_Score']=df['Credit_Score'].map({'Good':1,'Standard':2,'Poor':3})
x=np.array(df[['Credit_Score','Annual_Income','Monthly_Inhand_Salary','Num_Bank_Accounts','Num_Credit_Card','Interest_Rate','Num_of_Loan','Delay_from_due_date','Num_of_Delayed_Payment','Outstanding_Debt','Credit_History_Age','Monthly_Balance']])
df1=pd.DataFrame(x)
correlation=(df1.corr())
print(correlation[0])
#sns.pairplot(df1)
#plt.show()
#print(df1.corr())
'''
y=np.array(df[['Credit_Score']])
model=RandomForestClassifier()
#model=GaussianNB()
model.fit(x,y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
#y_pred=model.predict(x_test)

print("Credit Score Prediction : ")
a = float(input("Annual Income: "))
b = float(input("Monthly Inhand Salary: "))
c = float(input("Number of Bank Accounts: "))
d = float(input("Number of Credit cards: "))
e = float(input("Interest rate: "))
f = float(input("Number of Loans: "))
g = float(input("Average number of days delayed by the person: "))
h = float(input("Number of delayed payments: "))
i = input("Credit Mix (Bad: 0, Standard: 1, Good: 3) : ")
j = float(input("Outstanding Debt: "))
k = float(input("Credit History Age: "))
l = float(input("Monthly Balance: "))

features = np.array([[a, b, c, d, e, f, g, h, i, j, k, l]])
print("Predicted Credit Score = ", model.predict(features))

#print(y_pred)
print(df.corr())
#print()
'''