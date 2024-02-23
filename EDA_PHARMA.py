import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
df=pd.read_excel(r"C:\Users\anusha.raparthi\Downloads\data.xlsx")
#print(df)
#print(df.columns)
#print(df.info())
#print(df.describe())
#print(df.isnull().sum())
#print(df.duplicated())
#print(df.columns where df[columns].dtype='float64')
#m=df['rev'].mean()
#df['rev'].fillna(m,inplace=True)
#print(df['rev'].isnull().sum())
#for col in df.select_dtypes(exclude='object'):
#   m=df[col].mean()
#    df.fillna(m,inplace=True)
#print(df.select_dtypes(exclude='object').nunique())
#print(df.head())
#label=preprocessing.LabelEncoder()
#df['sid']=label.fit_transform(df['sid'])
#print(df['sid'].unique())
#print()
#a=df.select_dtypes(exclude='float64')
#print(a)
#print(df.select_dtypes(exclude='float64').columns)
#sns.kdeplot(df['rev'])
#plt.show()
#print()
#print(df['Date of birth'])
#df['age']=df['Date of birth']
df['year']=df['Date of birth'].dt.year
#print(df['year'])
today_date=date.today()
current_year=today_date.year
#print(current_year)
df['age']=current_year-df['year']
#print(df['age'])
data=df[['Height (m)','Weight (kg)','age']]
#print(data.head())
#print(data.isnull().sum())
#print(data.describe())
mh=data['Height (m)'].mean()
mw=data['Weight (kg)'].mean()
#print(mh,mw)
data['Height (m)'].fillna(mh)
#data['Weight (kg)'].fillna(mw,inplace=True)
#print(data['Weight (kg)'].isnull().sum())
#print(df.shape)
#dup=df[df.duplicated()]
#print(dup)
df=df.drop_duplicates()
#print(df.shape)
#sns.boxplot(x=df['age'])
#plt.show()
#print(df.columns)
print(data.corr())