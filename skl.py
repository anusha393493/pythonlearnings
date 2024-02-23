from sklearn.datasets import fetch_openml
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt
df=fetch_openml('titanic',version=1,as_frame=True)['data']
#print(df.isnull().sum())
#print(df.dtypes)
#print(df.head(5))
df1=df.copy()
#print(df1)
#df1['age'].fillna(df1['age'].mean,inplace=True)
m=df['age'].mean
#print(m)
#print(df['age'].values.mean)
m=np.mean(df['age'])
#print(m)
df['age'].fillna(m,inplace=True)
df['body'].fillna(m,inplace=True)
df['fare'].fillna(m,inplace=True)



label=preprocessing.LabelEncoder()
df['cabin']=label.fit_transform(df['cabin'])
df['embarked']=label.fit_transform(df['embarked'])
df['boat']=label.fit_transform(df['boat'])
df['home.dest']=label.fit_transform(df['home.dest'])
#print(df.isnull().sum())

#plt.boxplot(df['age'])
#plt.show()
#a=sorted(df['age'])
#print(a)
#q1,q3=np.percentile(a,[25,75])
#print(q1,q3)
#iqr=q3-q1
#print(iqr)
#lf=q1-(1.5)*iqr
#uf=q3+(1.5)*iqr
#print(lf,uf)
#b=sorted(df['fare'])
#q4,q5=np.percentile(b,[25,75])
#iqr1=q4-q5
#print(iqr1)
#out1=df[(df['age']<lf).values]
#print(df[(df['age']<lf).values])
#out2=df[(df['age']>uf).values]
#print(df['age'].replace(to_replace=df['age'],value=lf))
#x=lambda out1:df['age'].mean
#print(x)
#print(out1,out2)
#df['age'].replace(out1['age'],lf,inplace=True)
#df['age'].replace(out2['age'],uf,inplace=True)

#print(df['age'].hist(bins=20))
#plt.show()
#plt.boxplot(out1)
#plt.boxplot(out2)
#plt.show()

#boxplot
fig,axs=plt.subplots(13,1,dpi=225,figsize=(20,37))
i=0
for col in df.columns:
  if df[col].dtype==['float64', 'int64']:
    axs[i].boxplot(df[col],vert=False)
    axs[i].set_ylabel(col)
    i+=1
  else:
    break
plt.show()





'''

#drop the outliners
a=sorted(df['age'])
#print(a)
q1,q3=np.percentile(a,[25,75])
#print(q1,q3)
iqr=q3-q1
#print(iqr)
lf=q1-(1.5)*iqr
uf=q3+(1.5)*iqr
#print(lf,uf)
clean_data=df[(df['age']>=lf)&(df['age']<=uf)]
#print(clean_data)


#b=soretd(df[])
#print(df.columns)
'''