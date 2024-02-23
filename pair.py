import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
df=fetch_openml('titanic',version=1,as_frame=True)['data']
#print(df.columns)
#sns.pairplot(df,hue='day')
#sns.pairplot(df.head(),hue='day',diag_kind="hist")
#sns.pairplot(df,kind="kde",corner=True)
#plt.show()
#print(df['age'].sample())

#df['age'].dropna().sample()

df['age'].interpolate(method='linear',limit_direction='forward')
print(df['age'].isnull().sum())



