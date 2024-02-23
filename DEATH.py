import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score,mean_squared_error
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\death.csv")
#print(df.columns)
#print(df['county'].unique())
#print(df['age_adjusted_death_rate'])
#print(df.isnull().sum())
#sns.boxplot(df)
#plt.show()
#print(df.info())

df=df[df['met_objective_of_45_5_1']!='*']
df=df[df['recent_trend_2']!='**']
df=df[df['lower_95_confidence_interval_for_trend']!='**']
df=df[df['upper_95_confidence_interval_for_trend']!='**']
df=df[df['recent_5_year_trend_2_in_death_rates']!='**']

label=LabelEncoder()

df['country']=label.fit_transform(df['county'])
df['n_met_objective_of_45_5_1']=label.fit_transform(df['met_objective_of_45_5_1'])
df['n_recent_trend_2']=label.fit_transform(df['recent_trend_2'])

df=df.drop(['county'],axis=1)
df=df.drop(['met_objective_of_45_5_1'],axis=1)
df=df.drop(['recent_trend_2'],axis=1)

x=df.drop(['age_adjusted_death_rate'],axis=1)
y=df['age_adjusted_death_rate']

#print(x.columns)
#print(df['county'].nunique())


#print(df['county'].unique())

#print(x_train)
#print(df['country'])

#print(df.columns)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=1)
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
#print(y_test,y_pred)
a=r2_score(y_test,y_pred)
m=mean_squared_error(y_test,y_pred)
#print(a,m)
print(y_pred)
#print(df.columns)
