import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\BRCA.csv")
#print(df.info())
#print(df.isnull().sum())
#print(df.shape)
df=df.dropna()
#print(df.isnull().sum())
#print(df.shape)
#print(df.columns)
#'Patient_ID', 'Age', 'Gender', 'Protein1', 'Protein2', 'Protein3','Protein4',
# 'Tumour_Stage', 'Histology', 'ER status', 'PR status','HER2 status', 'Surgery_type',
# 'Date_of_Surgery', 'Date_of_Last_Visit', 'Patient_Status'

label=LabelEncoder()
for  column in df.columns:
    if df[column].dtype=='object':
        df[column]=label.fit_transform(df[column])
correlation=df.corr()
print(correlation)
#print(correlation['Patient_Status'].sort_values(ascending=False))
#print(df['Gender'])

df['Gender']=df['Gender'].map({'FEMALE':1,'MALE':0})
df['Tumour_Stage']=df['Tumour_Stage'].map({'I':1,'II':2,'III':3})
df['Histology']=df['Histology'].map({"Infiltrating Ductal Carcinoma": 1,"Infiltrating Lobular Carcinoma": 2,"Mucinous Carcinoma": 3})
df['ER status']=df['ER status'].map({'Positive':1})
df['PR status']=df['PR status'].map({'Positive':1})
df['HER2 status']=df['HER2 status'].map({'Positive':1,'Negative':0})
df['Surgery_type']=df['Surgery_type'].map({'Modified Radical Mastectomy':1,'Lumpectomy':2,'Simple Mastectomy':3,'Other':4})


#print(df['Surgery_type'].unique())
x=np.array(df[['Age','Gender','Protein1','Protein2','Protein3','Protein4', 'Tumour_Stage', 'Histology', 'ER status', 'PR status', 'HER2 status', 'Surgery_type']])
y=np.array(df[['Patient_Status']])

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
model=LogisticRegression()
model.fit(x_train,y_train)
'''
a=int(input("enter Age:"))
b=int(input("enter Gender('FEMALE':1,'MALE':0):"))
c=float(input("enter protein1:"))
d=float(input("enter protein2:"))
e=float(input("enter protein3:"))
f=float(input("enter protein4:"))
g=int(input("enter Tumour_Stage('I':1,'II':2,'III':3):"))
h=int(input("enter Histology('Infiltrating Ductal Carcinoma': 1,'Infiltrating Lobular Carcinoma': 2,'Mucinous Carcinoma': 3):"))
i=int(input("enter ER status(positive:1):"))
j=int(input("enter PR status(positive:1):"))
k=int(input("enter HER2 status(positive:1, Negative:0):"))
l=int(input("enter Surgery_type('Modified Radical Mastectomy':1,'Lumpectomy':2,'Simple Mastectomy':3,'Other':4):"))
features=np.array([[a,b,c,d,e,f,g,h,i,j,k,l]])
#y_pred=model.predict(features)
print("the patient will be:",model.predict(features))


'''

