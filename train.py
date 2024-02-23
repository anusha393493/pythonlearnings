import pandas as pd
from  sklearn import preprocessing
import numpy as np
df=pd.read_excel(r"C:\Users\anusha.raparthi\Downloads\Data_Train.xlsx")
#print(df)
#df.info()
#print(df['Total_Stops'])
label=preprocessing.LabelEncoder()
df['Route']=label.fit_transform(df['Route'])
#numbers = [1, 2, 3, 4, 5]



df['Total_Stops']=df['Total_Stops'].map({'1 stop':1,
                             '2 stops':2,
                             '3 stops':3,
                             '4 stops':4,
                             'non-stop':5,

})
df['Total_Stops'].fillna(6,inplace=True)
#print(df.isnull().sum())

#print(df['Total_Stops'].unique())
#print(df['Date_of_Journey'])
df['date']=(df['Date_of_Journey'].str.split('/').str[0])
df['month']=(df['Date_of_Journey'].str.split('/').str[1])
df['year']=(df['Date_of_Journey'].str.split('/').str[2])
#print(df['date'],df['month'],df['year'])
#print(df.info())
df['date']=df['date'].astype('int')
df['month']=df['month'].astype('int')
df['year']=df['year'].astype('int')
#print(df.dtypes)
#print(df['Duration'])
df['hours']=df['Duration'].str.split('h').str[0]
#print(df['hours'])
df.drop(['Date_of_Journey'],axis=1,inplace=True)
#print(df.columns)
#print(df['month'].value_counts())
#print(df.groupby(['date','month']).size().reset_index())

#print(df.groupby(['Airline','month']).size().reset_index())
#print(df.groupby(['Airline','Price']).size().reset_index())
#print(df['Airline'])
#df1=df.loc('Airline','Price'])
#df1=df.loc[:,['Airline','Price']]

#print(df.groupby(['Airline','Source','Destination'])['Price'].sum())
#print(df.head(5))
#print(df.columns)
#print(df.groupby(['Airline','Source','Destination'])['Total_Stops'].max())
#print(df.groupby(['Airline','Source','Destination','Total_Stops'])['hours'].size().reset_index())
#print(df.isnull().sum())
#print(df['Source'].unique())
#cor=np.corrcoef(df['month'],df['year'])
#print(cor)
print(df.info())
