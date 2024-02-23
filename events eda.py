import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
#from fbprophet import Prophet
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import datetime
import calendar
from sklearn.model_selection import train_test_split
df=pd.read_excel(r"C:\Users\anusha.raparthi\Downloads\Event.xlsx")
pd.set_option('display.max_columns',100)
pd.set_option('display.max_rows',1000)
pd.set_option('display.width',2000)
#print(df.head(10))
#print(df.isnull().sum())
label=LabelEncoder()
#print(df.info())
#df.drop('Expectedness (against CCSI)','Expectedness (against IB)','PROTOCOL ID','SUBJECT ID')
'''
for col in df.columns:
    if df[col].dtype=='float64':
        df[col].fillna('0',inplace=True)
    else:
        df[col]=label.fit_transform(df[col])
'''
#print(df.isnull().sum())
#print(df.duplicated())
#print(df)
#sns.boxplot(data=df)
#plt.show()
print(df.columns)

'''
q1=df['Case Type'].quantile(0.25)
q3=df['Case Type'].quantile(0.75)
iqr=q3-q1

l_bound=q1-1.5*iqr
u_bound=q3+1.5+iqr
df=df[(df['Case Type']>=l_bound)&(df['Case Type']<=u_bound)]
sns.boxplot(data=df)
plt.show()


for col in df.columns:
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    iqr=q3-q1
    l_bound=q1-1.5*iqr
    u_bound=q3+1.5+iqr
    df=df[(df[col]>=l_bound)&(df[col]<=u_bound)]
sns.boxplot(data=df)
plt.show()

'''

df1=df.groupby(['Case Num','Case Seriousness']).size().reset_index().rename(columns={0:'case_count'})
#print(df1)
p=df['Case Seriousness'].value_counts()

#plt.bar(height='p',x='Case Type')
#plt.show()
#sns.pairplot(df)
#plt.show()
#sns.barplot(data=df1,y='case_count',x='Case Seriousness')
#sns.countplot(data=df,x='Case Type',y='Case Seriousness',start='percent')


#country wise case count
df2=df[df['Country Of Reporter']=='UNITED STATES'].groupby(['Country Of Reporter']).size().reset_index().rename(columns={0:'case_count'})
#print(df2)
#sns.barplot(data=df2,x='Country Of Reporter',y='case_count',hue='Country Of Reporter')
#plt.show()
#print(df['Case Type'])


#case seriousness by case type
df3=df.groupby(['Case Seriousness','Case Type']).size().reset_index().rename(columns={0:'case_count'})
#sns.barplot(data=df3,x='Case Type',y='case_count')
#plt.show()



#company drugs and non company drugs
h=df['Is company drug?'].value_counts()
k=df['Is company drug?'].unique()
#plt.pie(h,labels=k)
#plt.show()


#cases product wise
df4=df.groupby(['Suspect Drug(Generic Name)','Case Num','Case Type']).size().reset_index().rename(columns={0:'case_count'})
#sns.barplot(data=df4,x='Suspect Drug(Generic Name)',y='case_count',hue='Case Type')
#plt.show()

#countplot
#sns.countplot(data=df,x='age group')
#plt.show()


#hcp based on gender
f=df['Is HCP Confirm?'].value_counts()
labe=LabelEncoder()
df['Is HCP Confirm?']=label.fit_transform(df['Is HCP Confirm?'])
#print(f)
#sns.barplot(data=df,x='Sex',y='Is HCP Confirm?')
#plt.show()


#casecount by case type
#sns.scatterplot(data=df,x='Case Type',y='Case Num')
#plt.show()


#case seriousness by age group
df['Case Seriousness']=label.fit_transform(df['Case Seriousness'])
#sns.barplot(data=df,x='Case Seriousness',y='age group')
#plt.show()


#count of cases by age group
df['Case Num']=label.fit_transform(df['Case Num'])
df['age group']=label.fit_transform(df['age group'])
#sns.scatterplot(data=df,x='age group',y='Case Num')
#plt.show()


#count of event seriousness
e=(0.1,0)
s=df['Event seriousness'].value_counts()
n=df['Event seriousness'].unique()
#plt.pie(s,labels=n,autopct='%1.1f%%',explode=e)
#plt.show()


#df.plot()
#plt.show()

df['month_num']=pd.DatetimeIndex(df['Last Edit Date']).month
#df['month']=datetime.datetime.strptime(df['month_num'],'%b')
#df['month']=df['month_num'].dt.month_name()
df['month']=[calendar.month_name[x] for x in df['month_num']]
#print((df['month']))


df['num']=df['Case Num'].value_counts()
#print(df['num'])


df1=df[['month','num']]

#print(df1)

plt.bar(data=df1,x='month',height='num')
#plt.show()
train_size=int(len(df1)*0.8)
train,test=df1.iloc[:train_size],df1.iloc[train_size:]
#print(train,test)
model=ExponentialSmoothing(train['num'],seasonal='add',seasonal_periods=12)
result=model.fit()
predictions=result.forecast(len(test))
plt.figure(figsize=(12, 6))
plt.plot(train.index, train['num'], label='Training Data')
plt.plot(test.index, test['num'], label='Test Data')
plt.plot(test.index, predictions, label='Predictions', color='red')
plt.legend()
plt.show()