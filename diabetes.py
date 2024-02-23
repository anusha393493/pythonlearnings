import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
df = load_diabetes(as_frame=True)
df = df.frame
print(df)
#cor=df.corr(method='pearson')
#print(cor["Target"])
#print(type(df))
#print(df.corr()['target'])
#print(df.columns)