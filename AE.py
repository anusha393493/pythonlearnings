import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
pd.set_option('display.max_columns',50)
pd.set_option('display.max_rows',1000)
pd.set_option('display.width',3000)
df=pd.read_csv(r"C:\Users\anusha.raparthi\Downloads\MICASE_DATA.csv")
#df1=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\AECASE_DATA.csv",on_bad_lines='skip')