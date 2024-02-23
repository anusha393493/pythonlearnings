import pandas as pd
import numpy as np
import dtale
import sweetviz as sv
#import autoviz
#from autoviz.AutoViz_Class import AutoViz_Class
#from pandas import ProfileReport
#from pandas_profiling import ProfileReport
import klib
from dataprep.eda import create_report
df=pd.read_csv(r"C:\Users\anusha.raparthi\Desktop\datasets\diabetes.csv")
pd.set_option('display.max_columns',10000)
pd.set_option('display.max_rows',10000)
pd.set_option('display.width',3000)
#dtale.show(df)
#print(df)
# Assigning a reference to a running D-Tale process
#d = dtale.show(df)
#d.open_browser()
#report=sv.analyze(df)
#report.show_html("sv_report.html")
#av=AutoViz_Class()
#df=av.AutoViz(r"C:\Users\anusha.raparthi\Desktop\datasets\diabetes.csv")
#create_report(df).save('dataprep_report.html')