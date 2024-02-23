import numpy as np
import pandas as pd
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\petrol_consumption.csv")
pd.set_option('display.max_columns',10000)
pd.set_option('display.max_rows',10000)
pd.set_option('display.width',5000)
#print(df)
#print(df.isnull().sum())
print(df.corr())