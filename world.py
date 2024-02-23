import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import OneHotEncoder
df=pd.read_excel(r"C:\Users\anusha.raparthi\Desktop\excel\34_years_world_export_import_dataset.xlsx")
#print(df)
#print(df.columns)
#print(df.info())
#print(df.isnull().sum())
#df.dropna()
#print(df.isnull().sum())
#d=[col for col in df.columns if df[col].isnull().sum()>0]
#print(type(df))

for col in df.select_dtypes(exclude='object'):
        #m=10
        m=df[col].mean()
        df[col].fillna(m,inplace=True)
#print(df.isnull().sum())
'''
#print(df.select_dtypes(exclude='int64'))
c=df.select_dtypes(exclude='object')
#print(c.columns)
for col in c.columns:
    m=df[col].mean()
    c[col]=c[col].fillna(m,inplace=True)
print(c['Export (US$ Thousand)'])
'''
df=df.drop_duplicates()
#print(df)
#print(df.info())
#col=df.select_dtypes(exclude='object')
#print(col)
#boxplot = df.boxplot(column=col)
#plt.show(boxplot)

#z=np.abs(stats.zscore(df['Year']))
#print(z)
#print(df.columns)
print(df.shape)
q1,q3=np.percentile(df['AHS Dutiable Imports (US$ Thousand)'],[25,75])
#print(q1,q3)
iqr=q3-q1
lf=q1-(1.5)*iqr
uf=q3+(1.5)*iqr
#print(lf,uf)
lower_array=np.where(df['Export (US$ Thousand)']<=lf)[0]
upper_array=np.where(df['Export (US$ Thousand)']>=uf)[0]
#print(lower_array)
df.drop(index=lower_array,inplace=True)
df.drop(index=upper_array,inplace=True)
print(df.shape)


for col in df.select_dtypes(exclude='object'):
        print(df.shape)
        q1,q3=np.percentile(df[col],[25,75])
        #print(q1,q3)
        iqr = q3 - q1
        lf = q1 - (1.5) * iqr
        uf = q3 + (1.5) * iqr
        #print(lf,uf)

        upper_array = np.where(df[col] >= uf)[0]
        lower_array = np.where(df[col] <= lf)[0]
        # print(lower_array)

        df.drop(index=upper_array,axis=0,inplace=True)
        df.drop(index=lower_array, axis=0, inplace=True)
        print(df.shape)
'''


#print(df.info())
#=pd.get_dummies(data=df)
#print(p)
o=OneHotEncoder()
s=pd.DataFrame(o.fit_transform(df.iloc[:[2,4]]))
df=pd.concat([df,s],axis=1)
print(df)

'''